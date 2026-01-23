# design-systems

Produce a **Design System Operating Pack**: charter + UI audit + blockframe-to-component mapping + token model + component roadmap + documentation plan + governance/adoption plan.

## What this skill produces
- Context snapshot (goals, constraints, success signals)
- Design system charter (mission, scope, principles, audiences, in/out)
- UI audit + operational blockers (what to standardize first)
- Blockframe-to-component map (lo-fi flows mapped to components/tokens)
- Token model (taxonomy + naming + elevation/depth tokens)
- Component inventory + roadmap (tiers + milestones)
- Documentation + enablement plan (easy for non-experts)
- Governance + adoption plan (contribution workflow + champions + release cadence)
- Quality gate (checklists + rubric) + Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `design-systems`. Context: <product + platforms>. Current state: <Figma library/code/Storybook + pain points>. Goal: <why now>. Constraints: <timeline + ownership + a11y/compliance>. Output: a Design System Operating Pack.”

If key details are missing, the skill asks up to 5 intake questions (see `references/INTAKE.md`) and then proceeds with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/design-system/`) using `references/TEMPLATES.md`.

## Example prompts
- “We need tokens + components to standardize our UI—create a charter, token model, and a 6-week roadmap.”
- “We want a more dimensional UI (elevation/motion) without breaking consistency—propose token changes + component impact + rollout plan.”
- “We’re selling to enterprises and need customization—add governance, theming strategy, and an adoption plan.”

