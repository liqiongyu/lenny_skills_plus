# Pricing Strategy Pack: Analytics for Finance Teams

---

## 1) Context Snapshot

- **Decision:** Redesign packaging and pricing to increase expansion revenue (upsell/cross-sell within accounts) without hurting retention. This includes introducing a free tier, restructuring plans, and optimizing conversion mechanics.
- **Timeline:** Strategy ready for review now; phased rollout recommended over 8--12 weeks following WTP validation.
- **Audience / decision-makers:** Founding team / Head of Product / Head of Growth. Finance and Sales leadership for rollout sign-off.
- **Product + use case:** Analytics platform for finance teams. Helps finance professionals consolidate data, build reports, track KPIs, and surface anomalies across financial data sources. Primary job-to-be-done: "Give me a single, trustworthy view of our financial health so I can make decisions faster and reduce reporting errors."
- **Segments (primary 1--3):**
  1. **SMB finance teams** (1--5 analysts, <$50k deal size, self-serve buyers)
  2. **Mid-market finance orgs** (5--25 analysts, $50k--$200k potential deal size, hybrid buyers)
  3. **Enterprise finance departments** (25+ analysts, >$200k deal size, procurement-led)
- **Motion:** Self-serve + sales assist (hybrid). Self-serve for SMB acquisition and initial mid-market landing; sales assist for expansion, mid-market upgrades, and all enterprise deals.
- **Current pricing:** $99/user/mo flat rate, 14-day free trial. No free tier. No published annual discount. No explicit enterprise plan.
- **Objective metrics:** Increase net revenue expansion rate (target: +15--25% within 12 months) while holding logo retention at or above current baseline.
- **Guardrails:**
  - Must introduce and maintain a free tier.
  - SSO only on enterprise plan.
  - Retention (logo churn) must not increase by more than 1 percentage point during rollout.
  - No breaking changes to existing customer workflows during migration.
- **Constraints:**
  - Billing system must support per-seat pricing and usage-based add-ons.
  - Enterprise requires invoicing, SOC 2 compliance narrative, SSO (SAML/OIDC).
  - Self-serve payments capped at typical credit card limits (~$25k/year without procurement).

**"Success looks like":** Expansion revenue (measured as net dollar retention) increases meaningfully within 12 months; free tier generates a healthy self-serve pipeline; mid-market accounts naturally upgrade from Pro to Team to Enterprise as their usage grows; retention holds steady or improves.

---

## 2) Segment Map + Value Narrative

| Segment | Buyer | User | Primary Job-to-be-Done | Value Outcomes | Key Risks / Constraints | Notes |
|---|---|---|---|---|---|---|
| **SMB Finance** (1--5 analysts) | CFO / Controller / Founder | Finance analyst, sometimes the CFO themselves | "Replace spreadsheets with a reliable, always-current financial dashboard" | Save 5--10 hrs/week on reporting; reduce errors in board/investor reporting; faster close cycle | Price sensitivity is high; low switching cost (still close to spreadsheets); limited IT/security needs | Self-serve acquisition; land with 1--2 seats, expand as team grows |
| **Mid-Market Finance** (5--25 analysts) | VP Finance / Director of FP&A | FP&A analysts, accounting managers | "Consolidate multi-entity/multi-source financial data into one platform for the whole team" | Unified view across entities; audit-ready reporting; team collaboration on budgets and forecasts | Need team admin controls; some require SSO; may hit credit card limits on larger teams; procurement may get involved | Hybrid: self-serve land, sales assist for expansion beyond ~10 seats or when procurement enters |
| **Enterprise Finance** (25+ analysts) | CFO / VP Finance + Procurement | Large FP&A and accounting teams | "Standardize financial analytics across the organization with security, compliance, and governance" | Enterprise-grade compliance; custom integrations; SLA-backed uptime; reduced audit prep time | Must have SSO, invoicing, SOC 2, data residency options; long sales cycles; heavy onboarding | Sales-led; require dedicated onboarding, CSM, and custom contracts |

**Value narrative (cross-segment):** The core value is **trustworthy financial visibility that scales with team size and data complexity**. For SMBs, the value is time savings and error reduction over spreadsheets. For mid-market, it is cross-team collaboration and multi-entity consolidation. For enterprise, it is governance, compliance, and organizational standardization. Value increases as more users, data sources, and entities are connected -- this is the natural expansion driver.

**Who should NOT buy this:** Teams that need real-time transactional monitoring (not analytics), teams that only need a single static report once a quarter, or teams whose data lives in a single spreadsheet with no integration needs.

