"""p14-01 lab: the agent loop with its five ingredients made explicit, and switchable.

  1. message buffer       self.messages: grows every step, re-sent every step
  2. tool registry        TOOLS (what the model sees) + Agent.dispatch (what your code runs)
  3. stop condition       --stop no-tools: a reply without tool calls ends the run (p11-09 style)
                          --stop finish:   only an explicit finish(...) call ends it, with a validated result
  4. budgets              --max-turns and --max-tokens (total input+output tokens for the whole run)
  5. observation format   every tool result or error becomes a string the model reads; nothing raises.
                          Default: cryptic errors are translated into hints, and repeated identical calls
                          get "you already did this". --naive turns both off (watch the agent get stuck).

Same read-only kubectl tools as p11-09, written as a small reusable class this time.

Run (scenario must be up):
  python lessons/p14-01/agent_loop.py lab-p14-01 --stop finish --naive
  python lessons/p14-01/agent_loop.py lab-p14-01 --stop finish
  python lessons/p14-01/agent_loop.py lab-p14-01 --stop no-tools
  python lessons/p14-01/agent_loop.py lab-p14-01 --stop finish --max-tokens 3000
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import k8s  # noqa: E402
from common.llm import backend, chat  # noqa: E402

NAME = re.compile(r"^[a-z0-9]([a-z0-9.-]*[a-z0-9])?$")


# ---- the structured result the finish tool must carry (p11-03's idea, used as a stop condition) ----
class Finding(BaseModel):
    deployment: str
    category: Literal["OOM", "APP_CRASH", "IMAGE", "SCHEDULING", "PROBE", "STORAGE", "NETWORK", "SECURITY"]
    root_cause: str
    evidence: str


class Report(BaseModel):
    findings: list[Finding]
    healthy: list[str]


def fn(name, description, properties, required):
    return {"type": "function", "function": {"name": name, "description": description,
            "parameters": {"type": "object", "properties": properties, "required": required}}}


POD = {"pod": {"type": "string", "description": "exact pod name from list_pods"}}
TOOLS = [
    fn("list_pods", "Pods with state, restarts, last exit code and termination reason.", {}, []),
    fn("get_events", "Warning events of the namespace.", {}, []),
    fn("get_logs", "Last log lines of one pod; previous=true reads the crashed container.",
       {**POD, "previous": {"type": "boolean"}}, ["pod"]),
]
FINISH = fn(
    "finish", "Call exactly once when the investigation is complete, with every failing deployment.",
    {"findings": {"type": "array", "items": {"type": "object", "properties": {
        "deployment": {"type": "string"},
        "category": {"type": "string", "enum": list(Finding.model_fields["category"].annotation.__args__)},
        "root_cause": {"type": "string"},
        "evidence": {"type": "string", "description": "a short verbatim quote from tool output"}},
        "required": ["deployment", "category", "root_cause", "evidence"]}},
     "healthy": {"type": "array", "items": {"type": "string"}, "description": "deployments that are fine"}},
    ["findings", "healthy"])


class Agent:
    def __init__(self, ns, stop, max_turns, max_tokens, naive=False):
        self.ns, self.stop, self.max_turns, self.max_tokens, self.naive = ns, stop, max_turns, max_tokens, naive
        self.seen = set()
        self.tools = TOOLS + ([FINISH] if stop == "finish" else [])
        end = ("call finish(...) with your findings" if stop == "finish"
               else "reply with one line per failing deployment: <name>: <root cause> (evidence: <quote>)")
        self.messages = [  # ingredient 1: the message buffer
            {"role": "system", "content": f"You are an SRE agent investigating Kubernetes namespace {ns} with "
                                          f"read-only tools. Back every claim with tool output. When done, {end}."},
            {"role": "user", "content": "Find every failing deployment in the namespace and its root cause."}]
        self.used = 0

    def dispatch(self, name, raw):
        """Ingredients 2 + 5: run a tool, and turn ANY outcome into an observation string."""
        try:
            args = json.loads(raw or "{}")
        except json.JSONDecodeError as e:
            return f"ERROR: arguments are not valid JSON ({e}). Send a JSON object."
        if name == "list_pods":
            return k8s.pods(self.ns)
        if name == "get_events":
            return k8s.events(self.ns)
        if name == "get_logs":
            pod = str(args.get("pod", ""))
            if not NAME.match(pod):
                return f"ERROR: {pod!r} is not a valid pod name. Use a name from list_pods."
            out = k8s.logs(self.ns, pod, tail=20, previous=bool(args.get("previous")))
            if not self.naive and out.startswith("unable to retrieve container logs"):
                # kubectl's raw message tells the model nothing useful; say what it means and where to look
                return ("ERROR: the previous container's logs no longer exist (the runtime removed that container). "
                        "Why it died is in list_pods: LAST_EXIT and LAST_REASON (e.g. 137 / OOMKilled).")
            return out or "(no log lines)"
        return f"ERROR: unknown tool {name!r}. Available: {[t['function']['name'] for t in self.tools]}"

    def run(self):
        for turn in range(1, self.max_turns + 1):                       # ingredient 4: turn budget
            if self.used >= self.max_tokens:                            # ingredient 4: token budget
                return "budget", f"token budget exhausted ({self.used} ≥ {self.max_tokens}) after {turn - 1} turns"
            r = chat(self.messages, tools=self.tools, temperature=0, max_tokens=1200)
            self.used += r.usage.prompt_tokens + r.usage.completion_tokens
            calls = r.message.tool_calls or []
            print(f"turn {turn}: prompt={r.usage.prompt_tokens:>5} tok  run total={self.used:>6}  "
                  f"calls={[c.function.name for c in calls] or '-'}")
            if not calls:                                               # ingredient 3: stop conditions
                if self.stop == "no-tools":
                    return "done", r.text
                self.messages.append({"role": "assistant", "content": r.text or "(empty)"})
                self.messages.append({"role": "user", "content": "Not finished: call finish(...) with your findings."})
                print("   ↳ prose reply without finish(): nudged")
                continue
            self.messages.append(r.message.model_dump(exclude_none=True))
            for c in calls:
                if c.function.name == "finish":
                    try:
                        report = Report.model_validate_json(c.function.arguments)
                        return "done", report
                    except ValidationError as e:
                        obs = f"ERROR: finish rejected, fix and call again: {e.errors()[0]['loc']} {e.errors()[0]['msg']}"
                else:
                    try:
                        key = (c.function.name, json.dumps(json.loads(c.function.arguments or "{}"), sort_keys=True))
                    except json.JSONDecodeError:
                        key = (c.function.name, c.function.arguments)
                    if not self.naive and key in self.seen:
                        obs = (f"NOTE: you already called {c.function.name} with exactly these arguments; the result "
                               f"has not changed. Work with what you have: decide, or call finish.")
                    else:
                        obs = self.dispatch(c.function.name, c.function.arguments)
                    self.seen.add(key)
                print(f"   → {c.function.name}({c.function.arguments or ''})  ← {len(obs)} chars"
                      + (f"  {obs[:80]!r}" if obs.startswith(("ERROR", "NOTE")) else ""))
                self.messages.append({"role": "tool", "tool_call_id": c.id, "content": obs})
        return "budget", f"turn budget exhausted ({self.max_turns} turns)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("namespace", nargs="?", default="lab-p14-01")
    ap.add_argument("--stop", choices=["finish", "no-tools"], default="finish")
    ap.add_argument("--max-turns", type=int, default=10)
    ap.add_argument("--max-tokens", type=int, default=30_000)
    ap.add_argument("--naive", action="store_true", help="raw kubectl errors, no repeated-call guard")
    a = ap.parse_args()
    print(f"backend: {backend()}\nnamespace: {a.namespace}  stop={a.stop}  max_turns={a.max_turns}  "
          f"max_tokens={a.max_tokens}  naive={a.naive}\n")
    agent = Agent(a.namespace, a.stop, a.max_turns, a.max_tokens, a.naive)
    status, result = agent.run()
    print(f"\n=== {status}: {agent.used} tokens, {len(agent.messages)} messages in the buffer ===")
    if isinstance(result, Report):
        for f in result.findings:
            print(f"  {f.deployment:<10} {f.category:<10} {f.root_cause}\n  {'':<21}evidence: {f.evidence}")
        print(f"  healthy: {', '.join(result.healthy) or '-'}")
    else:
        print(result)


if __name__ == "__main__":
    main()
