# AI Engineering Journey

My working repo for [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) ([site](https://aiengineeringfromscratch.com/), MIT, by Rohit Ghumare and contributors), from Senior DevOps/CloudOps engineer to AI Engineer / AIOps.

The upstream course is huge (20 phases, 540+ lessons) and local-first: most lesson code is stdlib Python that simulates the mechanism, with stubs where a real model, vector DB or cluster would be. This repo adds two layers on top of it:

1. **A curated path:** about 100 lessons from the phases that matter for building and running AI systems (LLM engineering, RAG and evals, tools and MCP, agents, production). I skip math, computer vision, speech, RL and pre-training. See [TRACK.md](TRACK.md).
2. **A GCP track:** after each stage I rebuild what I learned as a real deployment on Google Cloud: Vertex AI models, managed retrieval, MCP on Cloud Run, agents on Agent Engine, vLLM on GKE and an AIOps capstone. Everything is Terraform, with budget alerts and teardown. See [gcp/README.md](gcp/README.md).

The previous self-built plan (13 weeks across 5 course platforms) is archived on branch [`archive/v1-curated-plan`](../../tree/archive/v1-curated-plan) and tag `v1-curated-plan`.

## Repo layout

```
.
├── TRACK.md            # curated lesson path, stages, schedule, status (source of truth)
├── LOG.md              # weekly review log, newest on top
├── CLAUDE.md           # context and rules for Claude Code
├── lessons/<id>/       # one folder per lesson I do: NOTES.md + my code (id = p<phase>-<lesson>, e.g. p11-06)
├── gcp/                # GCP track: milestone plan + one folder per milestone (g1-… to g6-…)
├── templates/          # lesson notes, GCP milestone, weekly review
├── scripts/check_track.py   # checks TRACK.md lesson paths still exist upstream
└── .github/workflows/  # ci (pre-commit + gitleaks), track (weekly upstream drift check)
```

## Setup

```bash
# Upstream course next to this repo (read-only reference; fork it on GitHub only if I want to send PRs)
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git ../ai-engineering-from-scratch

cp .env.example .env
pre-commit install
python3 scripts/check_track.py --upstream ../ai-engineering-from-scratch
```

## How I work a lesson

1. **Read** `docs/en.md` of the lesson in the upstream clone. Take the quiz (`quiz.json`) after.
2. **Type** the lesson code into `lessons/<id>/` rather than copying it, and run it.
3. **Make it real:** replace the stub with a real model or service, through an OpenAI-compatible client (hosted, Vertex AI, vLLM or Ollama, set in `.env`). Record numbers: tokens, latency, cost, quality.
4. **Write** `lessons/<id>/NOTES.md` in my own words from [templates/lesson.md](templates/lesson.md), then tick the lesson in TRACK.md.
5. **Ship** the GCP milestone at the end of each stage, in `gcp/g<N>-<slug>/`.
6. **Review** every Sunday in LOG.md.

## Rules I keep

- **Notes in my own words.** Upstream code is MIT, so I may reuse it with attribution, but I type it and change it rather than copy whole lessons.
- **Upstream stays upstream.** I don't vendor upstream files here; TRACK.md links to a pinned upstream commit, and CI flags lessons that were renamed or removed upstream.
- **Model-agnostic by default:** code talks to an OpenAI-compatible API unless a lesson or GCP milestone is explicitly vendor-specific.
- **No secrets in git:** keys live in `.env`; pre-commit runs gitleaks. GCP auth via ADC locally and Workload Identity in GKE/Cloud Run, never key files.
- **Cloud spend is capped:** budget alerts on, everything in Terraform, `terraform destroy` at the end of every session that created billable resources.
