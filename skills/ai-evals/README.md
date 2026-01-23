# ai-evals

Create an **AI Evals Pack** for LLM/AI features: eval PRD (requirements), golden test set, error taxonomy, rubric, judge/harness plan, and an iteration loop.

## What this skill produces
- Eval PRD (decision, scope, target behaviors, acceptance thresholds)
- Test set spec + initial golden set (schema, coverage plan, tagged cases)
- Error taxonomy (open-coded failure modes + severity)
- Rubric + judging guide (dimensions, scale, examples, tie-breakers)
- Judge + harness plan (human vs LLM-as-judge vs automated checks; runbook + cost/time estimate)
- Reporting + iteration loop (regression policy; every bug becomes a new test)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `ai-evals`. SUT: <what the AI does + inputs/outputs>. Decision: <ship/no-ship | compare A vs B>. Target behaviors: <3–10>. Constraints: <privacy/safety, languages, cost/time>. Output: AI Evals Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the pack as files, ask the agent to write the artifacts under a folder you specify (e.g., `docs/evals/<initiative>/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “Design evals for our RAG support bot. Include a safety rubric, golden set schema, and an LLM-as-judge plan.”
- “We’re comparing two prompts for our scheduling assistant. Create a benchmark set and decision threshold.”
- “Turn our top 20 failures into an error taxonomy + rubric + repeatable eval harness plan.”

