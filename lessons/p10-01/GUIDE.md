# p10-01 Tokenizers: companion guide

Lesson: <https://aiengineeringfromscratch.com/learn/llms-from-scratch/tokenizers> · full code: `../ai-engineering-from-scratch/phases/10-llms-from-scratch/01-tokenizers/code/` · budget ≈ 2.5 h

Check this only when stuck or when you finish a step. My notes go here; yours go in [NOTES.md](NOTES.md).

## Plan

| Step | What | Time |
| --- | --- | --- |
| 1 | Read the lesson on the site, take the quiz | 30 min |
| 2 | Build It steps 1–5 in this folder (`bpe.py`), plus exercise 1 (print each merge) | 40 min |
| 3 | Make it real: token cost of ops data (below) | 60 min |
| 4 | NOTES.md in your words, tick TRACK.md | 15 min |

Skip exercises 2, 3 and 4 for now: the "make it real" task covers 4, and step 3 covers part of 5.

## What actually matters for you

- **The merge table is the tokenizer.** It's fixed after training, and the model only ever saw IDs produced by that table. A model and its tokenizer are one artifact: change one and the other is garbage. That's why you can't count Claude tokens with tiktoken.
- **Byte-level means no `[UNK]`, ever.** Anything (binary junk in logs, emoji, Cyrillic) still encodes, just into more tokens. "Never fails" ≠ "cheap".
- **Tokens are the unit of cost, latency and context.** Price, rate limits, context window, KV-cache memory on a vLLM server (G5) and time-to-generate all scale with tokens, not characters. Everything in this lesson is a capacity-planning input.
- **Infra analogy:** BPE training ≈ `zstd --train` building a dictionary from sample files. A dictionary trained on your own logs compresses your logs far better than a generic one, and both sides must use the same dictionary.

## Errata and gaps in the lesson text

- **The BPE walkthrough rambles** ("wait, …", "Actually tracking this precisely"). The point it's fumbling: after merging `(w,e)` → `we`, the pair `(e,s)` no longer exists in `lowest`/`newest` because that `e` was consumed. Merging changes the counts of overlapping pairs, so you must recount after every merge. Then `(we,s)` and `(s,t)` tie at 8.
- **Tie-breaking:** `max(pairs, key=pairs.get)` returns the first-inserted pair among equals, which means first occurrence in the text, not alphabetical order. Different tie rules produce different merge tables from the same corpus.
- **No pre-tokenization in the scratch version**, so merges can cross word boundaries (you'll see tokens like `e c` from "the cat"). Real tokenizers (GPT-2/tiktoken) first split text with a regex (words, numbers, punctuation, whitespace runs) and merge only inside those chunks. That's the biggest reason your tokens look odd next to tiktoken's.
- **Garbled sentence on BERT variants.** It means: DistilBERT uses WordPiece like BERT; RoBERTa uses byte-level BPE.
- **`meta-llama/Llama-3.1-8B` is gated on Hugging Face** (license acceptance + token). Use an ungated tokenizer instead, e.g. `Tokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")` from the `tokenizers` package (no `transformers` needed).
- **Mixed metrics:** compression ratio divides by bytes, the vocabulary analysis divides by characters. For Cyrillic, 1 char = 2 UTF-8 bytes, so the two disagree. For a fair language comparison, compare token counts of the *same* sentence in both languages.

## Make it real: token cost of ops data

Lesson code doesn't call a model here; the "real" part is measuring real tokenizers on your own data.

1. **Collect samples** (sanitize anything sensitive; keep them out of git, `data/` is git-ignored):
   - `kubectl get events -A -o json`, the same with `-o yaml`, and the plain table output (any cluster, kind/k3d is fine)
   - ~200 lines of app or nginx logs
   - one `terraform plan` output
   - one paragraph in English and the same paragraph in Ukrainian
2. **Count tokens** for each sample with: tiktoken `o200k_base` and `cl100k_base`, one open-model tokenizer (Qwen above), and your own BPE.
3. **Domain tokenizer:** train your BPE on half of the logs, encode the other half, compare against training on the lesson's toy corpus. (This is exercise 5 with your data.)
4. **Normalize and recount:** regex-replace timestamps, UUIDs, IPs and pod-hash suffixes (`-7d9f8c6b5-x2k4p`) with placeholders, then count again.
5. **Cost it:** tokens per MB of each format, and $ per GB of logs at a current input price you look up (don't hardcode one).

**Done when** NOTES.md has the table (sample × tokenizer → tokens, tokens/byte) and 2–3 conclusions, e.g. which output format to feed an LLM, how much normalization saves, how big the Ukrainian tax is.

Exact Gemini and Claude counts need their APIs (their tokenizers aren't public); that's part of G1.

## Gotchas

- tiktoken downloads its encoding files on first use, and Hugging Face downloads tokenizer files, so both need network once. In a container, set `TIKTOKEN_CACHE_DIR` and `HF_HOME` to a mounted path so the cache survives rebuilds.
- `pip install tiktoken tokenizers` is all you need; skip `transformers` (heavy).
