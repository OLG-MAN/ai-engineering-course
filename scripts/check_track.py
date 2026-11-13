#!/usr/bin/env python3
"""Check that every upstream lesson linked in TRACK.md still exists upstream.

Usage:
  python3 scripts/check_track.py                      # shallow-clones upstream into a temp dir
  python3 scripts/check_track.py --upstream ../ai-engineering-from-scratch   # use a local clone (git pull it first)

Exit 1 if a linked lesson path is missing at upstream HEAD (renamed or removed): fix TRACK.md and re-pin.
Stdlib only.
"""
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = "https://github.com/rohitg00/ai-engineering-from-scratch"
LINK_RE = re.compile(re.escape(REPO) + r"/tree/([0-9a-f]{7,40})/(phases/[^)\s#]+)")


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def upstream_dirs(root):
    head = git("-C", root, "rev-parse", "HEAD").strip()
    dirs = set(git("-C", root, "ls-tree", "-r", "-d", "--name-only", "HEAD", "phases").split())
    return head, dirs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream", help="path to a local clone of the upstream repo")
    ap.add_argument("--track", default=str(Path(__file__).resolve().parent.parent / "TRACK.md"))
    args = ap.parse_args()

    links = LINK_RE.findall(Path(args.track).read_text(encoding="utf-8"))
    if not links:
        sys.exit("no upstream lesson links found in TRACK.md")
    pins = {sha for sha, _ in links}
    paths = sorted({p.rstrip("/") for _, p in links})

    if args.upstream:
        head, dirs = upstream_dirs(args.upstream)
    else:
        with tempfile.TemporaryDirectory() as tmp:
            git("clone", "-q", "--depth", "1", "--filter=blob:none", "--no-checkout", REPO + ".git", tmp)
            head, dirs = upstream_dirs(tmp)

    missing = [p for p in paths if p not in dirs]
    print(f"lessons linked: {len(paths)} · pinned: {', '.join(sorted(s[:7] for s in pins))} · upstream HEAD: {head[:7]}")
    if not any(head.startswith(s) for s in pins):
        print("upstream moved since the pin; re-pin when convenient")
    for p in missing:
        print(f"MISSING upstream: {p}")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
