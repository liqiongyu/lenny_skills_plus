# evaluating-new-technology

Create a **Technology Evaluation Pack** for a new tool/vendor/platform (including AI products): clear problem framing, options, build vs buy, pilot plan, risk review, and a decision memo.

## What this skill produces
- Evaluation brief (problem, users, constraints, decision context)
- Options & criteria matrix (status quo + alternatives, scoring, integration notes)
- Build vs buy analysis (bandwidth/TCO, core competency, opportunity cost)
- Proof-of-value pilot plan (hypotheses, scope, metrics, exit criteria)
- Risk & guardrails review (security/privacy/compliance, vendor claims, mitigations)
- Decision memo (recommendation, trade-offs, adoption + rollback)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `evaluating-new-technology`. Candidate: <tool/vendor or what you might build>. Problem: <workflow + users + pain>. Current stack: <what exists today>. Constraints: <security/privacy/compliance, budget, timeline, deployment>. Decision context: <who decides + when>. Output: Technology Evaluation Pack.”

If details are missing, the skill will ask up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceed with explicit assumptions.

## Optional file output
If you want the pack as files, ask the agent to write the artifacts under a folder you specify (e.g., `docs/tech-evals/<initiative>/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “Use `evaluating-new-technology` to decide build vs buy for an internal analytics event pipeline. Constraints: 2 engineers for 6 weeks; data is sensitive; must support EU residency.”
- “Use `evaluating-new-technology` to evaluate an AI customer support platform. Include a pilot plan with measurable success metrics and a security/privacy risk review.”
- “Use `evaluating-new-technology` to pick a reverse-ETL tool (Hightouch vs Census) and recommend the best next step.”

