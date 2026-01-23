# marketplace-liquidity

Create a **Marketplace Liquidity Management Pack**: liquidity definition + metric tree, fragmentation map, segment scorecard, bottleneck diagnosis, intervention playbook, experiment backlog, measurement plan, and an operating cadence.

## What this skill produces
- Context snapshot (goal, timebox, segments, constraints)
- Liquidity definition + “good enough” thresholds (reliability)
- Liquidity metric tree (north-star + drivers)
- Fragmentation map + segment scorecard (local markets)
- Bottleneck diagnosis (supply vs demand vs mechanics vs quality)
- Intervention plan + prioritized experiment backlog
- Measurement + instrumentation plan (dashboards, alerts, event defs)
- Weekly liquidity operating cadence (agenda + decisions)
- Risks / Open questions / Next steps

## How to use (prompt)

“Use `marketplace-liquidity`. Marketplace: <what it is + who buys/sells>. Core action: <what counts as success>. Goal: <metric + target + by when>. Priority segments: <geo/category/cohort>. Baseline: <best-available metrics>. Constraints: <budget/capacity/policy>. Output: a Marketplace Liquidity Management Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and proceed with explicit assumptions.

## Optional file output
If you want deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/marketplace-liquidity/`) using `references/TEMPLATES.md`.

## Example prompts
- “Build a liquidity dashboard + weekly cadence. We need to stop the ‘whac-a-mole’ across cities.”
- “Diagnose whether we’re supply- or demand-limited by category and give us the top 5 experiments.”
- “We have the graduation problem: top suppliers churn once they succeed. Propose mitigations and how to measure them.”

