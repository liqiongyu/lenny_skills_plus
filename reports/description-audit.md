# Skill Description Audit Report

Generated: 2026-03-16

## Summary

| Issue | Count | Severity |
|-------|-------|----------|
| Missing `Use for` trigger keywords | 7 | High |
| Missing `Category:` tag | 48 | Medium |
| Description too long (>350 chars) | 11 | Low |
| Semantic overlap clusters | 16 groups | Needs review |

---

## Issue 1: Missing `Use for` Trigger Keywords (7 skills)

These skills lack explicit trigger keywords, making them harder to auto-trigger:

| Skill | Current Description |
|-------|-------------------|
| `lenny-skillpack-creator` | Converts a Refound/Lenny Skill into a high-density, agent-executable Skill Pack (Agent Skills standard). Output must be in English. |
| `prioritizing-roadmap` | Prioritize a product roadmap/backlog and produce a Roadmap Prioritization Pack (...) |
| `running-design-reviews` | Run high-signal design reviews (design critique / design crit / design feedback)... |
| `sales-qualification` | Build a Sales Qualification Pack (...). Use to fix pipeline quality... *(uses "Use to" instead of "Use for")* |
| `setting-okrs-goals` | Set aligned, measurable OKRs/goals and produce an OKR & Goals Pack (...) |
| `writing-north-star-metrics` | Define or refresh a product North Star metric + driver tree... |
| `writing-prds` | Write a clear, decision-ready PRD (and optionally a PR/FAQ, AI eval spec, and prompt set) for cross-functional alignment. |

**Fix**: Add `Use for <keyword1>, <keyword2>, ...` clause to each.

---

## Issue 2: Missing `Category:` Tag (48 skills)

55% of skills lack a Category tag. Existing categories used:

- Career (6 skills)
- Communication (4 skills)
- Engineering (1 skill)
- Growth (1 skill)
- Hiring & Teams (5 skills)
- Leadership (9 skills)
- Marketing (4 skills)
- Sales & GTM (6 skills)

### Skills needing Category assignment:

| Skill | Suggested Category |
|-------|-------------------|
| `ai-evals` | AI & Technology |
| `ai-product-strategy` | AI & Technology |
| `analyzing-user-feedback` | Product Discovery |
| `behavioral-product-design` | Product Design |
| `building-with-llms` | AI & Technology |
| `competitive-analysis` | Strategy |
| `conducting-user-interviews` | Product Discovery |
| `content-marketing` | Marketing |
| `cross-functional-collaboration` | Leadership |
| `defining-product-vision` | Strategy |
| `delegating-work` | Leadership |
| `design-engineering` | Engineering |
| `design-systems` | Engineering |
| `designing-growth-loops` | Growth |
| `designing-surveys` | Product Discovery |
| `dogfooding` | Product Quality |
| `evaluating-new-technology` | Engineering |
| `managing-tech-debt` | Engineering |
| `managing-timelines` | Execution |
| `marketplace-liquidity` | Growth |
| `measuring-product-market-fit` | Growth |
| `planning-under-uncertainty` | Execution |
| `platform-infrastructure` | Engineering |
| `platform-strategy` | Strategy |
| `positioning-messaging` | Marketing |
| `prioritizing-roadmap` | Strategy |
| `problem-definition` | Product Discovery |
| `product-operations` | Execution |
| `product-taste-intuition` | Career |
| `retention-engagement` | Growth |
| `running-decision-processes` | Leadership |
| `running-design-reviews` | Product Design |
| `running-effective-meetings` | Communication |
| `scoping-cutting` | Execution |
| `setting-okrs-goals` | Strategy |
| `shipping-products` | Execution |
| `startup-ideation` | Strategy |
| `startup-pivoting` | Strategy |
| `systems-thinking` | Leadership |
| `technical-roadmaps` | Engineering |
| `usability-testing` | Product Discovery |
| `user-onboarding` | Growth |
| `vibe-coding` | AI & Technology |
| `working-backwards` | Strategy |
| `writing-north-star-metrics` | Strategy |
| `writing-prds` | Product Management |
| `writing-specs-designs` | Product Management |
| `lenny-skillpack-creator` | Meta |

---

## Issue 3: Semantic Overlap Clusters Needing Disambiguation

### High Priority (confusable)

**"build vs buy" overlap**
- `evaluating-new-technology` triggers include "build vs buy"
- `evaluating-trade-offs` triggers include "build vs buy"
- **Fix**: `evaluating-new-technology` should own "build vs buy" for *technology choices*; `evaluating-trade-offs` should own it for *strategic/operational decisions*

**"decision" overlap**
- `running-decision-processes` — process/meeting for making a decision
- `evaluating-trade-offs` — analytical framework for weighing options
- `systems-thinking` — also mentions "trade-offs"
- **Fix**: Sharpen boundary: process vs. analysis vs. systems-level thinking

**"stakeholder/cross-functional" overlap**
- `stakeholder-alignment` — securing buy-in from execs/stakeholders
- `cross-functional-collaboration` — ongoing working relationship across functions
- `managing-up` — managing relationship with your boss
- **Fix**: Add "NOT for..." clauses to disambiguate

### Medium Priority (related but distinguishable)

**Sales motion (6 skills)** — already well-differentiated by stage/function, but `building-sales-team` and `product-led-sales` both mention "product-led sales pilot"

**Specs/docs (3 skills)** — `writing-prds` lacks triggers entirely; could collide with `writing-specs-designs` on "spec" keyword

**Meetings (4 skills)** — `running-design-reviews` lacks "Use for" triggers

---

## Issue 4: Description Length Outliers (>350 chars)

| Skill | Length |
|-------|--------|
| `having-difficult-conversations` | 399 |
| `organizational-transformation` | 389 |
| `marketplace-liquidity` | 379 |
| `product-operations` | 370 |
| `onboarding-new-hires` | 368 |
| `media-relations` | 363 |
| `evaluating-trade-offs` | 362 |
| `managing-up` | 357 |
| `engineering-culture` | 357 |
| `content-marketing` | 352 |
| `fundraising` | 351 |

---

## Recommended Fix Priority

1. **Add `Use for` triggers** to 7 skills (highest impact on discoverability)
2. **Add `Category:` tags** to 48 skills (consistency + filtering)
3. **Add disambiguation** to overlap clusters (reduce mis-triggers)
4. **Trim long descriptions** (optional, cosmetic)
