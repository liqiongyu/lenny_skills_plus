# PMF Measurement Plan: SOC2 Compliance Automation for Startups

## 1. Executive Summary

**Product:** SOC2 compliance automation platform for startups
**Stage:** Early product-market fit
**Key Decision:** Whether to double down on the self-serve founder segment or move upmarket to compliance leads at 200–500 employee companies
**Available Data:** 6-month cohorts, onboarding funnel metrics, and in-app survey responses

This plan outlines the metrics, frameworks, and analysis approach needed to determine which segment exhibits stronger PMF signals and should receive primary investment.

---

## 2. Segment Definitions

### Segment A: Founders Doing It Themselves
- **Company size:** Typically 5–50 employees
- **Buyer persona:** CEO/CTO or technical co-founder
- **Motivation:** Need SOC2 to close enterprise deals; no dedicated compliance hire
- **Buying behavior:** Self-serve, price-sensitive, speed-oriented
- **Success criteria:** Get SOC2 certification as fast and cheaply as possible

### Segment B: Compliance Leads at 200–500 Employee Companies
- **Company size:** 200–500 employees
- **Buyer persona:** Compliance manager, Head of Security, GRC lead
- **Motivation:** Operational efficiency, audit readiness, reducing manual work
- **Buying behavior:** Procurement-driven, feature-oriented, integration-focused
- **Success criteria:** Streamlined ongoing compliance management, audit confidence

---

## 3. PMF Measurement Framework

### 3.1 The Sean Ellis Test (Survey-Based)

Deploy the "how would you feel if you could no longer use this product?" question to both segments separately.

**Target benchmark:** 40%+ respondents answering "very disappointed"

**Segmented analysis:**
- Calculate the "very disappointed" percentage for Segment A and Segment B independently
- A segment scoring above 40% is exhibiting PMF; below 25% is a warning sign
- Compare the two segments head-to-head

**Implementation notes:**
- Trigger the survey after users have completed at least one meaningful workflow (e.g., completed a readiness assessment or connected an integration)
- Minimum sample size: 30+ respondents per segment for directional confidence
- Run quarterly to track trend over time

### 3.2 Retention Cohort Analysis

Using the 6-month cohort data, analyze retention curves for each segment.

**Metrics to calculate:**
| Metric | Definition | Strong PMF Signal |
|--------|-----------|-------------------|
| Month-1 retention | % of users active 30 days after signup | >60% |
| Month-3 retention | % of users active 90 days after signup | >40% |
| Month-6 retention | % of users active 180 days after signup | >30% |
| Retention curve shape | Whether the curve flattens or continues declining | Flattening by month 3–4 |

**Segmented analysis:**
- Plot separate retention curves for Segment A and Segment B
- Look for the segment where the curve flattens earlier and at a higher level
- A flattening retention curve is the single strongest quantitative signal of PMF

**Define "active" carefully:**
- For SOC2 compliance, "active" should mean a meaningful engagement (e.g., logged in and reviewed compliance status, completed a task, responded to an alert) — not just a login
- Consider weekly active vs. monthly active depending on expected usage cadence

### 3.3 Onboarding Funnel Analysis

Map the onboarding funnel and compare conversion rates by segment.

**Suggested funnel stages:**
1. Signup completed
2. Company profile created
3. First integration connected (cloud provider, HR system, etc.)
4. Readiness assessment completed
5. First policy generated/approved
6. Evidence collection initiated
7. Audit-ready milestone reached

**Key metrics per stage:**
- Conversion rate (stage N to stage N+1)
- Median time to complete each stage
- Drop-off rate at each stage
- Segment-level comparison at every stage

**What to look for:**
- Which segment completes onboarding faster?
- Where does each segment drop off? (This reveals product gaps per segment)
- Which segment reaches the "aha moment" more reliably?
- Time-to-value: median days from signup to first meaningful outcome

### 3.4 Engagement Depth Metrics

Beyond retention, measure how deeply each segment engages.

**Metrics:**
| Metric | Why It Matters |
|--------|---------------|
| Features used per week | Breadth of product adoption |
| Integrations connected | Depth of platform commitment (switching cost) |
| Policies customized vs. default | Investment in the platform |
| Team members invited | Organizational embedding |
| Evidence collection automation rate | Core value delivery |
| Return visit frequency | Habitual usage pattern |

**Segmented analysis:**
- Calculate averages and distributions for each metric by segment
- Identify which segment uses more of the product and integrates it more deeply into their workflow

### 3.5 Revenue and Willingness-to-Pay Indicators

