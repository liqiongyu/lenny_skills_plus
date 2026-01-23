# competitive-analysis

Create a **Competitive Analysis Pack**: competitive alternatives map + competitor landscape + differentiation & positioning hypotheses + battlecards + monitoring plan.

## What this skill produces
- Context snapshot (decision, ICP, use case, constraints)
- Competitive alternatives map (status quo, workarounds, analog, direct/indirect)
- Competitor landscape table (top 5–10) with evidence + confidence
- Customer decision criteria + comparison matrix
- Differentiation & positioning hypotheses (incl. proof points + tradeoffs)
- Win themes + loss risks
- Battlecards (3–5 priority competitors)
- Monitoring plan (signals, cadence, update triggers)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `competitive-analysis`. Context: <product + ICP + use case>. Decision: <what this analysis should change>. Known competitors: <list or ‘unknown’>. Constraints: <geo/price band/compliance>. Evidence: <links/notes>. Output: a Competitive Analysis Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/competitive-analysis/`) using `references/TEMPLATES.md`.

## Example prompts
- “We’re a B2B security product. We’re losing to Vendor X and internal builds. Create a battlecard for X and a competitive alternatives map.”
- “We’re entering a new segment. Compare alternatives from the customer’s perspective and propose two positioning options.”
- “We have 2 weeks before a board update. Produce a high-confidence competitor landscape for our top 5 alternatives and a monitoring plan.”

