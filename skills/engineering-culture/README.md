# engineering-culture

Create an **Engineering Culture Operating System Pack**: capability map + culture code + org↔architecture alignment + clock-speed/DevEx backlog + workflow contract + rollout + measurement plan.

## What this skill produces
- Culture + capability snapshot (evidence-based gaps)
- Engineering culture code (principles → behaviors → decision rules)
- Org ↔ architecture alignment brief (Conway’s Law analysis + changes)
- Clock speed + DevEx improvement backlog (prioritized initiatives + metrics)
- Cross-functional workflow contract (issues/PRs/releases + AI norms)
- Rollout + measurement plan (30/60/90, rituals, metrics + guardrails)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `engineering-culture`. Context: <product + org stage + eng size>. Symptoms: <2–5 examples>. Current delivery: <release cadence + CI/CD + tests>. Architecture: <coupling/ownership hotspots>. Goal: <what should be true in 4–12 weeks>. Constraints: <timeline, compliance, capacity>. Output: an Engineering Culture Operating System Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/engineering-culture/`) using `references/TEMPLATES.md`.

## Example prompts
- “Increase clock speed: we want daily deploys with fewer regressions—create a backlog and rollout plan.”
- “We’re restructuring teams—use Conway’s Law to propose team boundaries and interfaces.”
- “Define AI-assisted development norms so engineers shift toward specs, reviews, and architectural oversight.”

