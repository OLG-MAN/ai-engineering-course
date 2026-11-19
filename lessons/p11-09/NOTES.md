# p11-09: Function calling and tool use

| Field | Value |
| --- | --- |
| Upstream | <https://aiengineeringfromscratch.com/learn/llm-engineering/function-calling> |
| Dates | → |
| Time | 75 min estimate / actual min |
| Quiz | x / y |

## Questions to answer (my words)

1. Draw the function-calling loop. What exactly does the model output when it "calls" a tool, and who executes it?
2. List the guardrails in `k8s_agent.py` and `common/k8s.py`. Why is none of them in the prompt?
3. Why does `prompt=` grow on every step? What's the total input cost vs the last step's prompt, and what did p07-12 show about how a local server handles this?
4. How did the agent handle the injected billing log? What made the agent safe in that moment: the model or the code?
5. Which tool returned the most text? How would I redesign it to give the model what it needs in fewer tokens?
6. Function calling vs structured output (p11-03): when do I use which?

## Key ideas

-

## Infra analogy

## Results

| Model | steps | total in / out tokens | tools called | all 4 causes right? |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Break-it experiments (Task 3):

## Gotchas

-

## Open questions / feeds into

- [ ]
