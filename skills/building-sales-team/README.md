# building-sales-team

Create a **Sales Team Build Pack**: readiness gate + team design/hiring sequence + role scorecards + interview loop + onboarding/ramp + operating cadence.

## What this skill produces
- Context snapshot (stage, motion, ICP, constraints, targets)
- Readiness gate (hire-now vs wait) with measurable criteria
- Team design + hiring sequence plan (who to hire first/second; when; why)
- Role scorecards (AE/SDR/hybrid) + evaluation criteria
- Interview loop + practical exercises + score sheet
- Onboarding + 30/60/90 ramp plan + coaching/metrics cadence
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `building-sales-team`. Stage: <seed/Series A>. Motion: <PLG/inbound/outbound/enterprise>. ICP: <who buys + who uses>. Current baseline: <# first meetings, win rate, ACV, cycle>. Constraints: <budget/headcount/timeline>. Output: a Sales Team Build Pack with readiness gate, hiring sequence, role scorecards, interview plan, and 30/60/90 ramp.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/building-sales-team/`) using `references/TEMPLATES.md`.

## Example prompts
- “Should we hire sales now or wait? We have 40 first meetings and 6 closes.”
- “Create an interview loop for PM-like AEs who can sell to engineers.”
- “Design a PLG → product-led sales pilot pod (AE/SDR) and a ramp plan.”

