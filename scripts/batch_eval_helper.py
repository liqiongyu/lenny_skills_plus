#!/usr/bin/env python3
"""Helper to generate batch eval agent prompts for Claude Code subagents.

Usage:
    python3 scripts/batch_eval_helper.py --batch N [--size 5]

Outputs the agent prompts for batch N (0-indexed).
"""

import argparse
import json
from pathlib import Path

SKILLS_DIR = Path("skills")
PROMPTS_FILE = Path("scripts/eval_prompts.json")


def get_todo_list() -> list[tuple[str, str]]:
    """Return list of (slug, prompt) for skills that haven't been eval'd yet."""
    data = json.loads(PROMPTS_FILE.read_text())
    todo = []
    for slug, info in sorted(data.items()):
        if info.get("skip"):
            continue
        eval_dir = SKILLS_DIR / slug / "eval"
        # Skip if both outputs already exist
        if (eval_dir / "with_skill.md").exists() and \
           (eval_dir / "without_skill.md").exists():
            continue
        todo.append((slug, info["prompt"]))
    return todo


def get_skill_files(slug: str) -> list[str]:
    """Get list of all .md files in a skill directory."""
    skill_dir = SKILLS_DIR / slug
    files = [str(skill_dir / "SKILL.md")]
    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        files.extend(str(f) for f in sorted(refs_dir.glob("*.md")))
    return files


def strip_skill_prefix(prompt: str) -> str:
    """Remove 'Use `skill-name`.' prefix for baseline prompt."""
    import re
    return re.sub(r"^Use\s+`[^`]+`\.?\s*", "", prompt).strip()


def generate_with_skill_prompt(slug: str, prompt: str) -> str:
    """Generate the subagent prompt for with-skill run."""
    files = get_skill_files(slug)
    file_list = "\n".join(f"- {f}" for f in files)
    out_path = SKILLS_DIR / slug / "eval" / "with_skill.md"

    return f"""You are an expert agent executing a skill pack. Read ALL skill files, then follow the skill's workflow to produce the complete deliverable.

SKILL FILES (read ALL):
{file_list}

USER PROMPT:
{prompt}

INSTRUCTIONS:
1. Read all listed files first
2. Follow the skill's workflow step by step
3. Produce ALL required deliverables
4. Be thorough and concrete — this is a showcase of the skill's quality
5. Write the complete output to: {out_path}"""


def generate_without_skill_prompt(slug: str, prompt: str) -> str:
    """Generate the subagent prompt for without-skill (baseline) run."""
    baseline_prompt = strip_skill_prefix(prompt)
    out_path = SKILLS_DIR / slug / "eval" / "without_skill.md"

    return f"""You are a helpful AI assistant. Answer the following prompt thoroughly from your general knowledge. Do NOT read any skill files or reference documents.

PROMPT:
{baseline_prompt}

INSTRUCTIONS:
1. Do NOT read any files from the repository
2. Produce your best, most thorough response based on general knowledge
3. Structure your response well with clear sections
4. Write the complete output to: {out_path}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=0, help="Batch number (0-indexed)")
    ap.add_argument("--size", type=int, default=5, help="Batch size")
    ap.add_argument("--list", action="store_true", help="Just list remaining skills")
    args = ap.parse_args()

    todo = get_todo_list()

    if args.list:
        print(f"Remaining: {len(todo)} skills")
        for i, (slug, prompt) in enumerate(todo):
            batch_num = i // args.size
            print(f"  [{batch_num}] {slug}: {prompt[:60]}...")
        return

    start = args.batch * args.size
    batch = todo[start:start + args.size]

    if not batch:
        print("No more skills to process!")
        return

    print(f"Batch {args.batch}: {len(batch)} skills (of {len(todo)} remaining)")
    print(f"Skills: {', '.join(s for s, _ in batch)}")
    print()

    for slug, prompt in batch:
        print(f"=== {slug} ===")
        print(f"WITH_SKILL prompt ({len(generate_with_skill_prompt(slug, prompt))} chars)")
        print(f"WITHOUT_SKILL prompt ({len(generate_without_skill_prompt(slug, prompt))} chars)")
        print()


if __name__ == "__main__":
    main()
