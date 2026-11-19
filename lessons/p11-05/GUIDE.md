# p11-05 Context engineering: lab guide

Lesson: <https://aiengineeringfromscratch.com/learn/llm-engineering/context-engineering> · ~90 min + lab ~25 min · backend: `.env` (Gemma 4 26B)

## Why this lesson

A model only knows what's in its context window, and everything there costs tokens and attention. For an AIOps agent, choosing *what* goes into the context (which events, which log lines, which tools) matters more than the wording of the prompt. You saw it in p10-01 with formats; here you'll see it change the actual answer.

## Task 0: start

```bash
# Mac
orbctl start k8s
cd ~/git/ai-engineering-course && make sh
# container
C=/workspace/ai-engineering-from-scratch/phases/11-llm-engineering/05-context-engineering/code
lessons/common/scenario.sh up lab-p11-05          # ~1.5 min
```

## Task 1: read the article and the code together

Code: `$C/main.py` (uses numpy).

| Article section | Code | What to look for |
| --- | --- | --- |
| The Context Window is a Scarce Resource | `count_tokens`, `ContextBudget` | a budget per component (system, tools, history, documents) with hard caps |
| Lost-in-the-Middle | `reorder_lost_in_middle`, `score_relevance` | best items placed at the start and the end, weakest in the middle |
| Context Compression, Memory Systems | `ConversationManager` | old turns get summarized when history exceeds its budget |
| Dynamic Context Assembly | `TOOL_REGISTRY`, `classify_intent`, `select_tools` | only the tools relevant to this query go into the context |
| Build It step 6 | `ContextEngine`, `run_full_pipeline_demo` | all of it assembled per request |

```bash
python $C/main.py | less
```

## Task 2: make it real (A): what you select decides the answer

```bash
python lessons/p11-05/context_lab.py select lab-p11-05      # 3 calls
```

Same question ("each failing deployment and its root cause") answered from three contexts built from the live namespace:

- **all-events:** every event, oldest first, cut at 6,000 chars, like a naive tool with truncation
- **warnings:** only warning events
- **snapshot:** pod status table + warnings + last log lines ([common/k8s.py](../common/k8s.py))

It prints chars, prompt tokens and ✓/✗ per workload, plus each answer. Before running: predict which context will miss what. Hint: where does an OOM kill show up? Run `k -n lab-p11-05 get events` and `k -n lab-p11-05 get pods` and look.

## Task 3: make it real (B): lost in the middle

```bash
python lessons/p11-05/context_lab.py position               # 6 calls, waits on the free-tier token quota
```

Three kernel OOM-kill lines are hidden together in synthetic nginx logs at the start, the middle or the end, in a 30-line (~2.7K tokens) and a 150-line (~13K tokens) haystack. The model must list all three killed processes. Token counts come from the server's `usage`, so they're exact for this model.

Then on your local model (MLX server running):

```bash
LLM_BASE_URL=http://host.docker.internal:8080/v1 LLM_MODEL=mlx-community/gemma-4-e4b-it-4bit LLM_REASONING_EFFORT= LLM_PAUSE_S=0 \
  python lessons/p11-05/context_lab.py position
```

To make it harder, raise the sizes in `position()` (`for n_lines in (30, 150)`): try 400 lines on the local model (no quota there).

<details><summary>My test run (Gemma 4 26B) — look after your own</summary>

Select:

```
context       chars prompt tok  right (checkout / reports / search)
all-events     6028       2217  ✗ / ✗ / ✓      checkout, reports: "cause unknown"
warnings       1068        488  ✗ / ✗ / ✓
snapshot       2845       1191  ✓ / ✓ / ✓
```

The OOM kill isn't in events or logs, only in the pod's last termination state; the postgres error is only in the logs. Position: 3/3 everywhere on Gemma 26B at 13K tokens: a strong model finds a simple needle easily at this size. Lost-in-the-middle shows up with weaker models, longer contexts, or questions that need combining several facts.

</details>

## Cleanup

```bash
lessons/common/scenario.sh down lab-p11-05
```

## Errata and gotchas

- `count_tokens` in the lesson is `words × 1.3`. For logs that's far off: your p10-01 nginx log was 77 KB → 34K tokens (o200k), and one nginx line ≈ 90 Gemma tokens. Use the real tokenizer or the server's `usage`.
- The lesson's examples are about chat assistants. For ops data, the biggest win is usually *filtering at the source* (warnings only, a status table, `--tail`), before any compression.
- One nginx line ≈ 90 tokens means the 150-line haystack is near the free tier's tokens-per-minute quota; the `[429 … waiting]` pauses are expected.
