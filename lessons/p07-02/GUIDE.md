# p07-02 Self-attention from scratch: lab guide

Lesson: <https://aiengineeringfromscratch.com/learn/transformers-deep-dive/self-attention-from-scratch> · optional · ~90 min + lab ~20 min · backend: **local MLX** (the lab measures the server itself)

## Why this lesson

Every token of a prompt "looks at" every earlier token: that's the attention matrix. Before the model writes its first word it has to do this for the whole prompt (the *prefill*). So the size of what your agent sends (logs, events, history) turns directly into waiting time. This lab measures that on your own Mac.

## Task 0: start

On the Mac, terminal 1 (leave it running):

```bash
source ~/.mlx-lab/activate
mlx_lm.server --model mlx-community/gemma-4-e4b-it-4bit --port 8080 --chat-template-args '{"enable_thinking":false}'
```

Terminal 2:

```bash
cd ~/git/ai-engineering-course && make sh
C=/workspace/ai-engineering-from-scratch/phases/07-transformers-deep-dive/02-self-attention-from-scratch/code
```

## Task 1: read the article and the code together

Read one article section, then the matching code, then move on. The code is one file: `$C/self_attention.py` (open it in VS Code from `~/git/ai-engineering-from-scratch/phases/07-transformers-deep-dive/02-self-attention-from-scratch/code/`).

| Article section | Code | What to look for |
| --- | --- | --- |
| The Database Lookup Analogy, Q K V Computation | `SelfAttention.__init__`, `forward` | Q, K, V are the *same* input multiplied by three different learned matrices |
| The Attention Matrix, Why Scale? | `scaled_dot_product_attention` | `Q @ K.T` is n × n: every token scored against every token. The `/ sqrt(d_k)` keeps scores small so softmax doesn't saturate |
| Softmax Turns Scores into Weights | `softmax` | the `x - max` trick: same result, no overflow |
| Weighted Sum of Values | last line of `scaled_dot_product_attention` | output = weights @ V: each token becomes a mix of the others |
| Build It step 5 | `ascii_heatmap` | read one row: who does this token attend to? |

Run it:

```bash
python $C/self_attention.py
```

**Do exercise 1** (it's the one that matters later): copy the file into this folder and add an optional `mask` to `scaled_dot_product_attention` that sets scores above the diagonal to `-inf` before softmax.

```bash
cp $C/self_attention.py lessons/p07-02/self_attention.py
# edit, then:
python lessons/p07-02/self_attention.py
```

With the mask, the heatmap's upper triangle is empty: token 3 can't see token 4. That's a *causal* (decoder) model, and it's why generation goes left to right, one token at a time.

## Task 2: make it real: time to first token

```bash
python lessons/p07-02/ttft_lab.py            # local MLX
python lessons/p07-02/ttft_lab.py --remote   # optional: same test on Gemma 26B via the Gemini API
```

What it does ([ttft_lab.py](ttft_lab.py)): sends prompts of ~250 to ~16K tokens of nginx log lines (each prompt unique, so nothing is cached) and streams the reply. It prints:

- **TTFT**: seconds until the first answer token = the prefill over the whole prompt
- **ms per 1K prompt tokens**: is the cost per token constant, or does it grow?
- **decode tok/s**: generation speed after the first token

<details><summary>My test run (Mac mini, gemma-4-e4b) — look after your own run</summary>

```
 ≈prompt tokens   TTFT s  ms per 1K prompt tok  decode tok/s
            270     0.30                  1112          65.3
            990     0.84                   853          66.3
           3960     3.33                   841          63.2
           8010     6.72                   839          58.8
          16020    14.05                   877          53.7
```

</details>

## Cleanup

Ctrl+C in terminal 1 stops the model server (frees ~5 GB). `exit`, then `make down` if you're done for the day.

## Errata and gotchas

- The article treats attention as the whole cost. In a real model, the O(n) matrix multiplications in the other layers dominate until prompts get long, so prefill time grows close to linearly at these sizes; the n² part shows up at much longer contexts.
- `--remote` TTFT includes network and queueing at Google, so it's not comparable to local prefill; it's there to show the difference, not to benchmark.
- `ms per 1K` for the shortest prompt is high because of fixed per-request overhead (template, scheduling), not attention.
