# Pivot Decision & Execution Pack

## Company: AI Support Copilot for E-Commerce SMBs

**Date:** March 2026
**Prepared for:** Founding Team (3 people: 2 engineers + 1 founder/sales)

---

## Executive Summary

Your current trajectory is unsustainable. With $180k remaining (5 months of runway), a 25% trial-to-paid conversion rate (3/12), 40% D30 retention, and a 6-week sales cycle mismatched to a $200/month price point, the business will exhaust cash before reaching sustainability. Meanwhile, organic inbound pull from mid-market companies asking specifically for AI-powered returns/refunds handling represents a stronger signal than anything in your current pipeline. This pack walks through whether to pivot, what the options are, and how to validate and execute.

---

## Section 1: Exhaustion Check — Can We Fix Without Pivoting?

Before pivoting, we must honestly assess whether the current model can be rescued within the constraints of time, cash, and team capacity.

### 1.1 Retention Problem Analysis (D30 = 40%)

**What 40% D30 retention means:** Of every 10 customers who start using the product, only 4 are still active after 30 days. For a $200/month B2B SaaS tool, healthy D30 retention should be 80-90%+. You are losing more than half your customers within a month.

**Likely root causes:**

| Hypothesis | Evidence Required | Fix Difficulty | Time to Fix |
|---|---|---|---|
| Product doesn't deliver enough value for general support | Customer exit interviews, usage data | Hard — requires significant product work | 8-12 weeks |
| Onboarding is too complex / time-to-value is too long | Time-to-first-resolution metric, setup completion rates | Medium — UX/onboarding improvements | 4-6 weeks |
| AI quality is insufficient for broad support scenarios | Accuracy/resolution metrics across categories | Hard — model tuning, training data | 8-16 weeks |
| Customers expected a narrow tool and got confused by breadth | Customer feedback, feature usage heatmaps | Medium — could be positioning, not product | 2-4 weeks |
| SMBs churn inherently fast at this price point | Industry benchmarks | Intractable — structural market issue | N/A |

**Assessment:** General-purpose AI support for SMBs is an extremely broad problem. The AI must handle product questions, shipping inquiries, returns, complaints, escalations, and more — each requiring different knowledge bases, tone, and integration points. At $200/month, the expectation is "it just works," but the setup and tuning required for general support likely exceeds what SMBs will tolerate. This is a fundamental product-market mismatch, not a bug to fix.

### 1.2 Sales Cycle Problem Analysis (6 weeks average)

**What a 6-week cycle means at $200/month:** The customer lifetime value (LTV) at 40% D30 retention is roughly:
- Average lifespan estimate: ~2.5 months (given high churn)
- LTV: ~$500
- Customer acquisition cost (CAC) with a 6-week founder-led sales cycle: Founder time alone costs ~$3,000-5,000 in opportunity cost per deal
- LTV:CAC ratio: ~0.1-0.17x (catastrophically negative; needs to be 3x+ minimum)

**Why the cycle is long:**
- General AI support requires stakeholder buy-in (support lead, operations, sometimes IT)
- SMBs fear AI "going rogue" on customer communications — trust-building takes time
- No clear ROI story for general support (hard to measure deflection across all categories)
- Integration with existing helpdesk tools adds friction

**Can we shorten it without pivoting?**
- Self-serve / PLG motion: Possible but requires 4-8 weeks of engineering to build onboarding flows, and still doesn't fix the retention problem
- Content/demo-led approach: Could trim to 3-4 weeks but still uneconomic at $200/month
- Raise price: Hard to justify for general support to SMBs; they'll compare to Zendesk/Intercom bots at similar price points

### 1.3 Exhaustion Check Verdict

| Factor | Can Fix Without Pivot? | Confidence | Time Required |
|---|---|---|---|
| 40% D30 retention | Unlikely — structural breadth problem | Low | 8-16 weeks |
| 6-week sales cycle | Partially — but economics still broken | Medium | 4-8 weeks |
| $200/month price point | Could raise, but need stronger value prop first | Low | Requires product change |
| Unit economics (LTV:CAC) | No — fundamentally broken at current parameters | Very Low | N/A at current trajectory |

