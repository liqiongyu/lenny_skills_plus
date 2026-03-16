# Rubric (Scoring)

Score each dimension **1–5**. A “ship-ready” pack is typically **≥ 22/30** with no dimension below **3**.

## 1) Scope clarity (1-5)
- 1: Vague scope; unclear audiences and boundaries; no distinction from design-engineering or running-design-reviews.
- 2: Scope stated but overlaps with neighboring skills are not addressed; audiences listed without specificity.
- 3: Clear scope and audiences; some edge cases unresolved; at least one adjacent-skill redirect present.
- 4: Clear scope with explicit "not in scope" items and redirects to 2+ neighboring skills; audiences prioritized.
- 5: Crystal clear scope, boundaries, and when-not-to-use guidance; correct routing for all confusable neighbors (design-engineering, running-design-reviews, engineering-culture, writing-specs-designs).

## 2) Operational leverage (1-5)
- 1: No clear operational hook; unclear why the system will be adopted; no pain point identified.
- 2: Pain point mentioned generically ("UI is inconsistent") but no operational blocker tied to business impact.
- 3: Hook is stated; first slice is defined but could be tighter; success signals are present but not all are measurable.
- 4: Strong hook with a defined first slice and measurable success signals; connection to business impact is clear.
- 5: Strong hook with a narrow, high-leverage first slice and clear success signals; ROI argument is concrete (e.g., "reduces screen build time from 2 days to 4 hours").

## 3) Token architecture (1-5)
- 1: Tokens are ad-hoc or missing; components hard-code values; no naming convention.
- 2: Some tokens defined but naming is inconsistent; no semantic layer; theming and state tokens absent.
- 3: Token taxonomy exists; some state/theming/a11y gaps remain; naming convention present but not enforced.
- 4: Robust taxonomy with semantic tokens and naming convention; theming supported; minor gaps in state tokens or elevation/depth.
- 5: Robust taxonomy with semantic/state tokens (incl. elevation/depth where needed) and explicit a11y rules (contrast, focus, motion); token model supports style evolution without component rewrites.

## 4) Component roadmap executability (1-5)
- 1: Wishlist; no milestones/owners/acceptance criteria; components listed without prioritization.
- 2: Components prioritized but milestones are vague; no owners assigned; no acceptance criteria.
- 3: Roadmap exists; milestones are reasonable but acceptance criteria are partial; first milestone may be too broad.
- 4: Incremental milestones with owners and acceptance criteria; first milestone ships within 1-2 weeks; minor gaps in rollback/stop conditions.
- 5: Incremental milestones with clear acceptance criteria and rollback/stop conditions; tiered approach (primitives then composites then patterns) with each milestone having a committed product-team consumer.

## 5) Documentation usability (1-5)
- 1: Docs are abstract; no examples; hard for new users; single-audience (designer-only or engineer-only).
- 2: Some examples present but docs are aimed at one audience only; no recipes or starter templates.
- 3: Docs cover basics; some gaps in recipes/guardrails; both audiences acknowledged but coverage is uneven.
- 4: Docs address both designers and engineers with examples and do/don't guidance; starter templates present but limited.
- 5: Example-first docs with recipes/templates and guardrails that make correct usage easy; a non-expert can assemble a consistent screen using templates with minimal training.

## 6) Governance + adoption plan (1-5)
- 1: No owner; no contribution path; adoption is assumed; no enforcement mechanism.
- 2: Governance mentioned but decision rights are vague; no contribution workflow; adoption is "tell teams to use it."
- 3: Governance exists; adoption tactics are partial; decision rights defined but contribution workflow or enforcement is missing.
- 4: Decision rights, contribution workflow, and release cadence defined; champion plan exists; enforcement mechanism (e.g., CI lint, required review) planned but not yet specified.
- 5: Clear decision rights + contribution workflow + champion plan + release cadence; enforcement mechanism integrated into CI/review workflow; adoption tracking with measurable targets.

## Score summary
| Dimension | Score (1–5) | Notes / improvements |
|----------|-------------|----------------------|
| Scope clarity | | |
| Operational leverage | | |
| Token architecture | | |
| Component roadmap executability | | |
| Documentation usability | | |
| Governance + adoption plan | | |

**Total (out of 30):**  
**Top 3 improvements:**  

