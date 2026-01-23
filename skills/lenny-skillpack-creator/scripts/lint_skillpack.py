#!/usr/bin/env python3

"""
lint_skillpack.py

Validate a skill pack directory against the expected structure.

Usage:
  python skills/lenny-skillpack-creator/scripts/lint_skillpack.py <path/to/skill-folder>
"""

from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # type: ignore

FRONTMATTER_RE = re.compile(r"^---\s*$")
REQ_FIELDS = ["name", "description"]
REQ_REF_FILES = [
    "INTAKE.md",
    "WORKFLOW.md",
    "TEMPLATES.md",
    "CHECKLISTS.md",
    "RUBRIC.md",
    "SOURCE_SUMMARY.md",
    "EXAMPLES.md",
]

def read_frontmatter(text: str) -> tuple[dict, str | None]:
    lines = text.splitlines()
    if not lines or not FRONTMATTER_RE.match(lines[0]):
        return {}, "SKILL.md missing YAML frontmatter opening marker (---)."
    # find second --- line
    end = None
    for i in range(1, len(lines)):
        if FRONTMATTER_RE.match(lines[i]):
            end = i
            break
    if end is None:
        return {}, "SKILL.md missing YAML frontmatter closing marker (---)."

    raw = "\n".join(lines[1:end]).strip()
    if not raw:
        return {}, "SKILL.md YAML frontmatter is empty."

    if yaml is None:
        return {}, "PyYAML is required to parse SKILL.md frontmatter (install 'PyYAML')."

    try:
        data = yaml.safe_load(raw) or {}
    except Exception as e:
        return {}, f"SKILL.md has invalid YAML frontmatter: {type(e).__name__}: {e}"

    if not isinstance(data, dict):
        return {}, f"SKILL.md frontmatter must be a mapping, got: {type(data).__name__}"

    return data, None

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

    # README check
    readme_path = skill_dir / "README.md"
    if not readme_path.exists():
        errors.append(f"Missing README.md at {readme_path}")

    # frontmatter checks
    if skill_md_path.exists():
        txt = skill_md_path.read_text(encoding="utf-8", errors="replace")
        fm, fm_err = read_frontmatter(txt)
        if fm_err:
            errors.append(fm_err)
        else:
            for f in REQ_FIELDS:
                v = fm.get(f, None)
                if not isinstance(v, str) or not v.strip():
                    errors.append(f"Frontmatter missing required string field: {f}")

            # name match folder
            name = (fm.get("name") or "").strip() if isinstance(fm.get("name"), str) else ""
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
