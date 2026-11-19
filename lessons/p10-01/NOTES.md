# p10-01: Tokenizers — BPE, WordPiece, SentencePiece

| Field | Value |
| --- | --- |
| Upstream | <https://aiengineeringfromscratch.com/learn/llms-from-scratch/tokenizers> |
| Dates | 2026-11-13 → |
| Time | 90 min estimate / actual min |
| Quiz | x / 5 |

## Questions to answer (my words)

1. What does a model actually receive instead of text? What is the merge table, and why is it frozen after training?
2. Why can't tiktoken count tokens for Claude, Gemma or Qwen? What did the Qwen column show?
3. Bigger vocabulary → fewer tokens. What does it cost in return?
4. My BPE turned "The cat sat on the mat." into 3 tokens. Why was that bad, not good?
5. Which `kubectl get events` format should an agent's tool return, and why? (19,914 vs 2,354 tokens)
6. Why are logs so expensive per byte, and what should happen to them before a model sees them?
7. What does the Ukrainian vs English difference mean when choosing a model?

## Key ideas (my words)

-

## Infra analogy

## Code

## Made it real

| Sample | Bytes | o200k | cl100k | Qwen | My BPE | Tokens/byte (o200k) |
| --- | --- | --- | --- | --- | --- | --- |
| k8s events JSON | 72,329 | 19,914 | 19,654 | 22,667 |  | 0.275 |
| k8s events YAML | 44,364 | 16,309 | 16,181 | 19,194 |  | 0.368 |
| k8s events table | 10,526 | 2,354 | 2,312 | 2,623 |  | 0.224 |
| nginx log (raw) | 77,395 | 34,303 | 34,101 | 44,811 |  | 0.443 |
| nginx log (normalized) |  |  |  |  |  |  |
| paragraph EN | 472 | 101 | 102 | 102 |  | 0.214 |
| paragraph UK | 762 | 155 | 237 | 198 |  | 0.203 |

Same events in all three k8s rows (`kubectl get events -A`, OrbStack cluster, crash-looping busybox + nginx). Terraform plan skipped.

Conclusions:

-

## Gotchas

-

## Open questions / feeds into

- [ ]
