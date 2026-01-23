# written-communication

Create a **Written Communication Pack**: a brief, an outline, and a final-ready draft (email/memo/doc/status update) optimized for clarity and action.

## What this skill produces
- Message brief (audience, goal, ask, constraints)
- Outline (TL;DR, key points, “how/next steps”)
- Draft artifact (email/memo/doc/status update)
- Optional canonical doc skeleton (single source of truth)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `written-communication`. Artifact: <email|memo|doc|status update>. Audience: <who>. Goal/ask: <what they should do>. Context: <key facts + links>. Constraints: <tone, length, deadline>. Output: <final draft + next steps>.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, specify a folder path (e.g., `docs/comms/<topic>/`) and the agent will write the pack using `references/TEMPLATES.md`.

## Example prompts
- “Draft an exec email: we’re delaying launch 2 weeks; ask is approval to cut scope; include next steps with owners.”
- “Rewrite this doc to be clearer and more actionable; keep it under 400 words; add a TL;DR and explicit next steps.”
- “Create a canonical doc template for Project X and a weekly status update format we can reuse.”

