# managing-tech-debt

Create a **Tech Debt Management Pack**: debt register + scoring/prioritization + strategy decisions (refactor/migrate/rebuild/deprecate) + incremental execution plan + migration/rollback plan + metrics + stakeholder cadence.

## What this skill produces
- Context snapshot
- Tech Debt Register (inventory table)
- Scoring model + prioritized list
- Strategy decision memo(s) (refactor vs migrate vs rebuild vs deprecate)
- Execution plan (milestones, sequencing, resourcing)
- Migration + rollback plan (if applicable)
- Metrics plan (baseline, targets, instrumentation gaps, small tests)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `managing-tech-debt`. Context: <system/service>. Pain: <symptoms + why now>. Horizon: <timeline>. Constraints: <team capacity/compliance/freeze windows>. Stakeholders: <who decides>. Output: a Tech Debt Management Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/tech-debt/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “Create a tech debt register for our monolith and prioritize the top 10 items for the next 2 months.”
- “We suspect our UX fragmentation is caused by backend constraints—build a plan that ties debt paydown to user-visible improvements.”
- “Make the business case for funding a migration off legacy auth, including dual-run costs and a rollback plan.”

