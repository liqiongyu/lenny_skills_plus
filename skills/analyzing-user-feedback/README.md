# analyzing-user-feedback

Create a **User Feedback Analysis Pack**: source inventory + normalized feedback table + taxonomy/codebook + themes & evidence + recommendations + feedback loop plan.

## What this skill produces
- Context snapshot (scope, decision, time window, segments, constraints)
- Source inventory + sampling plan
- Taxonomy + codebook (tagging definitions + rules)
- Normalized feedback table (tagged items; no PII)
- Themes & evidence report (quotes/examples + frequency/severity + confidence)
- Recommendations + learning plan
- Feedback loop plan (cadence, owners, storage)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `analyzing-user-feedback`. Context: <product + area>. Decision: <what this should inform>. Sources: <tickets/interviews/surveys/reviews/logs>. Time window: <range>. Segments: <important segments>. Constraints: <PII/internal-only>. Output: a User Feedback Analysis Pack.”

If key details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/user-feedback-analysis/`) using `references/TEMPLATES.md`.

## Example prompts
- “Analyze 90 days of support tickets about onboarding for SMB users. Produce themes, evidence, and top fixes.”
- “Synthesize churn survey comments from the last quarter into a voice-of-customer report with recommended actions.”
- “We shipped a new AI feature. Review a sample of 200 traces and support tickets to identify failure modes and a learning plan.”

