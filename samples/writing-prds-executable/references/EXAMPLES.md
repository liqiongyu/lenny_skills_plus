# Example outputs (snippets)

These are short snippets to show the expected level of concreteness.

## Example 1 — Requirements section (PRD)

### Functional requirements
- R1: The system MUST allow a user to create a draft PRD from free-form notes in under 60 seconds.
- R2: The system MUST output a PRD with sections: TL;DR, Problem, Goals, Non-goals, Requirements, Metrics, Risks, Rollout, Open Questions.
- R3: The system MUST label assumptions explicitly when key inputs are missing.
- R4: The system MUST NOT invent metrics; if unknown, it MUST propose measurable proxies and ask for confirmation.

### Non-functional requirements
- R10: Latency: PRD draft generation MUST complete in < 10 seconds for inputs up to 3,000 words.
- R11: Privacy: User inputs MUST NOT be logged in plaintext; redact secrets and PII where possible.

## Example 2 — “Why now” (PRD)

Why now:
- Support ticket volume for onboarding failures increased from 120/week to 310/week in the last 6 weeks.
- Two enterprise prospects explicitly cited this workflow as a blocker for renewal.
- A competitor shipped an onboarding redesign in Dec 2025; churn risk is elevated if we don’t respond this quarter.

Assumptions:
- We can instrument activation in the new flow within 2 weeks.
- Design has capacity for 1 iteration before the target launch.

## Example 3 — Boundary / refusal example

If the user asks: “Write our company strategy and 3-year product vision,” this skill should redirect to a vision/strategy skill and only offer to produce a short PRD for a *specific* initiative once the strategy is clear.
