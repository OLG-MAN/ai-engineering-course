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

Why: an AIOps agent reads `kubectl` output and logs through its tools, and everything it reads is billed and limited in tokens. This measures what that input costs per format, per tokenizer and per language, so the agent's tools can be designed around it.

### Reproduce from scratch

Everything runs in a throwaway namespace, so cleanup is one command. Numbers will differ a little from run to run (event timing, restart counts).

**On the Mac** (repo root):

```bash
orbctl start k8s          # OrbStack Kubernetes (no-op if already running)
make sh                   # lab container shell, opens in /workspace/ai-engineering-course
```

**In the container:**

```bash
# 1. Workload that produces events and logs
NS=p10-01
k create namespace $NS
k -n $NS create deployment crashy --image=busybox -- sh -c 'echo boom; exit 1'   # crash loop → Warning events
k -n $NS create deployment web --image=nginx
k -n $NS expose deployment web --port 80
k -n $NS rollout status deployment/web --timeout=180s

# 2. Traffic: 200 OK + 200 404s into nginx's access log ("; true" so the pod ends Succeeded, not Failed)
k -n $NS run load --image=busybox --restart=Never -- \
  sh -c 'for i in $(seq 200); do wget -qO- web >/dev/null; wget -qO- web/nope >/dev/null; done; true'
k -n $NS wait --for=jsonpath='{.status.phase}'=Succeeded pod/load --timeout=180s
sleep 30                  # let crashy restart a few more times

# 3. Capture the same events in three formats + the access log
D=lessons/p10-01/data; mkdir -p $D
k -n $NS get events -o json > $D/events.json
k -n $NS get events -o yaml > $D/events.yaml
k -n $NS get events         > $D/events.txt
k -n $NS logs deployment/web > $D/nginx.log
ls -la $D

# 4. Count tokens (en.txt / uk.txt are hand-written: keep them, they aren't regenerated)
python lessons/p10-01/count_tokens.py

# 5. Cleanup
k delete namespace $NS
exit
```

**On the Mac**, end of session:

```bash
make down                 # stop the lab container
orbctl stop k8s           # optional: stop the cluster to free RAM
```

`data/` is git-ignored. If you clone the repo fresh, recreate `en.txt` and `uk.txt`: the same paragraph in English and Ukrainian, 5–10 sentences.

### Optional extensions

- **Your own BPE column:** move the demo code in `bpe.py` under `if __name__ == "__main__":`, then in `count_tokens.py` train `BPETokenizer` on the first half of `nginx.log` (~300 merges) and count every file, using only the second half for `nginx.log` itself.
- **Normalize and recount:** regex-replace timestamps, IPs, UUIDs and pod-hash suffixes (`-7d9f8c6b5-x2k4p`) with placeholders, then count again.
- **Cost it:** $ per GB of logs at a current input price you look up (don't hardcode one).
- **Terraform:** add a `plan.txt` from any project.

Exact Gemini and Claude counts need their APIs (their tokenizers aren't public); that's part of G1.

## Gotchas

- tiktoken and Hugging Face download their tokenizer files once (network needed); the lab container keeps them in the `/cache` volume.
- `tiktoken` and `tokenizers` are in `requirements.txt`; skip `transformers` (heavy).
- Use `encode_ordinary`, not `encode`: `encode` raises if the text happens to contain a special-token string like `<|endoftext|>`.
- `kubectl wait` needs the load pod to *succeed*; without the trailing `; true` its last command is a failing `wget` of a 404, and the pod ends `Failed`.