---

## 3) Value Metric Options

| Candidate Value Metric | Why It Matches Value | Pros | Cons / Risks | Best-Fit Segments | Notes |
|---|---|---|---|---|---|
| **Seats (users)** | More users = more team members getting value from analytics; scales with org size | Simple to understand and predict; industry-standard for B2B SaaS; easy to bill | Can suppress adoption (empty-seat anxiety); doesn't directly reflect data value; per-seat fatigue in market | All segments | Current metric; familiar to buyers |
| **Connected data sources** | More sources = richer, more consolidated view = more value | Directly tied to data consolidation value; grows naturally as customers mature; avoids seat-gating adoption | Harder for buyers to predict cost; may feel punitive for data-heavy small teams; billing complexity | Mid-market, Enterprise | Strong expansion signal but less intuitive for SMB |
| **Seats + usage-based add-ons (hybrid)** | Seats as base (predictable); add-ons for premium value (advanced reports, extra data sources, API calls) | Predictable base cost; expansion through natural usage growth; add-ons capture high-value use cases | More complex to communicate; billing system must support hybrid; requires clear add-on value | All segments (tiered) | **Recommended primary approach** |

**Recommendation: Seats as the primary value metric with usage-based add-ons for expansion.**

Rationale: Seats are simple, predictable, and familiar to finance buyers. The expansion revenue goal is best served by adding usage-based dimensions (connected data sources beyond plan limits, advanced report exports, API access) as paid add-ons. This avoids suppressing adoption with a pure usage model while creating natural expansion triggers as teams connect more data and use more advanced features.

### Packaging & Plans (Draft)

| Plan | Who It's For | Included Value | Limits (Aligned to Value) | Upgrade Triggers | Price (Draft) |
|---|---|---|---|---|---|
| **Free** | Individual analysts or small teams evaluating the product | Core dashboards, 2 data source connections, 1 user, basic reports, community support | 1 user, 2 data sources, 30-day data history, no API, no exports to PDF/Excel | Need more users, more data sources, longer history, export capability | $0 |
| **Pro** | SMB finance teams (1--10 users) | Full dashboards, 10 data source connections per user, 12-month data history, PDF/Excel exports, email support | 10 users max, 10 data sources, standard reports, email support (business hours) | Team grows past 10 users; needs advanced analytics, custom reports, or admin controls | $79/user/mo (annual) / $99/user/mo (monthly) |
| **Team** | Mid-market finance orgs (5--50 users) | Everything in Pro + advanced analytics, custom report builder, unlimited data sources, team admin controls, priority support | 50 users max, API access (rate-limited), team-level permissions, priority support | Need SSO, dedicated CSM, SLA, compliance docs, custom integrations, or 50+ users | $129/user/mo (annual) / $159/user/mo (monthly) |
| **Enterprise** | Enterprise finance departments (25+ users, procurement-led) | Everything in Team + SSO (SAML/OIDC), dedicated CSM, SLA, SOC 2 package, custom integrations, data residency options, invoicing | Unlimited users, unlimited data sources, custom API limits, audit log, advanced security | Ongoing: more entities, deeper integrations, professional services | Custom pricing (starting ~$149/user/mo annual; volume discounts at 50+, 100+ seats) |

**Add-ons (available on Pro and above):**

| Add-on | Who Buys It | Price Logic | Operational Notes |
|---|---|---|---|
| **Extra data source connections** (beyond plan limit) | Pro users hitting the 10-source cap | $15/additional source/mo | Self-serve purchase; natural expansion signal |
| **Advanced exports & scheduling** (automated report delivery, Slack/email scheduling) | Teams needing automated reporting | $19/user/mo | Available on Pro+; strong upsell from manual exports |
| **API access (Pro plan)** | Pro users needing programmatic access | $29/user/mo | Rate-limited; upgrade to Team for higher limits |
| **Extended data history** (beyond 12 months on Pro) | Compliance or trend analysis needs | $10/user/mo per additional 12-month block | |

### Self-Serve vs Sales-Led Boundary

