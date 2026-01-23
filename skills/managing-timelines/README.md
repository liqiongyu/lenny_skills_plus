# managing-timelines

Turn a deadline, launch date, or delivery target into a concrete **Timeline Management Pack** (phases, milestones, RAG cadence, scope/change control, and stakeholder comms).

## What this skill produces
- Deadline & commitment model (commit vs forecast vs target)
- Phase plan (Discovery/Solutioning/Build/Launch) + decision gates + next commitment date
- Milestone tracker (owners, dependencies, dates, confidence, RAG) + RAG definitions
- Governance cadence (weekly review agenda + escalation triggers)
- Scope & change-control plan (cut list, freeze points, “trade don’t add” rule)
- Stakeholder comms pack (weekly update + escalation note templates)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `managing-timelines`. Context: <what we’re shipping + why now>. Date: <fixed deadline/target/window>. Constraints: <non-negotiables>. Team: <who + capacity>. Dependencies/risks: <bullets>. Output: a Timeline Management Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/managing-timelines/<project>/`) using the templates in [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “We must ship onboarding v2 by March 31 (hard deadline). Create a milestone plan with RAG definitions and a weekly exec update template.”
- “Stakeholders want dates, but scope is unclear. Build a phase plan where we only commit to Discovery/Solutioning dates first.”
- “We can demo an AI prototype quickly; create a plan that manages expectations between demo and production.”

