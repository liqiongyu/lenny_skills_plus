# pricing-strategy

Create a **Pricing Strategy Pack**: value metric + WTP plan + packaging & plans + price-point options + conversion mechanics + rollout + review cadence.

## What this skill produces
- Context snapshot (goal, ICP, motion, constraints, time box)
- Value metric + segmentation hypotheses
- WTP evidence plan (who to talk to, what to ask, how to interpret)
- Packaging & plans table (free vs paid, limits, add-ons)
- Price-point options + recommendation (incl. discount policy)
- Conversion mechanics plan (sampling premium value, trial design, friction reduction)
- Rollout + migration + instrumentation plan (KPIs/guardrails)
- Pricing review cadence (default revisit every 6–12 months)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `pricing-strategy`. Context: <product + ICP + use case>. Current pricing: <plans/prices/trial or ‘none’>. Objective: <what decision this should change>. Motion: <self-serve/sales-led/hybrid>. Constraints: <billing/contracts/brand>. Evidence: <metrics/notes/links>. Output: a Pricing Strategy Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/pricing-strategy/`) using `references/TEMPLATES.md`.

## Example prompts
- “We’re moving from self-serve to sales assist. Define self-serve vs sales-led thresholds and propose new packaging.”
- “Design a reverse trial and sampling strategy for premium features, with guardrails and success metrics.”
- “We’re repricing after a major feature launch. Propose 2–3 price options, a WTP plan, and a rollout checklist.”

