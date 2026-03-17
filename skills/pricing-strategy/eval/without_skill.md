# Pricing Strategy: Analytics Platform for Finance Teams

## 1. Executive Summary

This document outlines a comprehensive pricing strategy for a finance-focused analytics platform currently priced at $99/user/month with a 14-day trial. The primary objective is to increase expansion revenue without degrading retention. The strategy introduces a four-tier model (Free, Starter, Professional, Enterprise) anchored around a value metric of "seats + data connections," with built-in self-serve upgrade paths and sales-assist triggers to drive natural account expansion.

---

## 2. Current State Assessment

### What We Know
- **Current pricing:** $99/user/month, flat rate
- **Trial:** 14-day free trial
- **Motion:** Self-serve + sales assist (hybrid)
- **Constraints:** Must maintain a free tier; SSO restricted to Enterprise

### Problems with the Current Model
1. **No expansion lever:** A single flat tier at $99/user gives no room for customers to grow into higher-value plans. Revenue only grows linearly with headcount.
2. **High entry barrier:** $99/user is a significant commitment for a first purchase, especially for small finance teams exploring tools. The 14-day trial creates urgency but not enough time to demonstrate ROI for a finance workflow (reporting cycles are often monthly or quarterly).
3. **No free tier:** The constraint requires one, and its absence today means lost top-of-funnel volume.
4. **No price discrimination:** Power users (CFOs running board-level dashboards) pay the same as analysts running ad-hoc queries. This leaves money on the table at the top end and prices out potential users at the bottom.

---

## 3. Strategic Principles

| Principle | Rationale |
|---|---|
| **Land cheap, expand on value** | Free and low-cost tiers acquire users; usage-based levers capture value as they grow. |
| **Align price to value delivered** | Finance teams derive value from data connections, reporting depth, and collaboration. Price should track these. |
| **Reduce friction to upgrade** | Self-serve upgrades for predictable tier jumps; sales assist only for Enterprise or custom needs. |
| **Protect retention with generous base** | Free and Starter tiers should be genuinely useful so users stay engaged and eventually expand. |
| **Gate on sophistication, not on crippling** | Lower tiers should limit scale/advanced features, not make the core product frustrating. |

---

## 4. Proposed Tier Structure

### Tier Overview

| Dimension | Free | Starter | Professional | Enterprise |
|---|---|---|---|---|
| **Price** | $0 | $49/user/mo | $99/user/mo | Custom (starting ~$149/user/mo) |
| **Billing** | N/A | Monthly or Annual (15% discount) | Monthly or Annual (15% discount) | Annual only |
| **Target User** | Individual analyst, evaluator | Small finance team (2-5 users) | Mid-market finance org (5-25 users) | Large/regulated finance org (25+ users) |
| **Data Connections** | 2 | 10 | Unlimited | Unlimited + custom connectors |
| **Dashboards** | 3 | 15 | Unlimited | Unlimited |
| **Historical Data** | 3 months | 12 months | 36 months | Unlimited |
| **Refresh Frequency** | Daily | Hourly | Real-time | Real-time + streaming |
| **Users** | 1 | Up to 10 | Up to 50 | Unlimited |
| **Exports** | CSV only | CSV + Excel | CSV + Excel + PDF + API | All + custom formats |
| **Collaboration** | View-only sharing | Comment + share | Full collaboration + approvals | Workflow automation + approvals |
| **Support** | Community | Email (48h SLA) | Priority email + chat (4h SLA) | Dedicated CSM + phone (1h SLA) |
| **SSO/SAML** | No | No | No | Yes |
| **Audit Logs** | No | No | Basic | Advanced + SIEM integration |
| **Custom Roles** | No | No | Basic roles | Granular RBAC |
| **SLA** | None | 99.5% | 99.9% | 99.95% + BAA available |

### Rationale for Each Tier

**Free Tier**
- Serves as the top-of-funnel acquisition engine. Finance professionals can connect a couple of data sources, build a few dashboards, and experience the core value loop (connect data -> build dashboard -> get insight).
- The 3-month historical data limit is the natural expansion trigger: once a user wants to do quarter-over-quarter or year-over-year analysis (the bread and butter of finance), they hit the limit and need to upgrade.
- Single-user keeps it simple and prevents abuse as a team tool.

