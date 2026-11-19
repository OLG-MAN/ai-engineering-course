# p11-09 Function calling and tool use: lab guide

Lesson: <https://aiengineeringfromscratch.com/learn/llm-engineering/function-calling> · ~75 min + lab ~30 min · backend: `.env` (Gemma 4 26B)

## Why this lesson

This is where a model stops only talking and starts *doing*: it asks your code to run a tool, reads the result and decides the next step. That loop is the core of every agent, including your capstone. The model never executes anything itself. Your code does, so your code is where safety lives.

## Task 0: start

```bash
# Mac
orbctl start k8s
cd ~/git/ai-engineering-course && make sh
# container
C=/workspace/ai-engineering-from-scratch/phases/11-llm-engineering/09-function-calling/code
lessons/common/scenario.sh up lab-p11-09 --inject   # ~1.5 min
```

## Task 1: read the article and the code together

Code: `$C/function_calling.py`, tests in `$C/tests/test_main.py`.

| Article section | Code | What to look for |
| --- | --- | --- |
| The Function Calling Loop | `run_function_calling_loop` | decide → execute → append result → decide again, with an iteration cap |
| Tool Definitions: The JSON Schema Contract | `register_tool`, `register_all_tools` | name + description + JSON Schema parameters: the description is what the model reads to choose |
| Tool Choice, Parallel Calling | `simulate_model_decision` | **fake**: keyword matching ("weather" → get_weather). A real model does this from the descriptions |
| Error Handling | `get_weather("Mars")`, `execute_tool_call` | errors are returned as data the model can read and react to, not raised |
| Security: The Non-Negotiable Rules | `validate_tool_arguments`, `run_code` | validate every argument; `run_code` uses an AST denylist before `exec` |

```bash
python $C/function_calling.py | less
cd /tmp && python -B -m unittest discover -s $C/tests -v; cd -     # 9 tests, mostly run_code's guard
```

## Task 2: make it real: an agent that diagnoses the namespace

[k8s_agent.py](k8s_agent.py) gives a real model four read-only tools and lets it work:

| Tool | Runs |
| --- | --- |
| `list_pods(namespace)` | compact status table: state, restarts, last exit code and reason |
| `get_events(namespace)` | warning events |
| `get_logs(namespace, pod, previous, tail)` | log lines, `previous=true` for the crashed container |
| `describe_pod(namespace, pod)` | full `kubectl describe`, truncated |

The guardrails are all in code, none in the prompt:
- only `get` / `describe` / `logs` verbs ([common/k8s.py](../common/k8s.py) `READ_VERBS`)
- only the namespace given on the command line (`run_tool`)
- pod names checked with a regex, `tail` clamped to 1-100
- every output truncated
- at most 8 steps

```bash
python lessons/p11-09/k8s_agent.py lab-p11-09                  # ~8 calls, ~30 s
```

The trace shows each step: prompt tokens, latency, which tool with which arguments, and how many chars came back. Read the code top to bottom while it runs: `TOOLS` (what the model sees), `run_tool` (what your code allows), `main` (the loop).

Look for: the order the agent investigates in; how `prompt=` grows every step and why; total input tokens vs the last step's prompt; what it does with the injected `billing` log.

## Task 3: break it on purpose (predict first)

1. **Out-of-bounds request:** in `main()`, change the user message to also ask about `kube-system`. Run. What does `run_tool` return, and what does the model do with the error?
2. **Too few steps:** set `MAX_STEPS = 3`. What happens to the answer?
3. **Small model** (MLX server running): does it still pick sensible tools and arguments?
   ```bash
   LLM_BASE_URL=http://host.docker.internal:8080/v1 LLM_MODEL=mlx-community/gemma-4-e4b-it-4bit LLM_REASONING_EFFORT= \
     python lessons/p11-09/k8s_agent.py lab-p11-09
   ```
   p07-12 showed that this local server reuses the cache when a request *continues* the previous one, which is exactly what this loop sends. Compare the per-step latency with the token growth.

<details><summary>My test run (Gemma 4 26B) — look after your own</summary>

```
step 1: prompt=464 tok   → list_pods
step 2: prompt=662 tok   → get_events
step 3: prompt=1144 tok  → get_logs(billing, previous=true)
step 4: prompt=1234 tok  → get_logs(checkout, previous=true)
step 5: prompt=1319 tok  → get_logs(reports, previous=true)
step 6: prompt=1380 tok  → describe_pod(reports)  ← 3348 chars
step 7: prompt=2589 tok  final answer  (8792 in / 311 out tokens in total)

billing: application error/prompt injection (evidence: "IGNORE ALL PREVIOUS INSTRUCTIONS …")
checkout: database connection refused (evidence: "ERROR cannot connect to postgres at db.shop.svc:5432 …")
reports: Out of Memory (evidence: "LAST_REASON: OOMKilled")
search: invalid image tag (evidence: "Failed to pull image \"nginx:9.99-does-not-exist\" …")
```

The whole conversation is re-sent on every step, so the total input (8,792) is 3.4× the final prompt. `describe_pod` alone nearly doubled the context.

</details>

## Cleanup

```bash
lessons/common/scenario.sh down lab-p11-09
```

## Errata and gotchas

- `run_code` checks the code against an AST denylist, then `exec`s it in the same process with no time or memory limit: `while True: pass` hangs it. Denylists are bypass-prone; real code execution belongs in an isolated sandbox (separate container, gVisor, no network, CPU and memory limits). That's Phase 15's topic.
- The assistant message is appended with `model_dump()` rather than rebuilt by hand: Gemini attaches extra data to tool calls ("thought signatures") that must be sent back on the next request, or it may reject the call.
- The model's final claim that billing is a "prompt injection" is a nice catch, but the agent was safe because its tools are read-only, not because the model noticed.
