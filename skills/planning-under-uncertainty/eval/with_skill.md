# Uncertainty Planning Pack — Self-Serve Onboarding Conversion

## 1) Decision frame

- **Objective:** Identify and fix the primary driver(s) of low trial-to-paid conversion (currently 4% vs. industry benchmark of 8-12%) through hypothesis-driven experimentation, then commit to a remediation path.
- **Why now:** At 4%, we are converting at roughly one-third to one-half the industry benchmark. Every month of delay compounds lost revenue and increases CAC payback period. The gap is large enough that even a partial fix (e.g., moving from 4% to 7%) would materially change unit economics.
- **Time horizon:** 6 weeks (Weeks 1-6). Decision to commit to a remediation build by end of Week 4; Weeks 5-6 for initial implementation of the winning direction.
- **Mode:** Peacetime (exploration). This is a chronic underperformance issue, not an acute crisis. We have time to learn before committing, but urgency is real given the revenue impact.
- **Decision owner (stop/pivot/scale):** PM (final call on direction), with designer and eng leads as decision inputs.
- **Success metrics:**
  - Primary: Trial-to-paid conversion rate (target: move from 4% toward 7%+ within 90 days of remediation launch)
  - Secondary: Activation rate (% of trial users completing the "aha moment" action), time-to-value (median time from signup to first meaningful use), pricing page engagement (click-through to checkout)