| Boundary Trigger | Why It Forces Sales Assist | Detection Signal | Recommended Path | Notes |
|---|---|---|---|---|
| Team size > 10 users on Pro | Likely mid-market; may need admin controls, team billing | Account hits 10-seat limit on Pro | In-app prompt to explore Team plan; route to sales assist if >$15k ACV | Sales assist = guided upgrade, not gated |
| SSO / SAML requirement | Enterprise security policy; not available on self-serve plans | User requests SSO in settings or support | Route to Enterprise sales conversation | SSO is enterprise-only per constraint |
| Procurement / invoicing required | Credit card limits or company policy | User requests invoice or PO-based billing | Route to sales; offer annual invoicing on Team+ | Threshold: ~$25k/year |
| SOC 2 / compliance documentation | Enterprise trust requirement | User asks for compliance docs or security questionnaire | Route to Enterprise sales | Package SOC 2 narrative + DPA |
| Contract value > $25k/year | Exceeds typical self-serve credit card authority | Calculated from seats x price | Proactive sales outreach; offer annual contract with discount | |

---

## 4) WTP Evidence Plan

### Hypotheses (by segment/plan)

1. **Free tier hypothesis:** A meaningful free tier (1 user, 2 data sources) will generate 2--3x more self-serve signups than the current 14-day trial, and 15--20% of free users will convert to Pro within 90 days.
2. **Pro pricing hypothesis:** $79/user/mo (annual) is within WTP range for SMB finance teams currently paying $99/user/mo, and the lower entry point combined with add-ons will increase net revenue per account over 12 months.
3. **Team plan hypothesis:** Mid-market accounts currently on $99/user/mo will see the Team plan ($129/user/mo) as justified by advanced analytics, unlimited data sources, and admin controls -- particularly those already hitting data source limits.
4. **Add-on expansion hypothesis:** At least 30% of Pro accounts will purchase at least one add-on within 6 months, driving expansion revenue without a plan upgrade.
5. **Enterprise pricing hypothesis:** Enterprise accounts will accept $149+/user/mo for SSO, compliance, CSM, and SLA -- anchored to the value of audit-readiness and governance.

### What We Need to Learn First

- WTP **ranges** for each segment (not exact numbers).
- Which features are perceived as "must-have" vs "nice-to-have" at each tier.
- Whether "connected data sources" resonates as a value driver worth paying for incrementally.
- How sensitive mid-market buyers are to per-seat pricing at the $129 level vs the current $99.
- Whether the free tier is enough to activate (i.e., does 1 user + 2 data sources deliver an "aha" moment?).

### Target Participants

| Segment | Count | Roles | Recruitment Source |
|---|---|---|---|
| SMB (current customers) | 5--8 | CFOs, Controllers, Founders who also do finance | Existing customer list; filter by 1--5 seats |
| Mid-market (current customers) | 5--8 | VP Finance, Director of FP&A, FP&A managers | Existing customer list; filter by 5--25 seats |
| Mid-market (prospects / churned) | 3--5 | Same roles; include recent trial drop-offs | CRM pipeline + churned accounts from last 6 months |
| Enterprise (prospects or expansion) | 3--5 | VP Finance + Procurement contacts | Sales pipeline; existing accounts requesting SSO/compliance |

**Total: 16--26 interviews over 3--4 weeks.**

### Method Mix

1. **Qualitative interviews (primary, weeks 1--3):** 20--25 min calls with the prompts below. Goal: understand value perception, switching costs, price anchors, and feature prioritization.
2. **Van Westendorp price sensitivity survey (week 3--4):** Short survey (4 questions per plan) sent to broader customer base (target: 50--100 responses). Goal: identify acceptable price ranges by segment.
3. **Pilot offer (weeks 5--8):** Offer the new Team plan to 20--30 mid-market accounts at the proposed price, with a 60-day satisfaction guarantee. Measure conversion, feature adoption, and qualitative feedback.

### Interview Prompts (Copy/Paste)

- "Walk me through your reporting workflow before and after using our platform. Where does it save you the most time?"
- "What would happen to your team's work if you lost access to this tool tomorrow?"
- "What alternatives did you evaluate? What did they cost in time, money, and risk?"
- "If we offered a plan with unlimited data sources and advanced custom reports at a higher price, what would feel fair? What would feel too expensive?"
- "If we charged per connected data source (on top of per-seat), how would that feel? What number of sources would make you think twice?"
- "What would make you upgrade to a higher tier? What features would you absolutely need?"
- "If we offered a free version with limited data sources and one user, would you have started there instead of the trial? Would your team have adopted it?"

### Risks / Biases and Mitigations

| Risk | Mitigation |
|---|---|
| Anchoring bias (current $99 price) | Ask about value and alternatives before revealing proposed prices |
| Selection bias (only happy customers) | Include churned accounts and trial drop-offs in the sample |
| Small sample size for enterprise | Supplement with competitive pricing analysis and sales team input |
| Respondents say "cheaper is better" | Focus on value-based framing; use Van Westendorp to find "too cheap" floor |

