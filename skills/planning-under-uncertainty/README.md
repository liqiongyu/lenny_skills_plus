# planning-under-uncertainty

Turn ambiguity into an executable plan by mapping unknowns, defining hypotheses, running experiments, and adding buffers/contingencies with explicit decision triggers.

## What this skill produces
- Decision frame (objective, why now, success + guardrails, decision rights)
- Uncertainty map (assumptions/unknowns, confidence, impact, validation plan)
- Hypotheses + experiment portfolio (learning goals + decision rules)
- Plan v0 with buffers + contingencies + triggers
- Cadence + comms (learning review ritual, update template, decision log)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `planning-under-uncertainty`. Context: <initiative + why now>. Time horizon: <weeks/months> and urgency: <wartime/peacetime>. Constraints/guardrails: <bullets>. Stakeholders/decision owner: <who decides stop/pivot/scale>. Top unknowns: <bullets>. Output: an Uncertainty Planning Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/planning-under-uncertainty/<project>/`) using the templates in `references/TEMPLATES.md`.

## Example prompts
- “We’re unsure if customers want this feature. Create a hypothesis-driven plan with 5 experiments and clear pivot triggers.”
- “We’re in a crisis: activation dropped after a change. Diagnose first, propose rapid tests, and define rollback/patch decision rules.”
- “We need to commit to a plan despite uncertainty. Build a Plan v0 with buffers and contingencies that we can iterate weekly.”