**Starter ($49/user/mo)**
- This is the new "easy yes" for small finance teams. At half the current price point, it dramatically lowers the barrier to a paid commitment.
- 10 data connections and 12 months of history cover the vast majority of small-team needs (bank feeds, ERP, a couple of SaaS tools).
- The per-user model means revenue grows naturally as the team adds members.

**Professional ($99/user/mo)**
- This is the current price point repositioned as a premium offering with significantly more value: unlimited dashboards, real-time data, 3 years of history, API access, and collaboration features.
- Existing customers migrate here with no price increase but gain a richer feature set, protecting retention.
- The collaboration and approval features are critical for mid-market finance teams that need sign-off workflows.

**Enterprise (Custom, ~$149+/user/mo)**
- SSO/SAML lives here per the constraint.
- Custom pricing allows for volume discounts, multi-year commitments, and professional services bundling.
- Audit logs, SIEM integration, granular RBAC, and compliance features justify the premium for regulated industries (banking, insurance, public companies).

---

## 5. Expansion Revenue Mechanics

### 5.1 Seat-Based Expansion (Primary Lever)

**How it works:** As finance teams prove ROI, they naturally add more users -- analysts, controllers, FP&A managers, and eventually the CFO and business partners.

**Tactics:**
- **Viewer seats (free):** Allow unlimited free viewer seats on Starter+ plans. This gets more eyeballs on dashboards, creates internal champions, and generates upgrade pressure when viewers want to build their own analyses.
- **Self-serve seat addition:** One-click seat purchase in the billing portal. No sales call needed for Starter and Professional.
- **Usage nudges:** When a team regularly shares dashboards with non-users, prompt them: "5 colleagues viewed your dashboards this week. Add them as users to enable collaboration."

### 5.2 Tier Upgrade Expansion (Secondary Lever)

**How it works:** Users hit natural limits on their current tier and upgrade to unlock more capability.

**Key triggers and nudges:**
| Current Tier | Trigger | Nudge Message | Target Tier |
|---|---|---|---|
| Free | Tries to add 3rd data connection | "Connect all your finance data. Upgrade to Starter." | Starter |
| Free | Hits 3-month history wall | "Unlock 12 months of history for trend analysis." | Starter |
| Free | Tries to invite a teammate | "Collaborate with your team on Starter." | Starter |
| Starter | Hits 10 data connection limit | "Connect unlimited sources on Professional." | Professional |
| Starter | Tries to use API or real-time data | "Get real-time data and API access on Professional." | Professional |
| Starter | Team grows past 10 users | "Scale your team with Professional (up to 50 users)." | Professional |
| Professional | Needs SSO | "Secure access with SSO on Enterprise." | Enterprise |
| Professional | Needs audit logs or compliance | "Meet compliance requirements with Enterprise." | Enterprise |
| Professional | Team exceeds 50 users | "Unlimited users on Enterprise. Let's talk." | Enterprise |

**Self-serve vs. sales-assist:**
- Free -> Starter: 100% self-serve. Credit card upgrade in-app.
- Starter -> Professional: Self-serve with optional sales assist. In-app upgrade, but also trigger a "congrats on growing" email from an AE if account hits certain usage thresholds.
- Professional -> Enterprise: Sales-assisted. "Contact sales" flow, but with a pre-filled form showing current usage so the conversation starts warm.

### 5.3 Usage-Based Add-Ons (Tertiary Lever)

Offer optional add-ons that let customers expand spend without changing tiers:

| Add-On | Price | Available On |
|---|---|---|
| Additional data connections (pack of 5) | $25/mo | Starter |
| Extended history (additional 12 months) | $20/user/mo | Starter, Professional |
| Advanced analytics (forecasting, anomaly detection) | $30/user/mo | Professional, Enterprise |
| Premium connectors (custom ERP, legacy systems) | $50/connector/mo | Professional, Enterprise |
| Dedicated compute (faster queries) | $100/mo | Professional, Enterprise |
| Data warehouse export | $75/mo | Professional, Enterprise |

**Why add-ons matter for expansion:** They give customers a way to increase spend incrementally without the psychological friction of a full tier upgrade. A Starter customer who needs 15 data connections can buy one add-on pack ($25/mo) instead of jumping to Professional ($99/user/mo for all users).

### 5.4 Annual Commitment Expansion

