# AI Engineering on 5 Free Platforms: Study Plan v2

Oct 1, 2026 · @OLEG

## 1. Executive summary

**Recommendation: build the whole course from your five platforms plus official tool docs. Core cost ≈ $40 (≈ 1,787 UAH), 3.2% of the reference price, for \~130 hours over 13 weeks (5 Oct – 31 Dec 2026).**

**The reference price.** 55,500 UAH = **$1,242** at the NBU rate of 44.68 UAH/USD for 1 Oct 2026 ($207/month).

**How the five platforms split the work.**

- **DataTalks.Club** — the hands-on spine and the community: LLM Zoomcamp 2026 (ingestion → vector search → RAG → evals → monitoring) and AI Dev Tools Zoomcamp 2026 (coding agents, FastAPI, CI/CD, OpenTelemetry + Grafana, skills/subagents). The AI Dev Tools cohort is live now, with Project 2 due **Mon 16 Nov 2026**.
- **DeepLearning.AI** — the structured theory: the 26-hour *Retrieval Augmented Generation* course (updated Feb 2026), Andrew Ng's *Agentic AI*, *Transformers in Practice*, plus short courses on vLLM (Jun 2026), semantic caching with Redis, guardrails, agent evaluation and agent memory.
- **Hugging Face Learn** — model internals and open-model inference (LLM Course), agents (Agents Course), and context engineering for coding agents (Context Course: skills, MCP, plugins, subagents, hooks).
- **Claude Academy** — API patterns, prompt evaluation, prompt caching, tool use, and the two MCP courses (incl. Streamable HTTP and stateless scaling). Vendor-specific, used only where it is the best source.
- **LangChain Academy** — LangGraph, Deep Agents, and the agent build → test → deploy → monitor loop; optional $99 proctored certification.

**Cost.**

| Item | USD | UAH (44.68) |
| --- | --- | --- |
| All course content on the five platforms | 0 | 0 |
| LLM API credits (estimate) | \~25 | \~1,117 |
| GPU rental for the vLLM lab, a few hours (estimate) | \~15 | \~670 |
| **Core total** | **\~40** | **\~1,787 (3.2%)** |
| Optional: DeepLearning.AI Pro for 1 month (graded labs, certificates; price not shown publicly) | \~30 (confirmed) | \~1,340 |
| Optional: LangChain Certified Agent Engineer exam | 99 | 4,423 |
| **Ceiling with both options** | **\~169** | **\~7,551 (13.6%)** |

**Time.** \~116 h of lessons, exercises and 4 checkpoints + \~14 h capstone polish = **\~130 h** at your 2 h × 5 days.

**Honest headline.** No single platform covers ≥ 60% of the competency map; DeepLearning.AI alone comes closest at \~58%. Together the five reach \~85% (17 full + 7 partial of 24); every partial has a scripted exercise.

**What changed from v1.** O'Reilly, Coursera, Udemy and Maven are gone; the Huyen book is replaced by DeepLearning.AI's RAG and Agentic AI courses as the theory spine. Every link in this version was opened on 1 Oct 2026; the v1 Udemy link was constructed rather than taken from a page and is removed.

## 2. Competency map

The five platforms cover 17 of 24 skills fully and 7 partially; no skill is left uncovered. Abbreviations: **DTC** = DataTalks.Club, **DLAI** = DeepLearning.AI, **HF** = Hugging Face Learn, **CA** = Claude Academy, **LCA** = LangChain Academy.

