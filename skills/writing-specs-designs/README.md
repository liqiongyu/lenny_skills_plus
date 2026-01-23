# writing-specs-designs

Create a **Spec & Design Doc Pack** that helps product, design, and engineering align quickly: a low‑fidelity diagram of moving pieces, flows/states, a prototype brief (when “feel” matters), and testable acceptance criteria.

## What this skill produces
- Context snapshot (problem, why now, goals/non-goals, constraints)
- Low‑fidelity diagram (≤10 moving pieces) + key decisions
- User flows + state tables (happy path + edge cases)
- Prototype brief (what to prototype, fidelity, timebox, success criteria)
- Requirements + acceptance criteria (must/should/could)
- Measurement plan (metrics → events/data → owner)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `writing-specs-designs`. Context: <product, user, problem, why now>. Platform: <web/iOS/Android>. Constraints: <timeline, dependencies>. Output: <spec+design doc pack>.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/specs/<feature>/`) using `references/TEMPLATES.md`.

## Example prompts
- “We’re a consumer iOS app. Spec a new invite flow; goal: improve invite conversion; optimize taps to first value.”
- “Turn these notes into a design doc/spec for a bulk edit feature; include states, edge cases, and acceptance criteria.”
- “Create a shaping-style spec with a diagram of moving pieces; call out open questions and the prototype plan.”

