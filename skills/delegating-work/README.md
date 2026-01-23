# delegating-work

Create a **Delegation Pack** to delegate work without micromanaging: context + decision rights + guardrails + cadence + review plan + debrief.

## What this skill produces
- Delegation brief (outcome, why, constraints, stakeholders, timeline)
- Decision rights + guardrails (autonomy level, escalation triggers, review points)
- Context handoff pack (background, links, “known gotchas”, example outputs)
- Execution cadence (check-ins + update format)
- Review plan (in the details, not in control)
- Debrief plan (learning capture + durable ownership)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `delegating-work`. Work: <what I’m delegating>. Owner: <who>. Why now: <context>. Outcome/DoD: <what good looks like>. Constraints: <non-negotiables>. Timeline: <dates>. Output: a Delegation Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/delegation/<project>/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “I need to delegate our Q2 pricing experiment to a PM. Draft the delegation brief + decision rights + weekly cadence.”
- “Delegate migrating a service to a junior engineer. I want to avoid micromanaging but need a high reliability bar—create a guardrails + review plan.”
- “I’m a new manager and I’m doing too much. Help me pick what to delegate and produce delegation briefs for the top 3.”

