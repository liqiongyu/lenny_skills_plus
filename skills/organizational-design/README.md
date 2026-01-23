# organizational-design

Create an **Organizational Design Pack** to redesign structure + operating model: clarify what you’re optimizing for, map dependency/decision bottlenecks, choose a centralization posture, propose org options, and plan a safe transition.

## What this skill produces
- Org Design Brief (goals, constraints, principles, success metrics)
- Current-State Map (teams/charters, dependency hotspots, decision rights, layers)
- Operating Model Decision (centralized ↔ decentralized; functional ↔ divisional/value-stream)
- Target Org Blueprint (team topology, charters, interfaces, leadership roles)
- Operating Mechanisms (decision rights, standards, planning cadence, interface contracts)
- Transition Plan (phasing, comms, risk mitigations, measurement)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `organizational-design`. Context: <company + stage + functions in-scope>. Current structure: <teams + reporting>. Symptoms: <examples>. Goals: <what must improve>. Constraints: <headcount/timeline/non-negotiables>. Output: an Organizational Design Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and proceed with explicit assumptions.

## Optional file output
If you want deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/org-design/<initiative>/`) using `references/TEMPLATES.md`.

## Example prompts
- “We’re debating centralized vs decentralized product decisions. Propose 2–3 org options and recommend one.”
- “We have too many layers and unclear decision rights. Produce an Organizational Design Pack and a transition plan.”
- “Redesign our teams to reduce dependencies between platform and product work while keeping an integrated UX.”

