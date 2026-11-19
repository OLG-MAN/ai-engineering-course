"""p11-03 lab: turn raw kubectl output into a typed Incident record, three ways.

The lesson's simulate_llm_extraction() returns canned JSON. Here a real model reads real
kubectl output for each broken workload, and we compare three ways of getting valid JSON:

  prompt   "reply in this JSON format" in the prompt, then parse + validate (Pydantic)
  retry    same, but on a parse/validation error send the error back and ask again (max 2 retries)
  schema   native structured output: response_format=json_schema, the server constrains decoding

Run (scenario must be up):
  python lessons/p11-03/extract_lab.py lab-p11-03
  LLM_MODEL=gemini-3.1-flash-lite LLM_REASONING_EFFORT=none python lessons/p11-03/extract_lab.py lab-p11-03  # weaker model
"""
import json
import sys
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.k8s import events, logs, pods  # noqa: E402
from common.llm import backend, chat  # noqa: E402

NS = sys.argv[1] if len(sys.argv) > 1 else "lab-p11-03"
RUNS = 2


class Incident(BaseModel):
    """The contract. Downstream code (alerting, ticketing, an agent) relies on exactly this shape."""
    workload: str = Field(description="deployment name, e.g. checkout")
    category: Literal["OOM", "APP_CRASH", "IMAGE", "SCHEDULING", "PROBE", "STORAGE", "NETWORK"]
    severity: Literal["critical", "warning"]
    evidence: list[str] = Field(description="1-3 short quotes copied verbatim from the kubectl output")
    next_check: str = Field(description="one kubectl command to run next")


EXPECTED = {"checkout": {"APP_CRASH", "NETWORK"}, "reports": {"OOM"}, "search": {"IMAGE"}}
SCHEMA = Incident.model_json_schema()
SYSTEM = "You are an SRE. Extract one incident record from the kubectl output for the named workload."
FORMAT_HINT = ("Reply with ONLY a JSON object with keys: workload (string), category (one of OOM, APP_CRASH, IMAGE, "
               "SCHEDULING, PROBE, STORAGE, NETWORK), severity (critical|warning), evidence (list of 1-3 verbatim "
               "quotes), next_check (one kubectl command).")


def workload_data(name):
    """Only the rows about this workload: smaller context, less to confuse the model."""
    pod_rows = [l for l in pods(NS).splitlines() if l.startswith(("NAME", name))]
    event_rows = [l for l in events(NS).splitlines() if f"/{name}-" in l]
    return "\n".join(["# pods", *pod_rows, "# warning events", *event_rows,
                      "# logs", logs(NS, f"deploy/{name}", tail=10)])


def validate(text):
    """Returns (Incident | None, error message | None). Strips ```json fences some models add."""
    raw = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    try:
        return Incident.model_validate(json.loads(raw)), None
    except json.JSONDecodeError as e:
        return None, f"not valid JSON: {e}"
    except ValidationError as e:
        return None, f"schema violation: {e.errors()[0]['loc']} {e.errors()[0]['msg']}"


def grounded(incident, data):
    """Schema-valid is not the same as true: how many 'verbatim' evidence quotes really are in the input?"""
    norm = lambda s: " ".join(s.split())
    return sum(norm(q) in norm(data) for q in incident.evidence), len(incident.evidence)


def extract(name, mode, data):
    """Returns (incident, attempts, tokens, last_error)."""
    msgs = [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Workload: {name}\n\n{data}"}]
    kwargs = {"temperature": 0.7, "max_tokens": 500}
    if mode == "schema":
        kwargs["response_format"] = {"type": "json_schema", "json_schema": {"name": "incident", "schema": SCHEMA}}
    else:
        msgs[1]["content"] += "\n\n" + FORMAT_HINT
    tokens, err = 0, None
    for attempt in range(1, 4 if mode == "retry" else 2):
        r = chat(msgs, **kwargs)
        tokens += r.usage.prompt_tokens + r.usage.completion_tokens
        incident, err = validate(r.text)
        if incident:
            return incident, attempt, tokens, None
        # retry: show the model its own answer and exactly what was wrong with it
        msgs += [{"role": "assistant", "content": r.text},
                 {"role": "user", "content": f"That reply was rejected: {err}. Reply again with ONLY the corrected JSON."}]
    return None, attempt, tokens, err


def main():
    print(f"backend: {backend()}\nnamespace: {NS}, {RUNS} runs per workload per mode, temperature 0.7\n")
    print(f"{'mode':<8}{'workload':<10}{'run':>4}  {'valid':<6}{'tries':>6}{'tokens':>8}  category / grounding  (expected)")
    summary = {}
    for mode in ("prompt", "retry", "schema"):
        for name in EXPECTED:
            for run in range(1, RUNS + 1):
                data = workload_data(name)
                inc, tries, tokens, err = extract(name, mode, data)
                ok_cat = bool(inc) and inc.category in EXPECTED[name]
                g, n_ev = grounded(inc, data) if inc else (0, 0)
                s = summary.setdefault(mode, {"valid": 0, "right": 0, "n": 0, "tokens": 0, "g": 0, "ev": 0})
                s["n"] += 1; s["tokens"] += tokens; s["valid"] += bool(inc); s["right"] += ok_cat
                s["g"] += g; s["ev"] += n_ev
                cat = f"{inc.category:<10} quotes found {g}/{n_ev}" if inc else f"✗ {err[:60]}"
                print(f"{mode:<8}{name:<10}{run:>4}  {'yes' if inc else 'NO':<6}{tries:>6}{tokens:>8}  {cat}  "
                      f"({'/'.join(EXPECTED[name])})")
                if inc and name == "reports" and run == 1:
                    print("          " + inc.model_dump_json())
    print(f"\n{'mode':<8}{'valid JSON':>11}{'right category':>16}{'quotes verbatim':>17}{'tokens':>8}")
    for mode, s in summary.items():
        print(f"{mode:<8}{s['valid']:>6}/{s['n']:<4}{s['right']:>11}/{s['n']:<4}{s['g']:>11}/{s['ev']:<5}{s['tokens']:>8}")


if __name__ == "__main__":
    main()
