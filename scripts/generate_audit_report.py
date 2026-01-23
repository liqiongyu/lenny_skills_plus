#!/usr/bin/env python3
"""
generate_audit_report.py

Generate `docs/AUDIT_REPORT.md` with a lightweight, reproducible audit summary.

This report is meant for humans (project credibility), not as a security/compliance guarantee.

Usage:
  python3 scripts/generate_audit_report.py
  python3 scripts/generate_audit_report.py --out docs/AUDIT_REPORT.md
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml  # type: ignore


CJK_RE = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").exists()


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening ---")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError("missing closing ---")
    raw = "\n".join(lines[1:end]).strip()
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-root", default="skills")
    ap.add_argument("--manifest", default="sources/refound/refound_lenny_skills_manifest.csv")
    ap.add_argument("--out", default="docs/AUDIT_REPORT.md")
    args = ap.parse_args()

    skills_root = Path(args.skills_root).resolve()
    manifest_path = Path(args.manifest).resolve()
    out_path = Path(args.out).resolve()

    skill_dirs = [p for p in sorted(skills_root.iterdir()) if is_skill_dir(p)]

    converted_count = 0
    if manifest_path.exists():
        with manifest_path.open("r", encoding="utf-8", newline="") as f:
            converted_count = sum(1 for _ in csv.DictReader(f))

    meta_count = max(0, len(skill_dirs) - converted_count) if converted_count else 0

    # Run canonical lint check (no mirrors).
    ci_cmd = [sys.executable, "scripts/ci_check_skillpacks.py", "--skip-mirror-check"]
    ci_rc = subprocess.call(ci_cmd)

    # Frontmatter + structure checks (lightweight).
    fm_failures: list[str] = []
    name_mismatch: list[str] = []
    desc_style = Counter()
    missing_files: list[str] = []

    for d in skill_dirs:
        skill_md = d / "SKILL.md"
        readme = d / "README.md"
        refs = d / "references"
        required_refs = [
            "INTAKE.md",
            "WORKFLOW.md",
            "TEMPLATES.md",
            "CHECKLISTS.md",
            "RUBRIC.md",
            "SOURCE_SUMMARY.md",
            "EXAMPLES.md",
        ]

        if not readme.exists():
            missing_files.append(f"{d.name}: README.md")
        if not refs.exists():
            missing_files.append(f"{d.name}: references/")
        else:
            for fn in required_refs:
                if not (refs / fn).exists():
                    missing_files.append(f"{d.name}: references/{fn}")

        try:
            fm = read_frontmatter(skill_md)
        except Exception as e:
            fm_failures.append(f"{d.name}: {type(e).__name__}: {e}")
            continue

        name = fm.get("name", "")
        if not isinstance(name, str) or not name.strip():
            fm_failures.append(f"{d.name}: missing/invalid name")
        elif name.strip() != d.name:
            name_mismatch.append(f"{d.name}: name={name!r}")

        desc = fm.get("description", "")
        if not isinstance(desc, str) or not desc.strip():
            fm_failures.append(f"{d.name}: missing/invalid description")

        # Style stats (how the description is written in YAML).
        # (Best-effort: inspect the raw frontmatter line.)
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        fm_lines = []
        lines = text.splitlines()
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_lines = lines[1:i]
                break
        desc_line = next((l for l in fm_lines if l.startswith("description:")), "")
        after = desc_line.split(":", 1)[1].lstrip() if ":" in desc_line else ""
        if after.startswith(">") or after.startswith("|") or after == "":
            desc_style["folded_or_multiline"] += 1
        else:
            desc_style["single_line"] += 1

    # Language check (CJK)
    cjk_hits: list[str] = []
    for p in skills_root.rglob("*.md"):
        if "__pycache__" in p.parts:
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        if CJK_RE.search(txt):
            cjk_hits.append(str(p.relative_to(skills_root)))

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    lines_out: list[str] = []
    lines_out.append("# Audit report")
    lines_out.append(f"Generated: {generated}")
    lines_out.append("")
    lines_out.append("This report summarizes automated checks over the skill packs in `skills/`.")
    lines_out.append("")
    lines_out.append("## Inventory")
    lines_out.append(f"- Canonical skill packs under `skills/`: {len(skill_dirs)}")
    if converted_count:
        lines_out.append(f"- Converted Refound/Lenny skills: {converted_count}")
        lines_out.append(f"- Meta-skill(s): {meta_count} (`lenny-skillpack-creator`, etc.)")
    lines_out.append("")
    lines_out.append("## Structural validation")
    if ci_rc == 0:
        lines_out.append("- ✅ `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` passed.")
    else:
        lines_out.append("- ❌ `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` failed.")
    if not missing_files:
        lines_out.append("- ✅ Each skill pack contains: `SKILL.md`, `README.md`, and `references/` with the required core files.")
    else:
        lines_out.append(f"- ❌ Missing required files in {len(missing_files)} place(s).")
    lines_out.append("")
    lines_out.append("## Frontmatter compliance (cross-tool)")
    if not fm_failures:
        lines_out.append("- ✅ Every `SKILL.md` has YAML frontmatter with required fields (`name`, `description`).")
    else:
        lines_out.append(f"- ❌ Frontmatter failures: {len(fm_failures)}")
    if not name_mismatch:
        lines_out.append("- ✅ `name` matches the folder slug.")
    else:
        lines_out.append(f"- ❌ Name mismatch: {len(name_mismatch)}")
    lines_out.append(f"- ℹ️ Description YAML style: {dict(desc_style)}")
    lines_out.append("")
    lines_out.append("## Language check")
    if not cjk_hits:
        lines_out.append("- ✅ No CJK (Chinese/Japanese/Korean) characters detected across `skills/**/*.md`.")
    else:
        lines_out.append(f"- ❌ Found CJK characters in {len(cjk_hits)} file(s).")
    lines_out.append("")
    lines_out.append("## Recommended ongoing checks")
    lines_out.append("- Run `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` before commits.")
    lines_out.append("- After mirroring into `.codex/skills/` and `.claude/skills/`, run `python3 scripts/ci_check_skillpacks.py` to ensure mirrors are identical.")
    lines_out.append("- Periodically smoke-test a few skills per category with real tasks.")
    lines_out.append("")
    lines_out.append(f"_Generated by `python3 scripts/generate_audit_report.py`._")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines_out).rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