**Conclusion: The current model cannot be fixed within your 5-month runway.** The problems are interconnected and structural. Fixing retention requires narrowing or deepening the product significantly. Fixing the sales cycle requires either a radically different go-to-market or a higher price point justified by clearer value. Both point toward the same direction: narrow and go deeper.

---

## Section 2: 4P Pivot Options Grid

We evaluate four pivot options across Product, Price, Persona, and Positioning (the 4Ps).

### Option A: Stay the Course (Baseline)

| Dimension | Details |
|---|---|
| **Product** | General AI support copilot for all ticket categories |
| **Price** | $200/month |
| **Persona** | E-commerce SMBs (1-50 employees) |
| **Positioning** | "AI-powered customer support for small online stores" |
| **Pros** | No switching cost; existing product works |
| **Cons** | Broken unit economics; low retention; broad competition (Zendesk, Intercom, Tidio) |
| **Survival probability** | 10-15% — runway exhausts before reaching PMF |

### Option B: Narrow to Returns/Refunds AI for SMBs

| Dimension | Details |
|---|---|
| **Product** | AI agent handling returns, refunds, and exchanges end-to-end |
| **Price** | $150-250/month (or per-transaction pricing at $1-3/return processed) |
| **Persona** | E-commerce SMBs with 50-500 returns/month |
| **Positioning** | "Autopilot for e-commerce returns — resolve returns and refunds without human agents" |
| **Pros** | Clear value prop; measurable ROI (cost-per-return); faster time-to-value; narrower AI scope improves accuracy |
| **Cons** | Smaller TAM within SMB; might still face SMB churn dynamics; limited expansion within account |
| **Survival probability** | 35-40% |

### Option C: Narrow to Returns/Refunds AI for Mid-Market (Recommended — see Section 3)

| Dimension | Details |
|---|---|
| **Product** | AI-powered returns/refunds automation with policy engine, analytics dashboard, and helpdesk integrations |
| **Price** | $1,000-3,000/month (or $2-5/return processed with minimum commit) |
| **Persona** | Mid-market e-commerce brands (50-500 employees, 1,000-20,000 returns/month) |
| **Positioning** | "The AI returns desk — automate 80% of returns and refunds with policy-compliant AI" |
| **Pros** | Follows existing demand signal; higher ACV fixes unit economics; narrower scope fixes retention; clear ROI story; less price sensitivity |
| **Cons** | Longer sales cycles possible (but justified by higher ACV); need to build policy engine and integrations; smaller initial market to sell into |
| **Survival probability** | 50-60% |

### Option D: Platform Pivot — Returns API/Infrastructure

| Dimension | Details |
|---|---|
| **Product** | API/SDK for e-commerce platforms to embed AI-powered returns processing |
| **Price** | Per-API-call or per-return transaction fee ($0.50-2.00/return) |
| **Persona** | E-commerce platform companies, 3PL providers, helpdesk vendors |
| **Positioning** | "Embed intelligent returns processing in your platform" |
| **Pros** | Massive scale potential; recurring usage-based revenue; defensible once embedded |
| **Cons** | Very long sales cycle (enterprise partnerships); requires significant technical investment; far from current capabilities; high execution risk with current team |
| **Survival probability** | 15-20% — too ambitious for current resources and timeline |

### Comparative Summary

| Criterion (Weight) | A: Stay Course | B: Returns SMB | C: Returns Mid-Market | D: Returns API |
|---|---|---|---|---|
| Demand signal (25%) | Weak (low conversion) | Moderate (inferred) | Strong (inbound requests) | None yet |
| Unit economics potential (25%) | Broken | Marginal | Strong | Very strong (long-term) |
| Speed to validate (20%) | Already invalidated | 3-4 weeks | 3-4 weeks | 8-12 weeks |
| Team capability fit (15%) | Adequate | Good | Good (needs sales uplift) | Weak (needs platform eng) |
| Defensibility (15%) | Low | Low-Medium | Medium | High |
| **Weighted Score** | **1.5/5** | **3.0/5** | **4.0/5** | **2.5/5** |

