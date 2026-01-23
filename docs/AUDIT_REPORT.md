# Audit report
Generated: 2026-01-23 03:33:40

This report summarizes automated checks over the skill packs in `skills/`.

## Inventory
- Canonical skill packs under `skills/`: 87
- Converted Refound/Lenny skills: 86
- Meta-skill(s): 1 (`lenny-skillpack-creator`)

## Structural validation
- ✅ All skill packs pass `scripts/ci_check_skillpacks.py --skip-mirror-check`.
- ✅ Each skill pack contains: `SKILL.md`, `README.md`, and `references/` with the required core files.

## Frontmatter compliance (cross-tool)
- ✅ Every `SKILL.md` has YAML frontmatter with `name` and `description`.
- ✅ `name` matches the folder slug.
- ✅ `name` and `description` are single-line scalars and within conservative size limits (name ≤ 100 chars, description ≤ 500 chars).

## Language check
- ✅ No CJK (Chinese/Japanese/Korean) characters detected across `SKILL.md`, `README.md`, and `references/*.md` for the 86 converted skills.

## Content contract
- ✅ All 86 converted skills include the standard sections in `SKILL.md`:
  - Scope (covers / when to use / when NOT to use)
  - Inputs (+ missing-info strategy)
  - Outputs (deliverables)
  - Workflow (step-by-step)

## Examples coverage
- ✅ All converted skills include `references/EXAMPLES.md` plus example prompts in `README.md`.

## Recommended ongoing checks
- Run `python3 scripts/ci_check_skillpacks.py --skip-mirror-check` before commits.
- After mirroring into `.codex/skills/` and `.claude/skills/`, run `python3 scripts/ci_check_skillpacks.py` to ensure mirrors are identical.
- Periodically smoke-test a few skills per category with real tasks.
