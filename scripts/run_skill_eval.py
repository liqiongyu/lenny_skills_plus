#!/usr/bin/env python3
"""Run a skill evaluation: compare skill-guided vs baseline LLM output.

Usage:
    python3 scripts/run_skill_eval.py skills/<slug> [--model MODEL] [--prompt "..."]

Requires: ANTHROPIC_API_KEY environment variable.

Outputs saved to skills/<slug>/eval/:
    - with_skill.md      Skill-guided output
    - without_skill.md   Baseline output (no skill)
    - eval_config.json   Metadata (prompt, tokens, timing)
"""

import argparse
import json
import re
import time
from datetime import date
from pathlib import Path

import anthropic

DEFAULT_MODEL = "claude-sonnet-4-6-20250514"


def load_skill_context(skill_dir: Path) -> str:
    """Load SKILL.md + all references/ into a single context string."""
    parts = []

    skill_md = skill_dir / "SKILL.md"
    if skill_md.exists():
        parts.append(f"# SKILL.md\n\n{skill_md.read_text()}")

    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        for ref_file in sorted(refs_dir.glob("*.md")):
            parts.append(f"# references/{ref_file.name}\n\n{ref_file.read_text()}")

    return "\n\n---\n\n".join(parts)


def extract_test_prompt(skill_dir: Path) -> str:
    """Extract the first example prompt from references/EXAMPLES.md."""
    examples_md = skill_dir / "references" / "EXAMPLES.md"
    if not examples_md.exists():
        raise FileNotFoundError(f"No EXAMPLES.md in {skill_dir}/references/")

    content = examples_md.read_text()

    # Try common patterns (bold and non-bold, straight and smart quotes)
    patterns = [
        r"""\*\*Prompt:\*\*\s*["\u201c](.+?)["\u201d]""",
        r"""Prompt:\s*["\u201c](.+?)["\u201d]""",
    ]
    for pat in patterns:
        m = re.search(pat, content, re.DOTALL)
        if m:
            return m.group(1).strip()

    raise ValueError(
        f"Could not auto-extract prompt from {examples_md}. "
        "Pass --prompt to provide one manually."
    )


def strip_skill_prefix(prompt: str) -> str:
    """Remove 'Use `skill-name`.' prefix so the baseline gets a neutral prompt."""
    return re.sub(r"^Use\s+`[^`]+`\.?\s*", "", prompt).strip()


def call_llm(client: anthropic.Anthropic, model: str, system: str | None,
             user_msg: str) -> dict:
    """Single LLM call. Returns output text + metadata."""
    kwargs: dict = dict(
        model=model,
        max_tokens=8192,
        messages=[{"role": "user", "content": user_msg}],
    )
    if system:
        kwargs["system"] = system

    start = time.time()
    resp = client.messages.create(**kwargs)
    duration = time.time() - start

    return {
        "output": resp.content[0].text,
        "duration_s": round(duration, 2),
        "tokens": {
            "input": resp.usage.input_tokens,
            "output": resp.usage.output_tokens,
        },
        "stop_reason": resp.stop_reason,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Run skill eval (with vs without skill)")
    ap.add_argument("skill_dir", type=Path,
                    help="Path to skill directory, e.g. skills/ai-product-strategy")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="Model ID")
    ap.add_argument("--prompt", default=None,
                    help="Custom test prompt (overrides EXAMPLES.md extraction)")
    ap.add_argument("--output-dir", default=None,
                    help="Output directory (default: <skill_dir>/eval/)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Extract prompt and print config without making API calls")
    args = ap.parse_args()

    skill_dir = args.skill_dir.resolve()
    if not (skill_dir / "SKILL.md").exists():
        ap.error(f"No SKILL.md found in {skill_dir}")

    slug = skill_dir.name
    out_dir = Path(args.output_dir) if args.output_dir else skill_dir / "eval"

    # --- prompt ---
    original_prompt = args.prompt or extract_test_prompt(skill_dir)
    baseline_prompt = strip_skill_prefix(original_prompt)

    print(f"Skill:   {slug}")
    print(f"Model:   {args.model}")
    print(f"Prompt:  {original_prompt[:120]}...")
    print(f"Output:  {out_dir}")
    print()

    if args.dry_run:
        print("[dry-run] Would run 2 API calls. Exiting.")
        return

    out_dir.mkdir(parents=True, exist_ok=True)

    # --- skill context ---
    skill_context = load_skill_context(skill_dir)
    system_prompt = (
        "You are an expert agent executing a skill pack. "
        "Follow the skill's workflow precisely, produce all required "
        "deliverables, and apply every quality check defined in the skill.\n\n"
        + skill_context
    )

    client = anthropic.Anthropic()

    # --- with skill ---
    print("Running WITH skill...")
    with_res = call_llm(client, args.model, system_prompt, original_prompt)
    print(f"  {with_res['tokens']['output']} output tokens, {with_res['duration_s']}s")

    # --- without skill (baseline) ---
    print("Running WITHOUT skill (baseline)...")
    without_res = call_llm(client, args.model, None, baseline_prompt)
    print(f"  {without_res['tokens']['output']} output tokens, {without_res['duration_s']}s")

    # --- save ---
    (out_dir / "with_skill.md").write_text(with_res["output"])
    (out_dir / "without_skill.md").write_text(without_res["output"])

    config = {
        "slug": slug,
        "model": args.model,
        "date": str(date.today()),
        "prompt": {
            "original": original_prompt,
            "baseline": baseline_prompt,
        },
        "with_skill": {
            "duration_s": with_res["duration_s"],
            "tokens": with_res["tokens"],
            "stop_reason": with_res["stop_reason"],
        },
        "without_skill": {
            "duration_s": without_res["duration_s"],
            "tokens": without_res["tokens"],
            "stop_reason": without_res["stop_reason"],
        },
    }
    (out_dir / "eval_config.json").write_text(
        json.dumps(config, indent=2, ensure_ascii=False) + "\n"
    )

    print(f"\nSaved to {out_dir}/")
    print(f"Next: python3 scripts/generate_showcase.py {args.skill_dir}")


if __name__ == "__main__":
    main()
