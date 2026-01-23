# sales-qualification

Create a **Sales Qualification Pack**: disqualifiers + qualification scorecard + discovery/qualification script + CRM notes template + pipeline hygiene rules.

## What this skill produces
- Context snapshot (ICP, motion, constraints, definition of “qualified”)
- Qualification charter (segments, disqualifiers, stage exit criteria)
- Qualification scorecard (weighted criteria + thresholds)
- Discovery/qualification call script + question bank + disqualify talk track
- CRM qualification notes template + required fields + hygiene rules
- Rollout + measurement plan
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `sales-qualification`. Product: <1 sentence>. ICP: <industry/size/titles + exclusions>. Motion: <inbound/outbound/enterprise>. Deal: <ACV/cycle/stakeholders>. Current issue: <examples of bad leads or stalls>. Output: a Sales Qualification Pack with disqualifiers, scorecard, call script, stage exit criteria, and CRM notes template.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/sales-qualification/`) using `references/TEMPLATES.md`.

## Example prompts
- “Define disqualifiers so SDRs stop booking bad meetings.”
- “Create a qualification scorecard and stage exit criteria for our CRM.”
- “Write a discovery script that surfaces urgency and decision process fast.”

