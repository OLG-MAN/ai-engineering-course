"""p11-05 lab: what you put in the context window decides the answer.

Experiment A, "select": the same question about the scenario namespace, answered from three contexts:
  all-events   every event, oldest first, cut at 6,000 chars (a naive tool output with truncation)
  warnings     warning events only
  snapshot     pod status table + warning events + last log lines (lessons/common/k8s.py)
  → prompt tokens vs how many of the 3 broken workloads the answer gets right.

Experiment B, "position": lost-in-the-middle. Three kernel OOM-kill lines are hidden together inside
synthetic nginx access logs, at the start, the middle or the end, in a small and a large haystack.
  Free tier: the large haystack is close to the tokens-per-minute quota, so expect '429: waiting' pauses.
  → how many of the 3 killed processes the model finds, by position and size.
  Token counts come from the server's usage report (exact for this model), not from words × 1.3.

Run (scenario must be up for A):
  python lessons/p11-05/context_lab.py select lab-p11-05
  python lessons/p11-05/context_lab.py position
"""
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.k8s import events, snapshot  # noqa: E402
from common.llm import backend, chat  # noqa: E402

# ---------------------------------------------------------------- A: select
EXPECT = {"checkout": r"postgres|connection refused|db\.", "reports": r"oom|memory", "search": r"image|pull|not found|does-not-exist"}


def select(ns):
    contexts = {
        "all-events": events(ns, warnings_only=False),        # kubectl helper truncates at 6,000 chars
        "warnings": events(ns, warnings_only=True),
        "snapshot": snapshot(ns),
    }
    q = ("For each failing deployment, give its name and the root cause in one line. "
         "Use only the data. If the data doesn't show a cause, write 'cause unknown'.")
    print(f"{'context':<12}{'chars':>7}{'prompt tok':>11}  right (checkout / reports / search)")
    for name, ctx in contexts.items():
        r = chat([{"role": "user", "content": f"{q}\n\n{ctx}"}], temperature=0, max_tokens=300)
        text = r.text.lower()
        right = {w: bool(re.search(rf"{w}[^\n]*({pat})", text)) for w, pat in EXPECT.items()}
        marks = " / ".join("✓" if ok else "✗" for ok in right.values())
        print(f"{name:<12}{len(ctx):>7}{r.usage.prompt_tokens:>11}  {marks}")
        print("            " + r.text.replace("\n", "\n            ")[:600])


# ---------------------------------------------------------------- B: position
NEEDLES = ["payments-worker", "pdf-renderer", "cache-warmer"]
PATHS = ["/", "/api/cart", "/api/items?page=2", "/static/app.js", "/healthz", "/api/checkout", "/login"]


def nginx_line(rng, i):
    ip = ".".join(str(rng.randint(1, 254)) for _ in range(4))
    status = rng.choice([200] * 8 + [301, 404, 500])
    return (f'{ip} - - [13/Nov/2026:16:{i // 60 % 60:02d}:{i % 60:02d} +0000] "GET {rng.choice(PATHS)} HTTP/1.1" '
            f'{status} {rng.randint(200, 9000)} "-" "Mozilla/5.0 (X11; Linux x86_64)" rt={rng.random():.3f}')


def haystack(n_lines, where, seed=7):
    rng = random.Random(seed)
    lines = [nginx_line(rng, i) for i in range(n_lines)]
    needles = [f"kernel: Out of memory: Killed process {rng.randint(1000, 9999)} ({p}) total-vm:{rng.randint(2, 9)}000000kB"
               for p in NEEDLES]
    at = {"start": int(n_lines * 0.05), "middle": n_lines // 2, "end": int(n_lines * 0.95)}[where]
    for k, needle in enumerate(needles):          # spread over a few lines around the target position
        lines.insert(at + k * 3, needle)
    return "\n".join(lines)


def position():
    q = "Which processes were killed by the kernel OOM killer in these logs? List every process name, nothing else."
    print(f"{'lines':>6}{'position':>9}{'prompt tok':>11}  found")
    for n_lines in (30, 150):           # ~2.7K and ~13K tokens: one nginx line ≈ 90 Gemma tokens
        for where in ("start", "middle", "end"):
            r = chat([{"role": "user", "content": f"{haystack(n_lines, where)}\n\n{q}"}], temperature=0, max_tokens=100)
            found = [p for p in NEEDLES if p in r.text]
            print(f"{n_lines:>6}{where:>9}{r.usage.prompt_tokens:>11}  {len(found)}/3  {r.text.strip()[:80]!r}")


if __name__ == "__main__":
    print(f"backend: {backend()}\n")
    exp = sys.argv[1] if len(sys.argv) > 1 else "position"
    if exp == "select":
        select(sys.argv[2] if len(sys.argv) > 2 else "lab-p11-05")
    else:
        position()
