# designing-surveys

Create a **Survey Pack**: a decision-driven product survey (brief + questionnaire/instrument + analysis plan + launch checklist + reporting outline).

## What this skill produces
- Context snapshot (decision, audience, channel, constraints)
- Survey brief (goal, sampling, timing, success criteria)
- Questionnaire (question IDs, response types, rationale)
- Survey instrument table (copy/paste-ready to build in a survey tool)
- Analysis + reporting plan (segments/cuts, coding plan, thresholds)
- Launch plan + QA checklist (pilot, mobile QA, bias checks, comms)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `designing-surveys`. Context: <product + users>. Decision: <what we’ll do based on results by when>. Survey type: <onboarding/CSAT/NPS/PMF/churn/etc>. Channels: <email/in-product/etc>. Constraints: <sample size, regions, privacy>. Output: a Survey Pack.”

If details are missing, the skill will ask up to 5 intake questions (see `references/INTAKE.md`) and then proceed with explicit assumptions.

## Optional file output
If you want deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/surveys/<project>/`) using the templates in `references/TEMPLATES.md`.

## Example prompts
- “We need an onboarding profiling survey to separate buyer vs user and personalize onboarding. Build a Survey Pack; keep it under 3 minutes.”
- “Design a CSAT survey for our API users to identify top friction points and how frequently they occur; include an analysis plan and decision thresholds.”
- “We want to validate messaging for a new landing page. Propose a survey-or-better alternative (ad test) and create the plan + measurement table.”

