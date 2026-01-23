#!/usr/bin/env python3
"""
normalize_doc_links.py

Convert non-clickable inline code references like `docs/FOO.md` into clickable Markdown links:
  `docs/FOO.md`  ->  [docs/FOO.md](docs/FOO.md)

Rules:
- Only converts inline code spans that contain a single token (no whitespace).
- Only converts when the referenced path resolves to an existing file relative to the current
  markdown file (so we don't create broken links for conceptual names like `SKILL.md`).
- Skips fenced code blocks.
- Skips absolute paths, home paths (~), URLs, and placeholder paths containing <...>.

Usage:
  python3 scripts/normalize_doc_links.py
  python3 scripts/normalize_doc_links.py --dry-run
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CODE_SPAN_RE = re.compile(r"`([^`\s]+)`")
FENCE_START_RE = re.compile(r"^\s*(`{3,}|~{3,})")
SKILLPACK_REF_FILENAMES = {
    "INTAKE.md",
    "WORKFLOW.md",
    "TEMPLATES.md",
    "CHECKLISTS.md",
    "RUBRIC.md",
    "SOURCE_SUMMARY.md",
    "EXAMPLES.md",
}


def _should_link(token: str, *, base_dir: Path) -> bool:
    if token.startswith(("http://", "https://")):
        return False
    if "://" in token:
        return False
    if token.startswith(("~", "/")):
        return False
    if token.startswith((".codex/", ".claude/")):
        return False
    if "<" in token or ">" in token:
        return False
    if token.endswith("/"):
        return False

    path_part = token.split("#", 1)[0].split("?", 1)[0]
    candidate = (base_dir / path_part).resolve()
    try:
        candidate.relative_to(base_dir.resolve())
    except Exception:
        # Prevent links that escape the current folder via weird paths.
        return False

    return candidate.exists() and candidate.is_file()


def _rewrite_markdown(text: str, *, md_path: Path) -> str:
    base_dir = md_path.parent
    out_lines: list[str] = []

    in_fence = False
    fence_marker = ""
    in_skillpack_ref_block = False
    skillpack_ref_block_indent = 0

    for line in text.splitlines(keepends=True):
        indent = len(line) - len(line.lstrip(" "))

        fence = FENCE_START_RE.match(line)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = marker[0]  # ` or ~
            else:
                # Close if marker matches the current fence type.
                if marker[0] == fence_marker:
                    in_fence = False
                    fence_marker = ""
            out_lines.append(line)
            continue

        if in_fence:
            out_lines.append(line)
            continue

        # In docs, a bullet that introduces `references/` typically means subsequent indented bullets
        # are describing per-skill pack files (not sibling docs). Avoid turning those filenames into
        # misleading links (e.g., `WORKFLOW.md` linking to docs/WORKFLOW.md).
        stripped = line.lstrip(" ")
        if stripped.startswith("-") and "`references/`" in line:
            in_skillpack_ref_block = True
            skillpack_ref_block_indent = indent
        elif in_skillpack_ref_block and stripped.strip() and indent <= skillpack_ref_block_indent:
            in_skillpack_ref_block = False

        def repl(m: re.Match[str]) -> str:
            token = m.group(1)
            if token == "README.md" and "English version:" not in line and "中文版:" not in line:
                # "README.md" is frequently used as a conceptual filename (e.g., skill pack structure),
                # and many folders contain a README.md, which can create misleading links.
                return m.group(0)
            if (
                in_skillpack_ref_block
                and md_path.parts[-2:-1] == ("docs",)
                and token in SKILLPACK_REF_FILENAMES
            ):
                return m.group(0)
            if not _should_link(token, base_dir=base_dir):
                return m.group(0)
            return f"[{token}]({token})"

        out_lines.append(CODE_SPAN_RE.sub(repl, line))

    return "".join(out_lines)


def _iter_markdown_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []

    # Root-level docs (*.md), including AGENTS.md.
    files.extend(sorted(repo_root.glob("*.md")))

    # docs/
    docs_dir = repo_root / "docs"
    if docs_dir.exists():
        files.extend(sorted(docs_dir.glob("*.md")))

    # skills/** (canonical only)
    skills_dir = repo_root / "skills"
    if skills_dir.exists():
        for p in sorted(skills_dir.rglob("*.md")):
            if "__pycache__" in p.parts:
                continue
            files.append(p)

    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Repo root (default: parent of scripts/).",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    md_files = _iter_markdown_files(repo_root)

    changed = 0
    for md in md_files:
        original = md.read_text(encoding="utf-8", errors="replace")
        rewritten = _rewrite_markdown(original, md_path=md)
        if rewritten != original:
            changed += 1
            rel = md.relative_to(repo_root)
            if args.dry_run:
                print(f"[would-fix] {rel}")
            else:
                md.write_text(rewritten, encoding="utf-8")
                print(f"[fixed] {rel}")

    print(f"[done] changed={changed} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
