#!/usr/bin/env python3
"""Generate SHOWCASE.md from eval outputs.

Usage:
    python3 scripts/generate_showcase.py skills/<slug> [--no-grade]

Reads eval outputs from skills/<slug>/eval/ and produces SHOWCASE.md.
With --no-grade, skips the LLM grading call and just compiles outputs.
"""

import argparse
import json
from pathlib import Path

import anthropic

GRADING_SYSTEM = """\
You are a skill-pack evaluation grader. You will compare two LLM outputs
produced for the same user prompt:

1. **Without Skill** — a baseline LLM response with no skill guidance.
2. **With Skill** — a response guided by a structured skill pack.

Evaluate both outputs and produce a structured comparison in Markdown.
Be specific, fair, and evidence-based. Reference concrete sections,
deliverables, or missing elements — not vague impressions.

Output exactly this format (no extra preamble):

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | [1-line assessment] | [1-line assessment] |
| Completeness | [X deliverables produced] | [Y deliverables produced] |
| Actionability | [can a reader act on this?] | [can a reader act on this?] |
| Specificity | [generic or concrete?] | [generic or concrete?] |
| Quality gates | [checks/rubric present?] | [checks/rubric present?] |

## Key Differences

1. [Most important difference — what does the skill add?]
2. [Second most important]
3. [Third most important]

## Verdict

[2-3 sentence summary: what value does the skill pack add over a vanilla LLM response?]
"""


def load_rubric(skill_dir: Path) -> str:
    """Load the skill's RUBRIC.md for grading context, if available."""
    rubric_path = skill_dir / "references" / "RUBRIC.md"
    if rubric_path.exists():
        return f"\n\n## Skill Rubric (for reference)\n\n{rubric_path.read_text()}"
    return ""


def grade_outputs(client: anthropic.Anthropic, model: str,
                  prompt: str, with_output: str, without_output: str,
                  rubric_context: str) -> str:
    """Call LLM to produce a structured comparison."""
    user_msg = (
        f"## User Prompt\n\n{prompt}\n\n"
        f"## Without Skill Output\n\n{without_output}\n\n"
        f"## With Skill Output\n\n{with_output}"
        f"{rubric_context}"
    )
    resp = client.messages.create(
        model=model,
        max_tokens=2048,
        system=GRADING_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )
    return resp.content[0].text


def build_showcase(config: dict, with_output: str, without_output: str,
                   comparison: str) -> str:
    """Assemble the final SHOWCASE.md content."""
    slug = config["slug"]
    title = slug.replace("-", " ").title()
    ws = config["with_skill"]
    wos = config["without_skill"]

    return f"""\
# Showcase: {title}

> Demonstrates the value of the `{slug}` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> {config['prompt']['original']}

{comparison}

## With Skill Output

<details>
<summary>Expand full output ({ws['tokens']['output']} tokens, {ws['duration_s']}s)</summary>

{with_output}

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output ({wos['tokens']['output']} tokens, {wos['duration_s']}s)</summary>

{without_output}

</details>

---

**Metadata**
- Model: `{config['model']}`
- Date: {config['date']}
- With-skill tokens: {ws['tokens']['input']} input / {ws['tokens']['output']} output
- Baseline tokens: {wos['tokens']['input']} input / {wos['tokens']['output']} output
"""


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate SHOWCASE.md from eval outputs")
    ap.add_argument("skill_dir", type=Path,
                    help="Path to skill directory, e.g. skills/ai-product-strategy")
    ap.add_argument("--no-grade", action="store_true",
                    help="Skip LLM grading call (just compile outputs)")
    args = ap.parse_args()

    skill_dir = args.skill_dir.resolve()
    eval_dir = skill_dir / "eval"

    if not (eval_dir / "eval_config.json").exists():
        ap.error(
            f"No eval results in {eval_dir}/. "
            "Run run_skill_eval.py first."
        )

    config = json.loads((eval_dir / "eval_config.json").read_text())
    with_output = (eval_dir / "with_skill.md").read_text()
    without_output = (eval_dir / "without_skill.md").read_text()

    comparison = ""
    if not args.no_grade:
        print("Grading outputs...")
        client = anthropic.Anthropic()
        rubric_ctx = load_rubric(skill_dir)
        comparison = grade_outputs(
            client, config["model"],
            config["prompt"]["original"],
            with_output, without_output,
            rubric_ctx,
        )
        print("  Done.")

    showcase = build_showcase(config, with_output, without_output, comparison)

    out_path = eval_dir / "SHOWCASE.md"
    out_path.write_text(showcase)
    print(f"Generated: {out_path}")


if __name__ == "__main__":
    main()