- **Guardrails ("must not worsen"):**
  - Trial signup rate (don't scare people away before trial)
  - NPS / CSAT of existing paid users (don't break the experience for converts)
  - Revenue per paid user (don't solve conversion by discounting into unprofitability)
- **Non-negotiable constraints:** 1 PM, 2 engineers, 1 designer for 6 weeks. No additional headcount. No changes to core pricing structure without executive approval.
- **What is flexible:** Scope of experiments (can narrow to one hypothesis), fidelity of tests (smoke tests acceptable), which segments we target first, timeline for full remediation (6 weeks is for learning + initial fix, not complete overhaul).

---

## 2) Uncertainty map (assumptions + unknowns)

### What we know
- Trial-to-paid conversion is 4%, well below the 8-12% industry benchmark.
- Users are signing up for trials (top of funnel is functioning).
- We have a self-serve onboarding flow, a product with paying users, and a pricing page.

### What we don't know
- Where in the trial journey users drop off (activation? value realization? checkout?)
- Whether the problem is uniform across segments or concentrated in a specific ICP mismatch
- Whether users who do convert share traits that non-converters lack
- How our onboarding, value demonstration, and pricing compare to competitors that hit 8-12%

### Top 5 unknowns (highest impact, lowest confidence)

1. **Where is the biggest drop-off in the trial funnel?** We don't know if users fail to activate, activate but don't see value, see value but churn at pricing, or never belonged in our ICP.
2. **What does "activation" mean for our product, and are trial users reaching it?** If the aha moment is unclear or unreachable in the trial window, nothing downstream matters.
3. **Is the pricing page creating unnecessary friction?** Confusion, sticker shock, or poor plan mapping could be killing conversion even among activated users.
4. **Are we attracting the wrong audience (ICP mismatch)?** If a large share of trial signups are outside our ideal customer profile, no amount of UX improvement will move conversion.
5. **Is value demonstration adequate during trial?** Users may activate but never see the product's core value clearly enough to justify paying.

| Assumption / unknown | Type | Confidence | Impact | How we'll validate | Owner | By when | Decision impacted |
|---|---|---|---|---|---|---|---|
| 1. Biggest drop-off point in trial funnel is unknown | User/Product | Low | High | Funnel analysis: instrument signup > activation > engagement > pricing page > checkout > paid. Identify the stage with the largest absolute drop. | PM + Eng 1 | Week 1 | Determines which hypothesis to prioritize |
| 2. We don't know if trial users reach the "aha moment" | User/Product | Low | High | Define activation event(s), measure % of trial users who complete them, segment by converter vs. non-converter | PM + Designer | Week 1-2 | If activation is low, focus on onboarding UX before anything else |
| 3. Pricing page may create friction or confusion | User/Market | Medium | High | Pricing page analytics (time on page, exit rate, plan comparison clicks); 5-8 user interviews with trial users who visited pricing but didn't convert | Designer + PM | Week 2 | If pricing is the bottleneck, redirect effort to pricing UX |
| 4. Significant share of trial users may be outside ICP | Market | Medium | Medium | Segment trial signups by firmographic/behavioral data; compare ICP-match rate of converters vs. non-converters | PM | Week 1-2 | If ICP mismatch is >40%, shift focus to acquisition targeting (outside this team's scope) |
| 5. Value demonstration during trial is inadequate | User/Product | Low | High | Compare feature usage depth of converters vs. non-converters; run 5-8 exit interviews with churned trial users asking "what would have made you pay?" | Designer + PM | Week 2-3 | If value demo is the gap, focus on in-trial education and feature exposure |
| 6. Trial duration may be too short or too long for value realization | Product | Medium | Medium | Analyze time-to-convert distribution; check if extending/shortening trial changes behavior | PM + Eng 1 | Week 2 | Affects experiment design for activation/value tests |
| 7. Competitor onboarding is significantly better | Market | Medium | Low | Competitive audit of 3 top alternatives (sign up for trials, document flows) | Designer | Week 1 | Informs solution design, not hypothesis prioritization |

---

## 3) Hypotheses + experiment portfolio

**Principle:** "Winning" = learning that changes a decision. A negative result that eliminates a hypothesis is as valuable as a positive one.

### Hypothesis statements

**H1 — Activation UX:** "If we redesign the first-run experience to guide users to complete [core activation event] within their first session, then activation rate will increase by 30%+ (relative) because most trial users currently get stuck or lost before reaching the aha moment."

**H2 — Value demonstration:** "If we add in-trial nudges (guided tours, use-case templates, progress indicators) that expose the product's core value within the first 3 days, then the rate of trial users who engage with the paid-tier feature set will increase by 25%+ because users currently don't discover enough value to justify paying."

**H3 — Pricing page friction:** "If we simplify the pricing page (clearer plan differentiation, remove ambiguity, add social proof), then pricing-page-to-checkout conversion will increase by 20%+ because the current page creates confusion or sticker shock that causes drop-off."

**H4 — ICP mismatch:** "If more than 40% of trial signups are outside our ICP (wrong company size, wrong use case, wrong role), then improving onboarding/pricing will have limited impact because the fundamental issue is audience quality, not product experience."

### Experiment portfolio

| # | Hypothesis | Experiment / test | Primary signal (compass) | Guardrails | Segment / sample | Duration | Decision rule | Owner |
|---|---|---|---|---|---|---|---|---|
| E1 | H1 (Activation UX) | **Funnel instrumentation + cohort analysis.** Instrument full trial funnel; measure activation rate for last 30 days of cohorts. Identify the step with the largest drop. | Activation rate (% completing core action) | Trial signup rate must not drop | All trial users (historical data) | Week 1 (data pull) | If activation rate is <30%, prioritize H1 experiments. If >60%, deprioritize H1 and focus elsewhere. | PM + Eng 1 |
| E2 | H1 (Activation UX) | **Guided first-run prototype.** Design a guided onboarding flow (interactive walkthrough to aha moment). Test with 5-8 new trial users in moderated usability sessions. | Task completion rate for activation event; qualitative "clarity" score | Session must be <10 min (don't create onboarding fatigue) | New trial signups, mix of ICP and non-ICP | Week 2-3 (design Week 2, test Week 3) | If >70% complete activation with guidance vs. <30% baseline, build the guided flow. If delta is <10pp, deprioritize H1. | Designer + Eng 2 |
| E3 | H2 (Value demo) | **Exit interviews with churned trial users.** Conduct 5-8 structured interviews with users who trialed but did not convert in the last 60 days. Ask: what they tried, what they valued, what was missing, what would have made them pay. | Thematic frequency: % citing "didn't see enough value" or "didn't know what to do" vs. "too expensive" vs. "not the right tool" | N/A (qualitative) | Churned trial users, ICP-matching preferred | Week 1-2 (recruit Week 1, interview Week 2) | If >50% cite value/activation gaps, validates H1/H2 as primary. If >50% cite price, validates H3. If >50% cite "wrong tool," validates H4. | PM + Designer |
| E4 | H3 (Pricing friction) | **Pricing page analytics + heatmap.** Install heatmap/session recording on pricing page. Analyze: exit rate, scroll depth, click patterns, time on page. Compare converters vs. bouncers. | Pricing page exit rate; click-through to checkout | N/A (observational) | All pricing page visitors (2 weeks of data) | Week 1-2 | If exit rate is >70% and click patterns show confusion (e.g., toggling between plans, scrolling past CTA), prioritize H3. If exit rate is <40%, deprioritize H3. | Eng 1 + Designer |
| E5 | H3 (Pricing friction) | **Simplified pricing page A/B test.** If E4 signals friction, design a simplified pricing page variant (fewer plans, clearer differentiation, added social proof). Run A/B test. | Pricing-page-to-checkout rate | Trial signup rate; revenue per user (no discount gimmicks) | 50/50 split of pricing page traffic | Week 3-4 (design Week 3, run Week 4) | If variant improves checkout rate by >15% (relative) with statistical significance, ship it. If <5% delta, pricing page is not the bottleneck. | Designer + Eng 2 |
| E6 | H4 (ICP mismatch) | **ICP segmentation analysis.** Pull firmographic + behavioral data on last 90 days of trial signups. Classify each as ICP-match or non-match. Compare conversion rates. | ICP-match % of trial base; conversion rate by segment | N/A (analytical) | All trial signups, last 90 days | Week 1 (data pull) | If ICP-match users convert at >8% and non-ICP at <2%, the problem is acquisition targeting (escalate to marketing). If both segments convert poorly, ICP mismatch is not the primary driver. | PM + Eng 1 |
| E7 | H2 (Value demo) | **In-trial nudge prototype.** If E3 validates value gaps, design 3-day drip of in-app nudges (tooltips, use-case templates, "try this next" prompts). Test with a small cohort of new trial users. | Feature engagement rate (# of paid-tier features used in trial); self-reported clarity score | Onboarding completion rate must not drop (nudges shouldn't overwhelm) | 50-100 new trial users (if volume allows) | Week 3-5 (design Week 3, implement Week 4, measure Week 5) | If nudged users engage with 2x more paid features than control, build the full system. If no engagement lift, the value demo framing may be wrong (revisit positioning). | Designer + Eng 2 |

### Experiment sequencing

```
Week 1:  E1 (funnel data), E4 (pricing analytics), E6 (ICP analysis), E3 begins (recruit interviewees)
Week 2:  E3 (conduct interviews), E1/E4/E6 results analyzed, E2 design begins
Week 3:  E2 (usability tests), E5 design (if E4 warrants), E7 design (if E3 warrants)
Week 4:  E5 (A/B test runs), E7 implementation begins, DECISION CHECKPOINT
Week 5:  E7 measurement, build sprint on winning direction
Week 6:  Build sprint continues, measure early signals, final decision checkpoint
```

---

## 4) Plan v0 (phases + learning gates)

**Principle:** Commit to learning milestones, not delivery dates. The plan adapts based on what we learn.

| Phase | Weeks | Goal | Output(s) | Learning gate (what must be true to proceed) |
|---|---|---|---|---|
| **Phase 1: Diagnose** | 1-2 | Reduce uncertainty. Identify the primary conversion bottleneck(s). | Funnel data (E1), ICP analysis (E6), pricing analytics (E4), exit interview themes (E3), competitive audit | We can rank the 4 hypotheses by evidence strength and know which 1-2 to pursue. At least 2 of 4 hypotheses have directional data. |
| **Phase 2: Test** | 3-4 | Validate the top 1-2 hypotheses with targeted experiments. | Usability test results (E2), pricing A/B results (E5), value nudge prototype (E7 design) | We have a clear "winner" hypothesis with supporting evidence, OR we have eliminated 2+ hypotheses and know where to focus. Decision checkpoint at end of Week 4. |
| **Phase 3: Build + measure** | 5-6 | Commit to one remediation direction and ship an initial version. Measure early conversion signals. | Shipped improvement (guided onboarding, simplified pricing, in-trial nudges, or acquisition change escalation), early metric movement | Early signals show directional improvement in the target metric (activation rate, pricing page conversion, or feature engagement). If not, document learnings and plan next iteration. |

### Phase transition decisions

- **Phase 1 to Phase 2:** PM reviews all Phase 1 evidence in a 60-min learning review (end of Week 2). Team ranks hypotheses by evidence. Top 1-2 move to Phase 2 testing. Others are parked or escalated (e.g., ICP mismatch goes to marketing).
- **Phase 2 to Phase 3:** PM makes a commit-or-pivot decision at the end of Week 4. If evidence is strong for one direction, commit to build. If evidence is mixed, extend Phase 2 by 1 week (using buffer) and narrow scope of Phase 3.

---

## 5) Buffers, contingencies, and triggers

### Buffers

- **Time buffer:** 1 week (Week 6 is designed as a flexible build/measure week). If Phase 2 needs to extend, Week 5 absorbs the overflow and Phase 3 compresses to a focused, minimal build in Week 6.
- **Capacity buffer:** Engineers split work so that E1/E4/E6 (data/analytics) run in parallel in Week 1 without blocking design work. Designer has Week 1 primarily for competitive audit and interview prep (lower-effort tasks) so capacity is available for higher-effort prototype work in Weeks 2-3.
- **Scope buffer:** Phase 3 build is scoped to a single intervention (not all 4 hypotheses). If time is tight, ship the smallest version that tests the hypothesis in production (e.g., a manual guided flow before building an automated one).

### Contingencies (Plan A / B / C)

- **Plan A (activation UX is the bottleneck):** Build a guided first-run experience. Eng 2 + Designer lead. Deliverable: interactive walkthrough shipped to 100% of new trials by Week 6.
- **Plan B (pricing page is the bottleneck):** Ship simplified pricing page. Designer + Eng 2 lead. Deliverable: new pricing page live and A/B tested by Week 5, shipped to 100% by Week 6.
- **Plan C (ICP mismatch is the primary driver):** Escalate to marketing/growth team with data package. This team shifts to "improve conversion for ICP-match segment only" with a targeted onboarding path. Deliverable: ICP-specific onboarding variant by Week 6.
- **Plan D (value demonstration gap):** Build in-trial nudge system. Designer + Eng 2 lead. Deliverable: 3-day drip of in-app nudges live for new trials by Week 6.
- **Plan E (multiple factors, no single winner):** Pick the highest-ROI intervention based on effort vs. expected impact. Ship that one. Document remaining hypotheses as backlog for the next cycle.

### Triggers (if X then Y)

| Trigger signal | Threshold | Action | Owner | Timing |
|---|---|---|---|---|
| ICP-match conversion rate is >8% while non-ICP is <2% | ICP conversion >= 2x non-ICP and non-ICP is >40% of trial base | Escalate ICP mismatch to marketing. This team pivots to Plan C (ICP-specific onboarding). | PM | End of Week 1 (E6 results) |
| Activation rate for all trial users is <25% | <25% complete core activation event | Prioritize H1 (activation UX) as the primary investment. Move to Plan A. | PM | End of Week 2 (E1 results) |
| Pricing page exit rate >70% with confusion signals | Exit rate >70% AND heatmap shows plan-toggling or scroll-past-CTA behavior | Prioritize H3 (pricing friction). Move to Plan B. | PM | End of Week 2 (E4 results) |
| >50% of exit interviewees cite "didn't see the value" or "didn't know what to do" | Majority theme from E3 interviews | Validate H1/H2 as primary. Weight experiment investment toward activation + value demo. | PM | End of Week 2 (E3 results) |
| Phase 2 experiments yield ambiguous results (no hypothesis shows >15% relative lift) | No clear winner after Week 4 experiments | Extend Phase 2 by 1 week (use time buffer). Narrow to the single best-signal hypothesis and run one more targeted test. | PM | End of Week 4 |
| Early signals in Phase 3 show zero movement on target metric after 1 week | Metric flat or declining after intervention ships | Stop and reassess. Conduct rapid post-mortem. Consider whether the hypothesis was wrong or the implementation was insufficient. | PM | End of Week 5 |
| Trial signup rate drops >10% after any change ships | >10% decline in weekly trial signups vs. prior 4-week average | Immediately rollback the change. Investigate cause. | Eng 1 | Continuous during Phase 3 |

---

## 6) Cadence + comms

### Learning / decision cadence

- **Weekly learning review (every Friday, 45 min):** Full team (PM, 2 Eng, Designer). This is the primary decision-making forum.
- **Mid-week sync (every Wednesday, 15 min):** Quick blockers check. PM + whoever is running active experiments. Async Slack update is acceptable if no blockers.
- **Decision checkpoints:** End of Week 2 (prioritize hypotheses), end of Week 4 (commit to build direction), end of Week 6 (assess early results and plan next cycle).

### Weekly learning review agenda

1. **What changed since last review?** (New data, experiment results, surprises) — 10 min
2. **What did we learn?** (Hypothesis results: confirmed, refuted, or inconclusive) — 10 min
3. **What decisions do we make now?** (Stop/pivot/scale any hypothesis; trigger any contingency) — 10 min
4. **What are the next experiments / build priorities?** (Assign owners and deadlines for the coming week) — 10 min
5. **Risks, blockers, and mitigations** — 5 min

### Stakeholder update template (sent weekly after Friday review)

```
Subject: Onboarding Conversion — Week [X] Update

Status: [GREEN / YELLOW / RED] — [one-line summary of what changed]

This week's learning:
- [Hypothesis tested]: [Result]. [What this means for our plan.]
- [Hypothesis tested]: [Result]. [What this means for our plan.]

Decisions made:
- [Decision]: [Rationale]. Owner: [name].

Decisions needed (from stakeholders):
- [Decision needed]: [Context]. Owner: [name]. Deadline: [date].

Next week's plan:
- [Experiment/build task]: Owner: [name]. Expected output by [date].

Risks / mitigations:
- [Risk]: [Mitigation plan].

Conversion metric snapshot:
- Trial-to-paid (trailing 2 weeks): [X]%
- Activation rate: [X]%
- Pricing page exit rate: [X]%
```

### Decision log location

Maintain a running decision log in the team's project wiki / Notion page. Format:

| Date | Decision | Decision owner | Evidence / rationale | Follow-ups (owner/date) |
|---|---|---|---|---|
| Week 2 | Prioritize activation UX (H1) as primary hypothesis | PM | Funnel data shows 78% drop before activation; exit interviews confirm confusion | Designer to prototype guided flow by Wed W3 |
| Week 4 | Commit to guided onboarding build (Plan A) | PM | Usability tests show 75% activation with guidance vs. 22% without | Eng 2 to build by end of Week 6 |

*(Rows above are illustrative examples)*

---

## 7) Risks / Open questions / Next steps

### Risks

| Risk | Impact | Probability | Early signal | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| Insufficient trial volume to run meaningful A/B tests in 1-2 weeks | High — inconclusive experiments waste time | Medium | <500 pricing page visitors/week for E5 | Use moderated usability tests (E2) and qualitative interviews (E3) instead of waiting for statistical significance. Accept directional evidence over statistical proof for the 6-week window. | PM | Monitor in Week 1 |
| Problem is multi-causal (no single dominant bottleneck) | Medium — harder to prioritize, slower progress | Medium | Phase 1 data shows moderate issues across all 4 hypotheses, no standout | Use trigger for Plan E: pick highest-ROI single intervention based on effort vs. expected impact. Scope Phase 3 to one bet. | PM | Assess at Week 2 checkpoint |
| Team capacity is stretched across too many parallel experiments | Medium — quality of experiments suffers | Low | Team members working >50 hours/week; experiment timelines slipping | Strictly limit active experiments to 2 per week. PM triages and defers lower-priority experiments. | PM | Continuous |
| ICP mismatch is the primary cause, but this team can't fix acquisition | High — 6 weeks yields diagnosis but no fix | Medium | E6 shows >50% of trials are non-ICP | Prepare escalation package for marketing by end of Week 2. This team pivots to ICP-specific onboarding (Plan C) as an interim measure. | PM | Week 1 (E6 results) |
| Stakeholder pressure to "just ship something" before learning phase completes | Medium — premature commitment to wrong solution | Low | Stakeholder asks for delivery dates in Week 1-2 | Share this planning pack proactively. Frame Phase 1-2 as "de-risking the investment" — building the wrong thing wastes more time than 2 weeks of diagnosis. | PM | Proactive — share pack Day 1 |

### Open questions

| # | Question | Why it matters | Owner | Resolve by |
|---|---|---|---|---|
| 1 | What is our defined "activation event"? (Do we have one? Is it instrumented?) | Cannot measure activation rate or design experiments without this. First task for Week 1. | PM + Eng 1 | End of Day 2 |
| 2 | What analytics / instrumentation do we currently have on the trial funnel? | Determines how much setup work is needed before E1/E4 can run. | Eng 1 | End of Day 1 |
| 3 | What is our current trial duration, and is there data on optimal trial length? | Affects experiment design and whether trial length itself is a variable. | PM | End of Week 1 |
| 4 | Do we have firmographic data on trial signups sufficient to classify ICP match? | If not, E6 requires manual enrichment or proxy metrics. | PM + Eng 1 | End of Day 2 |
| 5 | Is there executive appetite to change pricing structure if H3 is validated, or only pricing page UX? | Constrains the solution space for Plan B. | PM | End of Week 1 (ask exec sponsor) |

### Next steps (owners + dates)

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Define the activation event and verify instrumentation | PM + Eng 1 | Day 1-2 |
| 2 | Audit existing analytics: what funnel data, heatmaps, and session recording tools are available? | Eng 1 | Day 1 |
| 3 | Pull funnel data for E1 (signup > activation > engagement > pricing > checkout > paid) | Eng 1 | End of Week 1 |
| 4 | Pull ICP segmentation data for E6 | PM + Eng 1 | End of Week 1 |
| 5 | Install/configure pricing page heatmap for E4 | Eng 1 | Day 2-3 |
| 6 | Recruit 5-8 churned trial users for exit interviews (E3) | PM | Week 1 (interviews in Week 2) |
| 7 | Conduct competitive onboarding audit (3 alternatives) | Designer | Week 1 |
| 8 | Share this Uncertainty Planning Pack with stakeholders for async review | PM | Day 1 |
| 9 | Schedule recurring Friday learning review (45 min) and Wednesday async sync | PM | Day 1 |
| 10 | First weekly learning review: present E1/E4/E6 preliminary data and E3 recruitment status | All | Friday, Week 1 |

---

## Self-assessment (per RUBRIC.md)

| Dimension | Score | Rationale |
|---|---|---|
| 1. Decision clarity | 2 | Objective, "why now", time horizon, decision owner, and decision type (commit to remediation direction) are all explicit. |
| 2. Mode fit | 2 | Peacetime mode correctly chosen for chronic underperformance (not acute crisis). Plan structure uses weekly cadence and multi-week experiment phases, matching peacetime urgency. |
| 3. Uncertainty mapping | 2 | 7 unknowns captured with confidence/impact ratings. Top 5 prioritized. Each has validation method, owner, and time bound. |
| 4. Hypothesis quality | 2 | 4 hypotheses are falsifiable with mechanisms ("because..."). Each maps to a concrete decision (which plan to activate). |
| 5. Experiment portfolio | 2 | 7 experiments with owners, timelines, segments, and expected learning. Mix of fast tests (E1, E4, E6 in Week 1) and higher-confidence tests (E2, E5, E7 in Weeks 2-5). |
| 6. Metrics as compass | 2 | Primary signals are leading indicators (activation rate, pricing page exit rate, feature engagement). Guardrails defined. Explicitly avoids false precision (accepts directional evidence over statistical proof given volume constraints). |
| 7. Buffers + contingencies | 2 | Time buffer (1 week), capacity buffer (parallel workstreams), scope buffer (single intervention). 5 contingency plans (A-E). 7 operational triggers with thresholds and actions. |
| 8. Cadence + comms | 2 | Weekly learning review with 5-item agenda. Mid-week sync. Stakeholder update template. Decision log format and location specified. |
| 9. Actionability | 2 | Risks have owners and mitigations. Open questions have owners and deadlines. 10 next steps with owners and specific dates. A team could execute from Day 1 without additional interpretation. |
| **Total** | **18/18** | |
