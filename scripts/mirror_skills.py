#!/usr/bin/env python3
"""
mirror_skills.py

Mirror canonical skill packs from `skills/` into:
- `.codex/skills/`
- `.claude/skills/`

So both Codex and Claude Code can auto-discover them.

By default, this does NOT overwrite existing dirs (to avoid accidental clobber).
Pass --overwrite to replace destination versions.

Usage:
  python scripts/mirror_skills.py
  python scripts/mirror_skills.py --overwrite
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

def is_skill_dir(p: Path) -> bool:
    return p.is_dir() and (p / "SKILL.md").exists()

def sync(src_root: Path, dst_root: Path, overwrite: bool) -> int:
    dst_root.mkdir(parents=True, exist_ok=True)
    copied = 0
    for child in sorted(src_root.iterdir()):
        if not is_skill_dir(child):
            continue
        target = dst_root / child.name
        if target.exists():
            if not overwrite:
                continue
            shutil.rmtree(target)
        shutil.copytree(child, target)
        copied += 1
    return copied

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="skills", help="Canonical skills directory")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite destination skill dirs")
    args = ap.parse_args()

    src = Path(args.src).resolve()
    if not src.exists():
        raise SystemExit(f"Source does not exist: {src}")

    codex_dst = Path(".codex/skills").resolve()
    claude_dst = Path(".claude/skills").resolve()

    copied_codex = sync(src, codex_dst, args.overwrite)
    copied_claude = sync(src, claude_dst, args.overwrite)

    print(f"[ok] mirrored: codex={copied_codex} claude={copied_claude}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
