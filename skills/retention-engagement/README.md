# retention-engagement

Create a **Retention & Engagement Improvement Pack**: retention diagnosis, activation/aha moment definition, lever hypotheses, prioritized experiments, measurement plan, and a 30/60/90 execution plan.

## What this skill produces
- Context snapshot (goal, segments, constraints, timebox)
- Metric definitions + guardrails
- Retention + engagement diagnosis (failure modes + biggest leaks)
- Activation/aha moment spec + validation plan
- Lever hypotheses map (onboarding, habit, accruing value, re-engagement)
- Experiment backlog (prioritized) + experiment cards
- Measurement + instrumentation plan
- 30/60/90 plan
- Risks / Open questions / Next steps

## How to use (prompt)

“Use `retention-engagement`. Product: <what it is + for whom>. Segment(s): <1–2>. Stage: <pre-PMF/early PMF/growth>. Baseline: <retention + engagement numbers>. Problem: <where users drop/churn>. Constraints: <timebox/capacity/channels/privacy>. Output: a Retention & Engagement Improvement Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and proceed with explicit assumptions.

## Optional file output
If you want deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/retention/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “Our D1 is fine but D7 falls off a cliff. Diagnose the failure mode and propose experiments to improve weekly habit.”
- “Define our activation/aha moment and redesign onboarding to get more users there in their first session.”
- “Create a winback + reactivation plan and instrument the measurement we need to learn.”

