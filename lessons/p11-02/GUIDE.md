# p11-02 Few-shot, chain-of-thought, self-consistency: lab guide

Lesson: <https://aiengineeringfromscratch.com/learn/llm-engineering/few-shot-cot> · ~45 min + lab ~30 min · backends: local MLX for the lesson script, `.env` for the lab

## Why this lesson

These techniques buy accuracy with tokens and time: examples in the prompt, "think step by step", or several samples and a vote. Whether that trade is worth it depends on the task and the model. You'll measure it on an AIOps task: sorting Kubernetes failures into categories, the first step of any alert pipeline.

## Task 0: start

Mac, terminal 1: start the local MLX server (see p07-02 Task 0). Terminal 2:

```bash
cd ~/git/ai-engineering-course && make sh
C=/workspace/ai-engineering-from-scratch/phases/11-llm-engineering/02-few-shot-cot/code
```

No cluster needed for this lesson.

## Task 1: read the article and the code together

Code: `$C/advanced_prompting.py`. Unlike most lessons, it calls a **real** model.

| Article section | Code | What to look for |
| --- | --- | --- |
| Zero-Shot vs Few-Shot, Example Selection | `GSM8K_EXAMPLES`, `build_cot_prompt`, `few_shot_cot_solve` | examples show the *format* of the reasoning, not just the answer |
| Chain-of-Thought | `build_zero_shot_cot_prompt`, `zero_shot_cot_solve` | "think step by step" = more output tokens spent before the answer |
| Self-Consistency | `self_consistency_solve` | n samples at temperature 0.7, majority vote on the extracted answer |
| Tree-of-Thought | `tree_of_thought_solve` and helpers | branch, score with the model, keep the best: many calls per question |
| ReAct | `react_solve` | think → act → observe: the bridge to function calling (p11-09) and agents (p14) |
| Prompt Chaining | `prompt_chain_solve` | extract → solve → verify as three calls |
| Performance Comparison | `extract_answer`, `run_comparison` | how answers are graded. **Look at line 381** |

Run it on your local model (free, no rate limits; ~10 min, ~100 calls):

```bash
cd /tmp && OPENAI_BASE_URL=http://host.docker.internal:8080/v1 OPENAI_API_KEY=local \
  LLM_MODEL=mlx-community/gemma-4-e4b-it-4bit python $C/advanced_prompting.py; cd -
```

The `OpenAI()` client reads `OPENAI_BASE_URL` from the environment, so the lesson code runs unchanged against your server.

**Now find the bug.** Answers like `got 72., expected 72` are marked WRONG. Copy the file, fix the comparison, rerun the comparison, and see how the accuracy table changes:

```bash
cp $C/advanced_prompting.py lessons/p11-02/advanced_prompting.py
# fix: in extract_answer() strip a trailing "." / compare as numbers in run_comparison(), e.g.
#   is_correct = answer is not None and float(answer) == float(expected)
```

## Task 2: make it real: classify Kubernetes failures

[events_labeled.json](events_labeled.json) has 12 hand-labeled events/log lines in 8 categories (OOM, APP_CRASH, IMAGE, SCHEDULING, PROBE, STORAGE, NETWORK, NORMAL) and 3 few-shot examples. Some are traps: "Insufficient memory" while *scheduling* is not an OOM; exit code 137 after a failed liveness probe is a PROBE problem.

[classify_lab.py](classify_lab.py) runs four techniques on all 12 and reports accuracy, total tokens and seconds:

```bash
python lessons/p11-02/classify_lab.py                       # Gemma 26B, ~3-4 min
LLM_REASONING_EFFORT=none python lessons/p11-02/classify_lab.py --model gemini-3.1-flash-lite   # weaker model
LLM_BASE_URL=http://host.docker.internal:8080/v1 LLM_REASONING_EFFORT= LLM_PAUSE_S=0 \
  python lessons/p11-02/classify_lab.py --model mlx-community/gemma-4-e4b-it-4bit             # your local model
```

Look for: on which model does a technique *change* the accuracy, and what does it cost in tokens and seconds?

<details><summary>My test runs — look after your own</summary>

Gemma 4 26B: all four techniques 12/12. Tokens: zero-shot 3,051 · few-shot 4,722 · CoT 5,617 · self-consistency×3 16,017. Seconds: 29 · 25 · 69 · 203.

gemini-3.1-flash-lite: zero-shot 11/12 (ephemeral-storage eviction → SCHEDULING), few-shot / CoT / self-consistency 12/12.

Lesson script before the fix: few-shot CoT "0%", nearly all from `"72." != "72"`.

</details>

## Cleanup

Ctrl+C the model server. `exit`, `make down`.

## Errata and gotchas

- **Grading bug:** `run_comparison` compares strings (`str(answer) == str(expected)`, line 381) and `extract_answer`'s regex keeps a trailing period, so `72.` counts as wrong. The lesson's accuracy summary is wrong, and the "few-shot CoT 0%" conclusion is false. A broken evaluator produces confident, wrong conclusions: always look at the failures, not just the score.
- The lesson script has no rate-limit handling: on the free tier it can crash with 429. Use the local server for it.
- Running it from `/tmp` (`cd /tmp`) is only so Python doesn't try to write `__pycache__` into the read-only course mount.
