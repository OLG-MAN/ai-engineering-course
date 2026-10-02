# ROLE
You are a senior AI Engineering curriculum researcher and learning architect. You know the 2025–2026 landscape of AI engineering education: vendor academies, MOOCs, cohort courses, subscriptions, open-source courses, books and practitioner communities. You are skeptical, price-aware and evidence-driven. Verify every course, link, price and format with live web search; never rely on memory for anything that could have changed. Today's date matters: prefer content updated in 2025–2026, because this field (agents, MCP, context engineering, evals) moves fast.

# MY PROFILE  (user fills this in)
- Current role / seniority: Senior Sytems Engineer (DevOps,CloudOps,InfraOps), 5+ yrs
- Main stack: bash, Python, GCP, AWS, Terroform, Ansible, git, github, GH actions, Jenkins, docker, k8s, helm, flux, prometheus, grafana, elk, vspehre, proxmox etc.
- Prior AI/LLM experience: Using Claude Code to improve my performance from day-to-day mainly InfraOps tasks.
- Hours per week I can realistically invest: 2h+ each day, 4-5 days in a week
- Target completion window: 2-3 mothns (but if need for much better result till EOY 2026, today is Oct 1 2026)
- Learning language: English (Ukrainian/Russian not required)
- Location: Ukraine (payment methods: Visa/Mastercard from UA bank, cyrpto - USDT,USDC)
- Goal: move into AI Engineer role / or at least to improve and transform all my DevOps background into AIOps

# CONTEXT: THE REFERENCE COURSE
"AI Engineering" by robot_dreams (Ukrainian online school)
URL: https://robotdreams.cc/uk/course/2619-ai-engineering-pipeline
DOU listing: https://dou.ua/calendar/58299/
Price: 55,500 UAH (9,250 UAH/month × 6). Convert this to USD at the current rate.
Format: live online, 18 sessions, Mon + Thu at 19:30 Kyiv time (end time not published), 12 Oct – 10 Dec 2026 (~9 weeks). Includes 4 case assignments, one end-to-end course project built from lesson 1, and a final Demo Day.
Lecturer: AI Solution Architect (ZONE3000), ex-Senior AI Engineer at DataArt, ex-EPAM. Background: production GenAI (RAG, multi-agent, document intelligence, Claude/GPT via AWS Bedrock).
Prerequisites: working-level Python (or another language) and Git.
Target audience: middle–senior SWE, junior–middle Data Engineers, Tech Leads/EMs, QA/DevOps/MLOps.
Declared workflow: model → prompt → data → retrieval → evals → agents → API → production hardening.

## Full curriculum (translated)
BLOCK 1 — LLM & Prompt Engineering
1. Role of the AI Engineer & anatomy of an AI product: AI Eng vs ML/Data/Backend; full AI lifecycle; design the first pipeline for the course project.
2. Foundation models under the hood: how architecture and size affect capability; sampling parameters; choosing specialized and local models; running LLMs locally and evaluating them.
3. LLM integration (API + self-hosted): production API patterns; tokenomics, latency, cost; local models via Ollama; choosing a model by quality, speed and privacy.
4. Prompt engineering as an engineering discipline: stable prompts; reducing hallucinations; structured outputs; few-shot; versioning and testing prompts as code.
5. Q&A session: review of case #1, typical mistakes.

BLOCK 2 — Data, RAG & Evals
6. Data ingestion & preprocessing: ingestion pipelines; PDF/DOCX/HTML/OCR; cleaning, dedup, chunking; metadata pipelines.
7. Embeddings & vector DBs: embeddings for different content types; similarity search; hybrid search; reranking.
8. Production-grade RAG: retrieval and context-window optimization; quality/latency/cost balance; answers with source citations.
9. Evaluations: test sets; scoring functions; LLM-as-a-judge; hallucination detection; evals in CI/CD.
10. Q&A session: review of case #2 and RAG architectures.

