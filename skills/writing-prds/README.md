# writing-prds

Create a **PRD Pack** that cross-functional partners can execute: clear narrative, scoped requirements, measurable success metrics, and a quality gate before circulation.

## What this skill produces
- Context snapshot + artifact selection (PR/FAQ vs PRD vs AI add-ons)
- PR/FAQ (optional) to force customer narrative first
- PRD with goals/non-goals, requirements (R1…Rn), UX flows, metrics, rollout
- For AI features: Prompt Set + Eval Spec (judge prompts + pass/fail criteria)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `writing-prds`. Context: <product, user, problem, why now>. Constraints: <timeline, platform, policy>. Output: <PRD only | PR/FAQ + PRD | PRD + evals + prompt set>.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/prds/<feature>/`) using `references/TEMPLATES.md`.

## Example prompts
- “We’re a B2B SaaS. Write a PR/FAQ + PRD for ‘Saved views’. Goal: increase weekly active admins. Constraints: ship in 6 weeks.”
- “This is an AI feature: write a PRD + Prompt Set + Eval Spec for an AI reply assistant; include safety constraints and how we’ll test quality.”
- “Turn these notes into a PRD, but push back if we’re missing a clear problem statement or success metrics.”

