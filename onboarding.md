# Onboarding

Do this in week 1 (5 – 11 Oct 2026). Items marked ⏰ have a deadline or a time-limited offer.

## Accounts and enrollments

- [ ] ⏰ **DeepLearning.AI** — create a free account; enroll now in the courses marked free "for a limited time" even though they are studied in Block 4:
  - [ ] [Semantic Caching for AI Agents](https://www.deeplearning.ai/short-courses/semantic-caching-for-ai-agents)
  - [ ] [Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents)
  - [ ] [Safe and Reliable AI via Guardrails](https://www.deeplearning.ai/short-courses/safe-and-reliable-ai-via-guardrails)
- [ ] DeepLearning.AI — enroll in [Agentic AI](https://www.deeplearning.ai/courses/agentic-ai), [Transformers in Practice](https://www.deeplearning.ai/courses/transformers-in-practice), [Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation), [vLLM](https://learn.deeplearning.ai/courses/fast-and-efficient-llm-inference-with-vllm), [Agent Memory](https://www.deeplearning.ai/short-courses/agent-memory-building-memory-aware-agents)
- [ ] DeepLearning.AI — on a free account, check that the full RAG and Agentic AI videos play without Pro (decides whether Pro is worth ~$30 in Nov)
- [ ] ⏰ **DataTalks.Club** — register for [AI Dev Tools Zoomcamp 2026](https://courses.datatalks.club/ai-dev-tools-2026/); ask in #course-ai-dev-tools-zoomcamp whether late joiners can submit Project 2 (due **Mon 16 Nov, 23:00**)
- [ ] DataTalks.Club — join [Slack](https://datatalks.club/slack.html) (#course-llm-zoomcamp, #course-ai-dev-tools-zoomcamp) and Telegram ([AI Dev Tools](https://t.me/aidevtoolszoomcamp), [LLM Zoomcamp](https://t.me/llm_zoomcamp)); follow [DTC events](http://lu.ma/dtc-events)
- [ ] DataTalks.Club — star/fork [llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) and [ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
- [ ] **Hugging Face** — account; join Discord (#agents-course-questions, #mcp-course-questions); enroll in [LLM Course](https://huggingface.co/learn/llm-course), [Agents Course](https://huggingface.co/learn/agents-course), [Context Course](https://huggingface.co/learn/context-course)
- [ ] **Claude Academy** — account; enroll in [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api), [Intro to MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol), [MCP: Advanced topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics), [Claude Code in action](https://academy.claude.com/courses/claude-code-in-action), [agent skills](https://academy.claude.com/courses/introduction-to-agent-skills), [subagents](https://academy.claude.com/courses/introduction-to-subagents)
- [ ] **LangChain Academy** — account; LangSmith account (needed by the labs)
- [ ] Outside communities: [MLOps Community Slack](https://home.mlops.community/public/blogs/mlops-community-20), [Latent Space Discord](https://www.latent.space/p/community)

## Keys and billing

- [ ] API keys for one hosted provider (OpenAI-compatible) + Anthropic; set a monthly spend cap on each
- [ ] Check which provider accepts USDT/USDC top-ups (PLAN.md §6) before buying credits
- [ ] Put keys in `.env` (copy from `.env.example`); never commit it
- [ ] Pick a GPU rental provider for the L16 vLLM day (Dec); note price per hour

## Local setup

- [ ] Install [pre-commit](https://pre-commit.com/) and run `pre-commit install` in this repo (gitleaks secret scan + hygiene hooks)
- [ ] Python 3.12+ with `uv` or `venv`
- [ ] Docker + a K8s cluster for Qdrant, Langfuse, the capstone (existing homelab is fine)
- [ ] Ollama on a Proxmox VM; pull 3 small open models for L2
- [ ] Claude Code, Cursor and Cline installed (L14 compares them)
- [ ] Create the capstone repo (OpsCopilot) with CI skeleton and AGENTS.md; link it in README.md

## Calendar

- [ ] Block 2 hours a day, 5 days a week
- [ ] Checkpoints: Sun 25 Oct · Sun 15 Nov · Sun 6 Dec · Sun 27 Dec
- [ ] Project 2 deadline: Mon 16 Nov, 23:00
- [ ] Every Sunday: weekly review in [progress.md](progress.md) + DTC Slack post
- [ ] Start of each block: run `python3 scripts/check_links.py` and fix dead links in PLAN.md
