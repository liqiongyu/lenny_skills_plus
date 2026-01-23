#!/usr/bin/env python3
"""
generate_audit_report.py

Generate `docs/AUDIT_REPORT.md` with a lightweight, reproducible audit summary.

This report is meant for humans (project credibility), not as a security/compliance guarantee.

Usage:
  python3 scripts/generate_audit_report.py
  python3 scripts/generate_audit_report.py --out docs/AUDIT_REPORT.md
  python3 scripts/generate_audit_report.py --out docs/AUDIT_REPORT.md --out-zh docs/AUDIT_REPORT.zh-CN.md
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
    ap.add_argument("--out-zh", default="docs/AUDIT_REPORT.zh-CN.md")
    args = ap.parse_args()

    skills_root = Path(args.skills_root).resolve()
    manifest_path = Path(args.manifest).resolve()
    out_path = Path(args.out).resolve()
    out_zh_path = Path(args.out_zh).resolve() if args.out_zh else None

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

    def render(lang: str) -> str:
        if lang not in {"en", "zh-CN"}:
            raise ValueError(f"Unsupported lang: {lang}")

        if lang == "en":
            title = "# Audit report"
            counterpart = "> 中文版: [AUDIT_REPORT.zh-CN.md](AUDIT_REPORT.zh-CN.md)"
            generated_line = f"Generated: {generated}"
            intro = "This report summarizes automated checks over the skill packs in `skills/`."
            inv_title = "## Inventory"
            inv_canonical = f"- Canonical skill packs under `skills/`: {len(skill_dirs)}"
            inv_converted = f"- Converted Refound/Lenny skills: {converted_count}"
            inv_meta = f"- Meta-skill(s): {meta_count} (`lenny-skillpack-creator`, etc.)"
            structural_title = "## Structural validation"
            ci_pass = "- ✅ `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` passed."
            ci_fail = "- ❌ `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` failed."
            structural_ok = "- ✅ Each skill pack contains: `SKILL.md`, `README.md`, and `references/` with the required core files."
            structural_missing = f"- ❌ Missing required files in {len(missing_files)} place(s)."
            fm_title = "## Frontmatter compliance (cross-tool)"
            fm_ok = "- ✅ Every `SKILL.md` has YAML frontmatter with required fields (`name`, `description`)."
            fm_fail = f"- ❌ Frontmatter failures: {len(fm_failures)}"
            name_ok = "- ✅ `name` matches the folder slug."
            name_fail = f"- ❌ Name mismatch: {len(name_mismatch)}"
            desc_style_line = f"- ℹ️ Description YAML style: {dict(desc_style)}"
            lang_title = "## Language check"
            cjk_ok = "- ✅ No CJK (Chinese/Japanese/Korean) characters detected across `skills/**/*.md`."
            cjk_fail = f"- ❌ Found CJK characters in {len(cjk_hits)} file(s)."
            rec_title = "## Recommended ongoing checks"
            rec_1 = "- Run `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` before commits."
            rec_2 = "- After mirroring into `.codex/skills/` and `.claude/skills/`, run `python3 scripts/ci_check_skillpacks.py` to ensure mirrors are identical."
            rec_3 = "- Periodically smoke-test a few skills per category with real tasks."
            footer = "_Generated by `python3 scripts/generate_audit_report.py`._"
        else:
            title = "# 审计报告（Audit report）"
            counterpart = "> English version: [AUDIT_REPORT.md](AUDIT_REPORT.md)"
            generated_line = f"生成时间：{generated}"
            intro = "本报告汇总了对 `skills/` 下 skill packs 的自动化检查结果。"
            inv_title = "## 清单（Inventory）"
            inv_canonical = f"- `skills/` 下 canonical skill packs 数量：{len(skill_dirs)}"
            inv_converted = f"- 已转换的 Refound/Lenny skills：{converted_count}"
            inv_meta = f"- Meta-skill：{meta_count}（例如 `lenny-skillpack-creator`）"
            structural_title = "## 结构校验（Structural validation）"
            ci_pass = "- ✅ `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` 通过。"
            ci_fail = "- ❌ `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` 失败。"
            structural_ok = "- ✅ 每个 skill pack 都包含：`SKILL.md`、`README.md`，以及带必需核心文件的 `references/`。"
            structural_missing = f"- ❌ 有 {len(missing_files)} 处缺少必需文件。"
            fm_title = "## Frontmatter 合规（跨工具）"
            fm_ok = "- ✅ 每个 `SKILL.md` 都包含带必需字段（`name`、`description`）的 YAML frontmatter。"
            fm_fail = f"- ❌ Frontmatter 错误：{len(fm_failures)}"
            name_ok = "- ✅ `name` 与文件夹 slug 一致。"
            name_fail = f"- ❌ `name` 不一致：{len(name_mismatch)}"
            desc_style_line = f"- ℹ️ `description` 的 YAML 写法统计：{dict(desc_style)}"
            lang_title = "## 语言检查（Language check）"
            cjk_ok = "- ✅ `skills/**/*.md` 中未检测到 CJK（中/日/韩）字符。"
            cjk_fail = f"- ❌ 在 {len(cjk_hits)} 个文件中检测到 CJK 字符。"
            rec_title = "## 建议的持续检查（Recommended ongoing checks）"
            rec_1 = "- 提交前运行：`python3 scripts/ci_check_skillpacks.py --skip-mirror-check`。"
            rec_2 = "- 镜像到 `.codex/skills/` 与 `.claude/skills/` 后，运行：`python3 scripts/ci_check_skillpacks.py` 校验镜像一致。"
            rec_3 = "- 定期对每个 category 抽样做真实任务 smoke test。"
            footer = "_由 `python3 scripts/generate_audit_report.py` 生成。_"

        lines_out: list[str] = []
        lines_out.append(title)
        lines_out.append("")
        lines_out.append(counterpart)
        lines_out.append("")
        lines_out.append(generated_line)
        lines_out.append("")
        lines_out.append(intro)
        lines_out.append("")
        lines_out.append(inv_title)
        lines_out.append(inv_canonical)
        if converted_count:
            lines_out.append(inv_converted)
            lines_out.append(inv_meta)
        lines_out.append("")
        lines_out.append(structural_title)
        lines_out.append(ci_pass if ci_rc == 0 else ci_fail)
        lines_out.append(structural_ok if not missing_files else structural_missing)
        lines_out.append("")
        lines_out.append(fm_title)
        lines_out.append(fm_ok if not fm_failures else fm_fail)
        lines_out.append(name_ok if not name_mismatch else name_fail)
        lines_out.append(desc_style_line)
        lines_out.append("")
        lines_out.append(lang_title)
        lines_out.append(cjk_ok if not cjk_hits else cjk_fail)
        lines_out.append("")
        lines_out.append(rec_title)
        lines_out.append(rec_1)
        lines_out.append(rec_2)
        lines_out.append(rec_3)
        lines_out.append("")
        lines_out.append(footer)

        return "\n".join(lines_out).rstrip() + "\n"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render("en"), encoding="utf-8")

    if out_zh_path is not None:
        out_zh_path.parent.mkdir(parents=True, exist_ok=True)
        out_zh_path.write_text(render("zh-CN"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
