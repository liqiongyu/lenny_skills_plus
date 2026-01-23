#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DocPair:
    en: Path
    zh: Path


HEADING_RE = re.compile(r"^(#{1,6})\s+\S")


def iter_headings_levels(path: Path) -> list[int]:
    levels: list[int] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if match:
            levels.append(len(match.group(1)))
    return levels


def has_marker(path: Path, expected: str, *, max_lines: int = 20) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()[:max_lines]
    return any(expected in line for line in lines)


def find_pairs(repo_root: Path) -> list[DocPair]:
    scopes = [
        repo_root,  # root-level docs (*.md)
        repo_root / "docs",
        repo_root / "sources" / "refound",
    ]

    pairs: list[DocPair] = []
    for scope in scopes:
        for en in sorted(scope.glob("*.md")):
            if en.name.endswith(".zh-CN.md"):
                continue
            zh = en.with_name(en.stem + ".zh-CN.md")
            pairs.append(DocPair(en=en, zh=zh))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(description="Check EN + zh-CN doc pairing/alignment.")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Repo root (default: parent of scripts/).",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    pairs = find_pairs(repo_root)

    errors: list[str] = []

    for pair in pairs:
        en_rel = pair.en.relative_to(repo_root)
        zh_rel = pair.zh.relative_to(repo_root)

        if not pair.zh.exists():
            errors.append(f"Missing zh-CN doc for {en_rel}: expected {zh_rel}")
            continue

        # Markers: ensure quick language navigation exists near the top.
        if not has_marker(pair.en, f"> 中文版: `{pair.zh.name}`"):
            errors.append(f"Missing/incorrect zh marker in {en_rel} (expected: `> 中文版: `{pair.zh.name}``)")

        if not has_marker(pair.zh, f"> English version: `{pair.en.name}`"):
            errors.append(f"Missing/incorrect EN marker in {zh_rel} (expected: `> English version: `{pair.en.name}``)")

        # Heading structure: ensure section boundaries match.
        en_headings = iter_headings_levels(pair.en)
        zh_headings = iter_headings_levels(pair.zh)

        if not en_headings:
            errors.append(f"No headings found in {en_rel}")
        if not zh_headings:
            errors.append(f"No headings found in {zh_rel}")
        if en_headings and en_headings[0] != 1:
            errors.append(f"{en_rel} first heading is not H1")
        if zh_headings and zh_headings[0] != 1:
            errors.append(f"{zh_rel} first heading is not H1")

        if en_headings != zh_headings:
            errors.append(
                f"Heading mismatch: {en_rel} ({len(en_headings)}) vs {zh_rel} ({len(zh_headings)})"
            )

    if errors:
        print("Bilingual docs check failed:\n", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1

    print(f"Bilingual docs OK ({len(pairs)} pairs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