- **15% discount for annual billing** on Starter and Professional.
- **Multi-year discounts (20-25%)** available on Enterprise with 2-3 year commitments.
- Position annual plans as "locking in your rate" given planned price increases for new customers.
- Offer a "true-up" model on Enterprise: commit to a seat baseline, true up quarterly for seats above the commitment.

---

## 6. Migration Plan for Existing Customers

### Principles
1. No existing customer pays more for what they currently get.
2. Every existing customer gets more value at their current price.
3. Migration is an opportunity to deepen relationships, not a risk to retention.

### Execution

| Segment | Action | Communication |
|---|---|---|
| Active customers on $99/mo | Auto-migrate to Professional tier | "Great news: you now have access to Professional features at no extra cost, including unlimited dashboards, real-time data, and 3 years of history." |
| Low-usage customers ($99/mo, <3 data connections) | Offer option to downgrade to Starter at $49/mo | "We noticed you're using a few data connections. Our new Starter plan at $49/user/mo might be a better fit -- and you can always upgrade later." |
| High-usage customers (>25 users) | Proactive outreach for Enterprise | "Your team has grown significantly. Let's discuss Enterprise features like SSO and dedicated support that can help at your scale." |
| Trial users in pipeline | Convert to new tier structure | Extend trial to 30 days (see below) and let them choose a tier. |

### Retention Safeguard
- **90-day price protection:** Any customer who feels negatively impacted can request a rate hold for 90 days while they evaluate.
- **Downgrade path:** Make it easy to move from Professional to Starter. A customer who stays at $49/mo is better than a churned customer at $0.

---

## 7. Trial Strategy Overhaul

### Current Problem
A 14-day trial is too short for finance teams. Finance workflows are cyclical (month-end close, quarterly reporting). A 14-day trial might not coincide with a period when the tool's value is most apparent.

### New Approach

| Element | New Design |
|---|---|
| **Free tier** | Replaces the trial as the primary evaluation vehicle. No time limit. |
| **Professional trial** | 30 days (up from 14). Available to Free and Starter users. Self-serve activation. |
| **Enterprise trial** | 45 days with sales engagement. Includes onboarding call. |
| **Trial-to-paid conversion nudges** | Day 7: "Here's what you've built so far." Day 14: "Your team has saved X hours." Day 21: "Your trial is ending in 9 days. Here's what you'd lose." Day 28: "2 days left. Upgrade now to keep everything." |
| **Trial extension policy** | Sales can grant one 15-day extension on Professional; Enterprise trials can extend up to 90 days with VP approval. |

---

## 8. Packaging for Expansion: Feature Gating Philosophy

### Gate Generously at the Bottom, Gate Firmly at the Top

The goal is to make Free and Starter genuinely useful so users build habits and data dependencies, then gate the features that matter most to growing, sophisticated teams.

**Never gate (available on all tiers including Free):**
- Core analytics engine (queries, calculations, formulas)
- Basic visualizations (charts, tables, graphs)
- Data connection quality (all tiers get the same connector reliability)
- Mobile access
- Basic alerts

**Gate on scale (tier limits):**
- Number of data connections
- Historical data depth
- Number of dashboards
- Team size
- Refresh frequency

**Gate on sophistication (tier features):**
- API access (Professional+)
- Custom branding (Enterprise)
- Approval workflows (Professional+)
- Forecasting / ML features (add-on)
- Custom roles and permissions (Professional+ for basic, Enterprise for granular)
- Audit and compliance (Enterprise)

**Gate on security/compliance (Enterprise only):**
- SSO/SAML
- SIEM integration
- Advanced audit logs
- Data residency controls
- BAA / compliance certifications

---

## 9. Pricing Page and Positioning

### Positioning by Tier

| Tier | Headline | Subhead |
|---|---|---|
| Free | **Get Started** | "Connect your data and build your first dashboard in minutes." |
| Starter | **Grow Your Practice** | "Everything a small finance team needs to replace spreadsheets." |
| Professional | **Scale Your Impact** | "Advanced analytics and collaboration for data-driven finance orgs." |
| Enterprise | **Control and Compliance** | "Security, governance, and support for regulated finance teams." |

