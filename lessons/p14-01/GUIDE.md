# p14-01 The agent loop: lab guide

Lesson: <https://aiengineeringfromscratch.com/learn/agent-engineering/the-agent-loop> · ~60 min + lab ~30 min · backend: `.env` (Gemma 4 26B)

Moved into Stage 1 right after p11-09: there you built a loop; here you take it apart into its five ingredients and see what each one is for, mostly by watching it fail.

## Why this lesson

Every agent framework (Claude Agent SDK, OpenAI Agents SDK, LangGraph, ADK in G4) runs the same loop underneath. What makes an agent reliable isn't the loop itself, it's the parts around it: when it stops, what it's allowed to spend, and how tool results are turned into something the model can act on. Your capstone will live or die on those.

## Task 0: start

```bash
# Mac
orbctl start k8s
cd ~/git/ai-engineering-course && make sh
# container
C=/workspace/ai-engineering-from-scratch/phases/14-agent-engineering/01-the-agent-loop/code
lessons/common/scenario.sh up lab-p14-01 --inject   # ~1.5 min
```

## Task 1: read the article and the code together

Code: `$C/main.py` (stdlib, ~180 lines).

| Article section | Code | What to look for |
| --- | --- | --- |
| ReAct: the canonical format | `Turn` (kinds: user, thought, action, final) | the transcript is a list of typed turns: thought → action → observation, repeated |
| The 2026 shift: native reasoning | (no code) | modern APIs keep reasoning in a separate channel and return tool calls as structured data, which is what your p11-09 loop used |
| The five ingredients | `AgentLoop.run`, `ToolRegistry.dispatch`, `max_turns` | buffer = `self.history`; registry = `ToolRegistry`; stop = `kind == "finish"` or `max_turns`; observation = `dispatch` returns a string, even for errors |
| Build It | `ToyLLM` | **the model is a script**: it replays fixed thought/action steps and ignores the history |
| 2026 pitfalls | (no code) | trust boundary, cascading failure, loop length: you'll hit the third one in Task 3 |

```bash
python $C/main.py
```

## Task 2: make it real: one loop, switchable parts

[agent_loop.py](agent_loop.py) is the p11-09 agent rebuilt as a small class, with each ingredient commented by number. Read `Agent.run()` and `Agent.dispatch()` first. Then run the two stop strategies (the lesson's exercise 2):

```bash
python lessons/p14-01/agent_loop.py lab-p14-01 --stop no-tools   # a reply without tool calls = done (p11-09 style)
python lessons/p14-01/agent_loop.py lab-p14-01 --stop finish     # only finish(...) ends it, with a validated report
```

With `--stop finish`, the model must call a `finish` tool whose arguments match a Pydantic `Report` (deployment, category, root cause, evidence). A prose reply is not accepted: the loop nudges it back. Compare the two endings. Which one could a ticketing system or an alert router consume? Which one can end by accident?

## Task 3: watch it get stuck, then see why it doesn't by default

```bash
python lessons/p14-01/agent_loop.py lab-p14-01 --stop finish --naive
```

`--naive` turns off two things in the observation formatter (ingredient 5):

- **Error translation.** For an OOM-killed container, `kubectl logs --previous` returns only `unable to retrieve container logs for docker://…`. By default the agent instead gets: "those logs no longer exist; why it died is in list_pods (LAST_EXIT / LAST_REASON)".
- **Repeat guard.** By default, an identical repeated call returns "you already called this; the result hasn't changed", instead of running it again.

Before running, predict what happens without them. Then read the trace: which pod does it keep coming back to, and why? Hint: `finish` demands a verbatim evidence quote, and the OOM evidence isn't in any log.

## Task 4: budgets

```bash
python lessons/p14-01/agent_loop.py lab-p14-01 --stop finish --max-tokens 3000
python lessons/p14-01/agent_loop.py lab-p14-01 --stop finish --max-turns 4
```

Both stop the run cleanly with partial work. Look at `run total=` per turn: tokens grow faster than turns because the whole buffer is re-sent every turn.

<details><summary>My test runs (Gemma 4 26B) — look after your own</summary>

| Run | Turns | Tokens | Outcome |
| --- | --- | --- | --- |
| `--stop no-tools` | 8 | 6,013 | prose answer, all 4 causes right |
| `--stop finish --naive` | 10 (cap) | 10,655 | stuck re-reading `--previous` logs, never finished |
| `--stop finish` | 9 | 10,701 | validated report, all 4 right, `web` listed as healthy |
| `--stop finish --max-tokens 3000` | 4 | 3,283 | budget stop |

In the default run the agent got the translated error three times, then went straight to `finish`. It filed `billing` as APP_CRASH with the injection text as evidence, though SECURITY was in the enum. Would you accept that?

</details>

## Cleanup

```bash
lessons/common/scenario.sh down lab-p14-01
```

## Errata and gotchas

- `ToyLLM` ignores the history: it can't get stuck, never repeats itself and never misreads an observation. Real loops do all three, which is why Tasks 3 and 4 exist.
- The lesson lists "max tokens" among stop conditions but its code only has `max_turns`. The lab adds a run-wide token budget; for cost control that's the one that matters.
- The repeat guard compares tool name + arguments exactly. A model that alternates `previous=true` and `previous=false` (as in `--naive`) dodges a naive guard on the second call; it still catches the third.
- Free tier: a stuck run burns quota fast. That's the real-world point of budgets.
