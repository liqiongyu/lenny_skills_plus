#!/usr/bin/env python3
"""Check which skills have auto-extractable eval prompts from EXAMPLES.md."""

import re
from pathlib import Path

SKILLS_DIR = Path("skills")

def extract_prompt(examples_md: Path) -> str | None:
    content = examples_md.read_text()
    patterns = [
        r"""\*\*Prompt:\*\*\s*[""\u201c](.+?)[""\u201d]""",
        r"""Prompt:\s*[""\u201c](.+?)[""\u201d]""",
    ]
    for pat in patterns:
        m = re.search(pat, content, re.DOTALL)
        if m:
            return m.group(1).strip()
    return None

ok = []
fail = []

for skill_dir in sorted(SKILLS_DIR.iterdir()):
    if not skill_dir.is_dir():
        continue
    examples = skill_dir / "references" / "EXAMPLES.md"
    if not examples.exists():
        fail.append((skill_dir.name, "no EXAMPLES.md"))
        continue
    prompt = extract_prompt(examples)
    if prompt:
        ok.append((skill_dir.name, prompt[:80]))
    else:
        fail.append((skill_dir.name, "no extractable prompt"))

print(f"=== AUTO-EXTRACTABLE: {len(ok)} ===")
for slug, p in ok:
    print(f"  {slug}: {p}...")

print(f"\n=== NEED MANUAL PROMPT: {len(fail)} ===")
for slug, reason in fail:
    print(f"  {slug}: {reason}")
