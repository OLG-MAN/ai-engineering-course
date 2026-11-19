# p07-02: Self-attention from scratch

| Field | Value |
| --- | --- |
| Upstream | <https://aiengineeringfromscratch.com/learn/transformers-deep-dive/self-attention-from-scratch> |
| Dates | → |
| Time | 90 min estimate / actual min |
| Quiz | x / y |

## Questions to answer (my words)

1. What are Q, K and V, where do they come from, and what does one row of the attention matrix tell you?
2. Why divide the scores by √d_k? What would softmax do without it?
3. What does the causal mask change, and why does a chat model need it?
4. From my TTFT table: how does time-to-first-token grow with prompt length? What does that mean for an agent that sends 16K tokens of logs on every step?
5. Why does decode speed drop a little as the prompt gets longer?
6. Attention is n × n, yet my TTFT grew almost linearly up to 16K tokens. Why?

## Key ideas

-

## Infra analogy

## Results

| ≈prompt tokens | TTFT s | ms / 1K tok | decode tok/s |
| --- | --- | --- | --- |
|  |  |  |  |

## Gotchas

-

## Open questions / feeds into

- [ ]
