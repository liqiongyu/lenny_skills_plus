# scoping-cutting

Create a **Scoping & Cutting Pack** to right-size scope and ship a meaningful slice within a fixed time budget (“appetite”).

## What this skill produces
- Context snapshot (decision, appetite/date, DRI, constraints)
- Outcome + hypothesis (what you’re validating) + success metrics/guardrails
- Appetite + “done means…” success bar
- Minimum Lovable Slice (MLS) spec (core flow, must-haves, non-goals)
- Cut list (keep/cut/defer with rationale)
- Validation plan (Wizard-of-Oz/concierge/prototype) with success criteria
- Delivery plan (milestones) + scope-change guardrails
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `scoping-cutting`. Context: <product + users + what we’re building>. Appetite/date: <time budget>. Constraints: <non-negotiables>. Candidate scope: <bullets>. Output: a Scoping & Cutting Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/scoping-cutting/<project>/`) using the templates in [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “We have 4 weeks for ‘bulk CSV import’ for admins. Cut scope and propose a minimum lovable slice; include a cut list and a Wizard-of-Oz validation plan.”
- “Scope creep is killing the project. Create an appetite-based scope plan and a scope-change policy for requests from Sales.”
- “Define an MVP for ‘AI weekly insights email’ as a hypothesis test; propose what to build now vs later and how to validate quickly.”