### Pricing Page Best Practices
- **Highlight Professional as "Most Popular"** to anchor buyers toward the highest self-serve tier.
- **Show annual pricing by default** with a toggle to monthly, encouraging longer commitments.
- **Include a comparison table** below the tier cards for detailed feature comparison.
- **Add social proof per tier:** "Trusted by 500+ finance teams" on Starter, "Used by CFOs at [logos]" on Professional, compliance badges on Enterprise.
- **FAQ section** addressing: "What happens when I hit my limit?", "Can I switch plans?", "How does billing work when I add users mid-cycle?"

---

## 10. Sales-Assist Triggers and Handoff

### Self-Serve Boundaries
| Action | Motion |
|---|---|
| Sign up for Free | 100% self-serve |
| Upgrade Free -> Starter | 100% self-serve |
| Add seats on Starter (up to 10) | 100% self-serve |
| Upgrade Starter -> Professional | Self-serve with AE notification |
| Add seats on Professional (up to 50) | Self-serve |
| Any Enterprise inquiry | Sales-assisted |
| Add-on purchase | Self-serve |
| Downgrade any tier | Self-serve with retention offer |

### Product-Qualified Lead (PQL) Signals
Trigger a sales-assist outreach when a self-serve account exhibits:
- 5+ active users on Starter (approaching limit)
- 8+ data connections on Starter (approaching limit)
- 20+ active users on Professional (potential Enterprise candidate)
- Repeated hits against a tier limit (3+ times in 30 days)
- Usage of >80% of any tier limit
- Admin searches for "SSO," "SAML," or "audit" in help docs
- Account created by someone with a title containing "VP," "Director," or "CFO" (enriched via Clearbit or similar)

### Handoff Protocol
1. PQL signal fires.
2. AE receives Slack notification with account context (tier, usage, company size, user roles).
3. AE sends personalized email within 24 hours referencing specific usage patterns.
4. If no response in 3 days, trigger an in-app message from the AE.
5. AE offers a "strategy session" (not a "demo") to discuss how to get more value from the platform.

---

## 11. Financial Modeling

### Assumptions
- Current ARPU: $99/user/mo
- Current customer base: hypothetical 1,000 accounts, average 8 users each

### Projected Impact (12-Month Horizon)

| Metric | Current | Projected | Change |
|---|---|---|---|
| **Avg. users per account** | 8 | 12 | +50% (viewer seats drive adoption) |
| **Blended ARPU** | $99 | $89 | -10% (mix shift toward Starter) |
| **Avg. revenue per account** | $792/mo | $1,068/mo | +35% |
| **New account acquisition** | Baseline | +40% | Free tier drives top-of-funnel |
| **Gross retention** | Baseline | +3-5pp | Better tier fit reduces churn |
| **Net revenue retention** | ~105% | ~120% | Expansion from seats + tier upgrades + add-ons |
| **Add-on attach rate** | 0% | 15% | New revenue stream |

### Revenue Composition Shift
- **Before:** 100% seat-based, single tier
- **After (12 months):**
  - 55% seat-based (Professional + Starter)
  - 20% tier upgrade revenue (Free->Starter->Professional)
  - 10% add-on revenue
  - 15% Enterprise contracts

### Break-Even Analysis
The introduction of the Free tier and the lower-priced Starter tier will initially dilute ARPU. The model breaks even when:
- Free-to-Starter conversion rate exceeds 8% (benchmark for B2B freemium: 5-15%)
- Average seats per paid account reaches 10 (currently 8)
- At least 10% of Professional accounts upgrade to Enterprise within 18 months

---

## 12. Competitive Positioning

### Price Anchoring
- Position against spreadsheet alternatives (Excel + manual processes): "Replace 40 hours/month of manual reporting for less than the cost of one analyst's overtime."
- Position against enterprise BI tools (Tableau, Power BI): "Purpose-built for finance. No IT department required. 10x faster time-to-insight."
- Position against horizontal analytics (Looker, Mode): "The only analytics platform that speaks finance: GAAP, IFRS, cash flow, variance analysis out of the box."

### Defensible Premium
Justify the $99 Professional price point (and $149+ Enterprise) by emphasizing:
- Finance-specific data models and templates
- Pre-built connectors for ERP, banking, and accounting systems
- Compliance and audit capabilities
- Finance-specific AI/ML (forecasting, anomaly detection)

---

