# enterprise-sales

Create an **Enterprise Deal Execution Pack**: buying committee map + champion enablement, decision enablement (reduce “no decision”) + mutual action plan, procurement/security tracker, and a POC/pilot plan framed as a business case + ROI model.

## What this skill produces
- Deal snapshot (account, use case, stage, timeline, success definition)
- Buying committee map + champion plan
- Champion enablement kit (stakeholder one-pagers + FAQs)
- Decision enablement plan + Mutual Action Plan (MAP)
- POC/pilot plan + ROI business case (metrics + ROI model + decision criteria)
- Procurement + security packet plan (forms tracker, docs checklist, owners, timeline)
- Close + implementation handoff (signature plan, kickoff, first value milestones)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `enterprise-sales`. Context: <product + outcome>. Account: <company + segment>. Deal: <ACV + stage + target timeline>. Stakeholders: <champion + economic buyer + IT/security + procurement/legal>. Blockers: <procurement/security/POC/no-decision risk>. Output: an Enterprise Deal Execution Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/enterprise-sales/`) using `references/TEMPLATES.md`.

## Example prompts
- “They said yes but keep stalling—build a MAP and decision guide to reduce ‘no decision’.”
- “Procurement sent vendor onboarding forms—create a tracker and a plan to get through security review.”
- “They want a POC—turn it into a 30-day business-case pilot with an ROI model and decision criteria.”

