"""p07-02 lab: attention has to read the whole prompt before the first answer token appears.

Time-to-first-token (TTFT) is the "prefill": one forward pass over every prompt token, where each
token attends to all tokens before it (the lesson's attention matrix, n × n). This measures TTFT and
decode speed on your local MLX server for growing prompts.

Each prompt is unique (different random log lines), so the server can't reuse a cached prefix;
that reuse is the p07-12 lab.

Run (local MLX server must be running on the Mac, see GUIDE.md):
  python lessons/p07-02/ttft_lab.py
  python lessons/p07-02/ttft_lab.py --remote     # same test against the .env backend (network included)
"""
import os
import random
import sys
import time

from openai import OpenAI

REMOTE = "--remote" in sys.argv
if REMOTE:
    client = OpenAI(base_url=os.environ["LLM_BASE_URL"], api_key=os.environ["LLM_API_KEY"])
    MODEL, EXTRA = os.environ["LLM_MODEL"], {"reasoning_effort": os.environ.get("LLM_REASONING_EFFORT") or "minimal"}
else:
    client = OpenAI(base_url=os.environ.get("LOCAL_LLM_URL", "http://host.docker.internal:8080/v1"), api_key="local")
    MODEL, EXTRA = os.environ.get("LOCAL_LLM_MODEL", "mlx-community/gemma-4-e4b-it-4bit"), {}

PATHS = ["/", "/api/cart", "/api/items?page=2", "/static/app.js", "/healthz", "/api/checkout"]
TOKENS_PER_LINE = 90      # one nginx access-log line ≈ 90 Gemma tokens (measured in p11-05)


def log_lines(n, seed):
    rng = random.Random(seed)
    return "\n".join(f'{rng.randint(1, 254)}.{rng.randint(1, 254)}.{rng.randint(1, 254)}.{rng.randint(1, 254)} - - '
                     f'[13/Nov/2026:16:{i // 60 % 60:02d}:{i % 60:02d} +0000] "GET {rng.choice(PATHS)} HTTP/1.1" '
                     f'{rng.choice([200, 200, 200, 404, 500])} {rng.randint(200, 9000)} "-" "Mozilla/5.0" rt={rng.random():.3f}'
                     for i in range(n))


def measure(prompt):
    """Stream the reply: TTFT = time until the first content chunk; decode = chunks/s after that."""
    start = time.time()
    first, chunks = None, 0
    stream = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}],
                                            max_tokens=60, temperature=0, stream=True, **EXTRA)
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            first = first or time.time()
            chunks += 1
    end = time.time()
    return first - start, chunks / max(end - first, 1e-6)


def main():
    print(f"model: {MODEL} ({'remote' if REMOTE else 'local MLX'})")
    measure("Say OK.")                                  # warm-up: load weights, compile kernels
    print(f"\n{'≈prompt tokens':>15}{'TTFT s':>9}{'ms per 1K prompt tok':>22}{'decode tok/s':>14}")
    for n_lines in (3, 11, 44, 89, 178):               # ≈ 250 … 16K tokens
        q = "\n\nHow many requests above returned status 500? Answer with a number only."
        ttft, rate = measure(log_lines(n_lines, seed=time.time_ns()) + q)
        approx = n_lines * TOKENS_PER_LINE
        print(f"{approx:>15}{ttft:>9.2f}{ttft / approx * 1000 * 1000:>22.0f}{rate:>14.1f}")


if __name__ == "__main__":
    main()
