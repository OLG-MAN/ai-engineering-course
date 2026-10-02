# Labs

My re-implementations of course labs, ported to my own stack. One folder per lab: `labs/<slug>/`.

Rules:
- **No course code.** No notebooks, lab code or graded-assignment solutions copied from any course. Rebuild the pattern from scratch.
- **Port to my stack:** Weaviate → Qdrant, Oracle → Postgres, LangSmith → Langfuse, vendor SDK → OpenAI-compatible client (hosted / vLLM / Ollama).
- Each lab folder has a short `README.md`: what it does, how to run it, what changed versus the course version.
- The write-up goes in `notes/<block>/<LNN>-lab-<slug>.md` (from [templates/lab-note.md](../templates/lab-note.md)).
- Keys come from `.env`; never hard-code them.
