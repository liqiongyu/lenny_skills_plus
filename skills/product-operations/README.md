# product-operations

Build a **Product Ops Operating System Pack**: charter + operating model + cadences/rituals + standardized artifacts + insights pipeline + release enablement + a 30/60/90 implementation plan.

## What this skill produces
- Product Ops charter (mission, scope, non-goals, success metrics)
- Operating model (engagement + ownership/RACI + escalation paths)
- Cadence calendar (recurring check-ins with required outputs)
- Artifact library (roadmap updates, decision log, product update, launch enablement templates)
- Insights pipeline (intake/triage, taxonomy, routing, dashboards)
- Release enablement system (readiness, comms, training, feedback loop)
- 30/60/90 implementation plan (pilot → rollout → iterate)
- Risks / Open questions / Next steps

## How to use (prompt)

“Use `product-operations`. Context: <company + product + org stage>. Pain: <top 2–3 frictions>. Stakeholders: <teams + decision owners>. Current cadence/artifacts: <what exists>. Constraints: <time/tools/resourcing>. Output: a Product Ops Operating System Pack.”

If key details are missing, the skill asks up to 5 intake questions (see `references/INTAKE.md`) and then proceeds with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/product-ops/`) using `references/TEMPLATES.md`.

## Example prompts
- “Create a Product Ops charter and operating cadence for a 12-person PM org; standardize roadmap updates and decision logs.”
- “Design an insights pipeline that routes CS feedback + data to the right product forums; include templates and RACI.”
- “Set up release enablement so Support/Sales are never surprised; include readiness checks and comms templates.”

