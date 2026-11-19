"""Read-only kubectl helpers for the lesson labs (and the tools of the p11-09 agent).

Only read verbs are allowed, every call has a timeout, and output is truncated:
an LLM reads whatever these return, and every character costs tokens (p10-01).
"""
import subprocess

READ_VERBS = {"get", "describe", "logs"}


def kubectl(*args, timeout=20, max_chars=6000):
    if not args or args[0] not in READ_VERBS:
        raise ValueError(f"kubectl verb not allowed: {args[:1]}")
    p = subprocess.run(["kubectl", *args], capture_output=True, text=True, timeout=timeout)
    out = (p.stdout or "") + (p.stderr if p.returncode else "")
    if len(out) > max_chars:
        out = out[:max_chars] + f"\n…[truncated, {len(out) - max_chars} more chars]"
    return out.strip()


POD_COLUMNS = (
    "NAME:.metadata.name,"
    "STATE:.status.containerStatuses[0].state.*.reason,"
    "RESTARTS:.status.containerStatuses[0].restartCount,"
    "LAST_EXIT:.status.containerStatuses[0].lastState.terminated.exitCode,"
    "LAST_REASON:.status.containerStatuses[0].lastState.terminated.reason"
)


def pods(ns):
    """Compact pod status. LAST_REASON is where an OOM kill shows up: not in events, not in logs."""
    return kubectl("get", "pods", "-n", ns, "-o", f"custom-columns={POD_COLUMNS}")


def events(ns, warnings_only=True):
    """Warnings only by default: Normal events (Scheduled, Pulled, Created…) are most of the volume
    and almost none of the signal, and sorted oldest-first they push the warnings into truncation."""
    args = ["get", "events", "-n", ns, "--sort-by=.lastTimestamp"]
    if warnings_only:
        args.append("--field-selector=type=Warning")
    return kubectl(*args)


def logs(ns, workload, tail=30, previous=False):
    """workload: a pod name or deploy/<name>. previous=True reads the last crashed container."""
    args = ["logs", "-n", ns, workload, f"--tail={tail}"]
    if previous:
        args.append("--previous")
    return kubectl(*args)


def describe(ns, pod):
    return kubectl("describe", "pod", "-n", ns, pod, max_chars=4000)


def snapshot(ns, workloads=("checkout", "reports", "search", "web", "billing")):
    """Pod status + warning events + recent logs: the 'incident data' several labs feed to a model."""
    parts = [f"## kubectl get pods -n {ns}\n{pods(ns)}", f"## kubectl get events -n {ns} (warnings)\n{events(ns)}"]
    for w in workloads:
        out = logs(ns, f"deploy/{w}", tail=10)
        if "not found" in out.lower():
            continue
        parts.append(f"## kubectl logs deploy/{w} --tail=10\n{out}")
    return "\n\n".join(parts)
