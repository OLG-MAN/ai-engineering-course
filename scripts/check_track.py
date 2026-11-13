#!/usr/bin/env python3
"""Check that every course lesson linked in TRACK.md still resolves on the course website.

Usage: python3 scripts/check_track.py [--track TRACK.md]

Exit 1 if a lesson link returns 404/410 (renamed or removed upstream): fix TRACK.md.
Other HTTP errors and network failures are warnings, so a flaky site doesn't fail CI.
Stdlib only.
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SITE = "https://aiengineeringfromscratch.com/learn/"
LINK_RE = re.compile(re.escape(SITE) + r"[a-z0-9-]+/[a-z0-9-]+")
UA = "Mozilla/5.0 (track-check)"
DEAD = {404, 410}


def status(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return url, r.status
        except urllib.error.HTTPError as e:
            if e.code in (405, 501) and method == "HEAD":
                continue
            return url, e.code
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            return url, f"error: {e}"
    return url, "error: no response"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", default=str(Path(__file__).resolve().parent.parent / "TRACK.md"))
    args = ap.parse_args()

    urls = sorted(set(LINK_RE.findall(Path(args.track).read_text(encoding="utf-8"))))
    if not urls:
        sys.exit("no lesson links found in TRACK.md")

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(status, urls))

    dead = [(u, s) for u, s in results if s in DEAD]
    warn = [(u, s) for u, s in results if s != 200 and s not in DEAD]
    for u, s in dead:
        print(f"DEAD {s}: {u}")
    for u, s in warn:
        print(f"WARN {s}: {u}")
    print(f"lesson links: {len(urls)} · ok: {len(urls) - len(dead) - len(warn)} · dead: {len(dead)} · warnings: {len(warn)}")
    sys.exit(1 if dead else 0)


if __name__ == "__main__":
    main()
