# p11-05: Context engineering

| Field | Value |
| --- | --- |
| Upstream | <https://aiengineeringfromscratch.com/learn/llm-engineering/context-engineering> |
| Dates | → |
| Time | 90 min estimate / actual min |
| Quiz | x / y |

## Questions to answer (my words)

1. What competes for space in an agent's context window? Which parts grow during a conversation, and which stay fixed?
2. Why did "all events, truncated" miss causes that "snapshot" found with about half the tokens? Where does each failure's evidence actually live in Kubernetes?
3. Lost in the middle: what did I see on the strong vs the small model? Why might a model pay less attention to the middle?
4. The lesson counts tokens as words × 1.3. How far off is that for logs? (Use my p10-01 numbers.)
5. Write three design rules for my capstone agent's tool outputs: size, filtering, order.
6. `reorder_lost_in_middle` puts the best documents at both ends. When would that help, and when is it pointless?

## Key ideas

-

## Infra analogy

## Results

| Context | chars | prompt tokens | checkout | reports | search |
| --- | --- | --- | --- | --- | --- |
| all-events |  |  |  |  |  |
| warnings |  |  |  |  |  |
| snapshot |  |  |  |  |  |

| Model | lines | start | middle | end |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Gotchas

-

## Open questions / feeds into

- [ ]
