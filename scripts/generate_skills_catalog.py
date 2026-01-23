#!/usr/bin/env python3
"""
generate_skills_catalog.py

Generate `docs/SKILLS_CATALOG.md` from:
- `sources/refound/refound_lenny_skills_manifest.csv` (category/name/slug/upstream URLs)
- `skills/<slug>/SKILL.md` YAML frontmatter (description)

Usage:
  python3 scripts/generate_skills_catalog.py
  python3 scripts/generate_skills_catalog.py --out docs/SKILLS_CATALOG.md
  python3 scripts/generate_skills_catalog.py --out docs/SKILLS_CATALOG.md --out-zh docs/SKILLS_CATALOG.zh-CN.md
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

def _render(
    *,
    lang: str,
    by_cat: "OrderedDict[str, list[dict[str, str]]]",
    skills_root: Path,
    converted_count: int,
    meta_count: int,
    generated_at: str,
) -> str:
    if lang not in {"en", "zh-CN"}:
        raise ValueError(f"Unsupported lang: {lang}")

    if lang == "en":
        title = "# Skills catalog"
        counterpart = "> 中文版: `SKILLS_CATALOG.zh-CN.md`"
        converted_line = f"Converted skills: **{converted_count}** (from Refound/Lenny)"
        meta_line = f"Meta-skill(s): **{meta_count}** (e.g., `lenny-skillpack-creator`)"
        generated_line = f"_Generated: {generated_at} by `python3 scripts/generate_skills_catalog.py`._"
        upstream_line = "Upstream source: `https://refoundai.com/lenny-skills/`"
        table_header = "| Skill | Command | Description | Upstream |"
        table_sep = "|---|---|---|---|"
    else:
        title = "# 技能目录（Skills catalog）"
        counterpart = "> English version: `SKILLS_CATALOG.md`"
        converted_line = f"已转换 skills：**{converted_count}**（来自 Refound/Lenny）"
        meta_line = f"Meta-skill：**{meta_count}**（例如 `lenny-skillpack-creator`）"
        generated_line = f"_生成时间：{generated_at}（由 `python3 scripts/generate_skills_catalog.py` 生成）。_"
        upstream_line = "上游来源：`https://refoundai.com/lenny-skills/`"
        table_header = "| Skill | 命令 | 描述 | 上游 |"
        table_sep = "|---|---|---|---|"

    out_lines: list[str] = []
    out_lines.append(title)
    out_lines.append("")
    out_lines.append(counterpart)
    out_lines.append("")
    out_lines.append(converted_line)
    out_lines.append(meta_line)
    out_lines.append("")
    out_lines.append(generated_line)
    out_lines.append("")
    out_lines.append(upstream_line)
    out_lines.append("")

    for cat, items in by_cat.items():
        out_lines.append(f"## {cat} ({len(items)})")
        out_lines.append(table_header)
        out_lines.append(table_sep)

        for r in items:
            slug = r.get("slug", "")
            if not slug:
                continue
            display = r.get("skill_name", slug)
            skill_dir = skills_root / slug
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                desc = "(missing skill pack in `skills/`)" if lang == "en" else "（`skills/` 中缺少该 skill pack）"
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

    return "\n".join(out_lines).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="sources/refound/refound_lenny_skills_manifest.csv")
    ap.add_argument("--skills-root", default="skills")
    ap.add_argument("--out", default="docs/SKILLS_CATALOG.md")
    ap.add_argument("--out-zh", default="docs/SKILLS_CATALOG.zh-CN.md")
    args = ap.parse_args()

    manifest_path = Path(args.manifest).resolve()
    skills_root = Path(args.skills_root).resolve()
    out_path = Path(args.out).resolve()
    out_zh_path = Path(args.out_zh).resolve() if args.out_zh else None

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

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        _render(
            lang="en",
            by_cat=by_cat,
            skills_root=skills_root,
            converted_count=converted_count,
            meta_count=meta_count,
            generated_at=generated_at,
        ),
        encoding="utf-8",
    )

    if out_zh_path is not None:
        out_zh_path.parent.mkdir(parents=True, exist_ok=True)
        out_zh_path.write_text(
            _render(
                lang="zh-CN",
                by_cat=by_cat,
                skills_root=skills_root,
                converted_count=converted_count,
                meta_count=meta_count,
                generated_at=generated_at,
            ),
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
