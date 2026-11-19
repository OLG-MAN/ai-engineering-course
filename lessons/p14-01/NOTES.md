# p14-01: The agent loop

| Field | Value |
| --- | --- |
| Upstream | <https://aiengineeringfromscratch.com/learn/agent-engineering/the-agent-loop> |
| Dates | → |
| Time | 60 min estimate / actual min |
| Quiz | x / y |

## Questions to answer (my words)

1. Name the five ingredients and point to the line in `agent_loop.py` that implements each one.
2. "No tool calls = done" vs an explicit `finish` tool: what can go wrong with each? Which would I put in production, and why?
3. Why did the `--naive` run get stuck? Was it the model's fault, the tool's, or the loop's?
4. What does a good observation look like? Rewrite one raw kubectl error from today as an observation a model can act on.
5. Tokens grew faster than turns. Why? Which budget (turns or tokens) protects my bill, and which protects against a stuck loop?
6. The agent filed `billing` as APP_CRASH although SECURITY existed. How would I make sure injection attempts are always flagged, without trusting the model to notice?

## Key ideas

-

## Infra analogy

## Results

| Run | turns | tokens | outcome |
| --- | --- | --- | --- |
| `--stop no-tools` |  |  |  |
| `--stop finish --naive` |  |  |  |
| `--stop finish` |  |  |  |
| `--max-tokens 3000` |  |  |  |

## Gotchas

-

## Open questions / feeds into

- [ ]
