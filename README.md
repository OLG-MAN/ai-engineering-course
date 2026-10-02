# AI Engineering Journey

A 13-week, self-built AI Engineering course: from Senior DevOps/CloudOps engineer to AI Engineer / AIOps.
This repo is my learning journal: the plan, my notes in my own words, re-implemented labs, and small exercises.

- **Plan (source of truth):** [PLAN.md](PLAN.md)
- **Progress and weekly reviews:** [progress.md](progress.md)
- **Capstone:** OpsCopilot, an incident-response assistant for Kubernetes — separate repo: `TBD`

## Timeline

| Block | Dates | Focus | Checkpoint |
| --- | --- | --- | --- |
| 1 | 5 – 25 Oct 2026 | LLMs, API integration, prompt engineering | CP1 — Sun 25 Oct |
| 2 | 26 Oct – 15 Nov | Ingestion, vector search, RAG, evals | CP2 — Sun 15 Nov |
| — | Mon 16 Nov, 23:00 | AI Dev Tools Zoomcamp 2026 — Project 2 submission | Peer review |
| 3 | 16 Nov – 6 Dec | Agents, MCP, memory, AI-first DevEx | CP3 — Sun 6 Dec |
| 4 | 7 – 27 Dec | API layer, vLLM, guardrails, observability, system design | CP4 / Demo Day — Sun 27 Dec |
| Buffer | 28 – 31 Dec | Capstone polish, write-up | — |

Pace: \~2 h/day, 5 days/week (\~10 h/week, \~130 h total).

## Where I learn

Five platforms plus official tool docs — nothing else:

| Platform | What I use it for |
| --- | --- |
| [DataTalks.Club](https://courses.datatalks.club/) | LLM Zoomcamp, AI Dev Tools Zoomcamp, community and peer review |
| [DeepLearning.AI](https://www.deeplearning.ai/courses?types=course) | RAG, Agentic AI, Transformers in Practice + production short courses |
| [Hugging Face Learn](https://huggingface.co/learn) | LLM Course, Agents Course, Context Course |
| [Claude Academy](https://academy.claude.com/courses) | Claude API, prompt evals, MCP |
| [LangChain Academy](https://academy.langchain.com/collections) | LangGraph, Deep Agents, agent observability and evaluation |

## Repo layout

```
.
├── PLAN.md                       # the curriculum, lesson by lesson
├── ai-engineer-course-prompt.md  # the research brief that produced PLAN.md
├── progress.md                   # weekly table, checkpoints, weekly review log
├── onboarding.md                 # accounts, enrollments, setup checklist
├── CLAUDE.md                     # context and rules for Claude Code
├── notes/
│   ├── block1-llm-prompting/
│   ├── block2-rag-evals/
│   ├── block3-agents-mcp/
│   └── block4-production/        # one file per lesson + checkpoint-N.md
├── labs/                         # my re-implementations of course labs on my own stack
├── exercises/                    # small per-lesson tasks
├── templates/                    # lesson-note, lab-note, weekly-review
├── scripts/check_links.py        # dead-link checker for PLAN.md
└── .github/workflows/            # ci (pre-commit + gitleaks), links (weekly)
```

Setup: `cp .env.example .env` and `pre-commit install`. Full checklist in [onboarding.md](onboarding.md).

## How I work

1. **Study** the lesson's primary source from PLAN.md, then the secondary one if needed.
2. **Build** the lesson's hands-on exercise — in `exercises/`, or in the capstone repo when it belongs there.
3. **Write** the lesson note in my own words, using a template from `templates/`.
4. **Commit** small, with conventional messages.
5. **Review** every Sunday: update `progress.md`, then post progress in DataTalks.Club Slack.

## Rules I keep

- **Notes in my own words.** No course notebooks, lab code or graded-assignment solutions from DeepLearning.AI (or any paid course) in this repo.
- **`labs/` holds re-implementations only:** the course pattern ported to my stack (e.g. Weaviate → Qdrant, Oracle → Postgres, LangSmith → Langfuse, vendor SDK → OpenAI-compatible client).
- **Model-agnostic by default:** code talks to an OpenAI-compatible API (hosted, vLLM or Ollama) unless a lesson is explicitly vendor-specific.
- **No secrets in git:** keys live in `.env`; pre-commit runs a secret scanner.

## Follow along

I learn in public. Progress posts go to DataTalks.Club Slack and LinkedIn (`#aidevtools` for the AI Dev Tools cohort).
Feedback and issues are welcome.
