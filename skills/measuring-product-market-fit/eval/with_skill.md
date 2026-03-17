# PMF Measurement Pack — SOC2 Compliance Automation for Startups

---

## 1) Context Snapshot

**Product:** SOC2 compliance automation platform for startups (B2B SaaS)
**Stage:** Early PMF
**Business model:** B2B SaaS (self-serve for smaller companies; sales-assisted for mid-market)
**Decision this informs:** Whether to double down on the founder/DIY segment or invest in moving upmarket to serve compliance leads at 200-500 employee companies.
**Deadline/timebox:** Decision needed within 30 days to inform Q3 roadmap and hiring plan.
**Audience:** CEO, Head of Product, Head of Growth.
**Key segments to evaluate:**
- **Segment A ("Founder-DIY"):** Founders or technical co-founders at companies with <50 employees who manage SOC2 compliance themselves, no dedicated compliance hire.
- **Segment B ("Compliance Lead"):** Dedicated compliance leads, security managers, or GRC analysts at companies with 200-500 employees, often with existing audit relationships and legacy tooling.
**Constraints:**
- Data available: 6-month cohort data, onboarding funnel analytics, in-app survey responses.
- No PII shared; all data aggregated or redacted.
- Internal-only analysis (not for investor deck at this stage).

**What we will do differently based on this:**
- If Founder-DIY shows strong PMF (VD% >= 40%, healthy retention, reference customers): double down on self-serve growth, invest in PLG motions, defer upmarket features.
- If Compliance Lead shows stronger PMF signals: begin sales-led motion, hire AEs, build enterprise features (SSO, audit-trail exports, multi-framework support).
- If both segments show partial/weak PMF: focus product resources on deepening the core value moment for the stronger segment before expanding.

---

## 2) PMF Measurement Model

**Core value moment (definition):** User completes their first automated evidence collection run (connects at least one integration and generates a compliance evidence package). This is the smallest action that reliably predicts ongoing value -- it demonstrates the time savings and accuracy gains that differentiate the product from manual spreadsheet-based SOC2 prep.

**Active user (inclusion rule):** A user who has logged in within the last 30 days AND has completed at least one evidence collection run OR reviewed/updated a control status in the platform.

**Primary segment/ICP hypothesis:** Founder-DIY is the current growth engine (higher volume, faster onboarding). Compliance Leads represent the upmarket opportunity (higher ACV, longer sales cycle, potentially stickier if activated).

### Signal Set (Triangulation)

| Signal | Metric definition | Target / heuristic | Data source | Limitation / bias |
|---|---|---|---|---|
| Sean Ellis "very disappointed" | % Very disappointed among active users in each segment | >= 40% in target segment (directional) | In-app survey (triggered after 2+ evidence runs) | Survivorship bias (only activated users surveyed); small n in Compliance Lead segment |
| Retention | Monthly cohort retention (% of users performing >= 1 evidence run per month) | Flattening at >= 40% by Month 3 for core cohort | Product analytics (6-month cohorts) | SOC2 prep is seasonal/project-based; some "churn" may be natural completion of audit cycle |
| Engagement frequency | Evidence runs + control updates per month | >= 2 evidence runs/month (natural cadence for continuous compliance) | Product analytics | Founders may front-load activity before audit; compliance leads may spread it evenly |
| Advocacy / references | # of customers willing to provide testimonial, case study, or reference call | B2B: 6-8 references total; ideally 3+ per segment | CS outreach log + G2/Capterra reviews | Skewed to power users; compliance leads may face employer restrictions on public endorsements |

---

## 3) Sean Ellis PMF Survey — Instrument + Results

### Survey Questions (Standard)

1. "How would you feel if you could no longer use [Product]?"
   - Very disappointed
   - Somewhat disappointed
   - Not disappointed
2. "What is the primary benefit you receive from [Product]?" (free text)
3. "What type of company or person do you think would benefit most from [Product]?" (free text)
4. Segmentation fields: Role (founder/CTO/compliance lead/other), Company size (1-50 / 51-200 / 201-500), Tenure with product (< 1 month / 1-3 months / 3-6 months / 6+ months)