---

## Section 3: Recommended Pivot Thesis

### The Thesis

**"Mid-market e-commerce brands will pay $1,500+/month for an AI agent that autonomously handles 80% of returns and refunds according to their policies, because returns are their highest-volume, most costly, and most process-automatable support category."**

### Why This Thesis

1. **Demand signal is real.** You have mid-market companies proactively asking for this. Inbound pull at this stage is the strongest possible signal — they are telling you what to build.

2. **Returns are the perfect AI use case.** Returns follow predictable policy logic (return window, item condition, refund method, exceptions). This is much easier for AI to handle accurately than open-ended support questions. Higher accuracy = higher retention.

3. **ROI is crystal clear.** A mid-market brand processing 5,000 returns/month with an average handling cost of $8-12/return spends $40,000-60,000/month on returns processing. If your AI handles 80% at $2,000/month, the ROI is 16-24x. This makes the sale easy and the retention sticky.

4. **Higher ACV fixes everything.** At $1,500-3,000/month, a 6-8 week sales cycle is perfectly acceptable (standard for mid-market SaaS). LTV at 80%+ retention and $2,000/month ACV = ~$20,000. Even with a $3,000-5,000 CAC, you get 4-6x LTV:CAC.

5. **Narrow scope fixes retention.** Instead of being mediocre at everything, you can be excellent at one thing. This means faster setup, faster time-to-value, higher accuracy, and much higher D30 retention.

### Key Assumptions to Validate

| # | Assumption | How to Validate | Success Threshold |
|---|---|---|---|
| 1 | Mid-market brands will pay $1,500+/month for returns automation | Pricing conversations with 10+ prospects | 5+ say "yes" at $1,500+ |
| 2 | AI can handle 80%+ of returns accurately with policy configuration | Build MVP policy engine; test on real return data | 80% resolution rate on test set |
| 3 | Time-to-value is under 1 week (setup + integration) | Pilot with 2-3 design partners | All 3 live within 7 days |
| 4 | D30 retention improves to 80%+ | Track pilot customer usage | 80%+ DAU/MAU among pilots |
| 5 | Sales cycle compresses to 3-4 weeks for mid-market | Track from first contact to signed contract | Median under 4 weeks |

### Target Metrics (12-Week Horizon)

| Metric | Current | 4-Week Target | 8-Week Target | 12-Week Target |
|---|---|---|---|---|
| Pipeline (qualified mid-market leads) | ~3-5 (inbound) | 15 | 25 | 40 |
| Paid customers | 0 (new segment) | 1-2 (design partners) | 3-5 | 8-10 |
| Monthly revenue | $600 (3 x $200) | $2,000-3,000 | $6,000-10,000 | $15,000-25,000 |
| D30 retention | 40% | N/A (too early) | 75%+ (early signal) | 80%+ |
| Average sale cycle | 6 weeks | N/A | 3-4 weeks (target) | 3-4 weeks (confirmed) |
| Return resolution rate | N/A | 60%+ (MVP) | 75%+ | 80%+ |
| ACV | $2,400 | $18,000-24,000 | $18,000-24,000 | $18,000-30,000 |

### Kill Criteria — When to Abandon This Thesis

**Hard kills (if ANY of these are true after 4 weeks, stop and reassess):**

1. Fewer than 3 mid-market prospects agree to a discovery call out of 20+ outreach attempts
2. Zero prospects express willingness to pay $1,000+/month after pricing conversation
3. AI resolution rate on returns data is below 50% after focused engineering effort
4. All inbound mid-market interest evaporates upon deeper conversation (was curiosity, not need)

**Soft kills (if 2+ of these are true after 8 weeks, reassess seriously):**

5. Fewer than 2 signed design partners after 8 weeks of effort
6. Design partners churn or go inactive within first 2 weeks
7. Sales cycle exceeds 8 weeks consistently (worse than current)
8. Policy configuration is too complex for customers to complete without heavy hand-holding
9. Monthly burn rate increases without corresponding revenue acceleration