**Metrics:**
| Metric | Definition | Strong Signal |
|--------|-----------|---------------|
| Conversion rate (free to paid) | % of free users who upgrade | >5% for self-serve, >15% for sales-assisted |
| Net revenue retention (NRR) | Revenue from existing customers after churn, contraction, and expansion | >100% |
| Expansion rate | % of customers who upgrade plan or add seats | Higher = stickier |
| CAC payback period | Months to recover customer acquisition cost | <12 months |
| LTV/CAC ratio | Lifetime value divided by acquisition cost | >3x |
| Price sensitivity | Resistance to pricing in sales calls or survey feedback | Lower sensitivity = stronger PMF |

**Segmented analysis:**
- Compare LTV projections for both segments using 6-month cohort data
- Even if Segment A has lower ACV, it may have better unit economics due to lower CAC
- Segment B may have higher ACV but longer sales cycles and higher CAC

---

## 4. In-App Survey Design

Leverage the existing in-app survey infrastructure to collect qualitative PMF signals.

### 4.1 Core Questions

1. **Sean Ellis question:** "How would you feel if you could no longer use [Product]?" (Very disappointed / Somewhat disappointed / Not disappointed)
2. **Primary benefit:** "What is the main benefit you get from [Product]?" (Open text)
3. **Alternatives:** "What would you use instead if [Product] didn't exist?" (Open text)
4. **Who benefits most:** "What type of person do you think would benefit most from [Product]?" (Open text)
5. **Improvement:** "What is the one thing we could do to improve [Product] for you?" (Open text)

### 4.2 Segment-Specific Questions

**For founders (Segment A):**
- "Did this product help you close a deal that required SOC2?" (Yes/No/In progress)
- "How many hours per week do you spend on compliance tasks?" (Numeric)
- "Would you recommend this to another founder?" (0–10 NPS)

**For compliance leads (Segment B):**
- "How does this compare to your previous compliance process?" (Much better / Somewhat better / About the same / Worse)
- "Which integrations are most critical for your workflow?" (Multi-select)
- "Does this product meet your audit team's requirements?" (Yes / Partially / No)

### 4.3 Analysis Approach

- Code open-text responses into categories
- Look for the "word-of-mouth" signal: do respondents describe the product in language that would resonate with others in their segment?
- Identify the "must-have" features per segment from improvement requests
- Cross-reference survey responses with behavioral data (high-engagement users who are "very disappointed" = your PMF core)

---

## 5. Cohort Analysis Framework

### 5.1 Cohort Construction

Using the 6-month data, build cohorts along two dimensions:

**Time-based cohorts:**
- Monthly signup cohorts (Month 1 through Month 6)
- Track whether newer cohorts perform better (product improvement signal)

**Segment-based cohorts:**
- Segment A (founders) vs. Segment B (compliance leads)
- Within each segment, sub-cohort by company size, industry, and acquisition channel

### 5.2 Key Cohort Analyses

**Analysis 1: Retention by Segment**
- Create a retention table (rows = cohort month, columns = months since signup)
- Color-code by segment to visually compare
- Statistical test: is the difference in retention between segments significant?

**Analysis 2: Time-to-Value by Segment**
- Define "value moment" (e.g., first readiness assessment completed, first audit passed)
- Measure median time-to-value per segment
- Shorter time-to-value = better product-market alignment

**Analysis 3: Expansion Revenue by Segment**
- Track revenue trajectory within each cohort
- Are Segment B customers expanding faster (adding seats, upgrading tiers)?
- Are Segment A customers stable or churning after initial certification?

**Analysis 4: Cohort Improvement Over Time**
- Are later cohorts (months 4–6) performing better than earlier ones (months 1–3)?
- This signals product iteration is working for that segment

---

## 6. Decision Framework

### 6.1 Scoring Matrix

Rate each segment on a 1–5 scale across these dimensions:

| Dimension | Weight | Segment A (Founders) | Segment B (Compliance Leads) |
|-----------|--------|----------------------|------------------------------|
| Sean Ellis score (% very disappointed) | 25% | ? | ? |
| Month-3 retention rate | 20% | ? | ? |
| Onboarding completion rate | 15% | ? | ? |
| NRR / expansion potential | 15% | ? | ? |
| Time-to-value | 10% | ? | ? |
| Organic referral rate | 10% | ? | ? |
| Qualitative enthusiasm | 5% | ? | ? |

### 6.2 Decision Rules

**Double down on founders (Segment A) if:**
- Sean Ellis score is 40%+ for founders but below 30% for compliance leads
- Founder retention curve flattens; compliance lead curve does not
- Founders complete onboarding 2x+ faster
- Self-serve acquisition engine is working (low CAC, organic growth)
- LTV/CAC ratio is favorable even at lower ACV

