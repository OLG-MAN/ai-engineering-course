# p07-12: KV cache, Flash Attention and inference optimization

| Field | Value |
| --- | --- |
| Upstream | <https://aiengineeringfromscratch.com/learn/transformers-deep-dive/kv-cache-flash-attention> |
| Dates | → |
| Time | 75 min estimate / actual min |
| Quiz | x / y |

## Questions to answer (my words)

1. What exactly is stored in the KV cache, and what work does it save on each new token?
2. Write the KV-size formula and explain each factor. Which factor grows with the conversation?
3. Which three Gemma 4 tricks made its KV several times smaller than the formula says? What does each one give up?
4. Flash Attention gives bit-identical results to normal attention. So what does it actually save?
5. In the prefix test, which requests were fast and why? What does that mean for how an agent should build its requests?
6. For G5: roughly how much GPU memory would one 32K-token conversation need on a 70B dense model, and how many could fit on one 80 GB GPU next to the weights?

## Key ideas

-

## Infra analogy

## Results

| Model | context | lesson formula | Gemma-aware |
| --- | --- | --- | --- |
|  |  |  |  |

| Request | seconds | cached_tokens |
| --- | --- | --- |
| cold |  |  |
| same prefix, different question |  |  |
| conversation + new turn |  |  |
| exact repeat |  |  |

## Gotchas

-

## Open questions / feeds into

- [ ]