---

## 5) Price-Point Options + Recommendation

### Option A: Conservative (minimal disruption)

| Plan | Price | Notes |
|---|---|---|
| Free | $0 (1 user, 2 sources) | New tier; low-cost acquisition funnel |
| Pro | $99/user/mo (monthly) / $89/user/mo (annual) | Keeps current price as monthly; adds annual discount |
| Team | $139/user/mo (monthly) / $119/user/mo (annual) | New tier; modest premium over Pro |
| Enterprise | Custom (floor ~$139/user/mo annual) | Sales-led; SSO, compliance, CSM |

- **Who wins:** Existing customers (no price increase); cautious approach for risk-averse teams.
- **Who loses:** Expansion revenue growth is slower; Team plan premium may not be enough to justify sales investment.
- **Risk:** May not move the needle on expansion revenue fast enough.

### Option B: Expansion-Optimized (Recommended)

| Plan | Price | Notes |
|---|---|---|
| Free | $0 (1 user, 2 sources) | New tier; acquisition engine |
| Pro | $99/user/mo (monthly) / $79/user/mo (annual) | Monthly stays at current; significant annual discount to lock in retention |
| Team | $159/user/mo (monthly) / $129/user/mo (annual) | Clear value step-up (unlimited sources, advanced analytics, admin) |
| Enterprise | Custom (floor ~$149/user/mo annual; volume discounts at 50+ and 100+ seats) | SSO, CSM, SLA, compliance |

- **Who wins:** SMB customers get better annual pricing and a free tier to expand within their org; mid-market accounts get a clear upgrade path with tangible value; expansion revenue increases through Team upgrades and add-ons.
- **Who loses:** Monthly-only buyers on Pro see no price change; some mid-market accounts may resist the step up to $129.
- **Risk:** Mid-market WTP for Team plan needs validation; mitigation via pilot offer (Step 4).

### Option C: Aggressive (maximum expansion, higher risk)

| Plan | Price | Notes |
|---|---|---|
| Free | $0 (1 user, 3 sources) | Slightly more generous free tier |
| Pro | $89/user/mo (monthly) / $69/user/mo (annual) | Lower entry point to maximize land |
| Team | $169/user/mo (monthly) / $139/user/mo (annual) | Higher premium; more features gated to Team |
| Enterprise | Custom (floor ~$159/user/mo annual) | Premium enterprise pricing |

- **Who wins:** Maximum self-serve volume; strong expansion delta from Pro to Team.
- **Who loses:** Pro revenue per user drops significantly; risk of revenue dip during transition.
- **Risk:** Revenue cannibalization on Pro; may train market to expect lower prices; harder to raise later.

### Recommendation: Option B (Expansion-Optimized)

**Rationale:**
1. **Retains current monthly pricing** for Pro ($99/mo), so no existing customer sees a price increase.
2. **Introduces a meaningful annual discount** ($79/user/mo annual = 20% off monthly), which improves retention and cash flow.
3. **Creates a clear expansion path** from Pro ($79--$99) to Team ($129--$159) driven by tangible value (unlimited data sources, advanced analytics, admin controls).
4. **Enterprise pricing** starts at $149/user/mo annual with volume discounts, capturing the value of SSO, compliance, and dedicated support.
5. **Free tier** at 1 user + 2 sources is enough to demonstrate value without cannibalizing Pro.
6. **Add-ons** on Pro (extra data sources, advanced exports, API) create expansion revenue even before a plan upgrade.

### Discount / Annual Policy (Draft)

- **Annual discount:** 20% off monthly price (applied at annual commitment). Communicated as "Save 20% with annual billing."
- **Multi-year discount:** Available for Enterprise only, negotiated by sales (up to 10% additional for 2-year commitment).
- **Volume discounts (Enterprise):** 10% at 50+ seats, 15% at 100+ seats, custom at 200+.
- **No ad hoc discounts on self-serve plans.** All discounts are structural (annual, volume) to preserve pricing integrity.
- **Sales assist triggers for discounting:** Any request for a discount outside the published structure routes to sales. Sales can offer migration credits (1--2 months free) for annual commitment upgrades, not permanent price reductions.

---

## 6) Conversion Mechanics Plan (Trial + Sampling)

### Trial Design