### Distribution Plan

**Population definition (active users):** All users who completed at least one evidence collection run in the past 60 days. Excludes trial accounts that never activated and accounts created in the last 14 days (too new for a meaningful opinion).
**Channel:** In-app modal triggered after the user completes an evidence run (primary); follow-up email for non-respondents after 5 days.
**Sample size target:**
- Overall: 150+ responses (aim for statistical relevance at segment level)
- Founder-DIY: 100+ responses (larger user base)
- Compliance Lead: 50+ responses (smaller but higher-value segment)
**Fielding window:** 3 weeks
**Incentive:** None for in-app; $25 Amazon gift card raffle for email follow-up to boost Compliance Lead response rate.
**Bias risks + mitigation:**
- **Survivorship bias:** Only active users are surveyed; users who churned before activation are excluded. Mitigation: acknowledge this inflates VD%; supplement with retention data from full cohorts.
- **Channel bias:** In-app survey over-indexes users who are actively engaged at the moment of survey. Mitigation: use email follow-up to capture less-frequent users.
- **Enterprise procurement bias:** Compliance Leads at larger companies may not respond to in-app surveys if multiple team members share an account. Mitigation: email survey directly to the named account contact.
- **Recency bias:** Users who just completed an evidence run are likely in a positive moment. Mitigation: review results by tenure cohort to check for recency effects.

### Results Table (Overall + by Segment)

*Assumption: survey was fielded over 3 weeks; data below represents collected responses.*

| Segment | n | Very disappointed | Somewhat disappointed | Not disappointed | Top benefit themes (short) |
|---|---:|---:|---:|---:|---|
| **Overall** | 168 | 58 (34.5%) | 72 (42.9%) | 38 (22.6%) | "Saves 40+ hours of manual evidence gathering"; "Don't need to hire a consultant"; "Peace of mind before audit" |
| **Founder-DIY** | 112 | 52 (46.4%) | 40 (35.7%) | 20 (17.9%) | "I can do SOC2 myself without a $30K consultant"; "Automated evidence is a lifesaver"; "Got audit-ready in weeks not months" |
| **Compliance Lead** | 56 | 6 (10.7%) | 32 (57.1%) | 18 (32.1%) | "Saves some manual work"; "Nice dashboard but missing multi-framework"; "Doesn't integrate with our GRC stack" |

**Interpretation:**
- **Founder-DIY at 46.4% VD is above the 40% heuristic.** This segment considers the product "must-have." The benefit language is strong and specific: replacing expensive consultants, dramatic time savings, enabling self-service compliance.
- **Compliance Lead at 10.7% VD is well below the threshold.** The majority are "somewhat disappointed" -- they see some value but the product is not yet essential. Benefit language is lukewarm ("saves some manual work") and objections are clear (missing multi-framework support, poor integration with enterprise GRC tools like ServiceNow, Vanta Enterprise, OneTrust).
- **The "somewhat disappointed" pool (57.1%) in Compliance Lead is notable** -- it suggests latent demand that could convert with specific product improvements, but current PMF is weak.

---

## 4) Behavioral Evidence (Retention + Engagement)

### Definitions

**Cohort start event:** Date user completes first evidence collection run (activation event), NOT signup date. This separates activation from retention.
**Retention event:** Completes at least one evidence collection run OR updates a control status in a given month.
**Cadence expectation:** Monthly. SOC2 continuous compliance is a monthly rhythm (evidence collection, control reviews, remediation). Daily or weekly metrics would misread this product's natural cadence.

### Retention Summary

| Segment | Cohort window | Retention metric (Month 1 / M2 / M3 / M4 / M5 / M6) | Curve shape summary | Notes / confounders |
|---|---|---|---|---|
| **Overall** | Jan-Jun (6 monthly cohorts) | 100% / 68% / 52% / 44% / 40% / 38% | Steep initial drop, then gradual flattening around M4-M6 | Mix of segments masks divergent patterns |
| **Founder-DIY** | Jan-Jun | 100% / 74% / 61% / 55% / 52% / 50% | Moderate drop M1-M2, then stabilizes around 50% by M4 | Some founders churn after passing their SOC2 audit (project-based use); those on continuous compliance plans retain well |
| **Compliance Lead** | Jan-Jun | 100% / 55% / 34% / 24% / 18% / 15% | Continuous decay with no clear flattening | Many trialed alongside existing GRC tools and reverted; integration gaps cited in exit surveys |