**Runway checkpoint:** At $36,000/month burn rate and $180,000 remaining, you hit the wall at month 5. By week 8 (month 2), you should have at least $5,000/month in committed revenue and 3+ design partners. If not, you need to either cut burn dramatically or explore a bridge round.

---

## Section 4: Four-Week Validation Sprint Plan

### Sprint Philosophy

This is not a "build it and they will come" plan. This is a **sell-build-sell** loop. You sell the vision first, build only what's needed to deliver on the first design partner commitment, then sell again with proof.

### Team Allocation

| Person | Weeks 1-2 Focus | Weeks 3-4 Focus |
|---|---|---|
| **Founder (Sales)** | Outbound to mid-market prospects; close 2-3 design partners | Onboard design partners; start second wave outreach |
| **Engineer 1** | Build returns policy engine (rule-based + AI) | Integrate with first design partner's systems; iterate on accuracy |
| **Engineer 2** | Build returns-specific AI prompt pipeline + analytics dashboard MVP | Build self-serve policy configuration UI; support integration work |

### Existing Customer Transition

Your 3 paying SMB customers at $200/month ($600 total MRR) should be maintained on autopilot during the sprint. Do not actively invest in them, but do not churn them either — the $600/month buys you a few extra weeks of runway.

---

### Week 1: Signal Validation & Architecture

**Goal:** Confirm demand with real conversations; begin technical foundation.

**Sales (Founder):**
- [ ] Contact the mid-market companies who already expressed interest in returns/refunds AI. Schedule discovery calls with all of them this week.
- [ ] Identify 30 additional mid-market e-commerce brands (50-500 employees) with high return volumes. Sources: LinkedIn Sales Navigator, Shopify Plus merchant directories, BigCommerce Enterprise lists, industry reports on return rates by vertical (fashion/apparel has highest).
- [ ] Conduct 5-8 discovery calls. Key questions:
  - How many returns do you process monthly?
  - What is your current cost per return (labor, systems, refund costs)?
  - What systems do you use for returns today? (RMA systems, helpdesk, manual?)
  - What does your returns policy look like? How many exception scenarios exist?
  - Would you pay $1,500-2,500/month for an AI that resolves 80% of returns autonomously?
  - Would you be a design partner (discounted rate, early access, feedback commitment)?
- [ ] Document all conversations in a structured format: company, size, return volume, current pain, willingness to pay, design partner interest (Y/N).
- [ ] Draft a 1-page "Returns AI" pitch deck: Problem, Solution, How it Works, ROI Calculator, Pricing, Design Partner Offer.

**Engineering (Both Engineers):**
- [ ] Audit existing codebase: identify what can be reused for returns-specific AI (likely 40-60% of current NLP pipeline, conversation management, integration framework).
- [ ] Design the Returns Policy Engine schema: return windows, item conditions, refund methods (original payment, store credit, exchange), exception rules, escalation triggers.
- [ ] Set up a returns-specific AI evaluation harness: collect/generate 200+ synthetic return scenarios across categories (simple refund, exchange, damaged item, out-of-window, missing item, partial return).
- [ ] Begin building the policy configuration layer — the system that translates a merchant's return policy into machine-readable rules.
- [ ] Research integration points for top 3 mid-market e-commerce platforms: Shopify Plus, BigCommerce Enterprise, and Magento/Adobe Commerce (returns/orders APIs).

**Key Deliverables:**
- 5-8 discovery calls completed and documented
- Returns Policy Engine schema defined
- AI evaluation harness with 200+ test scenarios
- 1-page pitch deck ready

**Week 1 Kill Check:**
- If fewer than 3 discovery calls result in genuine interest, reassess the thesis immediately.

---

### Week 2: MVP Build & Design Partner Closing

**Goal:** Close 2-3 design partners; build functional returns AI MVP.

