# organizational-transformation

Create an **Organizational Transformation Pack** to move a company toward a **modern product operating model** (without treating “framework adoption” as the goal).

## What this skill produces
- Transformation Charter (why now, goals/non-goals, principles, success metrics, constraints)
- Current-State Diagnostic (system map, bottlenecks, capability gaps, resistance map)
- Target Product Operating Model Blueprint (team types, roles, decision rights, cadences, artifacts)
- Pilot / Nudge Plan (90 days) (2–4 safe-to-try pilots + learning loop)
- Transformation Roadmap (6–12 months) (phases, big rocks, milestones, resourcing)
- Change + Comms Plan (stakeholders, messages, enablement, resistance handling)
- Governance + Metrics (leading indicators, review cadence, guardrails)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `organizational-transformation`. Context: <company + stage + domain>. Why now: <drivers>. Current model: <how product work runs today>. Symptoms: <examples>. Constraints: <timeline/headcount/regulatory>. Output: an Organizational Transformation Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and proceed with explicit assumptions.

## Optional file output
If you want deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/org-transformation/<initiative>/`) using `references/TEMPLATES.md`.

## Example prompts
- “Move us from feature teams to empowered product teams; propose 90-day pilots and a 12-month roadmap.”
- “We keep adopting frameworks but behavior doesn’t change; create a transformation charter + governance plan.”
- “Build a comms + enablement plan for a product operating model shift with skeptical stakeholders.”

