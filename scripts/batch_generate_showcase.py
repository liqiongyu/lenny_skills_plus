#!/usr/bin/env python3
"""Batch generate SHOWCASE.md + eval_config.json for completed evals.

Usage:
    python3 scripts/batch_generate_showcase.py [--slugs slug1,slug2,...] [--all]

Scans skills/*/eval/ for completed evals (both with_skill.md and without_skill.md exist)
but no SHOWCASE.md yet. Generates SHOWCASE.md + eval_config.json for each.

Note: This generates a TEMPLATE showcase without LLM grading.
      Grading is done separately via subagents.
"""

import argparse
import json
import re
from datetime import date
from pathlib import Path

SKILLS_DIR = Path("skills")
PROMPTS_FILE = Path("scripts/eval_prompts.json")


def strip_skill_prefix(prompt: str) -> str:
    return re.sub(r"^Use\s+`[^`]+`\.?\s*", "", prompt).strip()


def generate_eval_config(slug: str, prompt: str) -> dict:
    return {
        "slug": slug,
        "model": "claude-opus-4-6",
        "date": str(date.today()),
        "prompt": {
            "original": prompt,
            "baseline": strip_skill_prefix(prompt),
        },
        "with_skill": {
            "file": "with_skill.md",
        },
        "without_skill": {
            "file": "without_skill.md",
        },
    }


def generate_showcase_template(slug: str, prompt: str) -> str:
    title = slug.replace("-", " ").title()
    return f"""\
# Showcase: {title}

> Demonstrates the value of the `{slug}` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> {prompt}

## Results Summary

_Grading pending._

## With Skill Output

<details>
<summary>Expand full output</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: {date.today()}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slugs", default=None, help="Comma-separated slugs to process")
    ap.add_argument("--all", action="store_true", help="Process all completed evals")
    args = ap.parse_args()

    prompts = json.loads(PROMPTS_FILE.read_text())

    if args.slugs:
        slugs = args.slugs.split(",")
    elif args.all:
        slugs = sorted(prompts.keys())
    else:
        # Auto-detect: has both outputs but no SHOWCASE.md
        slugs = []
        for slug in sorted(prompts.keys()):
            eval_dir = SKILLS_DIR / slug / "eval"
            if (eval_dir / "with_skill.md").exists() and \
               (eval_dir / "without_skill.md").exists() and \
               not (eval_dir / "SHOWCASE.md").exists():
                slugs.append(slug)

    if not slugs:
        print("No evals to process.")
        return

    generated = 0
    for slug in slugs:
        eval_dir = SKILLS_DIR / slug / "eval"
        if not (eval_dir / "with_skill.md").exists() or \
           not (eval_dir / "without_skill.md").exists():
            print(f"  SKIP {slug}: missing output files")
            continue

        prompt = prompts.get(slug, {}).get("prompt", "")

        # Write eval_config.json
        config = generate_eval_config(slug, prompt)
        (eval_dir / "eval_config.json").write_text(
            json.dumps(config, indent=2, ensure_ascii=False) + "\n"
        )

        # Write SHOWCASE.md template
        showcase = generate_showcase_template(slug, prompt)
        (eval_dir / "SHOWCASE.md").write_text(showcase)

        ws = (eval_dir / "with_skill.md").stat().st_size
        wos = (eval_dir / "without_skill.md").stat().st_size
        print(f"  {slug}: with={ws//1024}k without={wos//1024}k")
        generated += 1

    print(f"\nGenerated {generated} SHOWCASE.md files (template, grading pending)")


if __name__ == "__main__":
    main()