- **Free tier (permanent):** 1 user, 2 data sources, 30-day data history, basic reports. Always available. This replaces the "only way in" role of the 14-day trial.
- **Reverse trial on signup:** All new Free users get **14 days of Pro features** automatically upon signup. After 14 days, features downgrade to Free limits. This ensures every user experiences the premium value before deciding.
- **Upgrade prompts:** At day 7 (mid-trial) and day 12 (pre-expiry), show contextual prompts highlighting the Pro features they have used most. At downgrade, show a summary of what they are losing.

### Premium Value Sampling (In-Product)

| Premium Feature | Where It's Sampled | Sampling Mechanic | Upgrade Path |
|---|---|---|---|
| Advanced reports (custom builder) | Dashboard; "Create custom report" button is visible on Free | User can create 1 custom report during reverse trial; after trial, report remains visible (read-only) with "Upgrade to edit" | Pro plan |
| PDF/Excel export | Report view; "Export" button visible on all plans | Free users see export button with "Pro feature" badge; during reverse trial, exports work fully | Pro plan |
| Additional data sources | Data sources page; "Connect new source" | Free users see all available connectors; connecting source 3+ prompts upgrade (or works during reverse trial) | Pro plan |
| Advanced analytics (anomaly detection, forecasting) | Dashboard widgets | Free/Pro users see "Insights" widget with a preview of anomalies + "Unlock with Team plan" | Team plan |
| Team admin controls | Settings page | Visible but locked on Pro with "Available on Team" label | Team plan |
| SSO | Settings > Security | Visible on all plans with "Enterprise" label | Enterprise plan |

### Friction Reduction

- **No credit card required for Free tier.** Reduce signup friction to email + password only.
- **One-click upgrade from Free to Pro** with stored payment info (after initial purchase).
- **Annual billing default:** Present annual pricing as the default option (with monthly as the alternative). Frame as "Most popular: $79/user/mo billed annually."
- **Migration credit for existing trial users:** Any user currently on a 14-day trial gets an automatic 30-day extension on Pro features to ease the transition to the new model.

### Guardrails

- **Abuse controls for Free tier:** Rate limit API-like behavior (scraping, automated access); require email verification; limit to 1 free workspace per email domain for B2B.
- **Reverse trial abuse:** One reverse trial per account (tracked by email + domain). No re-trials without sales approval.
- **Free tier monitoring:** Track free-tier accounts that exceed typical usage patterns (high login frequency, many invited-but-blocked users) as signals for sales outreach, not for restriction.

### Success Metrics

| Metric | Target | Measurement Window |
|---|---|---|
| Free-to-Pro conversion rate | 15--20% within 90 days of signup | Monthly cohort tracking |
| Pro-to-Team upgrade rate | 10--15% of Pro accounts within 12 months | Quarterly cohort tracking |
| Reverse trial engagement | 60%+ of free users activate at least 2 Pro features during trial | Per-cohort, first 14 days |
| Add-on attach rate (Pro) | 30%+ of Pro accounts purchase at least 1 add-on within 6 months | Monthly tracking |
| Net dollar retention (all paid) | 110--120% | Quarterly |
| Logo retention (all paid) | Hold at or above current baseline (no more than +1pp churn) | Monthly |

### Experiment Backlog

| # | Experiment | Hypothesis | Segment | Primary Metric | Duration | Risk | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Reverse trial (14 days Pro) vs no reverse trial on Free | Reverse trial increases Free-to-Pro conversion by 30%+ vs Free-only | All new signups | Free-to-Pro conversion (90-day) | 8 weeks | May set expectation of perpetual free Pro access | A/B test; 50/50 split |
| 2 | Annual pricing as default vs monthly as default | Annual-default increases annual commitment rate by 20%+ | All new Pro purchasers | Annual vs monthly mix; total revenue per cohort | 6 weeks | Could reduce monthly conversion if sticker shock on annual | A/B test on pricing page |
| 3 | Data source add-on upsell prompt at limit | In-app prompt when hitting 10-source limit converts 25%+ to add-on purchase | Pro users at source limit | Add-on purchase rate | 6 weeks | May frustrate users if too aggressive | Triggered contextual prompt, not modal |
| 4 | Team plan pilot offer to mid-market | 20--30 mid-market accounts accept Team plan at $129/user/mo (annual) with satisfaction guarantee | Mid-market (5--25 seats) | Acceptance rate; feature adoption; NPS | 8 weeks (60-day guarantee) | Small sample; may create pricing expectations | Manual offer via CSM/sales assist |
| 5 | Sampling advanced analytics on Pro | Showing anomaly detection previews (locked) increases Team upgrade intent by 20%+ | Pro users with 6+ months tenure | Team upgrade rate; click-through on "Unlock" CTA | 8 weeks | May create frustration if perceived as teaser-ware | Feature flag; measure clicks + upgrades |