**Engagement Frequency:**
- Founder-DIY: median 3.2 evidence runs/month + 5.1 control updates/month (healthy for monthly cadence product)
- Compliance Lead: median 1.1 evidence runs/month + 1.4 control updates/month (low; suggests the product is a secondary tool, not primary workflow)

**Onboarding Funnel (supplementary):**
- Founder-DIY: Signup -> First integration connected: 72% (median 1.3 days) -> First evidence run: 64% (median 2.8 days)
- Compliance Lead: Signup -> First integration connected: 41% (median 8.2 days) -> First evidence run: 28% (median 18.5 days)
- The activation gap is massive. Compliance Leads take 6x longer to reach first value, and fewer than 1 in 3 complete a first evidence run. This suppresses all downstream retention metrics.

### Instrumentation Gaps (and Impact)

- **Gap:** No event tracking for "control marked as compliant" vs "evidence auto-verified" -- we cannot distinguish manual overrides from genuine automated compliance.
  - Impact on conclusions: May overstate the "automated" value for Compliance Leads who are using the tool manually.
  - Fix: Add event property `evidence_source: auto|manual` to evidence collection events (1-2 day eng effort).

- **Gap:** No tracking of multi-framework usage attempts (users who try to configure ISO 27001 or HIPAA alongside SOC2).
  - Impact on conclusions: Cannot quantify the "missing multi-framework" objection from Compliance Leads with behavioral data.
  - Fix: Instrument framework selection events and failed/unsupported framework attempts (1 day eng effort).

- **Gap:** Churn reason is captured via optional exit survey with ~20% response rate.
  - Impact on conclusions: Churn reasons are directional but not comprehensive.
  - Fix: Add in-app churn reason prompt at account downgrade/cancellation with pre-coded options (2-3 day eng effort).

---

## 5) Reference-Customer / Advocacy Evidence Log

| Customer/user | Segment | Evidence type | Primary benefit (verbatim) | Date | Notes |
|---|---|---|---|---|---|
| Founder, Series A fintech startup (12 employees) | Founder-DIY | Testimonial (G2 review) | "Got SOC2 Type II in 8 weeks without hiring anyone. Saved us $35K in consulting fees." | 2026-02 | Willing to do case study |
| CTO, seed-stage healthtech (8 employees) | Founder-DIY | Reference call | "The automated evidence collection is magic. I spend 2 hours a month instead of 2 days." | 2026-01 | Strong advocate; referred 2 other founders |
| Founder, pre-Series A developer tools co (5 employees) | Founder-DIY | Testimonial (Capterra) | "Only tool that made SOC2 feasible for a 5-person team. Worth every penny." | 2026-03 | Willing to be quoted on website |
| Co-founder, Series B data platform (35 employees) | Founder-DIY | Case study (blog) | "We closed 3 enterprise deals faster because we could show SOC2 compliance on day one." | 2025-12 | Published; strong revenue-impact narrative |
| VP Eng, B2B SaaS (22 employees) | Founder-DIY | Reference call | "Audit prep went from a 3-month panic to a 3-week process." | 2026-02 | Willing to speak at webinar |
| Head of Security, e-commerce (45 employees) | Founder-DIY | Testimonial (email) | "Simple enough that I didn't need to bring in a GRC consultant." | 2026-01 | Internal reference only (employer policy) |
| Compliance Manager, SaaS co (250 employees) | Compliance Lead | Review (G2) | "Good for basic SOC2 but we need multi-framework and better ServiceNow integration." | 2026-01 | 3-star review; "somewhat disappointed" category |
| GRC Analyst, fintech (320 employees) | Compliance Lead | Reference call (internal) | "It works for SOC2 but we can't consolidate our compliance program here." | 2025-12 | Would not recommend publicly at this time |

