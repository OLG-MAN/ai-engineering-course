# Track

My curated path through [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch). Lesson links go to the course website (`/learn/<phase>/<lesson>`, same slugs as `phases/NN-<phase>/LL-<lesson>` in the repo, minus the numbers). The site follows upstream `main`, which changes daily: `scripts/check_track.py` and the weekly `track` workflow report links that stopped resolving (lesson renamed or removed); when that happens, fix the link and title.

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
| 🟨 | `p10-01` | [Tokenizers: BPE, WordPiece, SentencePiece](https://aiengineeringfromscratch.com/learn/llms-from-scratch/tokenizers) | 90 |  |
| ⬜ | `p07-02` | [Self-Attention from Scratch](https://aiengineeringfromscratch.com/learn/transformers-deep-dive/self-attention-from-scratch) *(opt)* | 90 |  |
| ⬜ | `p07-12` | [KV Cache, Flash Attention & Inference Optimization](https://aiengineeringfromscratch.com/learn/transformers-deep-dive/kv-cache-flash-attention) *(opt)* | 75 |  |
| ⬜ | `p11-01` | [Prompt Engineering: Techniques & Patterns](https://aiengineeringfromscratch.com/learn/llm-engineering/prompt-engineering) | 90 |  |
| ⬜ | `p11-02` | [Few-Shot, Chain-of-Thought, Tree-of-Thought](https://aiengineeringfromscratch.com/learn/llm-engineering/few-shot-cot) | 45 |  |
| ⬜ | `p11-03` | [Structured Outputs: JSON, Schema Validation, Constrained Decoding](https://aiengineeringfromscratch.com/learn/llm-engineering/structured-outputs) | 90 |  |
| ⬜ | `p11-05` | [Context Engineering: Windows, Budgets, Memory, and Retrieval](https://aiengineeringfromscratch.com/learn/llm-engineering/context-engineering) | 90 |  |
| ⬜ | `p11-09` | [Function Calling & Tool Use](https://aiengineeringfromscratch.com/learn/llm-engineering/function-calling) | 75 |  |

## Stage 2 — Retrieval, RAG and evals

GCP milestone after this stage: **G2** (see [gcp/README.md](gcp/README.md#g2)). Core ≈ 7 h, optional ≈ 9 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p11-04` | [Embeddings & Vector Representations](https://aiengineeringfromscratch.com/learn/llm-engineering/embeddings) | 75 |  |
| ⬜ | `p11-06` | [RAG (Retrieval-Augmented Generation)](https://aiengineeringfromscratch.com/learn/llm-engineering/rag) | 90 |  |
| ⬜ | `p11-07` | [Advanced RAG (Chunking, Reranking, Hybrid Search)](https://aiengineeringfromscratch.com/learn/llm-engineering/advanced-rag) | 90 |  |
| ⬜ | `p11-10` | [Evaluation & Testing LLM Applications](https://aiengineeringfromscratch.com/learn/llm-engineering/evaluation) | 45 |  |
| ⬜ | `p11-11` | [Caching, Rate Limiting & Cost Optimization](https://aiengineeringfromscratch.com/learn/llm-engineering/caching-cost) | 45 |  |
| ⬜ | `p11-15` | [Prompt Caching and Context Caching](https://aiengineeringfromscratch.com/learn/llm-engineering/prompt-caching) | 60 |  |
| ⬜ | `p19-64` | [Chunking Strategies, Compared](https://aiengineeringfromscratch.com/learn/capstone-projects/chunking-strategies-advanced) *(opt)* | 90 |  |
| ⬜ | `p19-65` | [Hybrid Retrieval with BM25 and Dense Embeddings](https://aiengineeringfromscratch.com/learn/capstone-projects/hybrid-retrieval-bm25-dense) *(opt)* | 90 |  |
| ⬜ | `p19-66` | [Cross-Encoder Reranker](https://aiengineeringfromscratch.com/learn/capstone-projects/reranker-cross-encoder) *(opt)* | 90 |  |
| ⬜ | `p19-67` | [Query Rewriting: HyDE, Multi-Query, and Decomposition](https://aiengineeringfromscratch.com/learn/capstone-projects/query-rewriting-hyde) *(opt)* | 90 |  |
| ⬜ | `p19-68` | [RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance](https://aiengineeringfromscratch.com/learn/capstone-projects/rag-eval-precision-recall) *(opt)* | 90 |  |
| ⬜ | `p19-69` | [End-to-End RAG System](https://aiengineeringfromscratch.com/learn/capstone-projects/end-to-end-rag-system) *(opt)* | 90 |  |

## Stage 3 — Tools and MCP

GCP milestone after this stage: **G3** (see [gcp/README.md](gcp/README.md#g3)). Core ≈ 20 h, optional ≈ 12 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p13-01` | [The Tool Interface — Why Agents Need Structured I/O](https://aiengineeringfromscratch.com/learn/tools-and-protocols/the-tool-interface) | 45 |  |
| ⬜ | `p13-02` | [Function Calling Deep Dive — OpenAI, Anthropic, Gemini](https://aiengineeringfromscratch.com/learn/tools-and-protocols/function-calling-deep-dive) | 75 |  |
| ⬜ | `p13-03` | [Parallel Tool Calls and Streaming with Tools](https://aiengineeringfromscratch.com/learn/tools-and-protocols/parallel-and-streaming-tool-calls) | 75 |  |
| ⬜ | `p13-04` | [Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding](https://aiengineeringfromscratch.com/learn/tools-and-protocols/structured-output) | 75 |  |
| ⬜ | `p13-05` | [Tool Schema Design — Naming, Descriptions, Parameter Constraints](https://aiengineeringfromscratch.com/learn/tools-and-protocols/tool-schema-design) | 45 |  |
| ⬜ | `p13-06` | [MCP Fundamentals: Stateless Requests and JSON-RPC](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-fundamentals) | 55 |  |
| ⬜ | `p13-07` | [Building an MCP Server: Stateless Python and TypeScript](https://aiengineeringfromscratch.com/learn/tools-and-protocols/building-an-mcp-server) | 85 |  |
| ⬜ | `p13-08` | [Building an MCP Client: Discovery, Routing, and Dual-Era Fallback](https://aiengineeringfromscratch.com/learn/tools-and-protocols/building-an-mcp-client) | 85 |  |
| ⬜ | `p13-09` | [MCP Transports: stdio and Stateless Streamable HTTP](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-transports) | 65 |  |
| ⬜ | `p13-10` | [MCP Resources and Prompts: Addressable Context for Stateless Servers](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-resources-and-prompts) | 60 |  |
| ⬜ | `p13-11` | [MCP Model Input: Sampling Migration and Stateless MRTR](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-sampling) *(opt)* | 75 |  |
| ⬜ | `p13-12` | [Explicit Scope and Stateless Elicitation](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-roots-and-elicitation) *(opt)* | 60 |  |
| ⬜ | `p13-13` | [MCP Tasks Extension: Durable Work on a Stateless Core](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-async-tasks) *(opt)* | 90 |  |
| ⬜ | `p13-15` | [MCP Security: Poisoned Metadata, Routing, and MRTR State](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-security-tool-poisoning) | 60 |  |
| ⬜ | `p13-16` | [MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-security-oauth-2-1) | 90 |  |
| ⬜ | `p13-17` | [Stateless MCP Gateways and Registry Admission](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-gateways-and-registries) | 75 |  |
| ⬜ | `p13-18` | [MCP Auth in Production: Issuer-Bound Enrollment and Tokens](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-auth-production) | 90 |  |
| ⬜ | `p13-19` | [A2A — Agent-to-Agent Protocol](https://aiengineeringfromscratch.com/learn/tools-and-protocols/a2a-protocol) *(opt)* | 75 |  |
| ⬜ | `p13-20` | [OpenTelemetry GenAI — Tracing Tool Calls End-to-End](https://aiengineeringfromscratch.com/learn/tools-and-protocols/opentelemetry-genai) | 75 |  |
| ⬜ | `p13-21` | [LLM Routing Layer — LiteLLM, OpenRouter, Portkey](https://aiengineeringfromscratch.com/learn/tools-and-protocols/llm-routing-layer) | 45 |  |
| ⬜ | `p13-22` | [Agent Skills: Portable Contract and Runtime Boundary](https://aiengineeringfromscratch.com/learn/tools-and-protocols/skills-and-agent-sdks) | 90 |  |
| ⬜ | `p13-28` | [MCP Tool Contracts and Content](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-tool-contracts-and-content) *(opt)* | 120 |  |
| ⬜ | `p13-29` | [MCP Reliability, Cancellation, and Flow Control](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-reliability-cancellation-and-flow-control) *(opt)* | 120 |  |
| ⬜ | `p13-30` | [MCP Registry Supply Chain: Admission, Drift, and Rollback](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-registry-supply-chain-and-drift) *(opt)* | 90 |  |
| ⬜ | `p13-31` | [MCP Conformance Engineering: Versioning, Evidence, and Operations](https://aiengineeringfromscratch.com/learn/tools-and-protocols/mcp-conformance-versioning-and-operations) *(opt)* | 100 |  |

## Stage 4 — Agents

GCP milestone after this stage: **G4** (see [gcp/README.md](gcp/README.md#g4)). Core ≈ 21 h, optional ≈ 8 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p14-01` | [The Agent Loop: Observe, Think, Act](https://aiengineeringfromscratch.com/learn/agent-engineering/the-agent-loop) | 60 |  |
| ⬜ | `p14-02` | [ReWOO and Plan-and-Execute: Decoupled Planning](https://aiengineeringfromscratch.com/learn/agent-engineering/rewoo-plan-and-execute) | 60 |  |
| ⬜ | `p14-03` | [Reflexion: Verbal Reinforcement Learning](https://aiengineeringfromscratch.com/learn/agent-engineering/reflexion-verbal-rl) | 60 |  |
| ⬜ | `p14-05` | [Self-Refine and CRITIC: Iterative Output Improvement](https://aiengineeringfromscratch.com/learn/agent-engineering/self-refine-and-critic) *(opt)* | 60 |  |
| ⬜ | `p14-06` | [Tool Use and Function Calling](https://aiengineeringfromscratch.com/learn/agent-engineering/tool-use-and-function-calling) | 60 |  |
| ⬜ | `p14-07` | [Agent Memory — Virtual Context and Memory Paging](https://aiengineeringfromscratch.com/learn/agent-engineering/memory-virtual-context-memgpt) | 75 |  |
| ⬜ | `p14-09` | [Hybrid Memory: Vector + Graph + KV](https://aiengineeringfromscratch.com/learn/agent-engineering/hybrid-memory-mem0) *(opt)* | 75 |  |
| ⬜ | `p14-12` | [Anthropic's Workflow Patterns: Simple Over Complex](https://aiengineeringfromscratch.com/learn/agent-engineering/anthropic-workflow-patterns) | 60 |  |
| ⬜ | `p14-13` | [Stateful Graph Orchestration — Durable Execution and Checkpoints](https://aiengineeringfromscratch.com/learn/agent-engineering/langgraph-stateful-graphs) | 75 |  |
| ⬜ | `p11-17` | [Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration](https://aiengineeringfromscratch.com/learn/llm-engineering/agent-framework-tradeoffs) *(opt)* | 45 |  |
| ⬜ | `p14-17` | [The Harness as a Library — Subagents and Session Store](https://aiengineeringfromscratch.com/learn/agent-engineering/claude-agent-sdk) | 75 |  |
| ⬜ | `p14-23` | [OpenTelemetry GenAI Semantic Conventions](https://aiengineeringfromscratch.com/learn/agent-engineering/otel-genai-conventions) | 60 |  |
| ⬜ | `p14-24` | [Agent Observability: Langfuse, Phoenix, Opik](https://aiengineeringfromscratch.com/learn/agent-engineering/agent-observability-platforms) | 45 |  |
| ⬜ | `p14-26` | [Failure Modes: Why Agents Break](https://aiengineeringfromscratch.com/learn/agent-engineering/failure-modes-agentic) | 60 |  |
| ⬜ | `p14-27` | [Prompt Injection and the PVE Defense](https://aiengineeringfromscratch.com/learn/agent-engineering/prompt-injection-defense) | 75 |  |
| ⬜ | `p14-28` | [Orchestration Patterns: Supervisor, Swarm, Hierarchical](https://aiengineeringfromscratch.com/learn/agent-engineering/orchestration-patterns) | 60 |  |
| ⬜ | `p14-29` | [Production Runtimes: Queue, Event, Cron](https://aiengineeringfromscratch.com/learn/agent-engineering/production-runtimes) | 60 |  |
| ⬜ | `p14-30` | [Eval-Driven Agent Development](https://aiengineeringfromscratch.com/learn/agent-engineering/eval-driven-agent-development) | 60 |  |
| ⬜ | `p15-12` | [Long-Running Background Agents: Durable Execution](https://aiengineeringfromscratch.com/learn/autonomous-systems/durable-execution) | 60 |  |
| ⬜ | `p15-13` | [Action Budgets, Iteration Caps, and Cost Governors](https://aiengineeringfromscratch.com/learn/autonomous-systems/cost-governors) | 60 |  |
| ⬜ | `p15-14` | [Kill Switches, Circuit Breakers, and Canary Tokens](https://aiengineeringfromscratch.com/learn/autonomous-systems/kill-switches-canaries) | 60 |  |
| ⬜ | `p15-15` | [Human-in-the-Loop: Propose-Then-Commit](https://aiengineeringfromscratch.com/learn/autonomous-systems/propose-then-commit) | 60 |  |
| ⬜ | `p15-16` | [Checkpoints and Rollback](https://aiengineeringfromscratch.com/learn/autonomous-systems/checkpoints-rollback) | 60 |  |
| ⬜ | `p16-05` | [Supervisor / Orchestrator-Worker Pattern](https://aiengineeringfromscratch.com/learn/multi-agent-and-swarms/supervisor-orchestrator-pattern) *(opt)* | 75 |  |
| ⬜ | `p16-11` | [Handoffs and Routines — Stateless Orchestration](https://aiengineeringfromscratch.com/learn/multi-agent-and-swarms/handoffs-and-routines) *(opt)* | 60 |  |
| ⬜ | `p16-22` | [Production Scaling — Queues, Checkpoints, Durability](https://aiengineeringfromscratch.com/learn/multi-agent-and-swarms/production-scaling-queues-checkpoints) *(opt)* | 75 |  |
| ⬜ | `p16-23` | [Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors](https://aiengineeringfromscratch.com/learn/multi-agent-and-swarms/failure-modes-mast-groupthink) *(opt)* | 75 |  |

## Stage 5 — Production and infrastructure

GCP milestone after this stage: **G5** (see [gcp/README.md](gcp/README.md#g5)). Core ≈ 27 h, optional ≈ 4 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p10-11` | [Quantization: Making Models Fit](https://aiengineeringfromscratch.com/learn/llms-from-scratch/quantization) | 120 |  |
| ⬜ | `p10-12` | [Inference Optimization](https://aiengineeringfromscratch.com/learn/llms-from-scratch/inference-optimization) | 120 |  |
| ⬜ | `p11-12` | [Guardrails, Safety & Content Filtering](https://aiengineeringfromscratch.com/learn/llm-engineering/guardrails) | 45 |  |
| ⬜ | `p11-13` | [Building a Production LLM Application](https://aiengineeringfromscratch.com/learn/llm-engineering/production-app) | 120 |  |
| ⬜ | `p11-08` | [Fine-Tuning with LoRA & QLoRA](https://aiengineeringfromscratch.com/learn/llm-engineering/fine-tuning-lora) *(opt)* | 75 |  |
| ⬜ | `p17-01` | [Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/managed-llm-platforms) | 60 |  |
| ⬜ | `p17-02` | [Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/inference-platform-economics) | 60 |  |
| ⬜ | `p17-03` | [GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/gpu-autoscaling-kubernetes) | 75 |  |
| ⬜ | `p17-04` | [Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/vllm-serving-internals) | 75 |  |
| ⬜ | `p17-08` | [Inference Metrics — TTFT, TPOT, ITL, Goodput, P99](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/inference-metrics-goodput) | 60 |  |
| ⬜ | `p17-09` | [Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/production-quantization) | 75 |  |
| ⬜ | `p17-10` | [Cold Start Mitigation for Serverless LLMs](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/cold-start-mitigation) | 60 |  |
| ⬜ | `p17-13` | [LLM Observability Stack Selection](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/llm-observability) | 60 |  |
| ⬜ | `p17-14` | [Prompt Caching and Semantic Caching Economics](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/prompt-semantic-caching) | 60 |  |
| ⬜ | `p17-15` | [Batch APIs — the 50% Discount as Industry Standard](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/batch-apis) *(opt)* | 45 |  |
| ⬜ | `p17-16` | [Model Routing as a Cost-Reduction Primitive](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/model-routing) | 60 |  |
| ⬜ | `p17-18` | [Production Serving Stack — KV Offloading and Cache-Aware Routing](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/vllm-production-stack-lmcache) *(opt)* | 60 |  |
| ⬜ | `p17-19` | [AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/ai-gateways) | 60 |  |
| ⬜ | `p17-20` | [Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/shadow-canary-progressive) | 60 |  |
| ⬜ | `p17-22` | [Load Testing LLM APIs — Why k6 and Locust Lie](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/load-testing-llm-apis) | 75 |  |
| ⬜ | `p17-23` | [SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/sre-for-ai) | 60 |  |
| ⬜ | `p17-24` | [Chaos Engineering for LLM Production](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/chaos-engineering-llm) *(opt)* | 60 |  |
| ⬜ | `p17-25` | [Security — Secrets, API Key Rotation, Audit Logs, Guardrails](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/security-secrets-audit) | 60 |  |
| ⬜ | `p17-27` | [FinOps for LLMs — Unit Economics and Multi-Tenant Attribution](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/finops-llms) | 60 |  |
| ⬜ | `p17-28` | [Self-Hosted Serving Selection — Matching Engine to Hardware and Scale](https://aiengineeringfromscratch.com/learn/infrastructure-and-production/self-hosted-serving-selection) | 45 |  |
| ⬜ | `p18-15` | [Indirect Prompt Injection — Production Attack Surface](https://aiengineeringfromscratch.com/learn/ethics-safety-alignment/indirect-prompt-injection) | 75 |  |
| ⬜ | `p18-16` | [Red-Team Tooling — Garak, Llama Guard, PyRIT](https://aiengineeringfromscratch.com/learn/ethics-safety-alignment/red-team-tooling-garak-llamaguard-pyrit) | 75 |  |

## Capstone

GCP milestone after this stage: **G6** (see [gcp/README.md](gcp/README.md#g6)). Core ≈ 30 h, optional ≈ 0 h.

| Status | ID | Lesson | Min | Notes |
| --- | --- | --- | --- | --- |
| ⬜ | `p19-06` | [Capstone 06 — DevOps Troubleshooting Agent for Kubernetes](https://aiengineeringfromscratch.com/learn/capstone-projects/devops-troubleshooting-agent) | 1800 |  |
