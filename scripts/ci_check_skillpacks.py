#!/usr/bin/env python3
"""
ci_check_skillpacks.py

CI helper:
- Lints canonical skill packs under `skills/` using lint_skillpack.py
- Optionally verifies canonical skills are mirrored identically into:
  - `.codex/skills/<slug>/` (Codex project-local auto-discovery)
  - `.claude/skills/<slug>/` (Claude Code project-local auto-discovery)

This script is intentionally strict so drift is caught early.
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path
from typing import Iterable

LINTER = Path("skills/lenny-skillpack-creator/scripts/lint_skillpack.py")


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").exists()


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def snapshot_tree(root: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            continue
        if "__pycache__" in p.parts:
            continue
        rel = p.relative_to(root).as_posix()
        out[rel] = sha256_file(p)
    return out


def diff_summary(a: dict[str, str], b: dict[str, str]) -> tuple[list[str], list[str], list[str]]:
    a_keys = set(a.keys())
    b_keys = set(b.keys())
    missing_in_b = sorted(a_keys - b_keys)
    extra_in_b = sorted(b_keys - a_keys)
    changed = sorted([k for k in (a_keys & b_keys) if a[k] != b[k]])
    return missing_in_b, extra_in_b, changed


def print_limited(label: str, items: Iterable[str], limit: int = 20) -> None:
    items_list = list(items)
    if not items_list:
        return
    print(f"  - {label} ({len(items_list)}):", file=sys.stderr)
    for i, item in enumerate(items_list[:limit]):
        print(f"    - {item}", file=sys.stderr)
    if len(items_list) > limit:
        print(f"    - ... and {len(items_list) - limit} more", file=sys.stderr)


def run_lint(skill_dir: Path) -> int:
    if not LINTER.exists():
        print(f"[fail] Missing linter script: {LINTER}", file=sys.stderr)
        return 2
    cmd = [sys.executable, str(LINTER), str(skill_dir)]
    return subprocess.call(cmd)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-root", default="skills", help="Canonical skills directory")
    ap.add_argument("--codex-root", default=".codex/skills", help="Codex skills directory")
    ap.add_argument("--claude-root", default=".claude/skills", help="Claude skills directory")
    ap.add_argument("--skip-mirror-check", action="store_true", help="Only run lint (no mirror validation)")
    args = ap.parse_args()

    skills_root = Path(args.skills_root).resolve()
    codex_root = Path(args.codex_root).resolve()
    claude_root = Path(args.claude_root).resolve()

    if not skills_root.exists():
        print(f"[info] skills root not found: {skills_root} (skipping)")
        return 0

    skill_dirs = [p for p in sorted(skills_root.iterdir()) if is_skill_dir(p)]
    if not skill_dirs:
        print("[info] no skill packs under skills/ (nothing to lint)")
        return 0

    failures = 0

    for skill_dir in skill_dirs:
        name = skill_dir.name
        print(f"[check] {name}")

        rc = run_lint(skill_dir)
        if rc != 0:
            failures += 1
            continue

        if args.skip_mirror_check:
            continue

        codex_dir = codex_root / name
        claude_dir = claude_root / name

        missing_mirrors: list[str] = []
        if not codex_dir.exists():
            missing_mirrors.append(str(codex_dir))
        if not claude_dir.exists():
            missing_mirrors.append(str(claude_dir))

        if missing_mirrors:
            print(f"[fail] missing mirrored skill directory for {name}", file=sys.stderr)
            for m in missing_mirrors:
                print(f"  - {m}", file=sys.stderr)
            failures += 1
            continue

        src_tree = snapshot_tree(skill_dir)
        codex_tree = snapshot_tree(codex_dir)
        claude_tree = snapshot_tree(claude_dir)

        for mirror_label, mirror_tree in [("codex", codex_tree), ("claude", claude_tree)]:
            missing, extra, changed = diff_summary(src_tree, mirror_tree)
            if missing or extra or changed:
                print(f"[fail] {mirror_label} mirror differs for {name}", file=sys.stderr)
                print_limited("missing", missing)
                print_limited("extra", extra)
                print_limited("changed", changed)
                failures += 1

    if failures:
        print(f"[fail] {failures} failure(s)", file=sys.stderr)
        return 2

    print("[ok] skill packs validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
