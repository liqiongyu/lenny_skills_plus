# vibe-coding

Turn an idea into a **functional, demo-ready prototype** using AI-assisted “vibe coding”: tight scope, timeboxed build loop, prompt pack, build plan, demo script, and safety checks.

## What this skill produces
- Vibe Coding Brief (demo promise, non-goals, constraints, timebox)
- Prototype Spec (flow, screens/components, data shape, acceptance criteria)
- Prompt Pack (copy/paste prompts to drive the coding agent safely)
- Build Plan + Task Board (vertical slices + validation per slice)
- Demo Script + Runbook (how to run and demo reliably)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `vibe-coding`. Context: <idea + target user>. Timebox: <30/60/90m>. Platform: <web/mobile/CLI>. Constraints: <privacy/data/tools>. Demo goal: <what a user can do>. Output: Vibe Coding Prototype Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the pack as files, ask the agent to write the artifacts under a folder you specify (e.g., `docs/prototypes/<project>/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “Use `vibe-coding` to build a 60-minute prototype of an internal dashboard. Mock data is fine; include a demo script.”
- “Replace this Figma onboarding flow with a clickable prototype using `vibe-coding`. Keep it simple and reliable.”
- “I keep getting stuck while vibe coding. Use `vibe-coding` to create a task board + prompt pack that keeps diffs small and verifiable.”