**Sales (Founder):**
- [ ] Follow up on Week 1 discovery calls. Push interested prospects toward design partner agreements.
- [ ] Design partner terms: 3-month commitment at $500/month (discounted from $1,500-2,500), weekly feedback sessions, early access to all features, lock-in at design partner rate for 12 months after launch.
- [ ] Draft and send design partner agreements (keep them simple — 1-2 pages, not a full SaaS contract).
- [ ] Conduct 5-8 more discovery calls from the outbound list.
- [ ] Begin building case study framework: document each design partner's current returns process, costs, and pain points. You will need before/after data.
- [ ] Attend 1-2 e-commerce industry Slack communities or events to test positioning and generate additional leads.

**Engineering (Both Engineers):**
- [ ] Build Returns AI MVP:
  - Policy engine that accepts rules (return window, conditions, refund types, exceptions)
  - AI agent that can classify return requests, check eligibility against policy, and generate appropriate responses
  - Basic conversation flow: customer states reason for return -> AI checks policy -> AI either processes or escalates
  - Simple analytics: returns processed, resolution rate, escalation rate, average handling time
- [ ] Target: 70%+ resolution rate on the evaluation harness by end of Week 2
- [ ] Build basic Shopify Plus integration (read order data, process refunds via API) — this is the most likely platform for first design partners
- [ ] Create a demo environment that the founder can use in sales calls (pre-loaded with sample store, sample policy, sample return conversations)

**Key Deliverables:**
- 2-3 signed design partner LOIs/agreements
- Functional returns AI MVP (policy engine + conversation AI + Shopify integration)
- 70%+ resolution rate on test scenarios
- Demo environment ready for sales calls

**Week 2 Kill Check:**
- If zero design partners signed, hold an honest team meeting. Either the value prop needs reshaping or the market isn't there. Consider pivoting to Option B (returns for SMBs) or Option D.

---

### Week 3: Design Partner Onboarding & Iteration

**Goal:** Get design partners live; begin collecting real-world performance data.

**Sales (Founder):**
- [ ] Onboard design partners: configure their return policies in the system, connect their Shopify Plus store, set up the AI agent in their support flow.
- [ ] Target: All design partners live and processing real returns by end of Week 3.
- [ ] Daily check-ins with design partners during first 3 days. Switch to every-other-day after.
- [ ] Document every piece of feedback, every failure case, every "wow" moment.
- [ ] Continue outbound: schedule 5+ new discovery calls. Use early design partner data ("we just went live with Brand X and are resolving 65% of returns autonomously in Day 1") to accelerate conversations.
- [ ] Begin drafting pricing page and positioning for a simple landing page.

**Engineering (Both Engineers):**
- [ ] Support design partner onboarding: debug integration issues, tune AI for partner-specific edge cases.
- [ ] Implement real-time monitoring: track every return interaction, flag failures and escalations, measure resolution rate, CSAT where possible.
- [ ] Rapid iteration cycle: review escalated/failed cases daily, improve policy engine and AI prompts.
- [ ] Target: move from 70% to 80%+ resolution rate on live traffic by end of Week 3.
- [ ] Build self-serve policy configuration UI (even if basic) so that future onboarding is faster.
- [ ] Begin BigCommerce integration work if any prospect requires it.

**Key Deliverables:**
- All design partners live and processing returns
- Real-world resolution rate data (target: 75%+)
- First round of iteration based on live feedback
- 5+ new discovery calls conducted

**Week 3 Kill Check:**
- If design partners refuse to go live after signing, or go live and immediately want to turn it off, the product isn't ready. Focus all effort on product quality before continuing sales.

---

### Week 4: Data Collection, Iteration & Scale Planning

**Goal:** Prove retention signal; build pipeline for months 2-3; plan resource allocation.

**Sales (Founder):**
- [ ] Collect Week 1 performance data from design partners:
  - Returns processed by AI vs. escalated to humans
  - Customer satisfaction scores (if measurable)
  - Time saved per return
  - Estimated cost savings
- [ ] Build first mini case study: "[Design Partner] automated X% of returns in Week 1, saving Y hours/month"
- [ ] Use case study in 5-8 new prospect conversations. Test whether the data accelerates sales cycle.
- [ ] Finalize pricing strategy based on design partner feedback and willingness-to-pay data from all conversations to date.
- [ ] Build a target list of 50 mid-market prospects for Month 2 outreach.
- [ ] Draft a simple landing page with positioning, ROI calculator, and "request demo" CTA.

