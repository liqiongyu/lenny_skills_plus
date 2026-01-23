# Skill pack format (house style)

This repo standardizes each skill pack to maximize reliability in agent execution and portability across Codex + Claude Code.

## Canonical structure

Each skill lives at:

- `skills/<skill-slug>/`

Required files:

- `SKILL.md`
  - YAML frontmatter: `name`, `description` (YAML-safe and tool-friendly; prefer single-line quotes)
  - Short, operational instructions:
    - Scope (covers / when to use / when NOT to use)
    - Inputs (minimum required + missing-info strategy)
    - Outputs (deliverables / artifacts)
    - Workflow (5–9 steps)
    - Pointers to `references/` for details
- `README.md`
  - A human-friendly overview
  - Example prompts to trigger the skill
- `references/`
  - `INTAKE.md`: question bank + missing-info policy
  - `WORKFLOW.md`: expanded step-by-step
  - `TEMPLATES.md`: copy/paste templates
  - `CHECKLISTS.md`: DoD checklists
  - `RUBRIC.md`: scoring / quality thresholds
  - `SOURCE_SUMMARY.md`: upstream source compression + key insights
  - `EXAMPLES.md`: additional prompts + boundary example

## Design principles

- Progressive disclosure: keep `SKILL.md` compact; store depth in `references/`
- Artifact-driven outputs: the skill must produce concrete deliverables, not generic advice
- Boundary clarity: explicitly define when NOT to use the skill
- Safe-by-default: assume no external network, ask before risky actions, keep sensitive info out
