# Track

My curated path through [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch). Lesson links point at upstream commit `8afa245` (pinned on 2026-11-13) because upstream changes daily. `scripts/check_track.py` and the weekly `track` workflow report lessons that were renamed or removed upstream; when that happens, fix the paths and re-pin.

Status: ⬜ not started · 🟨 in progress · ✅ done · ⏭️ skipped. *(opt)* = optional, do it if the stage is on time or the topic is needed for a GCP milestone.

## Schedule

Pace ≈ 10 h/week. Upstream time estimates cover reading and typing the code; I add ~30% for the "make it real" step and notes. Total ≈ 190 h over 20 weeks.

| Weeks | Dates | Stage | Lessons (core) | GCP milestone | Plan h |
| --- | --- | --- | --- | --- | --- |
| 1–2 | 16 Nov – 29 Nov 2026 | 1 LLM engineering basics | ~8 h | G1 Vertex AI models | 16 |
| 3–4 | 30 Nov – 13 Dec | 2 Retrieval, RAG, evals | ~7 h | G2 RAG on GCP | 19 |
| 5–7 | 14 Dec – 3 Jan 2027 | 3 Tools and MCP | ~20 h | G3 MCP on Cloud Run | 32 |
| 8–11 | 4 Jan – 31 Jan | 4 Agents | ~21 h | G4 Agents on Vertex AI | 37 |
| 12–16 | 1 Feb – 7 Mar | 5 Production and infrastructure | ~27 h | G5 Serving and ops on GKE | 47 |
| 17–20 | 8 Mar – 4 Apr | Capstone | ~30 h | G6 AIOps agent on GKE | 40 |

Not in this track on purpose: phases 1–6, 8, 9, 12 (math, classic ML, CV, NLP basics, speech, generative image, RL, multimodal), most of 10 (pre-training) and 18 (alignment research), and the reverse-engineering lessons in 13. Upstream's [learning paths](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/learning-paths) are a good second opinion; this track is close to `building-and-deploying-ai-applications` + `agentic-ai-engineer` + `model-context-protocol`.

## Stage 1 — LLM engineering basics