**Engineering (Both Engineers):**
- [ ] Continue iterating on AI quality based on live data. Target 80%+ resolution rate.
- [ ] Build remaining analytics dashboard features: trend charts, policy violation alerts, refund amount tracking, return reason categorization.
- [ ] Harden the integration layer: error handling, retry logic, security audit.
- [ ] Begin documenting the onboarding process so it can be partially self-serve.
- [ ] Plan technical roadmap for Weeks 5-8: what's needed to support 10 customers simultaneously? 50?

**Key Deliverables:**
- Performance data from 1+ weeks of live operation at design partners
- First mini case study
- Finalized pricing
- Month 2 prospect pipeline of 50+ targets
- Landing page drafted

**Week 4 Checkpoint — The Go/No-Go Decision:**

Score each criterion 1-5 and sum:

| Criterion | Score (1-5) | Notes |
|---|---|---|
| Design partners actively using product (not churned) | ___ | 5 = all active and engaged; 1 = all churned or inactive |
| Resolution rate on live traffic | ___ | 5 = 80%+; 3 = 60-80%; 1 = below 50% |
| Design partner NPS/qualitative feedback | ___ | 5 = "can't live without it"; 1 = "meh" |
| Pipeline for Month 2 (qualified prospects) | ___ | 5 = 15+ qualified; 3 = 8-14; 1 = fewer than 5 |
| Willingness to pay $1,500+/month confirmed | ___ | 5 = 5+ prospects confirmed; 1 = none confirmed |
| Team energy and conviction | ___ | 5 = all in; 1 = doubt and fatigue |

**Scoring:**
- **25-30: Full speed ahead.** Double down. Consider raising a seed round to extend runway.
- **18-24: Promising but needs work.** Continue with focused iteration. Identify the weakest scores and address them in Week 5-8.
- **12-17: Warning zone.** Have an honest team conversation. Is there a sub-pivot that could work? Or is this the wrong direction entirely?
- **Below 12: Kill the thesis.** Return to the options grid. Consider Option B (returns for SMBs) or Option D (API/infrastructure), or explore an entirely new direction.

---

## Section 5: Financial Model & Runway Management

### Current State

| Item | Value |
|---|---|
| Cash remaining | $180,000 |
| Monthly burn (estimated) | ~$36,000 (3 people x ~$12k avg loaded cost) |
| Current MRR | $600 (3 SMB customers x $200) |
| Runway at current burn | 5 months |
| Runway with $600 MRR offset | 5.1 months (negligible difference) |

### Projected State Under Pivot (Conservative)

| Month | New MRR (Cumulative) | Burn | Net Burn | Cash Remaining |
|---|---|---|---|---|
| Month 1 (Weeks 1-4) | $1,500 (2 design partners @ $500 + existing $600) | $36,000 | $34,500 | $145,500 |
| Month 2 | $5,500 (add 2 full-price @ $2,000 + keep existing) | $36,000 | $30,500 | $115,000 |
| Month 3 | $12,000 (add 3 more @ $2,000 + retain existing) | $36,000 | $24,000 | $91,000 |
| Month 4 | $20,000 (add 4 more + retain) | $36,000 | $16,000 | $75,000 |
| Month 5 | $30,000 (add 5 more + retain at 85%) | $36,000 | $6,000 | $69,000 |

**Under this model, you approach break-even around Month 5-6 and have ~$69k remaining at the 5-month mark — giving you meaningful additional runway vs. the current path to zero.**

### Fundraising Trigger

If by Week 8 (Month 2) you have 3+ paying customers at $1,500+ ACV and 80%+ early retention, you have a compelling seed story:
- "We found PMF in AI-powered returns automation for mid-market e-commerce"
- "3 paying customers, $X MRR, 80%+ retention, 80%+ AI resolution rate"
- "$18,000+ ACV with 3-4 week sales cycles"

This is a strong enough signal to raise a $1-2M seed round and extend runway to 18+ months.

---

