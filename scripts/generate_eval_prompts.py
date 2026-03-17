#!/usr/bin/env python3
"""Generate eval_prompts.json with a test prompt for every skill.

Strategy:
1. Try extracting an explicit Prompt: line from EXAMPLES.md
2. Try constructing from Scenario:/Situation:/SUT: fields
3. Fall back to constructing from SKILL.md description + Example 1 text

Output: scripts/eval_prompts.json
"""

import json
import re
from pathlib import Path

SKILLS_DIR = Path("skills")
OUTPUT = Path("scripts/eval_prompts.json")


def try_explicit_prompt(content: str) -> str | None:
    """Extract Prompt: "..." or **Prompt:** "..." lines."""
    patterns = [
        r"""\*\*Prompt:\*\*\s*[""\u201c](.+?)[""\u201d]""",
        r"""Prompt:\s*[""\u201c](.+?)[""\u201d]""",
    ]
    for pat in patterns:
        m = re.search(pat, content, re.DOTALL)
        if m:
            return m.group(1).strip()
    return None


def try_scenario_fields(content: str, slug: str) -> str | None:
    """Construct prompt from Scenario:/Situation:/SUT: fields in Example 1."""
    # Find Example 1 section
    ex1_match = re.search(
        r"##\s+Example\s+(?:1|A)[^\n]*\n(.*?)(?=\n##\s+|$)",
        content, re.DOTALL
    )
    if not ex1_match:
        return None

    ex1 = ex1_match.group(1)

    # Try SUT + Decision + Constraints pattern (ai-evals style)
    sut = re.search(r"\*\*SUT:\*\*\s*(.+?)(?:\n|$)", ex1)
    decision = re.search(r"\*\*Decision:\*\*\s*(.+?)(?:\n|$)", ex1)
    if sut and decision:
        constraints = re.search(r"\*\*Constraints:\*\*\s*(.+?)(?:\n|$)", ex1)
        parts = [f"Use `{slug}`.", f"SUT: {sut.group(1).strip()}",
                 f"Decision: {decision.group(1).strip()}"]
        if constraints:
            parts.append(f"Constraints: {constraints.group(1).strip()}")
        return " ".join(parts)

    # Try Scenario: pattern (delegating-work style)
    scenario = re.search(r"\*\*Scenario:\*\*\s*(.+?)(?:\n|$)", ex1)
    if scenario:
        return f"Use `{slug}`. {scenario.group(1).strip()}"

    # Try Situation: pattern (founder-sales style)
    situation = re.search(r"\*\*Situation:\*\*\s*(.+?)(?:\n|$)", ex1)
    if situation:
        return f"Use `{slug}`. {situation.group(1).strip()}"

    # Try Context: pattern
    context = re.search(r"\*\*Context:\*\*\s*(.+?)(?:\n|$)", ex1)
    if context:
        return f"Use `{slug}`. {context.group(1).strip()}"

    return None


def try_example_title(content: str, slug: str) -> str | None:
    """Use Example 1 title + first descriptive line as prompt."""
    ex1_match = re.search(
        r"##\s+Example\s+(?:1|A)\s*[—–-]\s*(.+?)\n(.*?)(?=\n##\s+|$)",
        content, re.DOTALL
    )
    if not ex1_match:
        return None

    title = ex1_match.group(1).strip()
    body = ex1_match.group(2).strip()

    # Get first non-empty, non-header line from body
    for line in body.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("Expected") \
                and not line.startswith("**Good output"):
            # Clean up bold markers
            line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
            return f"Use `{slug}`. {title}: {line}"

    return f"Use `{slug}`. {title}."


def get_deliverable_name(skill_dir: Path) -> str:
    """Extract the main deliverable name from SKILL.md."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ""
    content = skill_md.read_text()
    # Look for "Produce a/an **X Pack**" or similar
    m = re.search(r"Produce\s+(?:a|an)\s+\*\*(.+?)\*\*", content)
    if m:
        return m.group(1)
    return ""


def generate_prompt(skill_dir: Path) -> tuple[str, str]:
    """Generate a test prompt for a skill. Returns (prompt, method)."""
    slug = skill_dir.name
    examples_path = skill_dir / "references" / "EXAMPLES.md"

    if not examples_path.exists():
        return f"Use `{slug}`. Produce the complete deliverable pack.", "no_examples"

    content = examples_path.read_text()

    # Method 1: Explicit Prompt: line
    prompt = try_explicit_prompt(content)
    if prompt:
        return prompt, "explicit_prompt"

    # Method 2: Scenario/Situation/SUT fields
    prompt = try_scenario_fields(content, slug)
    if prompt:
        return prompt, "scenario_fields"

    # Method 3: Example title + first line
    prompt = try_example_title(content, slug)
    if prompt:
        return prompt, "example_title"

    # Method 4: Fallback
    deliverable = get_deliverable_name(skill_dir)
    if deliverable:
        return f"Use `{slug}`. Produce a {deliverable}.", "fallback_deliverable"

    return f"Use `{slug}`. Produce the complete deliverable pack.", "fallback_generic"


def main():
    results = {}
    stats = {"explicit_prompt": 0, "scenario_fields": 0, "example_title": 0,
             "fallback_deliverable": 0, "fallback_generic": 0, "no_examples": 0}

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        prompt, method = generate_prompt(skill_dir)
        results[skill_dir.name] = {
            "prompt": prompt,
            "method": method,
        }
        stats[method] += 1

    OUTPUT.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")

    print(f"Generated {len(results)} prompts -> {OUTPUT}")
    print("\nExtraction methods:")
    for method, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {method}: {count}")

    # Show fallbacks that might need manual review
    fallbacks = [(k, v) for k, v in results.items()
                 if v["method"].startswith("fallback")]
    if fallbacks:
        print(f"\n=== FALLBACKS (may need manual review): {len(fallbacks)} ===")
        for slug, data in fallbacks:
            print(f"  {slug}: {data['prompt'][:80]}...")


if __name__ == "__main__":
    main()