---

## 7) Rollout + Instrumentation

### Rollout Approach (Phased, 8--12 Weeks)

| Phase | Week | Actions | Audience |
|---|---|---|---|
| **0: Internal prep** | Weeks 1--2 | Finalize plan structure in billing system; build pricing page; update in-app plan UI; train sales and support teams; draft migration comms | Internal |
| **1: New signups only** | Weeks 3--5 | Launch Free + Pro + Team plans for **new signups only**. Enterprise available via "Contact Sales." Existing customers remain on current plan. Run reverse trial experiment (Exp #1). | New users |
| **2: Existing customer migration (opt-in)** | Weeks 6--8 | Invite existing customers to migrate to new plans via email + in-app banner. Offer migration incentives (1 month free on annual for early adopters). Grandfathering: existing customers keep current pricing for 6 months if they do not migrate. | Existing customers |
| **3: Full migration** | Weeks 9--12 | All remaining customers migrated to new plan structure at their current or nearest-equivalent plan. Grandfathered pricing expires. Enterprise outreach for accounts meeting sales-led criteria. | All |

### Migration Rules

- **Grandfathering:** Existing customers on $99/user/mo are grandfathered for 6 months from Phase 2 launch. After 6 months, they are migrated to Pro (monthly) at $99/user/mo (same price) or Team if they use features that require it.
- **Proration:** Mid-cycle migrations are prorated. Upgrades are prorated immediately; downgrades take effect at next billing cycle.
- **Contract handling:** Any existing annual contracts are honored through their term. New pricing applies at renewal.
- **No forced downgrades:** If a customer is on $99/user/mo and uses features now in the Team plan (e.g., >10 data sources), they are offered Team pricing at a loyalty rate ($119/user/mo annual) for the first year.

### Communications Plan

| Channel | Timing | Message |
|---|---|---|
| Email (existing customers) | Phase 2 launch | "We're introducing new plans designed to grow with your team. Your current plan and pricing are guaranteed for 6 months. Here's what's new..." |
| In-app banner | Phase 2 launch | "New plans available -- see what's included" with link to comparison page |
| Blog post | Phase 1 launch | Public announcement of new pricing philosophy, free tier, and plan structure |
| Sales enablement deck | Phase 0 | Internal: positioning, objection handling, migration FAQ |
| Support knowledge base | Phase 0 | Updated FAQ: "What's changing?", "Will my price go up?", "How do I migrate?" |
| CSM outreach (mid-market + enterprise) | Phase 2 | Personal outreach to accounts with 10+ seats; offer guided migration and Team/Enterprise consultation |

### Instrumentation (Events + Dashboards)

**Key events to track:**
- `plan_viewed` (which plan, from where)
- `plan_selected` (plan, annual vs monthly, self-serve vs sales)
- `trial_started` (reverse trial activation)
- `trial_feature_used` (which Pro feature, how many times during trial)
- `trial_ended` (converted vs downgraded)
- `addon_purchased` (which add-on, from what plan)
- `upgrade_initiated` / `upgrade_completed` (from/to plan)
- `downgrade_initiated` / `downgrade_completed`
- `migration_opted_in` / `migration_completed`
- `sales_assist_triggered` (trigger reason: seat count, SSO request, invoice request, etc.)

**Dashboard:**
- Daily: signups (free vs paid), trial activations, conversions
- Weekly: cohort conversion rates (free-to-Pro, Pro-to-Team), add-on attach rates, revenue by plan
- Monthly: net dollar retention, logo retention, ARPA by segment, expansion revenue vs contraction

### KPIs and Guardrails

| KPI | Target | Guardrail (Pause/Rollback if...) |
|---|---|---|
| Free-to-Pro conversion (90-day cohort) | 15--20% | < 8% after 6 weeks of data |
| Net dollar retention (paid) | 110--120% | Drops below 100% for any 2 consecutive months |
| Logo retention (paid) | Hold baseline | Increases by > 1pp for any 2 consecutive months |
| ARPA (paid accounts) | Increase by 10--15% within 12 months | Decreases by > 5% vs pre-launch baseline |
| Support ticket volume (pricing-related) | < 5% of total tickets | > 15% of total tickets in any month |
| Payment failure rate | Hold baseline | Increases by > 2pp |

### Rollback Criteria + Playbook

**Trigger rollback discussion if any guardrail is breached for 2+ consecutive measurement periods.**

**Rollback playbook:**
1. **Pause new-signup enrollment** on the new plan structure; revert pricing page to legacy plans.
2. **Do not force-migrate** any additional existing customers.
3. **Communicate to affected users:** "We're refining our plans based on your feedback. Your current plan is unchanged."
4. **Diagnose:** Is the issue with pricing (too high/low), packaging (wrong feature gating), conversion mechanics (reverse trial not working), or communication (confusion)?
5. **Iterate:** Adjust the specific failing element (not the entire strategy) and re-launch to a smaller cohort.
6. **Full rollback (last resort):** Revert all new customers to the closest legacy plan equivalent. Honor any commitments made under new pricing.

---

## 8) Pricing Review Cadence

- **Cadence:** Review pricing and packaging every **6 months** for the first 18 months (3 reviews); then every **12 months** once stable.
- **Triggers to revisit sooner:**
  - Major new feature launch that changes the value delivered (e.g., AI-powered forecasting)
  - Net dollar retention drops below 105% for 2 consecutive quarters
  - Conversion rates (free-to-Pro or Pro-to-Team) drift more than 20% from targets
  - Competitive shift (major competitor changes pricing or enters market)
  - Significant segment shift (e.g., enterprise becomes >50% of revenue)
- **Owner(s):** Head of Product (pricing decisions) + Head of Growth (metrics and experimentation) + Finance (revenue impact modeling)
- **Required inputs for review:**
  - Conversion funnel metrics by plan (trailing 90 days)
  - Net dollar retention and expansion breakdown
  - WTP research refresh (at least 5--10 customer interviews per review)
  - Competitive pricing scan
  - Sales/support feedback summary
- **Decision forum:** Pricing review meeting with Product, Growth, Finance, and Sales leadership. Output is a written decision memo (ship, iterate, or revisit in 90 days).

---

## 9) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Free tier attracts low-quality users who never convert, increasing infrastructure cost | Medium | Medium | Monitor free-tier cost-to-serve monthly; set infrastructure budget guardrails; tighten free-tier limits if cost exceeds threshold |
| Mid-market WTP for Team plan ($129/user/mo) is lower than hypothesized | Medium | High | Validate with pilot offer (Experiment #4) before full rollout; have Option A pricing as fallback |
| Existing customers perceive new packaging as a price increase (even if grandfathered) | Medium | High | Proactive comms emphasizing "your price doesn't change"; loyalty rate for Team plan; 6-month grandfathering |
| Reverse trial sets expectation of free Pro access; increases churn when trial ends | Low--Medium | Medium | Clear messaging during trial ("Your Pro trial ends in X days"); strong downgrade experience showing what they keep on Free |
| Add-on complexity confuses self-serve buyers | Low | Medium | Limit to 3--4 add-ons at launch; test messaging with 5--10 users before launch; simplify over time |
| Enterprise pricing floor ($149/user/mo) is below market for compliance/SSO value | Low | Low | Enterprise is custom/negotiated; floor is a starting point; adjust based on early deals |
| Sales team not ready for hybrid motion (self-serve land, sales-assisted expand) | Medium | Medium | Phase 0 enablement; define clear handoff triggers; CRM alerts for expansion signals |

### Open Questions

1. **What is the current net dollar retention and logo retention baseline?** (Needed to set guardrails accurately.)
2. **What is the current free-trial-to-paid conversion rate?** (Needed to benchmark reverse trial experiment.)
3. **How many current customers use >10 data sources?** (Determines how many will be affected by Pro limits and need Team plan migration.)
4. **What is the current annual vs monthly billing mix?** (Affects revenue impact modeling for the 20% annual discount.)
5. **Does the billing system support usage-based add-on metering today, or is engineering work needed?** (May affect timeline.)
6. **Are there any existing enterprise contracts with custom pricing that need special handling?** (Migration complexity.)
7. **What is the cost-to-serve for a free-tier user?** (Determines sustainability of free tier at scale.)

### Next Steps

| # | Action | Owner | Target Date |
|---|---|---|---|
| 1 | Validate WTP hypotheses: conduct 16--26 customer interviews (per WTP plan above) | Head of Growth + Product | Weeks 1--4 |
| 2 | Run Van Westendorp survey to broader customer base (50--100 responses) | Growth team | Weeks 3--4 |
| 3 | Finalize billing system requirements for new plans + add-ons; confirm engineering timeline | Engineering + Finance | Weeks 1--2 |
| 4 | Build and test new pricing page and in-app plan comparison | Product + Design | Weeks 2--4 |
| 5 | Prepare sales enablement materials and migration FAQ | Sales + Product Marketing | Weeks 3--4 |
| 6 | Launch Phase 1 (new signups only) with reverse trial experiment | Growth team | Week 5 |
| 7 | Analyze Phase 1 results; decide on Phase 2 migration timing and approach | Product + Growth + Finance | Week 8 |
| 8 | Run Team plan pilot offer to 20--30 mid-market accounts | Sales + CSM | Weeks 5--8 |
| 9 | First pricing review meeting | Product + Growth + Finance + Sales | Month 6 |

### Validation Plan (What to Learn Next, By When)

- **By Week 4:** WTP ranges for Pro, Team, and Enterprise across segments (interviews + survey). Confirm or adjust price points before Phase 1 launch.
- **By Week 8:** Reverse trial conversion data (Experiment #1) and annual-vs-monthly default data (Experiment #2). Confirm or adjust conversion mechanics before Phase 2.
- **By Week 12:** Team plan pilot results (Experiment #4). Confirm Team pricing and feature gating before full migration.
- **By Month 6:** Full-funnel metrics across all plans. First pricing review meeting to assess expansion revenue impact and decide on iteration.

---

## Quality Gate: Checklist Verification

| Checklist Section | Status | Notes |
|---|---|---|
| **A) Scope + decision quality** | Pass | Decision (increase expansion revenue via new packaging), timeline (8--12 week rollout), audience (product/growth/finance leadership), and constraints (free tier, SSO on enterprise) are explicit. Blast radius addressed via phased rollout and grandfathering. |
| **B) Value metric + "price = value" coherence** | Pass | Seats + usage add-ons selected as primary metric with rationale. Each plan has a clear "who it's for" and upgrade path tied to value outcomes. Alternates (data sources, hybrid) evaluated. |
| **C) Evidence + WTP plan** | Pass | Concrete WTP plan with 16--26 interviews, Van Westendorp survey, and pilot offer. Hypotheses are explicit. Unknowns labeled in Open Questions. |
| **D) Self-serve vs sales-led boundary** | Pass | Boundary table defines triggers (10+ seats, SSO, invoicing, >$25k ACV). Sales assist triggers are operationally specific. |
| **E) Conversion mechanics** | Pass | Reverse trial, premium sampling, and add-on upsells designed. Abuse controls defined. Success metrics include retention + expansion, not just conversion. |
| **F) Rollout + measurement** | Pass | Phased rollout (3 phases, 8--12 weeks). Migration rules, grandfathering, comms plan, instrumentation, KPIs, guardrails, and rollback playbook included. |
| **G) Iteration cadence** | Pass | 6-month review cadence (first 18 months), then annual. Triggers, owners, required inputs, and decision forum defined. |
| **H) Required final section** | Pass | Risks, Open questions, and Next steps all included with specifics. |

