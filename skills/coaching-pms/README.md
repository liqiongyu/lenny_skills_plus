# coaching-pms

Create a **PM Coaching Pack** to coach product managers with a clear definition of “good PM”, an evidence-based assessment, a growth plan, and a follow-up cadence.

## What this skill produces
- Definition of “Good PM” (context-specific competency model + Bloom depth ladder)
- Current assessment (evidence-based strengths/gaps + current vs target levels)
- Shared vision (1–3 growth bets + success signals)
- Development plan (weekly reps + stretch work + artifacts + measurement)
- Coaching cadence + session toolkit (1:1 agenda + prompts + review points)
- Follow-up tracker + review plan
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `coaching-pms`. Context: <company/team/stage>. PM: <level/scope/tenure>. Goal: <what must be more true in 8–12 weeks>. Evidence: <2–5 anonymized examples>. Output: a PM Coaching Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/people/coaching/<pm-name>/`) using `references/TEMPLATES.md`.

## Example prompts
- “Coach my PM on strategic thinking. They ship well but struggle to pick the right problems. Build an 8-week plan.”
- “Assess a new senior PM’s strengths/gaps from these notes and propose the top 2 coaching bets.”
- “Define what ‘good PM’ means for our growth team and align expectations with a development plan for a mid-level PM.”

