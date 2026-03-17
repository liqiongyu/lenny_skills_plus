# Rubric (Score 1–5)

Score the draft across these dimensions. A “ship-ready” pack is typically **≥24/30** and no category below **3**.

## 1) Scope clarity (1–5)
- 1: Vague goals; missing why now; scope boundaries unclear.
- 2: Goals stated but non-goals or exclusions are missing; constraints are generic or incomplete.
- 3: Goals/non-goals exist; constraints listed; some assumptions unclear.
- 4: Boundaries are specific with tradeoff rationale; dependencies and assumptions are documented with owners.
- 5: Crisp decision framing; explicit tradeoffs; assumptions/dependencies are audit-friendly.

## 2) Diagram usefulness (1–5)
- 1: No diagram or overly detailed UI mock notes; moving pieces unclear.
- 2: Diagram exists but is decorative (restates prose) or has >10 moving pieces without clear relationships.
- 3: Diagram exists but missing key hand-offs/states.
- 4: Diagram shows moving pieces, data flow, and key decisions; minor hand-offs may be implicit.
- 5: ≤10 moving pieces; makes feasibility and responsibilities obvious; supports build planning.

## 3) Flows + state coverage (1–5)
- 1: Only a happy path; missing error/empty/loading and edge cases.
- 2: Happy path and 1-2 edge cases documented but error/empty/loading states are missing or vague.
- 3: Main edge cases captured; some states ambiguous.
- 4: Flows cover happy path + key edge cases with defined states; minor ambiguities remain in rare paths.
- 5: Role-playable flows; critical states defined; edge cases have intended outcomes.

## 4) Prototype plan quality (1–5)
- 1: Prototype is vague or not tied to a decision.
- 2: Prototype scope exists but no timebox, no success criteria, or no clear question it answers.
- 3: Timeboxed and scoped but realism or criteria are weak.
- 4: Clear question + timebox + fidelity choice; success criteria exist but data realism is partial.
- 5: Clear decision; right fidelity; realistic data; success criteria measurable; disposable-by-default code stance.

## 5) Testability (requirements + acceptance criteria) (1–5)
- 1: Requirements are aspirational; no acceptance criteria.
- 2: Some requirements have acceptance criteria but they are vague or untestable; non-functional requirements absent.
- 3: Some acceptance criteria; gaps in non-functional requirements.
- 4: Requirements are prioritized (must/should/could) with testable acceptance criteria; most non-functional needs addressed.
- 5: Falsifiable requirements; must/should/could; acceptance criteria cover edge cases and constraints.

## 6) Measurement + risk management (1–5)
- 1: No metrics; no risks/open questions.
- 2: Metrics mentioned but no owners, data sources, or instrumentation plan; risks are generic or missing.
- 3: Metrics exist but instrumentation/owners unclear; risks generic.
- 4: Metrics have data sources and owners; risks are specific with proposed mitigations; open questions are listed.
- 5: Metrics map to data/events and owners; guardrails defined; risks/open questions/next steps are actionable.

