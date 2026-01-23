# problem-definition

Create a **Problem Definition Pack**: a crisp, testable description of a user problem (problem statement + JTBD + alternatives + evidence/assumptions + success metrics + scope boundaries + prototype plan).

## What this skill produces
- Context snapshot (decision, timeline, constraints)
- Problem statement (1-liner + expanded) + why now
- Jobs To Be Done (JTBD) + target segment notes
- Current alternatives (including analog/non-digital) + gaps + switching costs
- Evidence & assumptions log (with tests)
- Success criteria + guardrails
- Scope boundaries (in/out, non-goals, dependencies)
- Prototype / learning plan
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `problem-definition`. Context: <product + target user + signal>. Decision: <what we need to decide by when>. Constraints: <must-haves>. Output: a Problem Definition Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/problem-definition/`) using the templates in `references/TEMPLATES.md`.

## Example prompts
- “We’re a B2B invoicing tool. SMB admins are churning in month 2. Define the problem space and JTBD; include alternatives and a prototype plan.”
- “Leadership wants ‘AI insights’. Push back and define the underlying user pain point and success metrics first.”
- “We see drop-off at onboarding step 3. Create a Problem Definition Pack with evidence/assumptions and guardrails.”

