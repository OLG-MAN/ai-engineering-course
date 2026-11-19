# Lessons

One folder per lesson, named by the TRACK.md ID: `p<phase>-<lesson>`, e.g. `p11-06/`.

| File | Who writes it | What |
| --- | --- | --- |
| `GUIDE.md` | Claude | the lab: start, read the article and the lesson code section by section, "make it real" on real infra, cleanup, errata |
| `NOTES.md` | me | questions to answer in my own words, key ideas, my results |
| `*.py`, data files | both | lab scripts (run them, read them, change them) and my own code |

Shared by all labs, in [common/](common/):

- [llm.py](common/llm.py): one OpenAI-compatible client configured from `.env` (Gemini API, local MLX, later vLLM); waits out free-tier rate limits
- [k8s.py](common/k8s.py): read-only kubectl helpers (also the tools of the p11-09 agent)
- [scenario.sh](common/scenario.sh): a namespace with three broken workloads and one healthy, `up`/`down`, optional prompt-injection pod

Every lab runs inside the lab container (`make sh`). Status and links: [TRACK.md](../TRACK.md).
