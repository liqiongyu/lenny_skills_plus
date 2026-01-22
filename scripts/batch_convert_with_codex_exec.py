#!/usr/bin/env python3
"""
batch_convert_with_codex_exec.py

OPTIONAL: Semi-automated conversion using `codex exec`.

This is intentionally conservative and meant as a starting point.
You should still review every generated skill pack.

Prereqs:
- Codex CLI installed and authenticated
- Sources already downloaded into `sources/refound/raw/<slug>/SKILL.md` (or HTML fallback: `page.html` / legacy `skill_page.html`)
- This repo contains the meta-skill at `.codex/skills/lenny-skillpack-creator`

Usage:
  python scripts/batch_convert_with_codex_exec.py --limit 3
  python scripts/batch_convert_with_codex_exec.py --only-category "Growth"
  python scripts/batch_convert_with_codex_exec.py --start-after-slug retention-engagement

Notes:
- By default, this runs Codex unattended in a sandbox:
  `codex --sandbox workspace-write --ask-for-approval never exec ...`
- Pass `--no-full-auto` to run `codex exec ...` using your Codex config defaults (may prompt for approvals).
"""

from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path
from typing import Optional

def find_source(slug: str) -> Optional[Path]:
    base = Path("sources/refound/raw") / slug
    # Support both legacy and current fallback HTML filenames.
    for candidate in [base / "SKILL.md", base / "skill_page.html", base / "page.html"]:
        if candidate.exists():
            return candidate
    return None

def run_codex(prompt: str, full_auto: bool = True) -> int:
    cmd = ["codex"]
    if full_auto:
        # Unattended, still sandboxed (no network by default in workspace-write).
        # NOTE: `--ask-for-approval` is a global flag and must appear before `exec`.
        cmd += ["--sandbox", "workspace-write", "--ask-for-approval", "never"]
    cmd += ["exec", prompt]
    proc = subprocess.run(cmd)
    return proc.returncode

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="sources/refound/refound_lenny_skills_manifest.csv")
    ap.add_argument("--limit", type=int, default=0, help="0 = no limit")
    ap.add_argument("--only-category", default="", help="Only convert skills in this category name")
    ap.add_argument("--start-after-slug", default="", help="Skip until after this slug is seen")
    ap.add_argument("--out-root", default="skills", help="Where to write converted skill packs")
    ap.add_argument(
        "--no-full-auto",
        action="store_true",
        help="Run codex exec without unattended flags (uses your Codex config defaults).",
    )
    args = ap.parse_args()

    manifest = Path(args.manifest)
    if not manifest.exists():
        raise SystemExit(f"Missing manifest: {manifest}")

    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    started = args.start_after_slug == ""
    converted = 0
    skipped_missing_src = 0

    with manifest.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = (row.get("slug") or "").strip()
            category = (row.get("category") or "").strip()
            if not slug:
                continue

            if args.only_category and category != args.only_category:
                continue

            if not started:
                if slug == args.start_after_slug:
                    started = True
                continue

            src = find_source(slug)
            if not src:
                print(f"[skip] missing source for {slug}")
                skipped_missing_src += 1
                continue

            out_dir = out_root / slug
            out_dir.mkdir(parents=True, exist_ok=True)

            prompt = (
                f"Use the $lenny-skillpack-creator skill to convert the Refound/Lenny skill at: {src}\n"
                f"Target persona: inferred from category = {category}\n"
                f"Output: write a complete executable skill pack to: {out_dir}\n"
                f"All output must be English.\n"
                f"After writing files, run: python3 .codex/skills/lenny-skillpack-creator/scripts/lint_skillpack.py {out_dir}\n"
                f"If lint fails, fix the skill pack and re-run lint until it passes, then stop.\n"
            )

            rc = run_codex(prompt, full_auto=(not args.no_full_auto))
            if rc != 0:
                print(f"[fail] codex exec returned {rc} for {slug}")
                return rc

            converted += 1
            if args.limit and converted >= args.limit:
                break

    print(f"[done] converted={converted} skipped_missing_src={skipped_missing_src}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