GCP milestone after this stage: **G1** (see [gcp/README.md](gcp/README.md#g1)). Core ≈ 8 h, optional ≈ 3 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p10-01` | [Tokenizers: BPE, WordPiece, SentencePiece](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/10-llms-from-scratch/01-tokenizers) | 90 |  |
| ⬜ | `p07-02` | [Self-Attention from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/07-transformers-deep-dive/02-self-attention-from-scratch) *(opt)* | 90 |  |
| ⬜ | `p07-12` | [KV Cache, Flash Attention & Inference Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/07-transformers-deep-dive/12-kv-cache-flash-attention) *(opt)* | 75 |  |
| ⬜ | `p11-01` | [Prompt Engineering: Techniques & Patterns](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/01-prompt-engineering) | 90 |  |
| ⬜ | `p11-02` | [Few-Shot, Chain-of-Thought, Tree-of-Thought](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/02-few-shot-cot) | 45 |  |
| ⬜ | `p11-03` | [Structured Outputs: JSON, Schema Validation, Constrained Decoding](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/03-structured-outputs) | 90 |  |
| ⬜ | `p11-05` | [Context Engineering: Windows, Budgets, Memory, and Retrieval](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/05-context-engineering) | 90 |  |
| ⬜ | `p11-09` | [Function Calling & Tool Use](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/09-function-calling) | 75 |  |

## Stage 2 — Retrieval, RAG and evals

GCP milestone after this stage: **G2** (see [gcp/README.md](gcp/README.md#g2)). Core ≈ 7 h, optional ≈ 9 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p11-04` | [Embeddings & Vector Representations](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/04-embeddings) | 75 |  |
| ⬜ | `p11-06` | [RAG (Retrieval-Augmented Generation)](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/06-rag) | 90 |  |
| ⬜ | `p11-07` | [Advanced RAG (Chunking, Reranking, Hybrid Search)](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/07-advanced-rag) | 90 |  |
| ⬜ | `p11-10` | [Evaluation & Testing LLM Applications](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/10-evaluation) | 45 |  |
| ⬜ | `p11-11` | [Caching, Rate Limiting & Cost Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/11-caching-cost) | 45 |  |
| ⬜ | `p11-15` | [Prompt Caching and Context Caching](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/15-prompt-caching) | 60 |  |
| ⬜ | `p19-64` | [Chunking Strategies, Compared](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/19-capstone-projects/64-chunking-strategies-advanced) *(opt)* | 90 |  |
| ⬜ | `p19-65` | [Hybrid Retrieval with BM25 and Dense Embeddings](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/19-capstone-projects/65-hybrid-retrieval-bm25-dense) *(opt)* | 90 |  |
| ⬜ | `p19-66` | [Cross-Encoder Reranker](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/19-capstone-projects/66-reranker-cross-encoder) *(opt)* | 90 |  |
| ⬜ | `p19-67` | [Query Rewriting: HyDE, Multi-Query, and Decomposition](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/19-capstone-projects/67-query-rewriting-hyde) *(opt)* | 90 |  |
| ⬜ | `p19-68` | [RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/19-capstone-projects/68-rag-eval-precision-recall) *(opt)* | 90 |  |
| ⬜ | `p19-69` | [End-to-End RAG System](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/19-capstone-projects/69-end-to-end-rag-system) *(opt)* | 90 |  |

## Stage 3 — Tools and MCP

GCP milestone after this stage: **G3** (see [gcp/README.md](gcp/README.md#g3)). Core ≈ 20 h, optional ≈ 12 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p13-01` | [The Tool Interface — Why Agents Need Structured I/O](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/01-the-tool-interface) | 45 |  |
| ⬜ | `p13-02` | [Function Calling Deep Dive — OpenAI, Anthropic, Gemini](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/02-function-calling-deep-dive) | 75 |  |
| ⬜ | `p13-03` | [Parallel Tool Calls and Streaming with Tools](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls) | 75 |  |
| ⬜ | `p13-04` | [Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/04-structured-output) | 75 |  |
| ⬜ | `p13-05` | [Tool Schema Design — Naming, Descriptions, Parameter Constraints](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/05-tool-schema-design) | 45 |  |
| ⬜ | `p13-06` | [MCP Fundamentals: Stateless Requests and JSON-RPC](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/06-mcp-fundamentals) | 55 |  |
| ⬜ | `p13-07` | [Building an MCP Server: Stateless Python and TypeScript](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/07-building-an-mcp-server) | 85 |  |
| ⬜ | `p13-08` | [Building an MCP Client: Discovery, Routing, and Dual-Era Fallback](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/08-building-an-mcp-client) | 85 |  |
| ⬜ | `p13-09` | [MCP Transports: stdio and Stateless Streamable HTTP](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/09-mcp-transports) | 65 |  |
| ⬜ | `p13-10` | [MCP Resources and Prompts: Addressable Context for Stateless Servers](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/10-mcp-resources-and-prompts) | 60 |  |
| ⬜ | `p13-11` | [MCP Model Input: Sampling Migration and Stateless MRTR](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/11-mcp-sampling) *(opt)* | 75 |  |
| ⬜ | `p13-12` | [Explicit Scope and Stateless Elicitation](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/12-mcp-roots-and-elicitation) *(opt)* | 60 |  |
| ⬜ | `p13-13` | [MCP Tasks Extension: Durable Work on a Stateless Core](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/13-mcp-async-tasks) *(opt)* | 90 |  |
| ⬜ | `p13-15` | [MCP Security: Poisoned Metadata, Routing, and MRTR State](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/15-mcp-security-tool-poisoning) | 60 |  |
| ⬜ | `p13-16` | [MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/16-mcp-security-oauth-2-1) | 90 |  |
| ⬜ | `p13-17` | [Stateless MCP Gateways and Registry Admission](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/17-mcp-gateways-and-registries) | 75 |  |
| ⬜ | `p13-18` | [MCP Auth in Production: Issuer-Bound Enrollment and Tokens](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/18-mcp-auth-production) | 90 |  |
| ⬜ | `p13-19` | [A2A — Agent-to-Agent Protocol](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/19-a2a-protocol) *(opt)* | 75 |  |
| ⬜ | `p13-20` | [OpenTelemetry GenAI — Tracing Tool Calls End-to-End](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/20-opentelemetry-genai) | 75 |  |
| ⬜ | `p13-21` | [LLM Routing Layer — LiteLLM, OpenRouter, Portkey](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/21-llm-routing-layer) | 45 |  |
| ⬜ | `p13-22` | [Agent Skills: Portable Contract and Runtime Boundary](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/22-skills-and-agent-sdks) | 90 |  |
| ⬜ | `p13-28` | [MCP Tool Contracts and Content](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/28-mcp-tool-contracts-and-content) *(opt)* | 120 |  |
| ⬜ | `p13-29` | [MCP Reliability, Cancellation, and Flow Control](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/29-mcp-reliability-cancellation-and-flow-control) *(opt)* | 120 |  |
| ⬜ | `p13-30` | [MCP Registry Supply Chain: Admission, Drift, and Rollback](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift) *(opt)* | 90 |  |
| ⬜ | `p13-31` | [MCP Conformance Engineering: Versioning, Evidence, and Operations](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/13-tools-and-protocols/31-mcp-conformance-versioning-and-operations) *(opt)* | 100 |  |

## Stage 4 — Agents

GCP milestone after this stage: **G4** (see [gcp/README.md](gcp/README.md#g4)). Core ≈ 21 h, optional ≈ 8 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p14-01` | [The Agent Loop: Observe, Think, Act](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/01-the-agent-loop) | 60 |  |
| ⬜ | `p14-02` | [ReWOO and Plan-and-Execute: Decoupled Planning](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/02-rewoo-plan-and-execute) | 60 |  |
| ⬜ | `p14-03` | [Reflexion: Verbal Reinforcement Learning](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/03-reflexion-verbal-rl) | 60 |  |
| ⬜ | `p14-05` | [Self-Refine and CRITIC: Iterative Output Improvement](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/05-self-refine-and-critic) *(opt)* | 60 |  |
| ⬜ | `p14-06` | [Tool Use and Function Calling](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/06-tool-use-and-function-calling) | 60 |  |
| ⬜ | `p14-07` | [Agent Memory — Virtual Context and Memory Paging](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/07-memory-virtual-context-memgpt) | 75 |  |
| ⬜ | `p14-09` | [Hybrid Memory: Vector + Graph + KV](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/09-hybrid-memory-mem0) *(opt)* | 75 |  |
| ⬜ | `p14-12` | [Anthropic's Workflow Patterns: Simple Over Complex](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/12-anthropic-workflow-patterns) | 60 |  |
| ⬜ | `p14-13` | [Stateful Graph Orchestration — Durable Execution and Checkpoints](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/13-langgraph-stateful-graphs) | 75 |  |
| ⬜ | `p11-17` | [Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/17-agent-framework-tradeoffs) *(opt)* | 45 |  |
| ⬜ | `p14-17` | [The Harness as a Library — Subagents and Session Store](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/17-claude-agent-sdk) | 75 |  |
| ⬜ | `p14-23` | [OpenTelemetry GenAI Semantic Conventions](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/23-otel-genai-conventions) | 60 |  |
| ⬜ | `p14-24` | [Agent Observability: Langfuse, Phoenix, Opik](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/24-agent-observability-platforms) | 45 |  |
| ⬜ | `p14-26` | [Failure Modes: Why Agents Break](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/26-failure-modes-agentic) | 60 |  |
| ⬜ | `p14-27` | [Prompt Injection and the PVE Defense](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/27-prompt-injection-defense) | 75 |  |
| ⬜ | `p14-28` | [Orchestration Patterns: Supervisor, Swarm, Hierarchical](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/28-orchestration-patterns) | 60 |  |
| ⬜ | `p14-29` | [Production Runtimes: Queue, Event, Cron](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/29-production-runtimes) | 60 |  |
| ⬜ | `p14-30` | [Eval-Driven Agent Development](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/14-agent-engineering/30-eval-driven-agent-development) | 60 |  |
| ⬜ | `p15-12` | [Long-Running Background Agents: Durable Execution](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/15-autonomous-systems/12-durable-execution) | 60 |  |
| ⬜ | `p15-13` | [Action Budgets, Iteration Caps, and Cost Governors](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/15-autonomous-systems/13-cost-governors) | 60 |  |
| ⬜ | `p15-14` | [Kill Switches, Circuit Breakers, and Canary Tokens](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/15-autonomous-systems/14-kill-switches-canaries) | 60 |  |
| ⬜ | `p15-15` | [Human-in-the-Loop: Propose-Then-Commit](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/15-autonomous-systems/15-propose-then-commit) | 60 |  |
| ⬜ | `p15-16` | [Checkpoints and Rollback](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/15-autonomous-systems/16-checkpoints-rollback) | 60 |  |
| ⬜ | `p16-05` | [Supervisor / Orchestrator-Worker Pattern](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern) *(opt)* | 75 |  |
| ⬜ | `p16-11` | [Handoffs and Routines — Stateless Orchestration](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/16-multi-agent-and-swarms/11-handoffs-and-routines) *(opt)* | 60 |  |
| ⬜ | `p16-22` | [Production Scaling — Queues, Checkpoints, Durability](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints) *(opt)* | 75 |  |
| ⬜ | `p16-23` | [Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink) *(opt)* | 75 |  |

## Stage 5 — Production and infrastructure

GCP milestone after this stage: **G5** (see [gcp/README.md](gcp/README.md#g5)). Core ≈ 27 h, optional ≈ 4 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p10-11` | [Quantization: Making Models Fit](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/10-llms-from-scratch/11-quantization) | 120 |  |
| ⬜ | `p10-12` | [Inference Optimization](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/10-llms-from-scratch/12-inference-optimization) | 120 |  |
| ⬜ | `p11-12` | [Guardrails, Safety & Content Filtering](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/12-guardrails) | 45 |  |
| ⬜ | `p11-13` | [Building a Production LLM Application](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/13-production-app) | 120 |  |
| ⬜ | `p11-08` | [Fine-Tuning with LoRA & QLoRA](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/11-llm-engineering/08-fine-tuning-lora) *(opt)* | 75 |  |
| ⬜ | `p17-01` | [Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/01-managed-llm-platforms) | 60 |  |
| ⬜ | `p17-02` | [Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/02-inference-platform-economics) | 60 |  |
| ⬜ | `p17-03` | [GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes) | 75 |  |
| ⬜ | `p17-04` | [Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/04-vllm-serving-internals) | 75 |  |
| ⬜ | `p17-08` | [Inference Metrics — TTFT, TPOT, ITL, Goodput, P99](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/08-inference-metrics-goodput) | 60 |  |
| ⬜ | `p17-09` | [Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/09-production-quantization) | 75 |  |
| ⬜ | `p17-10` | [Cold Start Mitigation for Serverless LLMs](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/10-cold-start-mitigation) | 60 |  |
| ⬜ | `p17-13` | [LLM Observability Stack Selection](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/13-llm-observability) | 60 |  |
| ⬜ | `p17-14` | [Prompt Caching and Semantic Caching Economics](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/14-prompt-semantic-caching) | 60 |  |
| ⬜ | `p17-15` | [Batch APIs — the 50% Discount as Industry Standard](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/15-batch-apis) *(opt)* | 45 |  |
| ⬜ | `p17-16` | [Model Routing as a Cost-Reduction Primitive](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/16-model-routing) | 60 |  |
| ⬜ | `p17-18` | [Production Serving Stack — KV Offloading and Cache-Aware Routing](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/18-vllm-production-stack-lmcache) *(opt)* | 60 |  |
| ⬜ | `p17-19` | [AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/19-ai-gateways) | 60 |  |
| ⬜ | `p17-20` | [Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/20-shadow-canary-progressive) | 60 |  |
| ⬜ | `p17-22` | [Load Testing LLM APIs — Why k6 and Locust Lie](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/22-load-testing-llm-apis) | 75 |  |
| ⬜ | `p17-23` | [SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/23-sre-for-ai) | 60 |  |
| ⬜ | `p17-24` | [Chaos Engineering for LLM Production](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/24-chaos-engineering-llm) *(opt)* | 60 |  |
| ⬜ | `p17-25` | [Security — Secrets, API Key Rotation, Audit Logs, Guardrails](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/25-security-secrets-audit) | 60 |  |
| ⬜ | `p17-27` | [FinOps for LLMs — Unit Economics and Multi-Tenant Attribution](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/27-finops-llms) | 60 |  |
| ⬜ | `p17-28` | [Self-Hosted Serving Selection — Matching Engine to Hardware and Scale](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/17-infrastructure-and-production/28-self-hosted-serving-selection) | 45 |  |
| ⬜ | `p18-15` | [Indirect Prompt Injection — Production Attack Surface](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/18-ethics-safety-alignment/15-indirect-prompt-injection) | 75 |  |
| ⬜ | `p18-16` | [Red-Team Tooling — Garak, Llama Guard, PyRIT](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit) | 75 |  |

## Capstone

GCP milestone after this stage: **G6** (see [gcp/README.md](gcp/README.md#g6)). Core ≈ 30 h, optional ≈ 0 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p19-06` | [Capstone 06 — DevOps Troubleshooting Agent for Kubernetes](https://github.com/rohitg00/ai-engineering-from-scratch/tree/8afa245ebc2e8861480edf8c4911a2b6d9769688/phases/19-capstone-projects/06-devops-troubleshooting-agent) | 1800 |  |
