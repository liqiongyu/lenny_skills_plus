#!/usr/bin/env python3
"""
generate_skills_catalog.py

Generate `docs/SKILLS_CATALOG.md` from:
- `sources/refound/refound_lenny_skills_manifest.csv` (category/name/slug/upstream URLs)
- `skills/<slug>/SKILL.md` YAML frontmatter (description)

Usage:
  python3 scripts/generate_skills_catalog.py
  python3 scripts/generate_skills_catalog.py --out docs/SKILLS_CATALOG.md
"""

from __future__ import annotations

import argparse
import csv
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

import yaml  # type: ignore


def _read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"Missing YAML frontmatter opening marker in {skill_md}")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError(f"Missing YAML frontmatter closing marker in {skill_md}")
    raw = "\n".join(lines[1:end]).strip()
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Frontmatter must be a mapping in {skill_md}")
    return data


def _table_escape(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="sources/refound/refound_lenny_skills_manifest.csv")
    ap.add_argument("--skills-root", default="skills")
    ap.add_argument("--out", default="docs/SKILLS_CATALOG.md")
    args = ap.parse_args()

    manifest_path = Path(args.manifest).resolve()
    skills_root = Path(args.skills_root).resolve()
    out_path = Path(args.out).resolve()

    if not manifest_path.exists():
        raise SystemExit(f"Manifest not found: {manifest_path}")
    if not skills_root.exists():
        raise SystemExit(f"Skills root not found: {skills_root}")

    rows: list[dict[str, str]] = []
    with manifest_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k: (v or "").strip() for k, v in r.items()})

    by_cat: "OrderedDict[str, list[dict[str, str]]]" = OrderedDict()
    for r in rows:
        cat = r.get("category", "Uncategorized") or "Uncategorized"
        by_cat.setdefault(cat, []).append(r)

    converted_count = len(rows)
    # Meta-skill(s) are whatever else exists in skills/.
    all_skill_dirs = [p for p in sorted(skills_root.iterdir()) if p.is_dir() and (p / "SKILL.md").exists()]
    meta_count = max(0, len(all_skill_dirs) - converted_count)

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    out_lines: list[str] = []
    out_lines.append("# Skills catalog")
    out_lines.append(f"Converted skills: **{converted_count}** (from Refound/Lenny)")
    out_lines.append(f"Meta-skill(s): **{meta_count}** (e.g., `lenny-skillpack-creator`)")
    out_lines.append("")
    out_lines.append(f"_Generated: {generated_at} by `python3 scripts/generate_skills_catalog.py`._")
    out_lines.append("")
    out_lines.append("Upstream source: `https://refoundai.com/lenny-skills/`")
    out_lines.append("")

    for cat, items in by_cat.items():
        out_lines.append(f"## {cat} ({len(items)})")
        out_lines.append("| Skill | Command | Description | Upstream |")
        out_lines.append("|---|---|---|---|")

        for r in items:
            slug = r.get("slug", "")
            if not slug:
                continue
            display = r.get("skill_name", slug)
            skill_dir = skills_root / slug
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                desc = "(missing skill pack in `skills/`)"
            else:
                fm = _read_frontmatter(skill_md)
                desc_raw = fm.get("description", "")
                desc = _table_escape(" ".join(str(desc_raw).split()))

            upstream_url = r.get("skill_page_url", "").strip()
            upstream_cell = f"[refound]({upstream_url})" if upstream_url else ""

            out_lines.append(
                f"| [{_table_escape(display)}](../skills/{slug}/) | `{slug}` | {_table_escape(desc)} | {upstream_cell} |"
            )
        out_lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(out_lines).rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