| # | Competency | Ref. lesson | Sources (5 platforms + official docs) | Coverage |
| --- | --- | --- | --- | --- |
| C1 | AI-engineer role, AI product lifecycle | L1 | DLAI *Agentic AI* (opening module); DTC LLM Zoomcamp capstone guide | Partial |
| C2 | Model internals, size vs capability, sampling, model choice | L2 | DLAI *Transformers in Practice*; HF LLM Course ch.1–2 | Full |
| C3 | Run and evaluate local models (Ollama) | L2–3 | Ollama OpenAI-compatibility docs + own benchmark | Partial |
| C4 | API integration: streaming, structured output, multi-provider | L3 | CA *Building with the Claude API* ("Accessing Claude with the API"); LCA *LangChain Essentials – Python* | Full |
| C5 | Tokenomics; prompt caching | L3, L16 | CA prompt-caching lessons; DLAI vLLM course | Full |
| C6 | Prompt engineering; prompts as versioned, tested code | L4 | CA "Prompt evaluation" + "Prompt engineering techniques" | Full |
| C7 | Ingestion: PDF/DOCX/HTML/OCR, dedup, chunking, metadata | L6 | DTC LLM Zoomcamp dlt workshop; CA chunking + PDF lessons | Partial |
| C8 | Embeddings, vector DBs | L7 | DLAI *RAG* modules 2–3; DTC LLM Zoomcamp module 2; Qdrant docs | Full |
| C9 | Hybrid search (BM25 + dense, RRF) and reranking | L7 | DLAI *RAG* module 2; DTC module 6; CA BM25 + multi-index; Qdrant reranking tutorial | Full |
| C10 | Production RAG: context limits, quality/latency/cost, citations | L8 | DLAI *RAG* modules 4–5; CA citations; DTC module 1 | Full |
| C11 | Eval sets, scoring, LLM-as-judge, hallucination checks | L9 | DTC module 4; CA model/code-based grading; DLAI *Evaluating AI Agents*; LCA *Intro to Agent Observability & Evaluations* | Full |
| C12 | Evals as a CI/CD gate | L9 | LCA *Building Reliable Agents*; DTC AI Dev Tools module 3 (CI deploys only after tests pass) | Full |
| C13 | Agents: ReAct, tool calling, frameworks, execution control | L11 | DLAI *Agentic AI*; HF Agents Course units 1–2; LCA *Intro to LangGraph*; CA "Agents and workflows" | Full |
| C14 | MCP servers and clients | L12 | CA *Intro to MCP* + *MCP: Advanced topics*; HF Context Course unit 2; MCP spec | Full |
| C15 | Agentic RAG, memory, context engineering | L13 | DLAI *Agent Memory*; LCA *Intro to Deep Agents*; HF Context Course unit 4 | Full |
| C16 | AI-first DevEx: coding agents, skills, subagents, hooks | L14 | DTC AI Dev Tools modules 1 & 5; CA *Claude Code in action*, *agent skills*, *subagents*; HF Context Course units 1, 5 | Full |
| C17 | FastAPI: async, background jobs, streaming | L15 | DTC AI Dev Tools module 2 (OpenAPI → FastAPI); FastAPI docs | Partial |
| C18 | Redis caching (exact + semantic), rate limiting | L15 | DLAI *Semantic Caching for AI Agents* (Redis) | Partial |
| C19 | Self-hosted serving: vLLM, quantization, benchmarking | L16 | DLAI vLLM course; HF LLM Course ch.2 "Optimized Inference Deployment"; vLLM production-stack | Full |
| C20 | Cost analysis; prompting vs RAG vs fine-tuning | L16 | DLAI vLLM course; HF LLM Course ch.11 (optional); own cost report | Full |
| C21 | Prompt injection, PII masking, guardrails | L17 | DLAI *Safe and Reliable AI via Guardrails*; OWASP Top 10 for LLM Apps 2026 | Partial |
| C22 | LLM observability: tracing, quality monitoring, alerting | L17 | DTC AI Dev Tools module 4 (OTel → Prometheus, Loki, Tempo, Grafana); LCA *Monitoring Production Agents*; DLAI *Evaluating AI Agents* | Full |
| C23 | System design: gateway, fallback, retrieval/reasoning/memory split | L18 | DLAI *Agentic AI* (later modules); CA MCP stateless-scaling lessons | Partial |
| C24 | Containerized deployment on Kubernetes | L15–18 | DTC AI Dev Tools module 3; vLLM production-stack and Langfuse Helm docs | Full |

Coverage score = (17 + 7 × 0.5) / 24 = **\~85%** (v1 with paid sources: \~88%).

## 3. The five platforms compared

DeepLearning.AI is the strongest single platform (\~58%), DataTalks.Club is the best for hands-on work and community, and the other three fill specific gaps. Coverage % = (full + 0.5 × partial) / 24, from published syllabi.