## Quality Gate: Rubric Scoring

| Category | Score (1--5) | Rationale |
|---|---|---|
| 1) Decision clarity | **5** | Decision, timeline, audience, constraints, and success criteria are all explicit and specific. |
| 2) Segment + value narrative | **4** | Segment map distinguishes buyer vs user; value is outcome-based; switching costs identified. Minor gap: exclusion criteria could be more segment-specific. |
| 3) Pricing architecture coherence | **5** | Value metric aligns to delivered value with rationale; plans have clear "who it's for"; upgrade drivers are explicit; self-serve vs sales-led boundary is defined. |
| 4) Evidence + WTP plan | **4** | Strong triangulation plan (qual interviews + Van Westendorp survey + pilot offer). Hypotheses explicit. Minor gap: no existing quantitative evidence was provided, so baseline metrics are assumed. |
| 5) Conversion mechanics + experimentation | **5** | Premium value demonstrated in-product via reverse trial and sampling. Experiments prioritized with metrics, guardrails, and abuse controls. |
| 6) Rollout + operational feasibility | **5** | Phased rollout with migration rules, grandfathering, comms plan, enablement, rollback criteria and playbook. |
| 7) Risk management + completeness | **4** | Risks are specific with mitigations; open questions are listed; next steps have owners and timelines. Minor gap: some open questions depend on data the team needs to provide. |

**Overall: 4.6/5 average. Ship-ready for review; pending WTP validation before execution.**
