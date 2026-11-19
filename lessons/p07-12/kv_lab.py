"""p07-12 lab: KV cache memory, on your own models, and prefix caching on your own server.

Part 1, "memory": the lesson's formula  bytes = 2 (K and V) × layers × kv_heads × head_dim × 2 bytes × N
assumes every layer attends to every previous token. Gemma 4 doesn't: most layers use a sliding
window (only the last 512/1024 tokens), some layers share another layer's KV, and the 12B's global
layers use one KV head with K = V. The numbers below come from each model's config.json
(~/git/models/hf_cache/hub/models--mlx-community--gemma-4-*/snapshots/*/config.json).
The "Gemma-aware" column is my reading of those fields: an estimate, not a measurement.

Part 2, "prefix": the server keeps the KV of recent prompts, and a request that can reuse it skips
that part of the prefill. Which requests can reuse it depends on the cache type. Gemma 4's sliding-window
layers keep a rotating cache that can be extended but not cut back, so on mlx_lm.server:
  same beginning + different question → no reuse (the cache would have to be cut back to the shared part)
  previous conversation + a new turn  → reuse (pure extension: exactly what an agent loop sends)
The server reports what it reused in usage.prompt_tokens_details.cached_tokens.

Run:
  python lessons/p07-12/kv_lab.py memory
  python lessons/p07-12/kv_lab.py prefix      # needs the local MLX server
"""
import os
import random
import sys
import time

GB = 1024 ** 3
BYTES = 2  # fp16 / bf16

MODELS = {
    # from config.json (text_config)
    "gemma-4-e4b": dict(layers=42, kv_heads=2, head_dim=256, sliding=35, full=7, window=512,
                        kv_shared_layers=18, global_kv_heads=2, global_head_dim=512, k_eq_v=False, weights_gb=5),
    "gemma-4-12B": dict(layers=48, kv_heads=8, head_dim=256, sliding=40, full=8, window=1024,
                        kv_shared_layers=0, global_kv_heads=1, global_head_dim=512, k_eq_v=True, weights_gb=7),
}


def lesson_formula(m, n):
    """The lesson's kv_cache_bytes(): every layer full attention, same heads everywhere."""
    return 2 * m["layers"] * m["kv_heads"] * m["head_dim"] * BYTES * n


def gemma_aware(m, n):
    own = m["layers"] - m["kv_shared_layers"]               # layers that store their own KV
    share = own / m["layers"]                               # assume shared layers are spread like the rest
    full, sliding = m["full"] * share, m["sliding"] * share
    kv_full = (1 if m["k_eq_v"] else 2) * m["global_kv_heads"] * m["global_head_dim"] * BYTES * n
    kv_sliding = 2 * m["kv_heads"] * m["head_dim"] * BYTES * min(n, m["window"])
    return full * kv_full + sliding * kv_sliding


def memory():
    budget = 17.8   # GB of the Mac mini's unified memory usable by the GPU (local-llm-setup-notes.md)
    print(f"{'model':<14}{'context':>9}{'lesson formula':>16}{'Gemma-aware':>13}   fits next to the weights in {budget} GB?")
    for name, m in MODELS.items():
        for n in (4_096, 32_768, 131_072):
            naive, real = lesson_formula(m, n) / GB, gemma_aware(m, n) / GB
            fits = "yes" if m["weights_gb"] + real < budget else "NO"
            print(f"{name:<14}{n:>9,}{naive:>13.2f} GB{real:>10.2f} GB   {fits} (weights ~{m['weights_gb']} GB)")


def prefix():
    from openai import OpenAI
    client = OpenAI(base_url=os.environ.get("LOCAL_LLM_URL", "http://host.docker.internal:8080/v1"), api_key="local")
    model = os.environ.get("LOCAL_LLM_MODEL", "mlx-community/gemma-4-e4b-it-4bit")
    rng = random.Random(time.time_ns())     # fresh logs every run, so nothing is cached from last time
    logs = "\n".join(f"10.0.{rng.randint(0, 9)}.{rng.randint(1, 254)} GET /api/{rng.choice(['cart', 'items', 'pay'])} "
                     f"{rng.choice([200, 200, 200, 500])}" for _ in range(250))

    def call(label, messages):
        start = time.time()
        r = client.chat.completions.create(model=model, messages=messages, max_tokens=15, temperature=0)
        details = r.usage.prompt_tokens_details
        cached = getattr(details, "cached_tokens", None) if details else None
        print(f"{label:<44}{time.time() - start:6.2f}s  prompt={r.usage.prompt_tokens:>5}  cached={cached}")
        return r.choices[0].message.content

    q1 = {"role": "user", "content": logs + "\n\nHow many lines have status 500? Number only."}
    print(f"model: {model}\n")
    a1 = call("1 cold: new logs + question", [q1])
    call("2 same logs, different question", [{"role": "user", "content": logs + "\n\nWhich path is most common?"}])
    call("3 conversation so far + a new turn", [q1, {"role": "assistant", "content": a1},
                                                {"role": "user", "content": "And how many have status 200?"}])
    call("4 exact repeat of request 1", [q1])


if __name__ == "__main__":
    {"memory": memory, "prefix": prefix}.get(sys.argv[1] if len(sys.argv) > 1 else "memory", memory)()
