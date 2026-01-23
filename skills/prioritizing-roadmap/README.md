# prioritizing-roadmap

Create a **Roadmap Prioritization Pack**: season framing + common-currency scoring + a ranked opportunity list + a coherent roadmap draft that stakeholders can align on.

## What this skill produces
- Context snapshot (goal, horizon, constraints, stakeholders)
- Season framing (bets + explicit non-goals)
- Opportunity inventory with conviction level + evidence
- Prioritization model (common currency + ICE scales + assumptions)
- Ranked opportunity list + “parking lot”
- Roadmap draft (Now/Next/Later or quarterly themes) + update cadence
- Decision narrative (“why these, why now”) + “Think Bigger” ideas
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `prioritizing-roadmap`. Context: <product + segment + goal>. Horizon: <timeframe>. Constraints: <capacity/deadlines/dependencies>. Input: <candidate initiatives or current backlog>. Output: a Roadmap Prioritization Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/roadmap-prioritization/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “We’re a B2B SaaS. Prioritize our Q2 roadmap across Growth and Core. We have 6 engineers and 1 designer. Output a Roadmap Prioritization Pack.”
- “We’re a marketplace. Prioritize 6 months of roadmap across supply, demand, and trust & safety; we need a model that makes cross-team tradeoffs comparable.”
- “Here’s our backlog list. Create a Now/Next/Later roadmap, but push back if we’re missing goals or constraints.”

