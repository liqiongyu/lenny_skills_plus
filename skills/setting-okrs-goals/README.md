# setting-okrs-goals

Create an **OKR & Goals Pack**: aligned objectives + measurable key results + anti-gaming guardrails + “default-on” systems/habits + review cadence + grading plan.

## What this skill produces
- Context snapshot (strategy anchor, horizon, scope, constraints, stakeholders)
- Alignment map (company goal → team objective(s), one step away)
- Draft OKRs (1–3 Objectives; 2–5 KRs each) with definitions, baselines, targets, owners, cadence
- Metric robustness + guardrails (anti-gaming; ratio/denominator rules; quality guardrails)
- Systems & habits plan (recurring mechanisms that drive progress)
- Review + grading plan (weekly cadence, mid-cycle checkpoint, end-of-cycle learning retro)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `setting-okrs-goals`. Context: <product + team>. Cycle: <quarter/year>. Company goal/North Star: <statement>. Baselines: <current metrics>. Constraints: <capacity/commitments>. Output: an OKR & Goals Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/okrs/`) using `references/TEMPLATES.md`.

## Example prompts
- “We’re a B2B SaaS. Set Q2 OKRs for Activation. Our company goal is ‘Increase weekly active teams completing the core workflow.’ Baseline: 2,400 WA teams. Output an OKR & Goals Pack.”
- “We’re a marketplace. Set OKRs for Trust & Safety for the next quarter; include guardrails so we don’t harm growth.”
- “Draft annual OKRs for our product org; propose base vs ambitious options, and include a grading plan.”