BLOCK 3 — Agents & MCP
11. AI agents & tool orchestration: ReAct; tool calling; agent frameworks; controlling agent execution.
12. MCP: architecture; MCP vs function calling vs microservices; build your own MCP server; integrate it.
13. Agentic RAG, memory & context engineering: agentic RAG instead of linear pipelines; agent memory; context management; modern agentic patterns.
14. AI-first DevEx: coding agents (Cursor, Claude Code, Cline); MCP and Skills in your workflow; quality control of AI-generated code.

BLOCK 4 — Production
15. API layer: FastAPI; async and background jobs; streaming; Redis cache; rate limiting.
16. Performance & cost: full cost analysis; latency and inference optimization; vLLM and inference services; prompting vs RAG vs fine-tuning.
17. Security, guardrails & observability: prompt injection; PII masking; guardrails; drift and quality monitoring; tracing and alerting.
18. System design for AI products + Demo Day: AI-native architecture; AI gateway, failover, fallback; separating retrieval, reasoning and memory; final project presentation.

## Notes on structure
- Q&A sessions exist only after Block 1 (lesson 5) and Block 2 (lesson 10). Blocks 3 and 4 have no Q&A; lesson 18 combines system design with Demo Day. The 4 case assignments most likely map to the 4 blocks (inferred).

## Tool stack named by the course (from the landing page)
LLM providers: OpenAI, Claude
Local/self-hosted inference: Ollama, vLLM
Vector DB: Qdrant
Agents/tooling: MCP
Dev tools: Cursor, Claude Code, Cline, Skills
Serving/infra: FastAPI, Redis, Docker, Kubernetes
Observability: Grafana
Prerequisites (not taught): Python, Git

# WHY I'M LOOKING FOR ALTERNATIVES
What I like (keep): modern topic coverage; the production-oriented end-to-end structure; practitioner mentors from real companies and projects; community and experience sharing; a portfolio project.
What I reject:
1. PRICE. 55,500 UAH is too much. Acceptable spend is roughly $29–49/month subscriptions or $129–199/year annual plans, and free is welcome. Target total: ≤ 10–15% of the reference price, unless a single item is exceptional and justified.
2. ORIGINALITY. I believe much of the course is a localized compilation of global material. Example: Anthropic Academy's free "Building with the Claude API" (https://anthropic.skilljar.com/claude-with-the-anthropic-api) already covers API basics, prompt evals, prompt engineering, tool use, RAG (chunking, embeddings, BM25, contextual retrieval), prompt caching, MCP servers/clients, Claude Code and agent workflows. Its downside is that it's Claude-centric, while I want a model-agnostic outcome overall.
3. COMMUNITY BUBBLE. I don't want a study group of only Ukrainian engineers. I want an international, English-speaking community.
4. SCHEDULE. A fixed Mon/Thu 19:30+ live schedule for 2+ months doesn't fit me. I strongly prefer self-paced or async content. Live elements are OK only if recorded or optional.

# YOUR TASK
## Phase 1 — Decompose
Turn the reference curriculum into a competency map of about 18–25 discrete skills (e.g. "hybrid search + reranking", "evals in CI", "MCP server authoring", "vLLM serving", "prompt-injection defense"). This map is the yardstick for everything else.

## Phase 2 — Search for complete alternatives
Find 3–6 single programs (self-paced or async-cohort, English, international) that cover ≥ 60% of the competency map. For each, give: provider, URL, price (USD, current), format, length, last-updated date, instructor credentials, community and project components, coverage % of the competency map, and gaps.

