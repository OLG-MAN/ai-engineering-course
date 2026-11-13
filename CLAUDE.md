# CLAUDE.md

Working repo for the learner's path through the upstream course [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT), plus a GCP track that rebuilds each stage on Google Cloud. Start: Mon 16 Nov 2026, ~20 weeks. The previous self-built plan is archived on branch `archive/v1-curated-plan` (tag `v1-curated-plan`); don't edit it.

## Key files

- `TRACK.md` — source of truth: curated lessons by stage, schedule, status. Lesson links point at a pinned upstream commit.
- `gcp/README.md` — GCP milestones G1–G6: what to build, which lessons each one upgrades, "done when".
- `LOG.md` — weekly reviews, newest on top.
- `lessons/p<NN>-<LL>/` — the learner's notes (`NOTES.md`) and code per lesson. `gcp/g<N>-<slug>/` — one folder per milestone, with its own Terraform stack.
- `templates/` — `lesson.md`, `gcp-milestone.md`, `weekly-review.md`.
- `scripts/check_track.py` — checks TRACK.md lesson paths exist at upstream HEAD.
- Upstream is expected as a sibling clone at `../ai-engineering-from-scratch`. Read lessons from there; never vendor upstream files into this repo.

## Learner

Senior systems/DevOps engineer (5+ yrs): Python, bash, GCP (Professional Cloud Architect) and AWS, Terraform, Ansible, Docker, K8s, Helm, Flux, Prometheus/Grafana, ELK. Uses Claude Code daily. Goal: AI Engineer or AIOps. ~10 h/week. Explain new ideas through infra analogies; skip DevOps and GCP basics. Dislikes lecture-style, surface-level explanations: go to the mechanism and the numbers.

## Rules

- **Notes are in the learner's own words.** Review, quiz and correct notes; don't write their body text unless asked.
- **The learner types the lesson code.** Help debug and extend it; don't paste whole upstream solutions into `lessons/`.
- **Make it real:** after the stub version works, swap stubs for real models/services through an OpenAI-compatible client configured from `.env`. Vendor SDKs only where a lesson or milestone is about that vendor.
- **GCP:** Terraform for every resource, separate state per milestone, ADC / Workload Identity (no key files), budget alerts on, remind to `terraform destroy` after billable sessions. For model, region, quota, IAM role or flag names that may have changed, give a lookup command instead of asserting.
- **No secrets or real project IDs in git.** Keys live in `.env`; pre-commit runs gitleaks.
- **Commits:** small, Conventional Commits (`feat:`, `docs:`, `notes:`, `chore:`, `infra:` …).
- **Markdown:** don't hard-wrap prose lines.

## Editing TRACK.md

Keep the table format (status, ID, linked title, minutes, notes). When upstream renames or removes a lesson, update the path and title and re-pin all links to the new upstream commit. Keep the schedule and the GCP milestone references in sync with `gcp/README.md`.

## Checks

- `pre-commit run --all-files` — whitespace, YAML, large files, private keys, gitleaks.
- `python3 scripts/check_track.py --upstream ../ai-engineering-from-scratch` — exit 1 if a linked lesson is gone upstream.
- CI: `.github/workflows/ci.yml` (pre-commit on push/PR), `track.yml` (weekly + on TRACK.md changes).
