# <Feature/Product Name> — AI Eval Spec (Draft)

Owner: <name or team>  
Last updated: <YYYY-MM-DD>  
Model / system under test: <TBD>  
Eval cadence: pre-merge / nightly / weekly / pre-launch

## 1) What this eval gates
- Feature area:
- Release gate (what must pass to ship):
- Monitoring gate (what regression alerts will fire):

## 2) Non-negotiable behaviors
Write as MUST / MUST-NOT.
- B1 MUST:
- B2 MUST:
- B3 MUST-NOT:

## 3) Test set design
Coverage buckets:
- Typical / happy path:
- Edge cases:
- Adversarial / red-team:
- Regression cases:

Add examples (at least 10 to start):
- Case 1:
  - Input:
  - Expected behavior:
- Case 2:
  - ...

## 4) Judge prompt (LLM-as-a-judge)
### Judge system prompt
<Define role, rubric, strictness, and what to ignore>

### Judge user prompt template
Include the candidate output and ask for a structured verdict.
- Input:
- Candidate output:
- Task / requirement:
- Rubric:

### Output schema (machine-readable)
Return JSON:
{
  "score": <0-5>,
  "pass": <true/false>,
  "reasons": ["..."],
  "failure_tags": ["hallucination", "policy", "format", "missing_requirement", ...]
}

## 5) Scoring rubric
Define what 0–5 means (keep it concrete).
- 5 =
- 4 =
- 3 =
- 2 =
- 1 =
- 0 =

Pass threshold: >= <TBD>

## 6) Reporting
- Aggregate metrics (pass rate, avg score)
- Per-bucket breakdown
- Top failure modes
- Links to failing examples

## 7) Iteration loop
- When failures happen:
  1) classify
  2) decide fix (prompt, data, model, product)
  3) add regression case
