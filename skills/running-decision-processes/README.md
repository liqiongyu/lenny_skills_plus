# running-decision-processes

Run a high-quality decision process and produce a **Decision Process Pack**: decision brief/pre-read, options + criteria matrix, RAPID/DACI roles, meeting plan, decision log entry, comms, and a review loop.

## What this skill produces
- Decision Brief / Pre-read
- Options + Criteria Matrix (with explicit assumptions/unknowns)
- Decision Rights + Process (RAPID/DACI/RACI) + meeting plan
- Decision Log Entry
- Decision Communication (announcement + next steps)
- Decision Review Plan (what to measure; when to revisit)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `running-decision-processes`. Decision: <one sentence>. Deadline: <date>. Context/why now: <what changed>. Constraints: <non-negotiables>. Stakeholders/approvers: <names/roles>. Options: <current options>. Output: a Decision Process Pack.”

If key details are missing, the skill asks up to 5 intake questions (see `references/INTAKE.md`) and proceeds with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/decisions/<topic>/`) using `references/TEMPLATES.md`.

## Example prompts
- “Create a decision memo and run a DACI process to decide whether we should expand to Germany this quarter.”
- “We’re stuck between two bad choices on pricing. Help us decide and draft the comms.”
- “Set up RAPID for a one-way door infrastructure migration decision and create a decision log entry + review date.”

