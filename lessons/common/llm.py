"""Shared LLM client for all lesson labs.

One OpenAI-compatible client, configured from .env (loaded into the lab container):
  LLM_BASE_URL          Gemini API: https://generativelanguage.googleapis.com/v1beta/openai/
                        local MLX:  http://host.docker.internal:8080/v1
  LLM_API_KEY           AI Studio key (any string for local MLX)
  LLM_MODEL             e.g. gemma-4-26b-a4b-it, gemini-3.5-flash, mlx-community/gemma-4-e4b-it-4bit
  LLM_REASONING_EFFORT  minimal (Gemma 4 on Gemini API) · none (Gemini Flash) · unset (local MLX)
  LLM_PAUSE_S           pause after each call, keeps free-tier rate limits happy (default 1)

Usage in a lab script:
  import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
  from common.llm import chat
  reply = chat([{"role": "user", "content": "hi"}])
  print(reply.text, reply.usage.prompt_tokens, reply.seconds)
"""
import os
import re
import time
from dataclasses import dataclass

from openai import OpenAI, RateLimitError

BASE_URL = os.environ.get("LLM_BASE_URL") or "http://host.docker.internal:8080/v1"
MODEL = os.environ.get("LLM_MODEL") or "mlx-community/gemma-4-e4b-it-4bit"
EFFORT = os.environ.get("LLM_REASONING_EFFORT") or None
PAUSE = float(os.environ.get("LLM_PAUSE_S") or 1)

client = OpenAI(base_url=BASE_URL, api_key=os.environ.get("LLM_API_KEY") or "local", max_retries=2)

# Some models leak their reasoning into the answer as <thought>...</thought>; strip it.
_THOUGHT = re.compile(r"<thought>.*?</thought>", re.S)


@dataclass
class Reply:
    text: str        # the answer, reasoning stripped
    message: object  # raw message: .tool_calls lives here
    usage: object    # .prompt_tokens / .completion_tokens, counted by the server
    seconds: float   # wall-clock latency of the call


def chat(messages, model=None, **kwargs):
    """One chat completion. Extra kwargs go straight to the API (temperature, tools, response_format …)."""
    if EFFORT and "reasoning_effort" not in kwargs:
        kwargs["reasoning_effort"] = EFFORT
    for attempt in range(5):
        start = time.time()
        try:
            r = client.chat.completions.create(model=model or MODEL, messages=messages, **kwargs)
            break
        except RateLimitError:
            # free tier: requests-per-minute and tokens-per-minute quotas; wait for the window to roll over
            wait = 20 * (attempt + 1)
            print(f"  [429 rate limit: waiting {wait}s, then retrying]", flush=True)
            time.sleep(wait)
    else:
        raise RuntimeError("still rate-limited after 5 attempts; check your quota in AI Studio")
    seconds = time.time() - start
    time.sleep(PAUSE)
    msg = r.choices[0].message
    text = _THOUGHT.sub("", msg.content or "").strip()
    if not text and not msg.tool_calls:
        # Typical cause: the model spent max_tokens on hidden reasoning. With Gemma 4 on the Gemini API,
        # set LLM_REASONING_EFFORT=minimal in .env and recreate the container (make down && make up).
        print(f"  [warning: empty answer, finish_reason={r.choices[0].finish_reason}, "
              f"reasoning_effort={EFFORT}; see lessons/common/llm.py]", flush=True)
    return Reply(text, msg, r.usage, seconds)


def backend():
    """Short description of the configured backend, for printing at the top of a lab."""
    return f"{MODEL} @ {BASE_URL.split('//')[-1].split('/')[0]}" + (f" (reasoning_effort={EFFORT})" if EFFORT else "")