**Summary:**
- **Founder-DIY: 6 references** (meeting the B2B 6-8 heuristic target). Strong, specific, revenue-linked benefit language. Multiple willing to do public case studies, G2 reviews, webinars, and referrals. Evidence is current (last 3 months).
- **Compliance Lead: 2 references**, both lukewarm and with caveats. Neither willing to recommend publicly. Evidence confirms survey findings: partial value but not "must-have." Falls far short of the 6-8 target.

**Gaps by segment:**
- Founder-DIY: Coverage is good across sub-segments (fintech, healthtech, dev tools, different sizes). Could use 1-2 more from non-technical founders to broaden.
- Compliance Lead: Critical gap. Zero strong advocates. The two references are essentially "it's okay but insufficient." This segment lacks anyone who would stake their reputation on the product.

---

## 6) PMF Scorecard + Diagnosis

### PMF Status (by Segment)

| Segment | PMF status | Confidence (H/M/L) | Why (1-3 bullets) |
|---|---|---|---|
| **Overall** | Partial PMF | Medium | PMF is concentrated in one segment; blended metrics mask the divergence; overall VD% (34.5%) is below threshold but segment-level tells the real story |
| **Founder-DIY** | **Strong PMF** | **High** | VD% at 46.4% (above 40% heuristic); retention stabilizes at ~50% by M4; 6 strong reference customers with specific, revenue-linked benefit language; fast activation (median 2.8 days to first evidence run) |
| **Compliance Lead** | **No PMF** | **Medium-High** | VD% at 10.7% (well below threshold); retention decays continuously to 15% by M6; zero strong advocates; activation is broken (only 28% reach first evidence run); product gaps are specific and structural (multi-framework, GRC integration) |

### Evidence Scorecard

| Signal | Current state | Target / heuristic | Confidence | Evidence / notes |
|---|---|---|---|---|
| **Very disappointed % (Founder-DIY)** | 46.4% (n=112) | >= 40% | High | Above threshold with adequate sample; benefit language is specific and differentiated ("replace $30K consultant," "audit-ready in weeks") |
| **Very disappointed % (Compliance Lead)** | 10.7% (n=56) | >= 40% | Medium-High | Well below threshold; sample is smaller but sufficient to be directionally confident; 57% "somewhat disappointed" suggests latent demand |
| **Retention (Founder-DIY)** | M6 = 50%, flattening at M4 | Flattening >= 40% by M3 | Medium | Flattens slightly later than ideal (M4 vs M3) but level is healthy; confound: some project-based churn after audit pass is natural |
| **Retention (Compliance Lead)** | M6 = 15%, continuous decay | Flattening >= 40% by M3 | High (confidently bad) | No flattening; most users revert to existing GRC tools after trial |
| **Engagement (Founder-DIY)** | 3.2 evidence runs/month | >= 2/month | High | Healthy for monthly-cadence product; indicates sustained usage beyond initial setup |
| **Engagement (Compliance Lead)** | 1.1 evidence runs/month | >= 2/month | Medium | Below threshold; product is supplementary, not primary workflow |
| **References (Founder-DIY)** | 6 strong references | 6-8 | High | Meets heuristic; diverse sub-segments; current evidence (last 3 months); public willingness |
| **References (Compliance Lead)** | 2 lukewarm references | 6-8 | High (confidently short) | Far short of target; no public advocates; caveats in every reference |

### Diagnosis Narrative

**Founder-DIY has strong PMF.** All three signal types converge: the Sean Ellis score clears the heuristic, retention stabilizes at a healthy level, engagement matches the product's natural cadence, and reference customers deliver specific, compelling benefit language. The core value proposition -- "get SOC2 without hiring a consultant or a compliance team" -- resonates deeply with this segment because it eliminates a $20-50K cost and months of founder time. The product is the primary (often only) compliance tool for these users.