**Move upmarket (Segment B) if:**
- Compliance leads show 40%+ Sean Ellis score
- Compliance lead retention is materially higher (10+ percentage points)
- Revenue expansion from Segment B offsets higher CAC
- Feature requests from Segment B align with your roadmap
- Segment B customers serve as references that attract similar buyers

**Pursue both (with caution) if:**
- Both segments show PMF signals above threshold
- The product can serve both without major feature divergence
- You have resources to maintain two GTM motions
- Consider a sequenced approach: solidify one segment first, then expand

**Pivot required if:**
- Neither segment hits 40% on Sean Ellis
- Both retention curves continue declining through month 6
- Onboarding completion is below 30% for both segments

### 6.3 Watch Out For

- **Segment A illusion:** Founders may show initial enthusiasm (fast signup, quick activation) but churn after getting certified — SOC2 can be a one-time event, not ongoing
- **Segment B false negative:** Compliance leads may have slower onboarding and longer time-to-value, which could mask genuine PMF; adjust timelines accordingly
- **Blended metrics masking segment differences:** Always disaggregate; a blended 35% Sean Ellis score could hide a 50% Segment A score and a 20% Segment B score

---

## 7. Implementation Roadmap

### Phase 1: Baseline Measurement (Weeks 1–2)
- [ ] Segment existing users into Segment A and Segment B using company size and role data
- [ ] Calculate current retention curves by segment from 6-month cohort data
- [ ] Deploy Sean Ellis survey to all active users with 2+ weeks of usage
- [ ] Map onboarding funnel with segment-level conversion rates

### Phase 2: Deep Analysis (Weeks 3–4)
- [ ] Analyze survey results by segment (minimum 30 responses per segment)
- [ ] Build cohort retention tables segmented by user type
- [ ] Calculate time-to-value and engagement depth metrics per segment
- [ ] Estimate LTV and unit economics per segment

### Phase 3: Qualitative Validation (Weeks 4–5)
- [ ] Conduct 5–8 customer interviews per segment, focusing on "very disappointed" respondents
- [ ] Ask about alternatives, workflow integration, and willingness to expand
- [ ] Document quotes and patterns for each segment

### Phase 4: Decision and Action (Week 6)
- [ ] Complete the scoring matrix with data from Phases 1–3
- [ ] Present findings to leadership with segment recommendation
- [ ] Define 90-day plan for the chosen segment focus
- [ ] Establish ongoing PMF tracking cadence (monthly metrics review, quarterly survey)

---

## 8. Ongoing PMF Tracking

PMF is not a binary state — it can strengthen or erode. Establish a recurring measurement cadence:

| Cadence | Activity |
|---------|----------|
| Weekly | Monitor activation rate, onboarding completion, key engagement metrics |
| Monthly | Update retention cohort tables, review churn reasons, track NRR |
| Quarterly | Re-run Sean Ellis survey, conduct customer interviews, update scoring matrix |
| Semi-annually | Full PMF audit with segment re-evaluation |

**Leading indicators to watch:**
- Decline in Sean Ellis "very disappointed" percentage
- Retention curve steepening (previously flat curve starts declining)
- Increase in support tickets about core workflows
- Slowdown in organic/referral signups

**Lagging indicators:**
- Revenue churn exceeding 5% monthly
- NRR dropping below 100%
- CAC payback period lengthening

---

## 9. Key Risks and Mitigations

| Risk | Mitigation |
|------|-----------|
| Insufficient sample size per segment | Extend survey window; supplement with interviews; use directional signals rather than statistical significance |
| Self-serve founders inflate early metrics then churn | Track post-certification retention specifically; measure 90-day post-audit retention |
| Compliance leads have long evaluation cycles | Adjust measurement windows; use leading indicators (integration depth, team invites) as proxies |
| Survey non-response bias (happy users respond more) | Cross-reference behavioral data with survey data; track non-respondent retention separately |
| Blending segments obscures true PMF | Always maintain segment-level views; never report only aggregate numbers |

---

## 10. Summary

The core question — founders vs. compliance leads — should be answered by comparing these five signals across segments:

1. **Sean Ellis score** — Who would miss the product more?
2. **Retention curve shape** — Who sticks around?
3. **Onboarding completion and time-to-value** — Who gets value faster?
4. **Revenue quality (NRR, expansion)** — Who generates durable revenue?
5. **Qualitative signal** — Who describes the product as a must-have?

The segment that scores higher across these dimensions is where PMF is emerging, and where resources should concentrate. The 6-month cohort data provides enough history to draw meaningful conclusions if segmented properly. Act on the data within 6 weeks — in early-stage PMF, speed of learning matters as much as depth of analysis.
