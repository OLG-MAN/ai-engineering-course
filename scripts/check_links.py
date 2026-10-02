#!/usr/bin/env python3
"""Check external links in Markdown files.

Usage: python3 scripts/check_links.py [FILE ...]   (default: PLAN.md)

Exit code 1 if any link is dead (404/410, DNS or connection failure).
403/429/5xx are reported as warnings: many course sites block bots.
Stdlib only, so it runs locally and in CI without installs.
"""
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

URL_RE = re.compile(r"https?://[^\s)<>\]`|]+")
UA = "Mozilla/5.0 (link-check; +https://github.com/OLG-MAN/ai-engineering-course)"
DEAD = {404, 410}


def extract(path):
    with open(path, encoding="utf-8") as f:
        return {u.rstrip(".,;:*") for u in URL_RE.findall(f.read())}


def check(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return url, r.status, None
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 404, 405, 501):
                continue  # some servers reject HEAD; retry with GET
            return url, e.code, None
        except Exception as e:  # DNS, TLS, timeout
            if method == "HEAD":
                continue
            return url, None, str(e)
    return url, None, "unreachable"


def main():
    files = sys.argv[1:] or ["PLAN.md"]
    urls = sorted(set().union(*(extract(p) for p in files)))
    dead, warn = [], []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, status, err in pool.map(check, urls):
            if err or status in DEAD:
                dead.append((url, status or err))
            elif status >= 400:
                warn.append((url, status))
    for url, why in warn:
        print(f"WARN {why}  {url}")
    for url, why in dead:
        print(f"DEAD {why}  {url}")
    print(f"\n{len(urls)} links checked: {len(dead)} dead, {len(warn)} warnings")
    sys.exit(1 if dead else 0)


if __name__ == "__main__":
    main()
