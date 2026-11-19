# p07-12 KV cache and Flash Attention: lab guide

Lesson: <https://aiengineeringfromscratch.com/learn/transformers-deep-dive/kv-cache-flash-attention> · optional · ~75 min + lab ~20 min · backend: **local MLX**

## Why this lesson

The KV cache is the model's working memory for a conversation: the keys and values of every token so far, kept so they aren't recomputed for each new token. It decides how much GPU memory a long context needs (capacity planning for G5, where you'll serve models on GKE) and whether a follow-up request is fast or slow (prefix caching). Both are measured here on your own models.

## Task 0: start

Same as p07-02: model server in terminal 1 on the Mac, then:

```bash
cd ~/git/ai-engineering-course && make sh
C=/workspace/ai-engineering-from-scratch/phases/07-transformers-deep-dive/12-kv-cache-flash-attention/code
```

## Task 1: read the article and the code together

Code: `$C/main.py` (pure Python, no numpy).

| Article section | Code | What to look for |
| --- | --- | --- |
| The Problem, KV cache math | `KVCache`, `decode_naive`, `decode_cached` | cached decoding appends one K/V per step instead of recomputing all of them; outputs are identical |
| KV cache math | `kv_cache_bytes` | the formula: 2 (K and V) × layers × kv_heads × head_dim × bytes × tokens |
| Flash Attention, the tiling trick | `attention_full`, `tiled_softmax_dot` | softmax computed tile by tile with a running max: same numbers, never holds the full n × n matrix in memory |
| Speculative decoding, Continuous batching, PagedAttention | (no code) | read for vocabulary; these are vLLM's features in G5 |

```bash
python $C/main.py
```

Look at the KV table at the end: Llama-3-70B at 128K context needs ~43 GB just for KV, more than your whole Mac.

## Task 2: make it real: KV memory of your own models

```bash
python lessons/p07-12/kv_lab.py memory
```

[kv_lab.py](kv_lab.py) applies the lesson's formula to the two Gemma 4 models in your `~/git/models` cache, then a "Gemma-aware" estimate from their `config.json`: most layers use a **sliding window** (they only keep the last 512 or 1,024 tokens), the small model **shares** KV between layers, and the 12B's global layers keep **one KV head with K = V**. Read the `MODELS` dict and `gemma_aware()`: every number is a config field.

Look for: how far off the lesson formula is, and which architecture tricks make the difference.

## Task 3: make it real: when does the server reuse the cache?

```bash
python lessons/p07-12/kv_lab.py prefix
```

Four requests over ~5K tokens of logs. For each: latency and `cached_tokens` (what the server says it reused).

1. cold: new logs + question
2. same logs, different question
3. the conversation so far + a new turn (what an agent loop sends)
4. exact repeat of request 1

Before running, **predict** which ones will be fast.

<details><summary>My test run — look after your own</summary>

```
1 cold: new logs + question                   4.95s  prompt= 4920  cached=0
2 same logs, different question               4.97s  prompt= 4913  cached=0
3 conversation so far + a new turn            0.13s  prompt= 4942  cached=4923
4 exact repeat of request 1                   0.08s  prompt= 4920  cached=4919
```

Request 2 gets no reuse although it shares ~4,900 tokens with request 1. Gemma 4's sliding-window layers keep a rotating cache that mlx can extend but not cut back to the shared part, so only pure extensions (3) and repeats (4) hit. Other servers and models (vLLM with PagedAttention, hosted prompt caching) behave differently: always measure your own stack.

| Model | context | lesson formula | Gemma-aware |
| --- | --- | --- | --- |
| e4b | 32K | 2.62 GB | 0.52 GB |
| 12B | 128K | 48.00 GB | 1.31 GB |

</details>

## Cleanup

Ctrl+C the model server. `exit`, `make down`.

## Errata and gotchas

- In `main.py`, "naive attention ops: 55 / cached: 55" looks like no saving. The script's own note explains it: it only counts attention dot products; the saving is in not recomputing K and V projections for old tokens, which it doesn't count.
- The Gemma-aware numbers are an estimate from config fields (my reading of `num_kv_shared_layers`, `attention_k_eq_v`, `global_head_dim`), not a measurement. The direction (several times less than the naive formula) is solid; the exact GB aren't.
- `cached_tokens` is reported by mlx in `usage.prompt_tokens_details`; other servers may name it differently or not report it.
