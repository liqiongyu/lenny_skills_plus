# building-with-llms

Produce an **LLM Build Pack** for shipping LLM-powered features/apps: clear contracts (prompts/tools), evals, data quality, production readiness, and an iteration loop.

## What this skill produces
- Feature brief (job, users, non-goals, constraints, success + guardrails)
- System design sketch (architecture + context strategy + budgets)
- Prompt + tool contract (system prompt, schemas, examples, guardrails)
- Data + evaluation plan (test set, rubric, red-team suite, acceptance thresholds)
- Build + iteration plan (prototype slice, instrumentation, debugging loop, safe use of coding agents)
- Launch + monitoring plan (logging, dashboards/alerts, fallback/rollback)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `building-with-llms`. Context: <product + users + workflow>. Goal: <what the LLM must do>. Constraints: <privacy, latency, cost, reliability>. Integrations: <tools/APIs + output schema>. Output: LLM Build Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the pack as files, ask the agent to write the artifacts under a folder you specify (e.g., `docs/llm/<initiative>/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “We’re adding an LLM copilot to our CRM. Use `building-with-llms` and include an eval plan, red-team tests, and monitoring/rollback.”
- “Design the system prompt + tool contract for an agent that proposes code changes, but requires human approval before executing commands.”
- “Our current prompt is inconsistent. Create a test set and rubric, then propose a prompt/tool refactor.”

