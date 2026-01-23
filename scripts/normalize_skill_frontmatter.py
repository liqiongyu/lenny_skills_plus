#!/usr/bin/env python3
"""
normalize_skill_frontmatter.py

Normalize `skills/*/SKILL.md` YAML frontmatter to be maximally compatible with Codex + Claude Code:

- `name` and `description` are single-line scalars (no `description: >` block scalars)
- both are YAML-quoted (double quotes) for safety
- preserves the rest of the markdown body unchanged

Usage:
  python3 scripts/normalize_skill_frontmatter.py
  python3 scripts/normalize_skill_frontmatter.py --skills-root skills --dry-run
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # type: ignore


def parse_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (raw_frontmatter, body). raw_frontmatter excludes --- lines."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text
    raw = "".join(lines[1:end])
    body = "".join(lines[end + 1 :])
    return raw, body


def make_yaml_frontmatter(name: str, description: str) -> str:
    name = re.sub(r"\s+", " ", name.replace("\r", " ").replace("\n", " ")).strip()
    description = re.sub(r"\s+", " ", description.replace("\r", " ").replace("\n", " ")).strip()

    # YAML-safe quoting (double quotes)
    name = name.replace("\\", "\\\\").replace('"', '\\"')
    description = description.replace("\\", "\\\\").replace('"', '\\"')

    return f"---\nname: \"{name}\"\ndescription: \"{description}\"\n---\n\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-root", default="skills")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if yaml is None:
        raise SystemExit("PyYAML is required: pip install PyYAML")

    root = Path(args.skills_root)
    if not root.exists():
        print(f"[info] {root} does not exist; nothing to do")
        return 0

    changed = 0
    for d in sorted(root.iterdir()):
        skill_md = d / "SKILL.md"
        if not d.is_dir() or not skill_md.exists():
            continue

        text = skill_md.read_text(encoding="utf-8", errors="replace")
        raw, body = parse_frontmatter(text)
        if raw is None:
            continue

        try:
            data = yaml.safe_load(raw) or {}
        except Exception as e:
            print(f"[skip] invalid YAML in {skill_md}: {type(e).__name__}: {e}")
            continue

        if not isinstance(data, dict):
            print(f"[skip] non-mapping frontmatter in {skill_md}")
            continue

        name = str(data.get("name", d.name))
        desc = str(data.get("description", ""))
        new_text = make_yaml_frontmatter(name, desc) + body.lstrip("\r\n")

        if new_text != text:
            changed += 1
            if args.dry_run:
                print(f"[would-fix] {skill_md}")
            else:
                skill_md.write_text(new_text, encoding="utf-8")
                print(f"[fixed] {skill_md}")

    print(f"[done] changed={changed} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
