# writing-north-star-metrics

Create a **North Star Metric Pack**: a crisp narrative + a measurable North Star metric + a driver tree (leading inputs + guardrails) that product teams can use as a decision tie-breaker.

## What this skill produces
- North Star Narrative (qualitative value model)
- Candidate metrics (3–5) + selection rationale
- North Star Metric spec (definition, formula, window, segmentation, owner, data source)
- Driver tree (inputs/proxies) + guardrails (anti-gaming)
- Validation & rollout plan (dashboards, cadence, owners, decision rules)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `writing-north-star-metrics`. Context: <product + customer + value moment>. Constraints: <what we can measure + horizon>. Output: a North Star Metric Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/north-star-metric/`) using the templates in `references/TEMPLATES.md`.

## Example prompts
- “We’re a B2B SaaS (team collaboration). Our value moment is ‘a team successfully completes their first project together’. Propose a North Star metric and driver tree we can move this quarter.”
- “We’re a marketplace for home services. Refresh our North Star metric; current issue is we optimize for bookings but quality is slipping.”
- “Our CEO says the North Star should be retention. Push back and propose a better operating metric + guardrails.”

