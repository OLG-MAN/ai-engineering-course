"""p11-02 lab: zero-shot vs few-shot vs chain-of-thought vs self-consistency, on Kubernetes failures.

The lesson measures these techniques on grade-school math (GSM8K). Same techniques here, on a job
an AIOps pipeline actually does: put each event/log line into one failure category.
12 hand-labeled cases in events_labeled.json; some are traps (scheduling "Insufficient memory" is
not an OOM; exit code 137 after a failed liveness probe is a PROBE problem).

Run:
  python lessons/p11-02/classify_lab.py            # all 12 cases, ~70 calls, ~3-4 min on the free tier
  python lessons/p11-02/classify_lab.py --limit 4  # quick look
  LLM_REASONING_EFFORT=none python lessons/p11-02/classify_lab.py --model gemini-3.1-flash-lite   # a weaker model
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.llm import backend, chat  # noqa: E402

DATA = json.loads((Path(__file__).parent / "events_labeled.json").read_text())
CATS = DATA["categories"]
LABELS = list(CATS)
CAT_LIST = "\n".join(f"- {k}: {v}" for k, v in CATS.items())
SYSTEM = f"You classify Kubernetes events and log lines into exactly one failure category.\nCategories:\n{CAT_LIST}"
ANSWER_RULE = "End your reply with a final line in the form: CATEGORY: <one of " + ", ".join(LABELS) + ">"


def parse(text):
    """Take the LAST 'CATEGORY: X' in the reply: with CoT, earlier lines may mention other categories."""
    found = re.findall(r"CATEGORY:\s*\**([A-Z_]+)", text)
    return found[-1] if found and found[-1] in LABELS else "PARSE_FAIL"


MODEL = None  # set by --model; None = LLM_MODEL from .env


def ask(user, temperature=0.0, max_tokens=400):
    r = chat([{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
             model=MODEL, temperature=temperature, max_tokens=max_tokens)
    return parse(r.text), r.usage.prompt_tokens + r.usage.completion_tokens, r.seconds


def zero_shot(text):
    return ask(f"Event:\n{text}\n\nAnswer with the category only. {ANSWER_RULE}")


def few_shot(text):
    shots = "\n\n".join(f"Event:\n{e['text']}\nCATEGORY: {e['label']}" for e in DATA["examples"])
    return ask(f"{shots}\n\nEvent:\n{text}\n{ANSWER_RULE}")


def chain_of_thought(text):
    return ask(f"Event:\n{text}\n\nThink step by step: what failed, at which stage of the pod lifecycle "
               f"(scheduling, image pull, start, running, probes), and what is the root cause vs the symptom. "
               f"Then answer. {ANSWER_RULE}", max_tokens=700)


def self_consistency(text, n=3):
    """n independent CoT samples at temperature 0.8, majority vote. Costs n× tokens."""
    votes, tokens, seconds = [], 0, 0.0
    for _ in range(n):
        label, t, s = ask(f"Event:\n{text}\n\nThink step by step about root cause vs symptom, then answer. "
                          f"{ANSWER_RULE}", temperature=0.8, max_tokens=700)
        votes.append(label); tokens += t; seconds += s
    return Counter(votes).most_common(1)[0][0], tokens, seconds


TECHNIQUES = {"zero-shot": zero_shot, "few-shot": few_shot, "CoT": chain_of_thought, "self-consist×3": self_consistency}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=len(DATA["test"]))
    ap.add_argument("--model", help="override LLM_MODEL, e.g. a smaller model to see where the techniques matter")
    args = ap.parse_args()
    global MODEL
    MODEL = args.model
    cases = DATA["test"][: args.limit]
    print(f"backend: {backend()}{' → model override: ' + MODEL if MODEL else ''}\ncases: {len(cases)}\n")
    stats = {name: {"ok": 0, "tokens": 0, "seconds": 0.0, "wrong": []} for name in TECHNIQUES}
    for i, case in enumerate(cases, 1):
        line = f"{i:2d}. {case['label']:<10}"
        for name, fn in TECHNIQUES.items():
            label, tokens, seconds = fn(case["text"])
            st = stats[name]
            st["tokens"] += tokens; st["seconds"] += seconds
            if label == case["label"]:
                st["ok"] += 1
            else:
                st["wrong"].append(f"#{i} {case['label']}→{label}")
            line += f"  {name}={'✓' if label == case['label'] else label}"
        print(line)
    print(f"\n{'technique':<16}{'accuracy':>10}{'tokens':>9}{'seconds':>9}  mistakes")
    for name, st in stats.items():
        print(f"{name:<16}{st['ok']}/{len(cases):<8}{st['tokens']:>9}{st['seconds']:>9.1f}  {', '.join(st['wrong']) or '-'}")


if __name__ == "__main__":
    main()