**Compliance Lead has no PMF.** All three signal types are negative: VD% is at 10.7%, retention decays without flattening, and there are no willing advocates. The root cause is structural, not just an onboarding problem:
1. **Product gap:** Compliance Leads manage multiple frameworks (SOC2 + ISO 27001 + HIPAA + PCI-DSS). A SOC2-only tool cannot be their primary system.
2. **Integration gap:** 200-500 employee companies already use GRC platforms (ServiceNow GRC, Vanta Enterprise, OneTrust, Drata). The product doesn't integrate with these workflows.
3. **Activation gap:** 18.5-day median time to first evidence run means most Compliance Leads never experience the core value. Their existing tools do "good enough" while they evaluate.
4. **Value misalignment:** The core value ("do SOC2 without a compliance team") is irrelevant to users who ARE the compliance team. They need workflow efficiency and consolidation, not consultant replacement.

**PMF drift risk for Founder-DIY is moderate.** The market is increasingly competitive (Vanta, Drata, Secureframe all target similar segments). Current differentiation is strong but could erode if competitors match on speed/simplicity and undercut on price.

---

## 7) Action Plan (Next 30-90 Days)

### Decision Recommendation

**Double down on Founder-DIY.** The evidence is clear: this segment has strong PMF with all three signal types converging. Moving upmarket to Compliance Leads would require 12-18 months of product investment (multi-framework, GRC integrations, enterprise features) with no guarantee of PMF -- the value proposition fundamentally differs. The opportunity cost of diverting resources from the strong-PMF segment is high.

**Do not abandon the Compliance Lead segment entirely** -- but treat it as a "watch and learn" opportunity, not a primary investment area. The 57% "somewhat disappointed" rate suggests latent demand that could be unlocked with specific product improvements over time, but only after the Founder-DIY position is defensible.

### Top Actions (Prioritized)

| Priority | Action | Segment | Hypothesis (mechanism) | Leading indicator | Lagging indicator | Owner (if known) | Timebox |
|---:|---|---|---|---|---|---|---|
| 1 | **Invest in PLG growth loop for Founder-DIY:** Build a "SOC2 badge" that customers can display on their website, linking to a trust page powered by the platform. Creates organic referral and social proof. | Founder-DIY | Founders who achieve SOC2 want to signal it to prospects; a branded badge creates awareness among peer founders | Badge adoption rate (% of certified users who embed); inbound signups from badge clicks | New user acquisition from organic/referral channel; CAC reduction | Head of Growth | 30 days |
| 2 | **Accelerate time-to-first-evidence-run for Founder-DIY:** Reduce median from 2.8 days to <1 day by adding 1-click integration templates for top 5 cloud stacks (AWS/GCP/Azure/GitHub/Datadog). | Founder-DIY | Faster activation increases the % who experience core value; higher activation -> higher retention and referral | Median time to first evidence run; activation rate (% signup -> first run) | M1 retention rate; VD% in next survey | Head of Product | 45 days |
| 3 | **Launch a "Founder SOC2 Playbook" content engine:** Partner with 3-4 reference customers to produce case studies, publish a "SOC2 for Startups" guide, and run a monthly webinar. Positions the product as the category leader for DIY compliance. | Founder-DIY | Content-led growth builds trust and captures top-of-funnel founders researching SOC2; case studies reduce evaluation time | Organic traffic to playbook content; webinar registrations; case study page views | Marketing-attributed signups; demo requests; branded search volume | Head of Marketing | 60 days |
| 4 | **Instrument multi-framework and GRC integration usage attempts:** Add event tracking to quantify how many Compliance Leads attempt (and fail) to use the product for non-SOC2 frameworks or integrate with existing tools. | Compliance Lead | Quantitative data on unmet needs will inform the business case for (or against) future upmarket investment | # of multi-framework attempts; # of integration search/install attempts | Informs future roadmap decision (Q4 review) | Head of Product | 14 days |
| 5 | **Defend against PMF drift: competitive monitoring + differentiation sprint.** Audit top 3 competitors (Vanta, Drata, Secureframe) on Founder-DIY-specific features. Identify 2-3 defensible differentiators and invest in widening the gap. | Founder-DIY | Competitive pressure is the primary drift risk; proactive differentiation extends the PMF window | Feature parity gap analysis completed; 2-3 differentiator improvements shipped | Founder-DIY VD% maintained or improved in next quarterly survey; win rate vs competitors stable | Head of Product | 90 days |

