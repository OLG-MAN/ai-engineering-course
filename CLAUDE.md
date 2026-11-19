# CLAUDE.md

Working repo for the learner's path through the upstream course [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT), plus a GCP track that rebuilds each stage on Google Cloud. Start: Mon 16 Nov 2026, ~20 weeks. The previous self-built plan is archived on branch `archive/v1-curated-plan` (tag `v1-curated-plan`); don't edit it.

## Key files

- `TRACK.md` — source of truth: curated lessons by stage, schedule, status. Lesson links go to the course website (`https://aiengineeringfromscratch.com/learn/<phase>/<lesson>`, repo dir names minus the `NN-` prefixes); the learner reads and copies code from there.
- `gcp/README.md` — GCP milestones G1–G6: what to build, which lessons each one upgrades, "done when".
- `LOG.md` — weekly reviews, newest on top.
- `lessons/p<NN>-<LL>/` — the learner's notes (`NOTES.md`) and code per lesson. `gcp/g<N>-<slug>/` — one folder per milestone, with its own Terraform stack.
- `templates/` — `lesson.md`, `gcp-milestone.md`, `weekly-review.md`.
- `scripts/check_track.py` — checks TRACK.md lesson links still resolve on the website (404 = renamed/removed upstream).
- Upstream is also cloned as a sibling at `../ai-engineering-from-scratch` (full `code/`, `quiz.json`, `outputs/`). Read lessons there when helping; never vendor upstream files into this repo or edit the clone.
- `lessons/<id>/GUIDE.md` — Claude's hands-on lab for each lesson, Skills Boost style: Task 0 start, Task 1 article section ↔ lesson code table + run commands, "make it real" tasks on real infra (OrbStack k8s, real LLM) with predict-first steps, my test run in a `<details>` spoiler, cleanup, errata. Test every command before writing it down.
- `lessons/<id>/NOTES.md` — the learner's notes; Claude writes only the header, a "Questions to answer" list (mechanism, the learner's measured numbers, the design decision) and empty result tables.
- `lessons/common/` — `llm.py` (shared OpenAI-compatible client from `.env`, rate-limit waits, strips leaked `<thought>`), `k8s.py` (read-only kubectl), `scenario.sh` (broken namespace: checkout crash loop, reports OOM, search bad image, web healthy, optional billing injection). Labs use namespace `lab-<id>`.
- LLM backends: default Gemma 4 26B on the Gemini API free tier (`LLM_REASONING_EFFORT=minimal`, otherwise answers come back empty); local MLX server on the Mac (`~/git/mlx-lab`, port 8080, `--chat-template-args '{"enable_thinking":false}'`) for p07 labs and lesson scripts with many calls.

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

Keep the table format (status, ID, linked title, minutes, notes). When upstream renames or removes a lesson, update the link and title. Keep the schedule and the GCP milestone references in sync with `gcp/README.md`.

## Lab container

Lesson code runs in the `aicourse-lab` container (`.devcontainer/`, `make sh|down|status|rebuild`), not on the Mac host: the host's `python3` is Xcode's 3.9 and the learner keeps the host free of dev tools. Run commands with `docker compose -f .devcontainer/compose.yaml exec -T lab bash -c '…'`. Python packages go in `requirements.txt` (then `make rebuild`); stable CLI tools go in the Dockerfile, pinned. gcloud and Terraform get added at G1.

## Checks

- `pre-commit run --all-files` — whitespace, YAML, large files, private keys, gitleaks.
- `python3 scripts/check_track.py` — exit 1 if a linked lesson returns 404 on the website.
- CI: `.github/workflows/ci.yml` (pre-commit on push/PR), `track.yml` (weekly + on TRACK.md changes).
