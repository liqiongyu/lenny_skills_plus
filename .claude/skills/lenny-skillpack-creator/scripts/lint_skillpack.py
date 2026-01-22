#!/usr/bin/env python3

"""
lint_skillpack.py

Validate a skill pack directory against the expected structure.

Usage:
  python scripts/lint_skillpack.py <path/to/skill-folder>
"""

from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys

FRONTMATTER_RE = re.compile(r"^---\s*$")
REQ_FIELDS = ["name", "description"]
REQ_REF_FILES = [
    "INTAKE.md",
    "WORKFLOW.md",
    "TEMPLATES.md",
    "CHECKLISTS.md",
    "RUBRIC.md",
    "SOURCE_SUMMARY.md",
]

def read_frontmatter(text: str) -> dict:
    lines = text.splitlines()
    if not lines or not FRONTMATTER_RE.match(lines[0]):
        return {}
    # find second --- line
    end = None
    for i in range(1, len(lines)):
        if FRONTMATTER_RE.match(lines[i]):
            end = i
            break
    if end is None:
        return {}
    raw = "\n".join(lines[1:end]).strip()
    data = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip()
        if k and k not in data:
            data[k] = v
    return data

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", help="Path to the skill directory (contains SKILL.md).")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).expanduser().resolve()
    errors = []

    skill_md_path = skill_dir / "SKILL.md"
    if not skill_md_path.exists():
        errors.append(f"Missing SKILL.md at {skill_md_path}")

    # references checks
    ref_dir = skill_dir / "references"
    if not ref_dir.exists():
        errors.append(f"Missing references/ directory at {ref_dir}")
    else:
        for fn in REQ_REF_FILES:
            if not (ref_dir / fn).exists():
                errors.append(f"Missing references/{fn}")

    # frontmatter checks
    if skill_md_path.exists():
        txt = skill_md_path.read_text(encoding="utf-8", errors="replace")
        fm = read_frontmatter(txt)
        if not fm:
            errors.append("SKILL.md missing or malformed YAML frontmatter (--- ... ---).")
        else:
            for f in REQ_FIELDS:
                if f not in fm or not fm[f].strip():
                    errors.append(f"Frontmatter missing required field: {f}")
            # name match folder
            name = fm.get("name", "").strip()
            if name and name != skill_dir.name:
                errors.append(f"Frontmatter name '{name}' does not match folder name '{skill_dir.name}'")

    if errors:
        print("[fail] Skill pack validation failed:")
        for e in errors:
            print(f" - {e}")
        return 2

    print("[ok] Skill pack looks structurally valid.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