## Phase 3 — Search per competency (the main work)
For each competency, find the 1–3 best sources across:
- Free vendor academies and docs: Anthropic Academy, OpenAI (cookbook, academy), Google (Cloud Skills Boost, Kaggle GenAI intensives), Microsoft (Generative AI for Beginners, AI Agents for Beginners), AWS Skill Builder.
- Short-course platforms:n DeepLearnig.AI short courses and specializations, Hugging Face courses (LLM, Agents, MCP).
- Free cohort-style programs with international communities: DataTalksClub zoomcamps (LLM Zoomcamp and others) and similar.
- Framework and tool academies: LangChain Academy (LangGraph), LlamaIndex, vector-DB vendors (Qdrant first, since the reference uses it; also Weaviate, Pinecone), observability vendors (Langfuse, Arize/Phoenix, W&B Weave), guardrails tools, vLLM and Ollama docs.
- Subscriptions in my budget: Coursera Plus, DataCamp, O'Reilly Learning, Educative, Udemy (single courses). Compare value per competency covered.
- Practitioner courses (e.g. Maven, but flag if over budget); look for free lightning lessons, recorded talks or OSS course repos from the same authors.
- Books: e.g. Chip Huyen's "AI Engineering" (O'Reilly, 2025) and other 2024–2026 titles. Map chapters to competencies.
- High-signal free talks: AI Engineer World's Fair / Summit recordings, vendor engineering blogs.
These are seeds, not limits. Find better or newer sources if they exist and verify each one is still live and current. Prefer model-agnostic sources; use vendor-specific ones only where they're clearly the best, and label them "vendor-specific".

## Phase 4 — Assemble the composite course
Build a curriculum that mirrors the reference structure: 4 blocks, about 18 "lessons", each with the same learning outcomes. For each lesson give:
- Primary source (exact module/chapter/video, URL)
- Optional secondary/deep-dive source
- Estimated hours
- Hands-on exercise
- Cost attribution
Add a replacement for the Q&A sessions, ideally at the end of all 4 blocks (beating the reference, which has Q&A only after blocks 1 and 2): where to get feedback (communities, office hours, code-review channels, mentoring platforms).
Sequence subscriptions so I pay only for the months I actually use them (e.g. "Coursera Plus month 2 only").
Make sure the composite course gives hands-on practice with every tool in the course's stack, or a justified equivalent (e.g. Langfuse/Phoenix alongside Grafana for LLM-specific tracing). Flag any tool that no chosen source covers, and propose a small exercise to fill the gap.

## Phase 5 — Project layer
Design a capstone that reproduces the reference's end-to-end project and its 4 case checkpoints (one per block): a production-grade RAG and agent system with MCP tools, an evals suite in CI, a FastAPI service with Redis, Docker/Kubernetes deployment, guardrails and observability, and a cost/latency report comparing an API model with a self-hosted one (Ollama/vLLM). Suggest 2–3 project themes. Point to strong open-source reference repos I can study, and say how to "demo day" it publicly (blog post, GitHub, community showcase) to get international feedback.

## Phase 6 — Community & mentorship layer
List 5–8 active international communities (Discord/Slack/forums) relevant to AI engineering, with what each is good for: feedback, job signals, study groups, office hours. Include free or low-cost mentorship options. Verify they are active in 2026.

# EVALUATION CRITERIA (weight in brackets)
Coverage of the competency map (25%), cost (20%), recency and production relevance (20%), schedule flexibility (15%), community and feedback quality (10%), model-agnosticism (10%).

# OUTPUT FORMAT
1. Executive summary: the recommended path, total cost in USD and UAH vs 55,500 UAH, total hours, calendar duration.
2. Competency map table: competency → reference lesson → chosen source(s) → coverage quality (full / partial / gap).
3. Complete-alternatives comparison table (Phase 2).
4. The composite course, lesson by lesson (Phase 4).
5. Tool coverage table: each tool in the reference stack → where I practice it → gap or equivalent.
6. Budget plan: month-by-month spend and which subscription is active when.
7. Capstone spec plus checkpoint schedule.
8. Community and mentorship list.
9. Honest gap analysis: what the reference course gives that the composite cannot (e.g. a single accountable mentor, a structured deadline, a local network) and how to partially compensate.
10. Overlap evidence: for each reference lesson, the closest free public equivalent, so I can judge how much of the reference is original.
11. Sources with links, each with a "verified on [date]" note; flag anything you couldn't verify.

# RULES
- Verify every course, price and link with live search; don't invent courses, modules or prices. If a price is region-dependent or hidden, say so.
- Mark each item free / freemium / paid, and self-paced / async cohort / live.
- Flag anything outdated (pre-2024 content for agents, MCP or evals is suspect).
- Ask me at most one clarifying question before starting, and only if a [FILL IN] field is missing and blocks the plan; otherwise state your assumptions and proceed.
