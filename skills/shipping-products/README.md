# shipping-products

Ship products with speed and safety by producing a decision-ready **Shipping & Launch Pack** (rollout/rollback, quality bar, comms, monitoring, and post-launch learning).

## What this skill produces
- Release brief (what/why now/who/when; scope + non-goals; DRI)
- Rollout plan (phases, eligibility, flags, kill switch, rollback)
- Product Quality List (PQL) + go/no-go criteria
- Measurement + monitoring plan (dashboards, alerts, owners)
- Comms + enablement plan (internal/external, docs, support readiness)
- Launch day runbook (timeline, checkpoints, escalation)
- Post-launch review plan + follow-ups
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `shipping-products`. Context: <what we’re shipping + users>. Date/timebox: <when>. Rollout: <beta/GA/flagged>. Constraints: <privacy/compliance/etc>. Output: a Shipping & Launch Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/shipping-products/<release>/`) using templates in `references/TEMPLATES.md`.

## Example prompts
- “We’re launching RBAC for admins in 3 weeks. Create a go/no-go checklist (PQL), rollout plan, and internal/external comms.”
- “Plan a 10% → 50% → 100% rollout behind a feature flag with monitoring + rollback triggers.”
- “We’re shipping a breaking API change. Create a launch runbook and customer comms + migration guidance.”

