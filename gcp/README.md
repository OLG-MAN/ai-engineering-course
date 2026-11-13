# GCP track

The upstream course teaches each mechanism locally, mostly in stdlib Python with stubs. In this track I rebuild each stage as a real system on Google Cloud: managed models, managed data stores, real auth, real deployment, real cost. One milestone closes each stage in [TRACK.md](../TRACK.md). The capstone (G6) reuses G3–G5.

Each milestone lives in `gcp/g<N>-<slug>/` with a README from [templates/gcp-milestone.md](../templates/gcp-milestone.md), its code, and its own Terraform stack (separate state, so `terraform destroy` is cheap and safe).

## Ground rules

- **Personal project, billing budget first.** Before G1: a budget with alerts at 50 / 90 / 100%, and a `bootstrap` Terraform stack (enabled APIs, a least-privilege service account, Artifact Registry). Lives in `gcp/terraform/bootstrap/`.
- **Destroy after every session** that created billable resources (GPU nodes, Vector Search endpoints, AlloyDB). Note the cost of the session in the milestone README.
- **No key files.** ADC locally (`gcloud auth application-default login`), Workload Identity on GKE, service identity on Cloud Run.
- **Verify, don't assume.** Model, region and quota availability change often. Check them in the console or with `gcloud` before designing around them, and write down what I found.
- **Same code, different backend.** Wherever possible keep the OpenAI-compatible client from the lessons and switch `LLM_BASE_URL`; use vendor SDKs (google-genai, ADK, the Anthropic SDK for Claude on Vertex) only where the milestone is about that SDK.

## G1

**Vertex AI models** · after Stage 1 · ~6 h

- **Upgrades:** `p11-01` prompting, `p11-03` structured outputs, `p11-09` function calling.
- **Build:** a small `llm` module with three backends: OpenAI-compatible (local Ollama or hosted), Gemini on Vertex AI, and Claude on Vertex AI (Model Garden partner model). Run the same prompt suite, structured-output schema and tool-calling task on each.
- **GCP:** Vertex AI API, Model Garden (partner models must be enabled per project), ADC, IAM, Billing budgets, Terraform bootstrap.
- **Done when:** one table with pass rate, tokens, latency and cost per backend; bootstrap stack applies and destroys cleanly.
- **Watch for:** partner-model access and per-region quotas; Gemini on Vertex also exposes an OpenAI-compatible endpoint, so check the current docs whether the lesson client works by swapping only the base URL and auth.

## G2

**RAG on GCP** · after Stage 2 · ~10 h

- **Upgrades:** `p11-04` embeddings, `p11-06`/`p11-07` RAG, `p11-10` evaluation, `p11-11`/`p11-15` caching and cost.
- **Build:** ingest a real corpus (my own runbooks or a slice of GCP docs) with Vertex AI embeddings into PostgreSQL with pgvector (Cloud SQL or AlloyDB), hybrid retrieval (full-text + vector), answers with citations. Then the same corpus in Vertex AI RAG Engine as the managed option. The golden-set eval from `p11-10` runs against both and gates CI.
- **GCP:** Vertex AI embeddings, Cloud SQL / AlloyDB + pgvector, Vertex AI RAG Engine, Cloud Run jobs for ingestion, Cloud Storage.
- **Done when:** eval report (recall@k, faithfulness, latency, monthly cost) comparing self-built vs managed, with a recommendation.
- **Watch for:** idle cost of managed vector services; pick the smallest instance tiers and destroy after.

## G3

**MCP on Cloud Run** · after Stage 3 · ~6 h

- **Upgrades:** `p13-07` MCP server, `p13-08` client, `p13-09` transports, `p13-15`–`p13-18` security and auth, `p13-20` OpenTelemetry.
- **Build:** a remote MCP server (streamable HTTP) with read-only GCP tools: list Cloud Run services and GKE workloads, query Cloud Logging, read Cloud Monitoring metrics. Deploy to Cloud Run with authentication required, secrets in Secret Manager, traces to Cloud Trace. Connect both Claude Code and my own client from `p13-08`.
- **GCP:** Cloud Run, IAM / OAuth, Secret Manager, Cloud Logging and Monitoring APIs, Cloud Trace.
- **Done when:** Claude Code uses the remote server, an unauthenticated call is rejected, and one tool call shows end to end in Cloud Trace.

## G4

**Agents on Vertex AI** · after Stage 4 · ~10 h

- **Upgrades:** `p14-01` agent loop, `p14-07` memory, `p14-13` LangGraph, `p14-23`/`p14-24` observability, `p14-30` eval-driven development, `p15-12`–`p15-16` durable execution, cost governors, kill switches, propose-then-commit, rollback.
- **Build:** one agent that uses the G3 MCP tools, two ways: with Google's Agent Development Kit (ADK) deployed to Vertex AI Agent Engine, and as a LangGraph container on Cloud Run. Long jobs via Cloud Tasks or Workflows, a human approval step, a per-task cost cap.
- **GCP:** ADK, Vertex AI Agent Engine, Cloud Run, Cloud Tasks / Workflows, Cloud Trace.
- **Done when:** both deployments pass the same eval set; trace and cost per task for each; a short "when I'd pick which" note.

## G5

**Serving and ops on GKE** · after Stage 5 · ~12 h

- **Upgrades:** `p17-03` GPU autoscaling, `p17-04` vLLM, `p17-08` inference metrics, `p17-10` cold starts, `p17-16` routing, `p17-19` gateways, `p17-20` canary, `p17-22` load testing, `p17-23` SRE for AI, `p17-27`/`p17-28` FinOps and self-hosted selection, `p11-12` and `p18-16` guardrails.
- **Build:** GKE (Terraform) with a spot L4 GPU node pool, vLLM serving a small open model, autoscaling on queue or KV-cache metrics, TTFT/TPOT dashboards via Managed Service for Prometheus + Grafana, a load test, a LiteLLM gateway that falls back from vLLM to Vertex AI, a canary rollout of a new model version, and a guardrail in front (Model Armor or Llama Guard). Compare against the same model on Cloud Run with GPU.
- **GCP:** GKE, GPU node pools, Managed Service for Prometheus, Cloud Monitoring, Cloud Run GPU, Model Armor.
- **Done when:** load-test report and cost per 1M tokens for self-hosted GKE vs Cloud Run GPU vs Vertex API, plus the break-even point.
- **Watch for:** GPU quota per region (request it early, at the start of Stage 5) and stockouts; check with `gcloud compute accelerator-types list --filter="name=nvidia-l4"` and the Quotas page. Destroy the GPU node pool after every session.

## G6

**Capstone: AIOps troubleshooting agent on GKE** · ~10 h on top of upstream `p19-06` (~30 h)

- **Base:** upstream capstone `p19-06` (DevOps troubleshooting agent for Kubernetes), which is designed around the AWS DevOps Agent. This is the GCP version and the successor of the OpsCopilot idea from v1.
- **Build:** demo app on GKE with fault injection → alert from Managed Prometheus / Cloud Monitoring → webhook receiver → the G4 agent with G3 read-only tools over the GKE API, metrics and Cloud Logging → ranked root-cause hypotheses with telemetry citations → brief to Slack or Google Chat with approval buttons → gated remediation (Flux or Argo CD rollback). Models through the G5 gateway. Audit log of every command considered vs executed.
- **Done when:** eval on ~20 synthetic incidents (accuracy of top-1/top-3 root cause, time to hypothesis, cost per incident), demo video, public write-up.