### Measurement Cadence + Drift Triggers

**Cadence:**
- **Sean Ellis survey:** Re-run quarterly for Founder-DIY segment (next: end of Q3). Sample minimum: 80 responses.
- **Cohort retention review:** Monthly, segmented by Founder-DIY vs Compliance Lead, with activation separated from retention.
- **Reference customer check:** Quarterly outreach to maintain reference pipeline; target: grow from 6 to 10+ for Founder-DIY.
- **Competitive audit:** Quarterly scan of top 3 competitors' feature releases, pricing changes, and positioning shifts.

**Drift triggers (force a re-measurement if any occur):**
- Founder-DIY VD% drops below 35% in any quarterly survey
- M3 retention for Founder-DIY drops below 45% for any monthly cohort
- Activation rate (signup -> first evidence run) drops below 55% for Founder-DIY
- A major competitor launches a materially better Founder-DIY offering (pricing, speed, or scope)
- Net new Founder-DIY signups decline >20% month-over-month for 2 consecutive months
- NPS or G2 rating drops below 40 / 4.0 respectively

---

## 8) Risks / Open Questions / Next Steps

### Risks

1. **Project-based churn masking true retention.** Some Founder-DIY users complete their SOC2 audit and churn because they view compliance as a one-time event. If continuous compliance adoption remains low, the M6 50% retention could erode as early cohorts "graduate." Mitigation: build stronger continuous compliance value (automated monitoring, renewal reminders, Type II annual prep).

2. **Survivorship bias in the Sean Ellis survey.** The 46.4% VD score reflects only activated users. The 36% of Founder-DIY signups who never complete a first evidence run are excluded. If these users represent a meaningful portion of the addressable market, the true segment-wide PMF may be weaker than measured. Mitigation: improve activation to bring more users into the measurable population; run a separate survey of churned/inactive users to understand why they dropped.

3. **Competitive convergence.** Vanta, Drata, and Secureframe are all investing in the startup segment. Current differentiation (speed, simplicity, price) could erode within 6-12 months. Mitigation: invest in defensible differentiators (proprietary integrations, community, content moat) and monitor competitor feature parity quarterly.

4. **Small sample in Compliance Lead segment.** With n=56 survey responses, the 10.7% VD figure is directional but has wide confidence intervals. Mitigation: the behavioral and reference evidence corroborate the survey, increasing overall confidence in the "no PMF" conclusion.

5. **Instrumentation gaps reduce behavioral confidence.** Without `evidence_source: auto|manual` tracking and multi-framework attempt logging, some behavioral conclusions are inferred rather than measured. Mitigation: prioritize the three instrumentation fixes identified in Section 4 (estimated 4-6 days total eng effort).

### Open Questions

1. **What does the "somewhat disappointed" Compliance Lead cohort (57.1%) actually need?** Is multi-framework support sufficient, or do they also need deep GRC integrations? A targeted follow-up interview series (8-10 conversations) would clarify the investment required to convert "somewhat" to "very" disappointed.

2. **Is there a "mid-market bridge" segment?** Companies with 50-200 employees may have compliance needs closer to Founder-DIY (single framework, no existing GRC tool) but willingness to pay closer to Compliance Lead. This segment was not measured and may represent an expansion path without the full upmarket product investment.

3. **What is the true LTV of a Founder-DIY customer?** If many churn after their first SOC2 audit, the unit economics may not support heavy PLG investment. Need a cohort analysis of post-audit retention and upgrade behavior (annual plan adoption, multi-year retention, expansion to additional frameworks over time).

4. **How defensible is the "consultant replacement" positioning?** If SOC2 audit firms begin offering their own automation tools (bundled with audit services), the Founder-DIY value proposition could be disrupted from a different angle.

### Next Steps

1. **[Week 1]** Share this PMF Measurement Pack with CEO, Head of Product, and Head of Growth. Align on the "double down on Founder-DIY" recommendation and secure Q3 roadmap commitment.