## Section 6: Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Mid-market sales cycle is actually 10+ weeks | Medium | High | Offer aggressive design partner terms; use warm inbound leads first; build ROI calculator to shortcut decision process |
| AI accuracy plateau below 80% | Medium | High | Invest in policy engine (rule-based) to handle predictable cases; use AI only for classification and edge cases; human-in-the-loop fallback |
| Existing SMB customers churn during pivot | High | Low | Accept this risk — $600/month MRR is not worth protecting at the cost of pivot velocity |
| Larger competitors (Loop Returns, Returnly, Narvar) copy AI feature | Medium | Medium | Move fast; build deep integrations; mid-market relationships are your moat; consider features competitors can't easily replicate (policy learning, anomaly detection) |
| Team burnout during sprint | Medium | High | Maintain sustainable pace; celebrate small wins; 4-week sprint has a clear end date and decision point |
| Design partners are low-quality (too small, too niche) | Low-Medium | Medium | Screen for 1,000+ returns/month and mainstream product categories; avoid highly specialized verticals initially |

---

## Section 7: Communication Plan

### Existing Customers (3 SMB accounts)

- Continue service as-is. Do not deprecate or reduce their experience during the sprint.
- If they churn naturally, do not invest in saving them.
- After pivot validation, decide whether to maintain SMB tier or sunset it.

### Team Alignment

- Day 1 meeting: Present this pack. Get buy-in from both engineers. Address concerns.
- Daily standup (15 min): What did you do yesterday? What are you doing today? Any blockers?
- Weekly retro (Friday, 30 min): What worked? What didn't? What will we change?
- Week 4: Formal go/no-go review using the scorecard above.

### Advisors/Investors (if applicable)

- Brief update at end of Week 1: "We're pivoting to returns/refunds AI for mid-market. Here's why. Here's the plan."
- Week 4 update with data: pipeline, design partner status, resolution rates, go/no-go decision.

---

## Appendix A: Mid-Market Returns Economics Calculator

Use this in sales conversations to demonstrate ROI.

**Inputs (ask the prospect):**
- Monthly return volume: ___
- Average cost per return (labor + systems): ___
- Current support FTE hours spent on returns: ___

**Outputs (calculate for them):**

| Metric | Current | With Returns AI |
|---|---|---|
| Returns processed/month | [their volume] | Same |
| Human-handled returns | 100% | 20% (AI handles 80%) |
| Cost per return | $[their cost] | ~$[their cost x 0.25] |
| Monthly returns cost | $[volume x cost] | $[volume x cost x 0.25 + our price] |
| Monthly savings | — | $[difference] |
| ROI | — | [savings / our price]x |

**Example with a typical mid-market brand:**
- 3,000 returns/month x $10/return = $30,000/month current cost
- With AI: 600 human-handled x $10 + $2,000 platform fee = $8,000/month
- Savings: $22,000/month
- ROI: 11x

---

## Appendix B: Competitive Landscape Quick Reference

| Company | Focus | Pricing | AI Capability | Your Differentiation |
|---|---|---|---|---|
| Loop Returns | Returns management platform | $300-2,000+/month | Limited (rules-based) | AI-native; autonomous resolution vs. workflow tool |
| Returnly | Returns & exchanges | Custom pricing | Minimal | AI handles conversation + decision vs. just logistics |
| Narvar | Post-purchase experience | Enterprise pricing | Some (tracking/notifications) | Purpose-built for returns resolution, not broad post-purchase |
| AfterShip Returns | Returns portal | $200-500/month | Basic automation | Deep AI reasoning vs. simple if/then rules |
| Generic AI support (Zendesk, Intercom) | All support categories | $50-200/agent/month | Broad but shallow | Domain-specific depth; returns policy expertise; higher accuracy on returns |

**Your positioning:** "Not a returns logistics platform. Not a general support bot. The AI returns agent that actually resolves returns autonomously, accurately, and per your policy."

---

*This Pivot Decision & Execution Pack should be reviewed as a team, adapted to your specific context, and used as a living document throughout the 4-week validation sprint. Update the metrics, kill criteria, and risk register weekly.*
