#!/usr/bin/env python3
"""
sync_to_claude.py

Copies skills from a source directory into `.claude/skills/` (project-local).

Default source: `.codex/skills` (because this repo is Codex-first).
You can also use `--src skills` if you keep canonical skills in `./skills/`.

Usage:
  python scripts/sync_to_claude.py
  python scripts/sync_to_claude.py --src skills
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

def is_skill_dir(p: Path) -> bool:
    return p.is_dir() and (p / "SKILL.md").exists()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=".codex/skills", help="Source skills directory")
    ap.add_argument("--dst", default=".claude/skills", help="Destination skills directory")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing destination skill dirs")
    args = ap.parse_args()

    src = Path(args.src).resolve()
    dst = Path(args.dst).resolve()

    if not src.exists():
        raise SystemExit(f"Source does not exist: {src}")
    dst.mkdir(parents=True, exist_ok=True)

    copied = 0
    for child in sorted(src.iterdir()):
        if not is_skill_dir(child):
            continue
        target = dst / child.name
        if target.exists():
            if not args.overwrite:
                # Skip by default to avoid clobbering manual edits.
                continue
            shutil.rmtree(target)
        shutil.copytree(child, target)
        copied += 1

    print(f"[ok] Synced {copied} skill(s) from {src} -> {dst}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
