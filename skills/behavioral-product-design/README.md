# behavioral-product-design

Create a **Behavioral Product Design Pack**: target behavior + behavioral diagnosis + intervention map + prioritized concepts + build-ready intervention specs + experiment/instrumentation plan.

## What this skill produces
- Context snapshot + target behavior spec (incl. guardrails)
- Behavioral diagnosis table (barriers/drivers + likely mechanisms)
- Intervention map (ideas mapped to journey moments + mechanism tags)
- Prioritized shortlist (top 1–3 bets)
- Behavioral design specs (1–3 intervention cards)
- Experiment + instrumentation plan (events, metrics, rollout/rollback)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `behavioral-product-design`. Context: <product + user segment>. Target behavior: <what action, where, how often>. Baseline: <current funnel/retention>. Constraints: <platform/channels/brand/time box>. Evidence: <links/notes>. Output: a Behavioral Product Design Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/behavioral-design/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “Users drop during checkout because they’re uncertain. Diagnose the moment and propose 3 interventions + an A/B test plan.”
- “We’re launching a daily habit feature. Design a streak and ‘bend not break’ policy with ethical guardrails.”
- “Activation is flat. Use behavioral science to generate and prioritize interventions across onboarding.”

