# p11-03 Structured outputs: lab guide

Lesson: <https://aiengineeringfromscratch.com/learn/llm-engineering/structured-outputs> · ~90 min + lab ~20 min · backend: `.env` (Gemma 4 26B)

## Why this lesson

Code can't act on prose. If a model's answer feeds a ticket, an alert router or an agent's next step, it has to be data with a fixed shape: a contract. This lesson is about getting that contract reliably, and about the part no schema can check: whether the content is true.

## Task 0: start

```bash
# Mac
orbctl start k8s
cd ~/git/ai-engineering-course && make sh
# container
C=/workspace/ai-engineering-from-scratch/phases/11-llm-engineering/03-structured-outputs/code
lessons/common/scenario.sh up lab-p11-03          # ~1.5 min, start it now and read meanwhile
```

## Task 1: read the article and the code together

Code: `$C/main.py` (stdlib only).

| Article section | Code | What to look for |
| --- | --- | --- |
| The Structured Output Spectrum | (no code) | prompt-only → JSON mode → schema-constrained: each step moves the guarantee from "hope" to "enforced" |
| JSON Schema: The Contract Language | `validate_schema`, `_validate`, `PRODUCT_SCHEMA` | type, required, enum, minimum: what a validator can and can't catch |
| The Pydantic Pattern | `SchemaField`, `model_to_schema` | define the shape once in code, generate the schema from it (the lab uses real Pydantic) |
| Build It step 3 | `next_valid_tokens`, `demonstrate_constrained_decoding` | constrained decoding: at each step, only tokens that keep the JSON valid are allowed |
| Build It step 4, Common Failure Modes | `simulate_llm_extraction`, `extract_with_retry` | validate → on error, retry. **The model is simulated**: canned JSON by keyword |

```bash
python $C/main.py | less
```

## Task 2: make it real: incident records from kubectl output

[extract_lab.py](extract_lab.py) defines the contract as a Pydantic model:

```python
class Incident(BaseModel):
    workload: str
    category: Literal["OOM", "APP_CRASH", "IMAGE", "SCHEDULING", "PROBE", "STORAGE", "NETWORK"]
    severity: Literal["critical", "warning"]
    evidence: list[str]      # 1-3 quotes copied verbatim from the kubectl output
    next_check: str          # one kubectl command
```

For each broken workload (`checkout`, `reports`, `search`) it collects only that workload's rows (pod status, warning events, logs) and extracts an `Incident` three ways, 2 runs each at temperature 0.7:

- **prompt:** JSON format described in the prompt, then `json.loads` + Pydantic validation
- **retry:** same, but on failure the model gets its own answer back plus the exact error, up to 2 retries
- **schema:** native `response_format={"type": "json_schema", ...}` generated from the Pydantic model

Per run it reports valid JSON, attempts, tokens, category vs expected, and a **grounding** check: how many "verbatim" evidence quotes are really in the input.

```bash
python lessons/p11-03/extract_lab.py lab-p11-03               # 18 calls, ~1 min
LLM_MODEL=gemini-3.1-flash-lite LLM_REASONING_EFFORT=none python lessons/p11-03/extract_lab.py lab-p11-03
```

Then try your local model (MLX server running), where format errors and the retry path are more likely to show up:

```bash
LLM_BASE_URL=http://host.docker.internal:8080/v1 LLM_MODEL=mlx-community/gemma-4-e4b-it-4bit LLM_REASONING_EFFORT= \
  python lessons/p11-03/extract_lab.py lab-p11-03
```

Look for: which mode ever fails on which model, what the retry fixed, how many tokens each mode costs, and whether evidence was invented.

<details><summary>My test run (Gemma 4 26B) — look after your own</summary>

```
mode     valid JSON  right category  quotes verbatim  tokens
prompt       6/6             6/6            12/12       2356
retry        6/6             6/6            12/12       2408
schema       6/6             6/6            15/15       1893
```

A strong model rarely breaks the format, so the retry path never fired. `schema` was cheapest: no format instructions in the prompt. `checkout` came back as NETWORK, not APP_CRASH (both accepted): is the category list good enough?

</details>

## Cleanup

```bash
lessons/common/scenario.sh down lab-p11-03
```

## Errata and gotchas

- `simulate_llm_extraction` returns fixed JSON by keyword ("sony", "laptop"), so the lesson's retry demo shows the control flow, not real model behaviour.
- Native schema support differs by provider and model: some JSON Schema keywords (e.g. `minItems`, `$defs`, `additionalProperties`) may be ignored or rejected. Validate the result anyway, even in `schema` mode.
- Some models wrap JSON in ```` ```json ```` fences; `validate()` strips them. That's a real-world parsing chore, not a model error.
