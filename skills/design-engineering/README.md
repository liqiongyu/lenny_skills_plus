# design-engineering

Create a **Design Engineering Execution Pack** to stand up (or level up) a design engineering practice: charter + prototype→production workflow + design-to-code contract + component/flow delivery plan + quality bar.

## What this skill produces
- Context snapshot (goals, constraints, success signals)
- Design Engineering charter (mission, scope, boundaries, engagement model)
- Prototype → production workflow (prototype ladder + rules + review gates)
- Design-to-code contract (tokens/components/spec handoff, PR expectations, QA)
- Component/flow delivery plan (prioritized backlog + milestones + owners)
- Quality bar (checklists + rubric score)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `design-engineering`. Context: <product + team>. Goal: <why now>. Current state: <design artifacts + stack + existing design system>. Constraints: <timeline/a11y/perf/compliance>. Output: a Design Engineering Execution Pack.”

If key details are missing, the skill asks up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceeds with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/design-engineering/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “We want to create a design engineering function—write the charter, boundaries, and operating cadence.”
- “Our prototypes don’t survive handoff—define a prototype→production pipeline and review gates.”
- “We need a high-craft UI component library—create the design-to-code contract and a delivery plan.”

