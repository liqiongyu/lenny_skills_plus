# user-onboarding

Create an **Onboarding & Activation Pack** to improve product onboarding (FTUE) and drive activation: aha moment definition, first 30 seconds + first mile plan, journey map + friction log, experiment backlog, and measurement plan.

## What this skill produces
- Context snapshot (goal, segment, constraints, baseline)
- Current FTUE map + friction log + biggest leak
- Activation / aha moment spec + validation plan
- “First 30 seconds” experience spec (fast, interactive win)
- “First mile” onboarding plan (milestones → activation + mechanics)
- Prioritized experiment backlog + experiment cards
- Measurement + instrumentation plan (events, properties, dashboards, guardrails)
- Rollout/rollback + risk plan
- Risks / Open questions / Next steps

## How to use (prompt)

“Use `user-onboarding`. Product: <what it is + for whom>. Segment: <1–2>. Platform: <web/mobile>. Baseline: <signup→activation funnel + time-to-value>. Problem: <where users drop + why>. Constraints: <timebox/capacity/channels/privacy>. Output: an Onboarding & Activation Pack.”

If details are missing, the skill asks up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and proceeds with explicit assumptions.

## Optional file output
If you want deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/onboarding/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “Define our activation event and redesign onboarding to improve D7 activation by 30% this quarter.”
- “Make the first 30 seconds feel magical and reduce time-to-first-value from 3 minutes to under 60 seconds.”
- “Create 6 onboarding experiments with success metrics, guardrails, and an instrumentation plan.”