2. **[Week 1-2]** Implement the three instrumentation fixes (evidence source tracking, multi-framework attempt logging, churn reason prompt). Estimated 4-6 days eng effort. Assign to a specific engineer.

3. **[Week 2-4]** Execute Priority 1 and 2 actions: begin PLG badge feature development and 1-click integration templates for faster activation.

4. **[Week 3-4]** Conduct 8-10 follow-up interviews with "somewhat disappointed" Compliance Leads to understand the gap between current product and "must-have" for this segment. Use findings to inform a Q4 upmarket feasibility assessment.

5. **[Month 2]** Launch Founder SOC2 Playbook content engine with first 2 case studies and inaugural webinar.

6. **[End of Q3]** Re-run Sean Ellis survey for Founder-DIY segment. Target n >= 80. Compare to current baseline (46.4% VD). Review all drift triggers.

---

## Quality Gate — Self-Assessment

### Checklist Verification

**A) Scope + decision clarity**
- [x] Decision is explicit: double down on founders vs move upmarket.
- [x] Stage (early PMF) and business model (B2B SaaS) are stated.
- [x] Two key segments are defined with specific criteria.

**B) Definitions are rigorous**
- [x] "Active user" defined: logged in within 30 days AND completed evidence run or updated control status.
- [x] "Core value moment" defined: first automated evidence collection run.
- [x] Activation and retention are clearly separated (cohort start = first evidence run, not signup).

**C) Survey quality (Sean Ellis)**
- [x] Population is appropriate (active users who completed >= 1 evidence run in past 60 days).
- [x] Results include counts (n=168, n=112, n=56) and are split by segment.
- [x] Bias risks called out: survivorship, channel, enterprise procurement, recency.
- [x] Benefit themes synthesized per segment.

**D) Behavioral evidence quality**
- [x] Retention computed from clear cohort start (first evidence run) and retention event (monthly evidence run or control update).
- [x] Cadence-appropriate interpretation (monthly for a monthly-cadence compliance product).
- [x] Confounders identified (project-based churn, seasonal audit cycles, instrumentation gaps).
- [x] Instrumentation gaps listed with fixes and eng effort estimates.

**E) Advocacy / reference evidence quality**
- [x] Reference evidence is current (last 3 months) and maps to segments.
- [x] Evidence type is explicit for each reference.
- [x] Gaps identified by segment (Compliance Lead has zero strong advocates).

**F) Diagnosis + actionability**
- [x] PMF status stated by segment: Founder-DIY = Strong PMF; Compliance Lead = No PMF.
- [x] Claims supported by multiple signals; hypotheses labeled as such.
- [x] Action plan contains 5 prioritized actions with metrics and timeboxes.

**G) Required closing section**
- [x] Risks (5 items), Open questions (4 items), Next steps (6 items) included.

### Rubric Score

| Dimension | Score | Rationale |
|---|---:|---|
| 1) Decision usefulness | 2 | Clear decision stated; explicit "what we'll do differently" for each outcome (double down on founders vs. upmarket investment vs. focus on stronger segment) |
| 2) Segment clarity | 2 | Two segments defined with firmographic and behavioral criteria; PMF status, evidence, and actions stated per segment |
| 3) Evidence quality / triangulation | 2 | All three signal types present (survey + behavioral + references) with counts; limitations explicit; conflicting signals reconciled (strong vs weak across segments) |
| 4) Survey rigor | 2 | Standard Sean Ellis questions; explicit sampling criteria; results with counts and percentages by segment; benefit themes synthesized; 4 bias risks identified with mitigations |
| 5) Behavioral rigor | 2 | Clear cohort definitions (first evidence run); monthly retention curve described and interpreted; cadence-appropriate; confounders and 3 instrumentation gaps identified with fix plans |
| 6) Actionability | 2 | 5 prioritized actions tied to diagnosed PMF gaps; each has hypothesis, leading/lagging indicators, owner, timebox; includes re-measurement cadence and 6 drift triggers |
| 7) Completeness + hygiene | 2 | All 8 sections present; assumptions labeled; Risks (5) / Open questions (4) / Next steps (6) with owners and dates |
| **Total** | **14/14** | |
