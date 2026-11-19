# p11-03: Structured outputs

| Field | Value |
| --- | --- |
| Upstream | <https://aiengineeringfromscratch.com/learn/llm-engineering/structured-outputs> |
| Dates | → |
| Time | 90 min estimate / actual min |
| Quiz | x / y |

## Questions to answer (my words)

1. Prompt-only JSON, validate-and-retry, native schema: what does each one guarantee, and what doesn't it?
2. What does constrained decoding do at the token level (the lesson's `next_valid_tokens`)? Why can't it produce invalid JSON?
3. "Valid JSON ≠ true." What does my grounding check catch, and what other checks would a real incident pipeline need?
4. Why does the retry message include the model's own previous answer plus the exact error?
5. The Pydantic model is a contract. What breaks downstream if I rename a field or add a category? How would I version it?
6. `checkout` came back as NETWORK or APP_CRASH. Which is right, and is my category list good enough?

## Key ideas

-

## Infra analogy

## Results

| Model | mode | valid JSON | right category | quotes verbatim | tokens |
| --- | --- | --- | --- | --- | --- |
|  | prompt |  |  |  |  |
|  | retry |  |  |  |  |
|  | schema |  |  |  |  |

## Gotchas

-

## Open questions / feeds into

- [ ]
