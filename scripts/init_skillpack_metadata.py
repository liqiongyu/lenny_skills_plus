#!/usr/bin/env python3
"""
init_skillpack_metadata.py

Create `skillpack.json` files for skill packs under `skills/`.

This keeps `SKILL.md` frontmatter minimal (name/description) while allowing the
repo to track package-like metadata such as per-skill versioning and authors.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").exists()


def load_manifest(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    out: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = (row.get("slug") or "").strip()
            if not slug:
                continue
            out[slug] = {k: (v or "").strip() for k, v in row.items()}
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-root", default="skills")
    ap.add_argument("--manifest", default="sources/refound/refound_lenny_skills_manifest.csv")
    ap.add_argument("--default-version", default="0.1.0")
    ap.add_argument(
        "--author",
        action="append",
        default=[],
        help="Default author identifier (repeatable). Example: --author liqiongyu",
    )
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing skillpack.json files.")
    args = ap.parse_args()

    skills_root = Path(args.skills_root).resolve()
    manifest_path = Path(args.manifest).resolve()

    if not skills_root.exists():
        print(f"[error] skills root not found: {skills_root}", file=sys.stderr)
        return 2

    manifest = load_manifest(manifest_path)
    default_authors = [a.strip() for a in args.author if a.strip()] or ["liqiongyu"]

    created = 0
    updated = 0
    skipped = 0

    for skill_dir in sorted([p for p in skills_root.iterdir() if is_skill_dir(p)]):
        slug = skill_dir.name
        out_path = skill_dir / "skillpack.json"

        row = manifest.get(slug)
        origin = "refound" if row else "original"
        category = (row.get("category") or "").strip() if row else ""
        upstream = None
        if row:
            upstream = {
                "page_url": (row.get("skill_page_url") or "").strip(),
                "skill_md_url": (row.get("skill_md_url") or "").strip(),
            }

        data = {
            "schema_version": 1,
            "skill_slug": slug,
            "version": args.default_version,
            "authors": default_authors,
            "contributors": [],
            "origin": origin,
        }
        if category:
            data["category"] = category
        if upstream and (upstream.get("page_url") or upstream.get("skill_md_url")):
            data["upstream"] = upstream

        if out_path.exists() and not args.overwrite:
            skipped += 1
            continue

        if out_path.exists():
            updated += 1
        else:
            created += 1

        out_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"[ok] skillpack.json: created={created} updated={updated} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

