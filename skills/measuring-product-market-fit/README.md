# measuring-product-market-fit

Create a **PMF Measurement Pack** to assess product-market fit using survey + retention/usage evidence + reference-customer signals, then translate findings into an action plan and cadence.

## What this skill produces
- Context snapshot (decision, timebox, segments, constraints)
- PMF measurement model (core value moment, active user definition, signal set)
- Sean Ellis PMF survey plan + results (“very disappointed” overall + by segment)
- Retention/engagement evidence summary (with confidence + instrumentation gaps)
- Reference-customer / advocacy evidence log
- PMF Scorecard + diagnosis (by segment)
- Action plan + re-measurement cadence
- Risks / Open questions / Next steps

## How to use (prompt)

“Use `measuring-product-market-fit`. Product: <what it is + for whom>. Stage: <pre-PMF/early PMF/growth>. Segments: <ICP + key segments>. Data: <survey channel + analytics/retention>. Decision: <what we’ll do based on results by when>. Output: a PMF Measurement Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/pmf-measurement/`) using `references/TEMPLATES.md`.

## Example prompts
- “Run a Sean Ellis PMF survey plan for our B2B onboarding product and tell me what segments show must-have.”
- “Our retention is slipping. Diagnose whether we’re losing PMF and propose a re-measurement cadence and drift triggers.”
- “We’re a marketplace—measure PMF for the supply side first and give us the top actions to improve the core exchange.”

