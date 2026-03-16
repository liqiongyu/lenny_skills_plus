# Rubric (Scoring)

Score each dimension **1–5**. A “ship-ready” pack is typically **≥ 22/30** with no dimension below **3**.

## 1) Scope clarity (1–5)
- 1: Vague; unclear what design engineering means here; no distinction from design-systems or engineering-culture.
- 2: Scope stated but overlaps with neighboring skills (design-systems, running-design-reviews) are not addressed.
- 3: Clear definition and boundaries; some edge cases unresolved; at least one adjacent-skill redirect present.
- 4: Clear scope with explicit "not in scope" items and redirects to 2+ neighboring skills.
- 5: Crystal clear scope, boundaries, and when-not-to-use guidance; correct routing for all confusable neighbors (design-systems, engineering-culture, running-design-reviews, writing-specs-designs).

## 2) Operating model fit (1–5)
- 1: Model not chosen or mismatched to the problem; no rationale.
- 2: Model mentioned but not justified; ownership boundaries between design engineering, design, and engineering are unclear.
- 3: Model chosen and justified; interfaces mostly defined; some ambiguity on who owns component API vs visual QA.
- 4: Model well-justified with clear ownership boundaries; rituals defined but escalation paths are thin.
- 5: Model strongly matches constraints; ownership and rituals are crisp; escalation paths and decision rights explicitly documented.

## 3) Prototype-to-production rigor (1-5)
- 1: Prototypes and production are conflated; no gates; everything is "just build it."
- 2: Prototype concept mentioned but no fidelity ladder; no throwaway vs shippable distinction.
- 3: Ladder exists; some graduation rules/gates defined; throwaway/shippable labels present for some but not all rungs.
- 4: Clear ladder with graduation rules and labels; review gates defined but time-box for disposal decisions is missing.
- 5: Clear ladder with graduation rules, throwaway/shippable labels, review gates, and explicit time-boxed decision points for graduation or disposal.

## 4) Design-to-code contract quality (1-5)
- 1: Handoff is ad-hoc; missing states/a11y expectations; no PR requirements defined.
- 2: Contract lists topics (tokens, states, a11y) but without specifics (e.g., "a11y compliant" without WCAG level or test method).
- 3: Contract covers key items; some ambiguity remains; PR expectations exist but verification method is unclear.
- 4: Contract is specific for most items; states, tokens, a11y level, and PR expectations defined; minor gaps in edge-case coverage.
- 5: Contract is implementable with minimal back-and-forth; states, tokens, a11y (with WCAG level + test method), and PR expectations (screenshots, storybook, test plan) are all explicit and verifiable.

## 5) Delivery plan executability (1-5)
- 1: No milestones/owners; feels aspirational; output is a wish-list of components.
- 2: Milestones listed but without owners, dependencies, or acceptance criteria; no thin-slice approach.
- 3: Milestones exist; acceptance criteria are partial; first milestone may be too large (more than 2 weeks).
- 4: Incremental milestones with owners and acceptance criteria; first milestone is a thin vertical slice; minor gaps in dependency mapping.
- 5: Incremental milestones with owners, dependencies, acceptance criteria, and rollback/stop conditions; first milestone ships within 1-2 weeks and sets patterns for the rest.

## 6) Quality bar + sustainability (1-5)
- 1: Quality depends on taste; no repeatable checks; success is undefined.
- 2: Some checklists mentioned but not tied to workflow gates; success signals are vague ("better UI").
- 3: Checklists exist; automation/docs are partial; at least one measurable success signal defined.
- 4: Review gates with checklists integrated into workflow; success signals are measurable; documentation plan exists but may lack non-expert onboarding.
- 5: Repeatable quality mechanisms (review gates + docs + optional automation) and measurable success signals; quality bar is enforceable by anyone on the team, not just the design engineer.

## Score summary
| Dimension | Score (1–5) | Notes / improvements |
|----------|-------------|----------------------|
| Scope clarity | | |
| Operating model fit | | |
| Prototype→production rigor | | |
| Design-to-code contract quality | | |
| Delivery plan executability | | |
| Quality bar + sustainability | | |

**Total (out of 30):**  
**Top 3 improvements:**  

