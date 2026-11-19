"""p11-09 lab: a real function-calling loop. The model diagnoses a namespace with read-only kubectl tools.

The lesson's simulate_model_decision() picks tools with keyword matching. Here the model decides,
through the API's native tool calling, and your code executes. The loop (lesson: "The Function
Calling Loop"):

  1. send messages + tool definitions (JSON Schema)
  2. model replies with tool_calls (name + JSON arguments)  … or with a final answer → stop
  3. YOUR code validates the arguments and runs the tool
  4. append the results as role=tool messages, go to 1

Guardrails, all in your code, none in the prompt: read-only verbs only (common/k8s.py), one
allowed namespace, argument validation, output truncation, max 8 steps.

Run (scenario must be up):
  python lessons/p11-09/k8s_agent.py lab-p11-09
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import k8s  # noqa: E402
from common.llm import backend, chat  # noqa: E402

NS = sys.argv[1] if len(sys.argv) > 1 else "lab-p11-09"
MAX_STEPS = 8
NAME = re.compile(r"^[a-z0-9]([a-z0-9.-]*[a-z0-9])?$")   # Kubernetes resource name


def fn(name, description, properties, required):
    return {"type": "function", "function": {"name": name, "description": description,
            "parameters": {"type": "object", "properties": properties, "required": required}}}


NS_PARAM = {"namespace": {"type": "string", "description": "Kubernetes namespace"}}
POD_PARAM = {"pod": {"type": "string", "description": "exact pod name, as shown by list_pods"}}
TOOLS = [
    fn("list_pods", "List pods with state, restart count and last termination reason (e.g. OOMKilled).",
       NS_PARAM, ["namespace"]),
    fn("get_events", "Warning events in the namespace (scheduling, image pull, probe, back-off).",
       NS_PARAM, ["namespace"]),
    fn("get_logs", "Recent log lines of one pod. Set previous=true to read the last crashed container.",
       {**NS_PARAM, **POD_PARAM,
        "previous": {"type": "boolean", "description": "logs of the previous (crashed) container"},
        "tail": {"type": "integer", "description": "number of lines, 1-100", "minimum": 1, "maximum": 100}},
       ["namespace", "pod"]),
    fn("describe_pod", "Full kubectl describe of one pod: limits, state history, events. Large output.",
       {**NS_PARAM, **POD_PARAM}, ["namespace", "pod"]),
]


def run_tool(name, raw_args):
    """Validate, then execute. Errors go back to the model as tool output, so it can correct itself."""
    try:
        args = json.loads(raw_args or "{}")
    except json.JSONDecodeError:
        return "ERROR: arguments are not valid JSON"
    if args.get("namespace") != NS:
        return f"ERROR: namespace {args.get('namespace')!r} is not allowed; you may only inspect {NS!r}"
    pod = args.get("pod", "")
    if name in ("get_logs", "describe_pod") and not NAME.match(pod):
        return f"ERROR: invalid pod name {pod!r}"
    if name == "list_pods":
        return k8s.pods(NS)
    if name == "get_events":
        return k8s.events(NS)
    if name == "get_logs":
        tail = min(max(int(args.get("tail", 30)), 1), 100)
        return k8s.logs(NS, pod, tail=tail, previous=bool(args.get("previous", False))) or "(no log lines)"
    if name == "describe_pod":
        return k8s.describe(NS, pod)
    return f"ERROR: unknown tool {name!r}"


SYSTEM = (
    "You are an SRE agent. Diagnose the Kubernetes namespace you are given using the tools. "
    "Don't guess: every root cause must be backed by tool output. Prefer cheap tools first "
    "(list_pods, get_events) and read logs only for pods that need it. "
    "When done, answer with one line per failing workload: <deployment>: <root cause> (evidence: <quote>)."
)


def main():
    print(f"backend: {backend()}\nnamespace: {NS}, max {MAX_STEPS} steps\n")
    msgs = [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Something is wrong in namespace {NS}. Find every failing workload and its root cause."}]
    total_in = total_out = 0
    for step in range(1, MAX_STEPS + 1):
        r = chat(msgs, tools=TOOLS, temperature=0, max_tokens=1000)
        total_in += r.usage.prompt_tokens
        total_out += r.usage.completion_tokens
        calls = r.message.tool_calls or []
        print(f"step {step}: prompt={r.usage.prompt_tokens} tok, {r.seconds:.1f}s, tool calls: {len(calls)}")
        if not calls:
            print(f"\n=== final answer (after {step} steps, {total_in} in / {total_out} out tokens) ===\n{r.text}")
            return
        # Echo the assistant turn back unchanged: some APIs attach data to tool calls (e.g. Gemini's
        # thought signatures) that must be returned on the next request.
        msgs.append(r.message.model_dump(exclude_none=True))
        for call in calls:
            out = run_tool(call.function.name, call.function.arguments)
            print(f"   → {call.function.name}({call.function.arguments})  ← {len(out)} chars"
                  + (f"  {out[:70]!r}" if out.startswith("ERROR") else ""))
            msgs.append({"role": "tool", "tool_call_id": call.id, "content": out})
    print(f"\nstopped: hit the {MAX_STEPS}-step limit without a final answer ({total_in} in / {total_out} out tokens)")


if __name__ == "__main__":
    main()