| Platform | Role in this plan | Courses used | Cost | Format | Community / feedback | Coverage alone | Watch out for |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [DeepLearning.AI](https://www.deeplearning.ai/courses?types=course) | Theory spine + production short courses | RAG (26 h), Agentic AI (\~10 h), Transformers in Practice (11 h); vLLM, Semantic Caching, Guardrails, Evaluating AI Agents, Agent Memory | Videos free; Pro unlocks graded labs and certificates | Self-paced | Forum | \~58% | RAG course uses Weaviate; Agent Memory uses Oracle DB; some short courses marked free "for a limited time" |
| [DataTalks.Club](https://courses.datatalks.club/) | Hands-on spine, deadlines, peer review | LLM Zoomcamp 2026 (self-paced); AI Dev Tools Zoomcamp 2026 (live cohort) | Free | Async cohort / self-paced | \~100k-member Slack; peer-reviewed projects; certificates | \~55% | LLM Zoomcamp 2026 uses pgvector, not Qdrant; no MCP server authoring |
| [Hugging Face Learn](https://huggingface.co/learn) | Model internals, open models, agents, context engineering | LLM Course ch.1–2 (+11 optional); Agents Course units 1–2 + bonus 2; Context Course units 1–5 | Free, free certificates | Self-paced | Discord (course channels) | \~29% | Little on RAG, serving APIs, deployment |
| [Claude Academy](https://academy.claude.com/courses) | API patterns, prompt evals, caching, MCP depth | Building with the Claude API (9 h); Intro to MCP; MCP: Advanced topics; Claude Code in action; agent skills; subagents | Free, completion badges | Self-paced | None on the site | \~33% | Vendor-specific: translate patterns to an OpenAI-style interface |
| [LangChain Academy](https://academy.langchain.com/collections) | Agent frameworks + build/test/deploy/monitor loop | LangChain Essentials; Intro to LangGraph; Intro to Deep Agents; Building Reliable Agents; Monitoring Production Agents; Agent Observability & Evaluations | Free; certification exam $99 | Self-paced | LangChain community + events | \~23% | Tooling is LangSmith (SaaS); mirror it with self-hosted Langfuse |
| **All five together** |  |  | **$0 content** |  |  | **\~85%** |  |

**Not used and why:** DTC MLOps and ML Zoomcamps (classic ML, not LLM apps); DLAI *Generative AI with LLMs* and *Fine-tuning & RL* (optional depth only); HF Robotics, Audio, Diffusion, Deep RL courses (off-topic); Claude Academy AI Fluency and Cowork/Tag courses (end-user topics); Claude Academy Bedrock / Vertex AI courses (similar length and scope to the API course, delivered through AWS/GCP — swap one in if you prefer your cloud's endpoint).

## 4. The course, lesson by lesson

18 lessons in 4 blocks mirror the reference outcomes, with a checkpoint after every block. Each exercise adds to one capstone repo (§7). Pace: \~10 h/week. All items are free and self-paced unless marked.

### Block 1 — LLM & prompt engineering (weeks 1–3, 5–25 Oct, \~26 h)

| Lesson | Primary | Secondary / docs | Hours | Hands-on exercise |
| --- | --- | --- | --- | --- |
| 1. Role of the AI engineer, anatomy of an AI product | DLAI [Agentic AI](https://www.deeplearning.ai/courses/agentic-ai), first module | DTC [LLM Zoomcamp capstone guide](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md); CA [The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook) | 4 | Pick a theme (§7); 1-page design doc + component diagram; repo with CI skeleton and AGENTS.md |
| 2. Foundation models under the hood | DLAI [Transformers in Practice](https://www.deeplearning.ai/courses/transformers-in-practice) (model behavior and deployment modules, \~4 of 11 h) | HF [LLM Course](https://huggingface.co/learn/llm-course) ch.1 and ch.2 "Optimized Inference Deployment" | 6 | Ollama on a Proxmox VM; 3 open models × 20 fixed prompts; sweep temperature/top-p; record quality and tokens/s |
| 3. LLM integration: API + self-hosted | CA [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api): [Accessing the API](https://academy.claude.com/courses/building-with-the-claude-api/accessing-the-api) → [Structured data](https://academy.claude.com/courses/building-with-the-claude-api/structured-data), plus [Prompt caching](https://academy.claude.com/courses/building-with-the-claude-api/prompt-caching) | LCA [LangChain Essentials – Python](https://academy.langchain.com/courses/langchain-essentials-python) (multi-provider, streaming, structured output); [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility.md) | 6 | One provider-agnostic client on the OpenAI-style API: hosted model + Ollama; log tokens, TTFT, latency, $ per call |
| 4. Prompt engineering as engineering | CA [Prompt evaluation](https://academy.claude.com/courses/building-with-the-claude-api/prompt-evaluation) + [Prompt engineering](https://academy.claude.com/courses/building-with-the-claude-api/prompt-engineering) modules | CA [Model based grading](https://academy.claude.com/courses/building-with-the-claude-api/model-based-grading), [Code based grading](https://academy.claude.com/courses/building-with-the-claude-api/code-based-grading) | 6 | Prompts as versioned files; JSON-schema outputs; pytest regression suite with code + model graders, run on 2 providers |
| **Checkpoint 1** | Post CP1 in DTC Slack; ask for review of eval design | Optional: register for the AI Dev Tools cohort (§7) | 4 | Fix top 3 review findings |

### Block 2 — Data, RAG & evals (weeks 4–6, 26 Oct – 15 Nov, \~30 h)

| Lesson | Primary | Secondary / docs | Hours | Hands-on exercise |
| --- | --- | --- | --- | --- |
| 6. Data ingestion & preprocessing | DTC [LLM Zoomcamp dlt workshop](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/workshops/dlt.md) | CA [Text chunking strategies](https://academy.claude.com/courses/building-with-the-claude-api/text-chunking-strategies), [PDF support](https://academy.claude.com/courses/building-with-the-claude-api/pdf-support) | 6 | Ingest your corpus (PDF, Markdown, HTML; OCR one scan); hash dedup; 2 chunking strategies; metadata |
| 7. Embeddings & vector DBs | DLAI [Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) modules 2–3 (BM25, semantic, RRF, vector DBs) | DTC [module 2](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search); [Qdrant hybrid + reranking docs](https://qdrant.tech/documentation/search-precision/reranking-hybrid-search) | 8 | Port the course's Weaviate labs to Qdrant on your K8s; dense + sparse + RRF; Recall@10/MRR vs dense-only |
| 8. Production-grade RAG | DLAI RAG modules 4–5 (generation, production, Phoenix monitoring) | DTC [module 1](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-agentic-rag) + [module 6](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/06-best-practices); CA [Citations](https://academy.claude.com/courses/building-with-the-claude-api/citations), [Multi-Index RAG](https://academy.claude.com/courses/building-with-the-claude-api/a-multi-index-rag-pipeline) | 7 | Reranker; cited answers; quality vs top-k and context size; cost per query |
| 9. Evaluations | DTC [module 4](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/04-evaluation) | LCA [Intro to Agent Observability & Evaluations](https://academy.langchain.com/courses/intro-to-langsmith) | 6 | 50-question golden set; retrieval metrics; LLM-judge calibrated on 20 hand labels; GitHub Actions gate failing a bad PR |
| **Checkpoint 2** | Post CP2 in #course-llm-zoomcamp | Compare with [2025 Zoomcamp projects](https://courses.datatalks.club/llm-zoomcamp-2025/projects) | 3 | "RAG design decisions" note in README |

### Block 3 — Agents & MCP (weeks 7–9, 16 Nov – 6 Dec, \~28 h)

| Lesson | Primary | Secondary / docs | Hours | Hands-on exercise |
| --- | --- | --- | --- | --- |
| 11. Agents & tool orchestration | DLAI [Agentic AI](https://www.deeplearning.ai/courses/agentic-ai) (tool use, planning, evaluation modules) | HF [Agents Course](https://huggingface.co/learn/agents-course) units 1–2; LCA [Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph); CA [Agents and workflows](https://academy.claude.com/courses/building-with-the-claude-api/agents-and-workflows) | 8 | ReAct agent: tool allowlist, max steps, timeouts, human approval for writes |
| 12. MCP | CA [Introduction to MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol) + [MCP: Advanced topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics) | HF [Context Course](https://huggingface.co/learn/context-course) unit 2 (build & deploy a server); [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) | 6 | Two MCP servers on Streamable HTTP (stateless, behind a K8s Service): RAG search + read-only PromQL; connect to your agent and to Claude Code |
| 13. Agentic RAG, memory, context | DLAI [Agent Memory](https://www.deeplearning.ai/short-courses/agent-memory-building-memory-aware-agents) (2026) | LCA [Intro to Deep Agents](https://academy.langchain.com/courses/foundation-introduction-to-deepagents); HF Context Course unit 4 (subagents) | 6 | Retrieval as a tool; long-term memory on Postgres or Qdrant (course uses Oracle DB); eval delta vs linear RAG |
| 14. AI-first DevEx | DTC [AI Dev Tools module 1](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/01-ai-native-workflow/01-ai-native-developer-workflow.md) + [module 5](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/05-agent-capabilities) | CA [Claude Code in action](https://academy.claude.com/courses/claude-code-in-action), [agent skills](https://academy.claude.com/courses/introduction-to-agent-skills), [subagents](https://academy.claude.com/courses/introduction-to-subagents); HF [Context Course unit 5 (hooks)](https://huggingface.co/learn/context-course/unit5/introduction) | 5 | SKILL.md for your repo; hook blocking destructive kubectl/terraform; AI review job in CI; one task in Cline vs Claude Code |
| **Checkpoint 3** | Post CP3 + 3-min demo video in DTC Slack and HF Discord |  | 3 |  |

### Block 4 — Production (weeks 10–12, 7–27 Dec, \~32 h; week 13 is buffer)

| Lesson | Primary | Secondary / docs | Hours | Hands-on exercise |
| --- | --- | --- | --- | --- |
| 15. API layer | DTC [AI Dev Tools module 2](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/02-development/01-build-and-ship-an-ai-assisted-full-stack-app.md) (OpenAPI → FastAPI) | DLAI [Semantic Caching for AI Agents](https://www.deeplearning.ai/short-courses/semantic-caching-for-ai-agents); [FastAPI streaming responses](https://fastapi.tiangolo.com/advanced/custom-response) | 6 | SSE streaming, async calls, background ingestion; Redis exact + semantic cache; Redis token-bucket rate limit |
| 16. Performance & cost | DLAI [Fast & Efficient LLM Inference with vLLM](https://learn.deeplearning.ai/courses/fast-and-efficient-llm-inference-with-vllm) | [vLLM production-stack](https://github.com/vllm-project/production-stack) (Helm, router, Grafana); HF LLM Course ch.11 for the fine-tune option | 8 | Rent one GPU node; deploy via production-stack; benchmark vs hosted API; prompting vs RAG vs fine-tune memo |
| 17. Security, guardrails, observability | DLAI [Safe and Reliable AI via Guardrails](https://www.deeplearning.ai/short-courses/safe-and-reliable-ai-via-guardrails) + DTC [AI Dev Tools module 4](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/04-devops/01-devops-and-observability-for-ai-built-apps.md) | [OWASP LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/); LCA [Monitoring Production Agents](https://academy.langchain.com/courses/production-monitoring); DLAI [Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents); [Langfuse Helm](https://langfuse.com/self-hosting/deployment/kubernetes-helm) | 8 | Injection suite (direct + poisoned doc) in CI; PII masking before logs; OTel → Prometheus/Loki/Tempo/Grafana + Langfuse traces; alerts on cost, p95, judge score |
| 18. System design + Demo Day | DLAI Agentic AI (remaining modules) | LCA [Building Reliable Agents](https://academy.langchain.com/courses/building-reliable-agents); DTC [AI Dev Tools module 3](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/03-deployment/01-test-containerize-and-deploy-an-ai-assisted-app.md) (deploy only after tests pass) | 6 | Gateway with fallback (hosted → vLLM → Ollama) and timeouts; split retrieval / reasoning / memory; publish Demo Day |
| **Checkpoint 4 / Demo Day** | Public write-up, repo, video; post to §8 communities | Optional: LCA certification exam | 4 | Turn reviewer feedback into issues |

**Totals:** 26 + 30 + 28 + 32 = 116 h, plus \~14 h capstone polish in week 13.

## 5. Tool coverage

Every reference tool gets hands-on time; three — Ollama, Qdrant and Cline — are not the main tool of any course on the five platforms, so you practice them through official docs and your own exercises.

| Reference tool | Where you practice it | Status |
| --- | --- | --- |
| OpenAI API | DTC LLM Zoomcamp (OpenAI or Groq keys); LCA LangChain Essentials (multi-provider) | Covered |
| Claude API | CA Building with the Claude API | Covered, vendor-specific |
| Ollama | L2–3 exercises; fallback tier in L18; [Ollama OpenAI-compatibility docs](https://docs.ollama.com/api/openai-compatibility.md) | **Docs + exercise** |
| vLLM | DLAI vLLM course labs; production-stack Helm deploy (L16) | Covered |
| Qdrant | DLAI RAG labs use Weaviate and LLM Zoomcamp 2026 uses pgvector → port both to Qdrant in L7 using [Qdrant docs](https://qdrant.tech/documentation/search-precision/reranking-hybrid-search). The DLAI catalog also lists 3 Qdrant-partner short courses (filter by collaborator "Qdrant") | **Docs + exercise** |
| MCP | CA Intro to MCP + Advanced topics; HF Context Course unit 2; MCP spec | Covered |
| Cursor | DTC AI Dev Tools module 1 (compares agentic IDEs and coding agents) | Covered |
| Claude Code | CA Claude Code in action; HF Context Course (hooks examples); daily work | Covered |
| Cline | No course on the five platforms | **Exercise:** in L14 run one task with Cline on Ollama/vLLM and compare with Claude Code on the same diff |
| Skills | CA Introduction to agent skills; HF Context Course unit 1; DTC AI Dev Tools module 5 | Covered |
| FastAPI | DTC AI Dev Tools module 2 (OpenAPI → FastAPI); [FastAPI docs](https://fastapi.tiangolo.com/advanced/custom-response) | Covered; async jobs by exercise |
| Redis | DLAI Semantic Caching for AI Agents (Redis engineers) | Caching covered; **rate limiting by exercise** |
| Docker | DTC AI Dev Tools module 3 (Compose, Postgres); every lesson | Covered |
| Kubernetes | vLLM production-stack, Langfuse Helm, Qdrant on your cluster | Covered (prior skill) |
| Grafana | DTC AI Dev Tools module 4: OpenTelemetry → Prometheus, Loki, Tempo, Grafana + an actionable alert | Covered |
| *Added:* LangSmith | All LCA courses | SaaS; account needed for the labs |
| *Added:* Langfuse | Self-hosted via Helm in L17 | Open-source mirror of LangSmith so the capstone is not tied to one vendor |
| *Added:* Arize Phoenix | DLAI RAG module 5; DLAI Evaluating AI Agents | Agent/RAG tracing |
| *Added:* GitHub Actions | Eval gate (L9), injection suite (L17), DTC AI Dev Tools module 3 | Uses your stack |

**Model-agnostic rule:** the capstone talks only to an OpenAI-style chat API. vLLM's production stack exposes that interface and Ollama provides it at `/v1/chat/completions`, so hosted and self-hosted models swap by config.

## 6. Budget plan

There are no subscriptions in the core plan: you pay only for API calls and a few GPU hours. Two optional purchases buy proof of completion, not content.

| Month | Paid items | Spend (USD) | Spend (UAH, 44.68) | Notes |
| --- | --- | --- | --- | --- |
| Oct 2026 | API credits | \~8 | \~357 | Use a small model for development; frontier model only for final runs |
| Nov 2026 | API credits; *optional* DLAI Pro, 1 month | \~10 (+ \~30) | \~447 (+ \~1,340) | Nov is when you do the DLAI RAG course — Pro unlocks its 10 graded assignments and the certificate |
| Dec 2026 | API credits; GPU rental by the hour | \~7 + \~15 | \~983 | Rent the GPU only for the L16 benchmark; tear it down the same day |
| Jan 2027 | *Optional* LangChain Certified Agent Engineer exam | (99) | (4,423) | 40 questions, online proctored, valid 24 months |
| **Core total** |  | **\~40** | **\~1,787** | **3.2% of 55,500 UAH** |
| **With both options** |  | **\~169** | **\~7,551** | **13.6%** |

**DLAI Pro price:** \~$30/month, confirmed by you on 1 Oct 2026. One thing still worth checking on a free account: whether the full video set of the RAG and Agentic AI courses plays without Pro — the course page marks only the graded assignments and certificate as Pro.

**Time-limited free access:** DLAI marks Semantic Caching, Evaluating AI Agents and the Guardrails course as free "for a limited time". Enroll in all three in week 1 even though you study them in Block 4.

**Payment from Ukraine:** DLAI uses Stripe; LangChain's exam runs through Talview. Neither advertises USDT/USDC. For API credits, a provider that accepts crypto top-ups would let you pay in USDT/USDC; check its current terms before choosing.

## 7. Capstone

Build **OpsCopilot**, an incident-response assistant for a Kubernetes platform, and submit an early version to the live AI Dev Tools Zoomcamp cohort for peer review by **Mon 16 Nov 2026**.

### Themes

1. **OpsCopilot (recommended).** RAG over runbooks, postmortems and Helm/Terraform READMEs. MCP tools: read-only PromQL, Loki log search, `kubectl get/describe`. The agent drafts a diagnosis and remediation plan; write actions need human approval. It extends AI Dev Tools module 4's "read-only AI on-call responder" into a full product.
2. **IaC PR Reviewer.** RAG over your org's policies and provider docs; an MCP tool runs `terraform plan` and a policy scanner; evals on a labelled set of past PRs.
3. **Cloud Cost Analyst.** RAG over FinOps guidance plus an MCP tool running SQL on GCP/AWS billing exports; answers with cited numbers.

### Spec

- **Data:** dlt ingestion with dedup, chunking, metadata; Qdrant hybrid index with reranking.
- **Reasoning:** agentic RAG with memory; 2+ MCP servers on stateless Streamable HTTP; tool allowlist, step limits.
- **Quality:** 50+ question golden set; retrieval metrics + calibrated LLM-judge; injection suite; both as GitHub Actions gates.
- **Service:** FastAPI with OpenAPI contract, SSE streaming, background jobs, Redis exact + semantic cache, per-key rate limit.
- **Platform:** Docker; Helm charts for app, Qdrant, Langfuse, vLLM; GitOps via Flux.
- **Ops:** OpenTelemetry → Prometheus/Loki/Tempo/Grafana; Langfuse traces and scores; alerts on p95 latency, cost/hour, judge-score drift.
- **Report:** hosted API vs vLLM vs Ollama on the same eval set — quality, TTFT, tokens/s, $ per 1k queries, break-even volume.

### Checkpoints

1. **CP1 — Sun 25 Oct:** provider-agnostic client; prompt regression suite; local-vs-API table.
2. **CP2 — Sun 15 Nov:** ingestion + Qdrant hybrid RAG with citations; golden set; eval gate.
3. **Cohort submission — Mon 16 Nov, 23:00:** AI Dev Tools Zoomcamp **Project 2**. It requires a frontend, a FastAPI backend with an OpenAPI contract, persistent storage, tests, containers, a public deployment, and notes on how AI tools were used. That pulls \~8 h of L15 work into weeks 5–6; in return you get peer reviews and certificate eligibility. Register now and confirm in #course-ai-dev-tools-zoomcamp that late joiners can submit.
4. **CP3 — Sun 6 Dec:** agent with memory using both MCP servers; Claude Code connected to the same servers; demo video.
5. **CP4 / Demo Day — Sun 27 Dec (buffer to Thu 31 Dec):** full K8s deployment, guardrails, observability, cost report, public write-up.

### Reference repos

- [LLM Zoomcamp 07-project-example](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/07-project-example) and [2025 cohort projects](https://courses.datatalks.club/llm-zoomcamp-2025/projects).
- [AI Dev Tools Zoomcamp project folder](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/project) — grading criteria for the cohort submission.
- [vllm-project/production-stack](https://github.com/vllm-project/production-stack) — Helm, router, Prometheus + Grafana dashboard.
- [langfuse/langfuse-k8s](https://github.com/langfuse/langfuse-k8s) — Helm chart for self-hosted Langfuse.

### Demo Day, in public

- **Repo:** README with architecture diagram, eval table, cost report, one-command `make demo`.
- **Write-up:** a blog post built around one finding, e.g. what self-hosting saved or cost.
- **Video:** 5-minute walkthrough.
- **Showcase:** DTC Slack (#course-llm-zoomcamp, #course-ai-dev-tools-zoomcamp), HF Discord, plus the outside communities in §8; LinkedIn posts tagged #aidevtools count as learning in public for the cohort.
- **Second credential:** resubmit to the next LLM Zoomcamp cohort (2026 ran Jun–Aug) for its certificate.

## 8. Community and feedback

DataTalks.Club Slack is the main feedback channel because it is the only one of the five platforms with peer review; the other platforms' forums handle course-specific questions.

### Communities attached to the five platforms

| Community | Use it for | Cost |
| --- | --- | --- |
| [DataTalks.Club Slack](https://datatalks.club/slack.html) — #course-llm-zoomcamp, #course-ai-dev-tools-zoomcamp; Telegram announcements ([AI Dev Tools](https://t.me/aidevtoolszoomcamp), [LLM Zoomcamp](https://t.me/llm_zoomcamp)) | Checkpoint reviews, study buddies, cohort deadlines, peer review | Free |
| [DataTalks.Club events](http://lu.ma/dtc-events) | Live workshops and office hours, recorded to YouTube | Free |
| Hugging Face Discord — #agents-course-questions, #mcp-course-questions | Help with HF courses; open-model questions | Free |
| [DeepLearning.AI Forum](https://community.deeplearning.ai/) | Per-course Q&A threads | Free |
| [LangChain community](https://www.langchain.com/join-community) and [LangChain events](https://lu.ma/langchain) | LangGraph / Deep Agents questions; live sessions | Free |
| Claude Academy | No community linked from the course pages | — |

### Outside the five, still free and international

| Community | Use it for |
| --- | --- |
| [MLOps Community Slack](https://home.mlops.community/public/blogs/mlops-community-20) (31k members; Linux Foundation since May 2026) | The DevOps → AIOps crowd; deployment, observability and evaluation of AI systems; job signals |
| [Latent Space Discord](https://www.latent.space/p/community) (\~11.6k members) | Applied AI-engineering discussion; weekly Paper Club |
| vLLM Slack, #production-stack (linked from the [production-stack repo](https://github.com/vllm-project/production-stack)) | Serving and K8s questions |
| OWASP Slack, #team-genai-top-10-llm | Security review of your guardrails |

**Mentorship without a paid mentor:** the AI Dev Tools cohort peer review (§7), DTC office hours, and LangChain live events are the closest free substitutes for a lecturer's case review.

## 9. Honest gap analysis

Dropping the paid sources costs one coherent textbook and adds vendor tilt; the reference's real advantage is still a single accountable mentor.

| What you lose | Why it matters | Partial compensation |
| --- | --- | --- |
| One accountable mentor reviewing 4 cases + project | Expert eyes catch architecture mistakes early | AI Dev Tools Project 2 peer review (16 Nov); checkpoint posts in DTC Slack; DTC office hours |
| Fixed live pacing | Self-paced plans slip | Calendar the 4 checkpoints and the 16 Nov cohort deadline now; one study buddy from DTC Slack |
| A single textbook-style narrative (v1 used Huyen's *AI Engineering*) | Concepts arrive in one consistent vocabulary | DLAI RAG (26 h) + Agentic AI (\~10 h) act as the narrative; keep a personal glossary in the repo |
| Vendor-neutral labs | Several labs use one vendor's stack: Weaviate (DLAI RAG), Oracle DB (Agent Memory), LangSmith (LangChain), Claude (Claude Academy) | Every exercise ports the pattern to your stack: Qdrant, Postgres, Langfuse, OpenAI-style client |
| Qdrant-first teaching | The reference standardises on Qdrant | Qdrant docs + the porting exercise in L7 |
| A lecturer with production Bedrock experience | War stories and judgment | MLOps Community and Latent Space discussions; DLAI and LangChain courses are taught by the tools' own engineers |
| Local network and a certificate known to Ukrainian employers | Helps local hiring filters | You don't want the bubble; a public repo, DTC certificate and optional LangChain certification carry more weight internationally |

**Risks:** DLAI's "free for a limited time" labels can end — enroll early; platforms move lessons around — re-check links at the start of each block; LangSmith-based labs need a LangSmith account.

## 10. Overlap evidence

Every content lesson of the reference has a free equivalent on your five platforms; only the two Q&A sessions and the lecturer's reviews have none. This compares published syllabi, since the reference's materials are not public.

| Ref. lesson | Closest equivalent on the five platforms | Overlap |
| --- | --- | --- |
| 1. Role of AI engineer | DLAI Agentic AI (opening module); CA AI-native SDLC playbook | Medium |
| 2. Foundation models | DLAI Transformers in Practice; HF LLM Course ch.1–2 | High |
| 3. LLM integration | CA "Accessing Claude with the API" + prompt caching; LCA LangChain Essentials | High |
| 4. Prompt engineering | CA prompt-evaluation + prompt-engineering modules | High |
| 5. Q&A | — | None |
| 6. Ingestion | DTC LLM Zoomcamp dlt workshop; CA chunking + PDF lessons | Medium (OCR/DOCX thin) |
| 7. Embeddings & vector DBs | DLAI RAG modules 2–3; DTC module 2 | High (different vector DB) |
| 8. Production RAG | DLAI RAG modules 4–5; DTC modules 1 & 6; CA citations | Very high |
| 9. Evaluations | DTC module 4; CA eval module; LCA observability & evals; DLAI Evaluating AI Agents | Very high |
| 10. Q&A | — | None |
| 11. Agents | DLAI Agentic AI; HF Agents Course; LCA Intro to LangGraph | Very high |
| 12. MCP | CA Intro to MCP + Advanced topics; HF Context Course unit 2 | Very high |
| 13. Agentic RAG, memory | DLAI Agent Memory; LCA Deep Agents; DTC module 1 | High |
| 14. AI-first DevEx | DTC AI Dev Tools modules 1 & 5; CA Claude Code, skills, subagents; HF Context Course | Very high |
| 15. API layer | DTC AI Dev Tools module 2 (FastAPI); DLAI Semantic Caching (Redis) | High |
| 16. Performance & cost | DLAI vLLM course (Red Hat) | High |
| 17. Security & observability | DLAI Guardrails; DTC AI Dev Tools module 4 (OTel + Grafana); LCA Monitoring Production Agents | High |
| 18. System design + Demo Day | DLAI Agentic AI (later modules); LCA Building Reliable Agents | Medium |

**Reading:** your "localized compilation" hypothesis holds at syllabus level. The reference's flow (model → prompt → data → retrieval → evals → agents → API → production) is the same arc that LLM Zoomcamp and AI Dev Tools Zoomcamp cover between them, in a slightly different order.

## 11. Sources

Every page below was opened (or returned verbatim by search) on 1 Oct 2026; nothing is linked from memory.

| Source | Supports | Note |
| --- | --- | --- |
| [robot\_dreams AI Engineering](https://robotdreams.cc/uk/course/2619-ai-engineering-pipeline) | Reference syllabus and dates | Price not on page; taken from your brief |
| [NBU rate for 1 Oct 2026 (Mezha)](https://mezha.net/eng/news/f1bfccd3_ukraine-s_national_bank/) | 44.68 UAH/USD |  |
| [DataTalks.Club courses](https://courses.datatalks.club/) | Active cohorts and dates |  |
| [AI Dev Tools Zoomcamp 2026 course page](https://courses.datatalks.club/ai-dev-tools-2026/) | Project 1 due 26 Oct, Project 2 due 16 Nov |  |
| [AI Dev Tools Zoomcamp repo](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp) | Modules 1–5, project, certificate rules |  |
| [LLM Zoomcamp repo](https://github.com/DataTalksClub/llm-zoomcamp) | Modules, dlt workshop, capstone |  |
| [DLAI course catalog (type = course)](https://www.deeplearning.ai/courses?types=course) | 13 long courses incl. RAG, Agentic AI, Transformers in Practice |  |
| [DLAI Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) | 26 h, 5 modules, updated 2 Feb 2026, graded labs = Pro |  |
| [DLAI vLLM course](https://learn.deeplearning.ai/courses/fast-and-efficient-llm-inference-with-vllm) | Quantization, vLLM serving, benchmarking (Jun 2026) |  |
| [DLAI Semantic Caching](https://www.deeplearning.ai/short-courses/semantic-caching-for-ai-agents), [Guardrails](https://www.deeplearning.ai/short-courses/safe-and-reliable-ai-via-guardrails), [Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents), [Agent Memory](https://www.deeplearning.ai/short-courses/agent-memory-building-memory-aware-agents) | Lessons 13, 15, 17 | Guardrails dates from Nov 2024 |
| [DLAI membership](https://www.deeplearning.ai/membership) | Pro features | Price confirmed by you: \~$30/month |
| [Hugging Face Learn](https://huggingface.co/learn), [Agents Course](https://huggingface.co/learn/agents-course), [Context Course unit 5](https://huggingface.co/learn/context-course/unit5/introduction), [LLM Course ch.1](https://huggingface.co/learn/llm-course/chapter1/1) | Course list and syllabi | MCP Course no longer listed on the catalog; its material is in Context Course unit 2 |
| [Claude Academy courses](https://academy.claude.com/courses) | Course list |  |
| [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) | 67 lessons, 9 h; per-lesson links used in §4 |  |
| [MCP: Advanced topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics) | Sampling, transports, stateless HTTP |  |
| [LangChain Academy courses](https://academy.langchain.com/collections) (pages 1–3) | Course list |  |
| [LangChain Certified Agent Engineer](https://academy.langchain.com/pages/certifications-lcae) | $99, 40 questions, online proctored |  |
| [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility.md) | `/v1/chat/completions` |  |
| [FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response) | StreamingResponse |  |
| [Qdrant hybrid search + reranking](https://qdrant.tech/documentation/search-precision/reranking-hybrid-search) | L7 porting exercise |  |
| [vLLM production-stack](https://github.com/vllm-project/production-stack) | Helm, Grafana dashboard |  |
| [Langfuse Kubernetes (Helm)](https://langfuse.com/self-hosting/deployment/kubernetes-helm) | Self-hosted tracing |  |
| [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) | OAuth for HTTP MCP servers |  |
| [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | Lesson 17 |  |
| [MLOps Community](https://home.mlops.community/public/blogs/mlops-community-20), [Latent Space community](https://www.latent.space/p/community) | §8 |  |