## 13. Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)
- [ ] Finalize tier definitions and feature gating logic
- [ ] Build billing infrastructure for multi-tier support
- [ ] Implement free tier with appropriate limits
- [ ] Design and build pricing page
- [ ] Create migration communication plan
- [ ] Set up PQL scoring and alerting

### Phase 2: Soft Launch (Weeks 5-8)
- [ ] Launch new pricing for new customers only
- [ ] A/B test pricing page (emphasize Professional vs. Starter)
- [ ] Monitor free tier sign-up velocity and activation rates
- [ ] Train sales team on new tier structure and expansion playbook
- [ ] Implement self-serve upgrade flows in-product

### Phase 3: Migration (Weeks 9-12)
- [ ] Begin existing customer migration in cohorts
- [ ] Execute proactive Enterprise outreach for high-usage accounts
- [ ] Offer voluntary downgrades to low-usage accounts
- [ ] Monitor retention closely (daily cohort analysis)

### Phase 4: Optimization (Weeks 13-24)
- [ ] Launch add-on marketplace
- [ ] Implement expansion nudges and in-app upgrade prompts
- [ ] Analyze conversion funnel: Free -> Starter -> Professional -> Enterprise
- [ ] Tune PQL signals based on actual conversion data
- [ ] Conduct first price sensitivity analysis on Starter tier
- [ ] Evaluate usage-based pricing for high-volume Enterprise accounts

---

## 14. Metrics and Success Criteria

### Primary KPIs (Track Weekly)
| Metric | Target (6 months) | Target (12 months) |
|---|---|---|
| Net Revenue Retention | 115% | 120% |
| Expansion Revenue as % of Total | 25% | 35% |
| Free-to-Paid Conversion Rate | 6% | 10% |
| Average Seats per Paid Account | 10 | 12 |
| Gross Revenue Retention | Current +2pp | Current +4pp |

### Secondary KPIs (Track Monthly)
| Metric | Target |
|---|---|
| Time to first paid conversion (from Free sign-up) | <45 days |
| Self-serve upgrade rate (no sales touch) | >60% of upgrades |
| Add-on attach rate | 15% of Professional accounts |
| Pricing page conversion rate | >4% visitor-to-signup |
| Tier distribution (Starter : Professional : Enterprise) | 50 : 35 : 15 |

### Guardrail Metrics (Alert if Breached)
- Gross churn rate increases by more than 1 percentage point in any month
- ARPU drops below $75 without corresponding volume increase
- Free tier accounts exceed 10x paid accounts (indicates monetization problem)
- Customer satisfaction (NPS/CSAT) drops by more than 5 points

---

## 15. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Existing customers perceive downgrade | Medium | High | Generous migration: everyone gets more at same price. Proactive communication. |
| Free tier attracts non-ICP users (noise) | Medium | Low | Gate free tier behind work email. Limit to finance-relevant connectors. |
| Starter cannibalizes Professional | Medium | Medium | Monitor closely. Ensure Professional has clear "must-have" features for teams >5. Adjust Starter limits if needed. |
| Enterprise deals slow down due to self-serve | Low | Medium | Set PQL triggers aggressively. Ensure sales team is incented on expansion, not just new logos. |
| Competitor undercuts on price | Medium | Medium | Compete on value and specialization, not price. Finance specificity is the moat. |
| Add-ons create billing complexity | Low | Low | Start with 2-3 add-ons only. Expand based on demand. Keep billing UI simple. |

---

## 16. Summary of Key Decisions

1. **Move from one tier ($99) to four tiers (Free / $49 / $99 / Custom).**
2. **Introduce a permanent Free tier** that replaces the 14-day trial as the primary acquisition vehicle.
3. **Extend trials to 30 days** for Professional and 45 days for Enterprise.
4. **Create three expansion levers:** seat growth, tier upgrades, and usage-based add-ons.
5. **Implement free viewer seats** on all paid plans to drive organic adoption within accounts.
6. **Gate SSO on Enterprise** per constraint; gate scale on lower tiers, sophistication on upper tiers.
7. **Protect existing customers:** auto-migrate to Professional at current price with more features.
8. **Launch add-on marketplace** in Phase 4 after validating core tier structure.
9. **Target 120% net revenue retention** within 12 months through combined expansion mechanics.
10. **Maintain self-serve as primary motion** with sales assist triggered by PQL signals, not arbitrary thresholds.
