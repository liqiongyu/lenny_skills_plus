# ai-product-strategy

Create an **AI Product Strategy Pack** that is executable: clear thesis, prioritized bets, explicit autonomy boundaries, measurable eval/learning plan, and a roadmap with exit criteria.

## What this skill produces
- Context snapshot (decision, users, constraints, why now)
- Strategy thesis (value prop, differentiation, non-goals, assumptions)
- Use-case portfolio (prioritized bets with feasibility + risk)
- Autonomy policy (assistant/copilot/agent boundaries + human control)
- System plan (build/buy, data, evals, cost/latency budgets)
- Empirical learning plan (experiments + instrumentation + iteration cadence)
- Roadmap (phases, milestones, owners, exit criteria)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `ai-product-strategy`. Context: <product, user, job, why now>. Goal: <what outcome>. Constraints: <timeline, budget, policy/legal, data>. Scope: <assistant|copilot|agent>. Output: AI Product Strategy Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want artifacts as files, ask the agent to write the pack under a folder you specify (e.g., `docs/strategy/<initiative>/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “We’re building an AI agent for expense approvals. Use `ai-product-strategy` and include autonomy limits, security risks, and a phased rollout plan.”
- “We have an existing B2B SaaS. Propose and prioritize AI features that improve retention; include a measurement plan and cost/latency budget.”
- “Turn these notes into an AI strategy thesis + roadmap; push back if the ICP or success metrics aren’t clear.”

