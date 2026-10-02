# CLAUDE.md

Learning-journal repo for a self-built, 13-week AI Engineering course (5 Oct – 31 Dec 2026). Docs, notes and small exercises; the capstone (OpsCopilot) lives in a separate repo.

## Key files

- `ai-engineer-course-prompt.md` — the research brief: learner profile, the reference course (robot_dreams "AI Engineering", 55,500 UAH), evaluation criteria and research rules. It produced PLAN.md.
- `PLAN.md` — source of truth: competency map (C1–C24), 18 lessons in 4 blocks, tool coverage, budget, capstone spec, communities, sources.
- `progress.md` — weekly table, checkpoints, spend, weekly review log (newest on top).
- `onboarding.md` — accounts, enrollments, setup checklist.
- `templates/` — `lesson-note.md`, `lab-note.md`, `weekly-review.md`.
- `notes/<block>/` — one file per lesson (`LNN-<slug>.md`), lab notes (`LNN-lab-<slug>.md`), `checkpoint-N.md`. Each block folder has a README index.
- `labs/<slug>/` — re-implementations of course labs. `exercises/<LNN>-<slug>/` — per-lesson tasks.
- `scripts/check_links.py` — stdlib link checker; `python3 scripts/check_links.py [files]`.

## Learner

Senior systems/DevOps engineer (5+ yrs): Python, bash, GCP/AWS, Terraform, Ansible, Docker, K8s, Helm, Flux, Prometheus/Grafana, ELK, Proxmox. Uses Claude Code daily. Goal: AI Engineer or AIOps. ~2 h/day, 5 days/week. Explain new ideas through infra analogies; skip DevOps basics.

## Rules

- **Notes are in the learner's own words.** Review, quiz and correct notes; don't write their body text unless asked.
- **No course material in git:** no notebooks, lab code or graded-assignment solutions from DeepLearning.AI or any course. `labs/` holds re-implementations only.
- **Model-agnostic by default:** code calls an OpenAI-compatible chat API (hosted, vLLM or Ollama) configured from `.env`. Vendor-specific code only when a lesson is explicitly vendor-specific.
- **Port course stacks to the learner's:** Weaviate → Qdrant, Oracle → Postgres, LangSmith → Langfuse.
- **No secrets in git.** Keys live in `.env` (see `.env.example`); pre-commit runs gitleaks.
- **Commits:** small, Conventional Commits (`docs:`, `feat:`, `chore:`, `notes:` …).

## Editing PLAN.md

Follow the brief's rules: verify every course, price and link with live search before adding or changing it; never link from memory; mark free / freemium / paid and self-paced / async cohort / live; flag pre-2024 content on agents, MCP or evals; record a "verified on <date>" note in §11. Keep progress.md and the block READMEs in sync when lessons move. Prices: USD and UAH; budget ceiling ≈ 10–15% of 55,500 UAH. Payments from Ukraine: Visa/Mastercard or USDT/USDC.

## Checks

- `pre-commit run --all-files` — whitespace, YAML, large files, private keys, gitleaks.
- `python3 scripts/check_links.py PLAN.md onboarding.md README.md` — dead links fail; 403/429 are warnings.
- CI: `.github/workflows/ci.yml` (pre-commit on push/PR), `links.yml` (weekly + on plan changes).
