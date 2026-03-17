# Pivot Decision & Execution Pack

**Company:** AI Support Copilot (E-commerce)
**Date prepared:** 2026-03-17
**Decision owner:** Founder/CEO
**Decision date:** 2026-04-14 (4 weeks from today)

---

## 1) Context Snapshot

- **Product today:** AI-powered customer support copilot for e-commerce businesses. Handles general support tickets (order status, product questions, complaints, returns, refunds) with AI-assisted responses and automation.
- **Target customer (current):** E-commerce SMBs (small and medium businesses).
- **Current promise:** "AI handles your support tickets so your small team can focus on growing the business."
- **Stage:** Pre-PMF. Early revenue but no repeatable, retainable customer base.
- **Key metrics:**
  - 12 trial sign-ups total
  - 3 converted to paid ($200/month each) = $600 MRR
  - D30 retention: 40% (of converted customers; effectively losing more than half within a month)
  - Sales cycle: ~6 weeks average (too long for a $200/month product; typical target is <2 weeks for this ACV)
  - Runway: 5 months ($180k remaining)
  - Team: 3 people (2 engineers + 1 founder doing sales)
- **Emerging signal:** Mid-market companies (larger than current ICP) are reaching out specifically asking for AI-powered returns/refunds handling rather than general support.
- **Non-negotiables:** Must remain an AI/software product (not a services business). Team of 3 cannot grow headcount before proving the pivot. Must find a path to revenue within 5 months.
- **Decision owner + stakeholders:** Founder/CEO makes the final call. Two engineer co-founders must be aligned. No board/investors mentioned, but runway pressure makes this urgent.

### Decision statement

> **By April 14, 2026 (4 weeks), the founder will decide: pivot to a returns/refunds-focused AI product for mid-market e-commerce vs. persevere with the current general support copilot for SMBs vs. pursue an alternative pivot direction.**

---

## 2) Stuck Diagnosis

### Symptoms (what we observe)

1. **Low trial-to-paid conversion:** 3/12 = 25%. Not terrible for B2B trials, but the absolute numbers are too small to be confident and the funnel is thin.
2. **Poor D30 retention (40%):** Customers who pay are churning within a month. This is the most alarming signal -- it suggests the product is not delivering enough sustained value to justify even $200/month.
3. **Long sales cycles (~6 weeks):** For a $200/month product, this means CAC is wildly disproportionate to LTV. Founder-led sales at 6 weeks per deal = ~2 deals/month max, and with 40% D30 retention, net revenue growth is near zero or negative.
4. **Unsolicited mid-market pull:** Companies outside the target ICP are asking for a specific use case (returns/refunds), which is a classic "hair on fire" signal from an adjacent segment.

### Hypothesized causes (ranked by likelihood)

1. **Value gap for SMBs (demand/value problem):** General AI support is a "nice to have" for SMBs, not a "hair on fire" problem. SMBs have low ticket volume, so automation saves little time. The product doesn't solve a painful-enough problem to retain users. **Evidence: 40% D30 retention suggests customers try it, see marginal value, and leave.**
2. **Wrong ICP / wrong buyer (demand problem):** SMBs buying a $200/month support tool often don't have the ticket volume, complexity, or staffing pain to justify it. The 6-week sales cycle suggests the founder is pushing a product into a market with low urgency. **Evidence: mid-market companies are pulling for a specific painful use case, while SMBs need convincing.**
3. **Product too broad / too shallow (execution problem):** A general "AI support copilot" tries to do everything (order status, product questions, complaints, returns) but does none of them exceptionally well. **Evidence: mid-market interest is specifically for returns/refunds, suggesting depth > breadth.**
4. **Pricing/packaging mismatch (execution problem):** $200/month may be too high for SMBs getting general support help, or too low for mid-market companies getting returns automation. The price point sits in a dead zone. **Evidence: 6-week sales cycle at $200/month is a red flag for price-value alignment.**

### Signal vs. execution separation

| Category | Issue | Classification |
|---|---|---|
| 40% D30 retention | Customers don't get enough ongoing value from general support AI | **Demand/value problem** |
| 6-week sales cycle | SMBs don't have urgent pain; requires education-heavy selling | **Demand problem** (wrong ICP urgency) |
| Mid-market pull for returns | Adjacent segment has acute, specific pain | **Demand signal** (positive, in a different direction) |
| Low absolute trial volume (12) | Could be distribution or could be weak market pull | **Ambiguous** (need more data) |

### Evidence we have (tagged)

| Evidence | Type | Confidence |
|---|---|---|
| 12 trials, 3 paid, $600 MRR | Fact | High |
| D30 retention = 40% | Fact | High |
| Sales cycle = ~6 weeks | Fact | High |
| Mid-market companies asking for returns/refunds AI | Fact (qualitative) | Medium (how many? how qualified?) |
| $180k runway, 5 months | Fact | High |
| Team of 3 (2 eng + 1 founder/sales) | Fact | High |

### Evidence gaps (what we must learn)

1. **How many mid-market inbound requests?** Is it 2 companies or 10? Are they qualified buyers with budget?
2. **Why are D30 churners leaving?** Exit interviews or usage data needed -- is it "not useful enough" or "too hard to set up" or "we found something better"?
3. **What do the 3 retained paid customers love?** Is there a specific use case or workflow they depend on?
4. **Returns/refunds pain: how big is it?** What do mid-market e-commerce companies currently spend on returns processing? What's the cost of errors?
5. **Competitive landscape for returns-specific AI:** Who else is doing this? Is the window open?

---

## 3) Exhaustion Check (Butterfield Rule)

**Core question:** "Have we exhausted the possibilities with the current direction before pivoting?"

| Lever | Have we tried it well? | Evidence/result | Why it did/didn't work | Best next attempt (time-boxed) |
|---|---|---|---|---|
| **ICP refinement** (narrower SMB segment) | Partially. Selling to "e-commerce SMBs" is broad. No evidence of testing a specific sub-segment (e.g., Shopify stores with 50+ tickets/day). | 12 trials across a mix of SMBs; no clear pattern of which sub-segment retains. | Too broad to develop depth; SMBs with low volume churn because value is marginal. | Could test: target only high-volume Shopify stores (100+ tickets/day). **But:** finding enough of these and converting in <2 weeks is unproven and eats into 5-month runway. |
| **Positioning/promise** (clearer value prop) | Not tried well. Current positioning is generic ("AI support copilot"). No evidence of testing sharper promises (e.g., "Cut support response time by 80%"). | No A/B on messaging or landing pages. | Generic promise doesn't create urgency for SMBs. | Could test: rewrite positioning around a specific outcome metric. **Feasible in 1-2 weeks.** |
| **Pricing/packaging** | Not tried. $200/month flat; no usage-based, no freemium, no tiered. | No experiments. | $200/month may be in a dead zone: too high for low-volume SMBs, too low for mid-market. | Could test: lower price ($49-99/month) for SMBs or usage-based pricing. **But:** this doesn't fix the retention problem if the core value is weak. |
| **Onboarding / time-to-value** | Unknown. No data on how quickly users see value or where they drop off during setup. | Gap: no onboarding funnel metrics. | If onboarding is broken, users never experience the value. But 40% D30 retention (not D7) suggests they do try it and then leave, not that they fail to set up. | Could instrument onboarding and optimize. **Feasible but takes 2-3 weeks and only matters if the core value is there.** |
| **Distribution/channel** | Limited. Founder-led outbound sales only. No inbound, no partnerships, no product-led growth. | 12 trials in an unspecified timeframe suggests thin distribution. | Outbound-only for a $200/month product is structurally broken -- the math doesn't work. | Could test: Shopify App Store listing, content marketing, partner channel. **Feasible to start in 1-2 weeks, but time-to-results is 4-8 weeks.** |
| **Reliability/trust** | Unknown. No evidence of bugs/trust issues blocking retention. | Gap: no NPS or qualitative feedback on reliability. | Probably not the primary issue given that the symptoms point to value, not quality. | N/A unless churn interviews reveal trust issues. |

### Exhaustion check verdict

**The current direction has NOT been thoroughly exhausted**, but the critical question is whether the remaining levers can move fast enough given 5 months of runway:

- **Positioning rewrite** is cheap and fast (1-2 weeks). Worth doing regardless.
- **Pricing experiments** are feasible but don't fix the core retention problem.
- **Onboarding optimization** assumes the core value is there; 40% D30 retention after conversion suggests it may not be.
- **ICP narrowing within SMBs** is possible but requires finding a high-volume sub-segment that may be too small.
- **Distribution** improvements take too long to validate (4-8 weeks to see results) and don't fix retention.

**The "last best" non-pivot moves:**

1. **Churn interviews (1 week):** Call every churned customer and the 3 retained ones. Understand exactly what drove retention vs. churn. This is a must-do regardless of pivot decision.
2. **Positioning sharpening (1 week, parallel):** Rewrite the value prop around a specific, measurable outcome. Test with 5 outbound prospects.

**However:** Even if these moves improve conversion slightly, the structural problem remains -- general AI support for SMBs at $200/month faces a painful combination of (a) moderate pain intensity, (b) low willingness to pay, (c) high-touch sales for low ACV. Meanwhile, a strong demand signal is pulling from a different direction.

**Recommendation:** Complete the churn interviews and positioning test in Week 1 of the pivot sprint (they inform the pivot too), but do not delay the pivot exploration. The risk of spending 2-3 months optimizing the current direction and failing is too high given 5 months of runway.

---

## 4) Pivot Options Map (4P Grid)

| # | Option name | Problem | Persona | Product | Positioning/Package | 10% or 200% | Why this could win | What must be true | Biggest risks |
|---|---|---|---|---|---|---|---|---|---|
| **A** | **Narrow to returns/refunds for SMBs** | Returns/refunds processing is time-consuming and error-prone | Same: e-commerce SMBs | Narrow the AI to returns/refunds only; deeper automation (policy lookup, auto-approve, fraud detection) | "AI returns manager: auto-process 80% of returns" | **10%** | Sharper value prop for a specific pain point; reuses existing tech; easier to demo and prove value | SMBs have enough returns volume to justify $200/month; returns are painful enough to create urgency | SMBs may still have low volume; same sales cycle problem; still a "nice to have" for small shops |
| **B** | **Returns/refunds AI for mid-market e-commerce** | Returns/refunds at scale are expensive, error-prone, and a major customer experience pain point | Mid-market e-commerce (50-500 employees, $10M-$500M revenue, thousands of returns/month) | Purpose-built returns/refunds AI: auto-classify, auto-approve/deny, fraud flagging, analytics dashboard | "Cut returns processing cost by 60% and resolution time by 80%" | **200%** | Follows the existing demand signal; mid-market has budget ($1k-5k/month), volume to prove ROI, and returns are a P&L line item; higher ACV justifies longer sales cycles | Mid-market e-commerce will pay $1k-5k/month for returns automation; you can reach and close 5-10 design partners in 3 weeks; the product can be narrowed and deepened in 4 weeks | Mid-market sales cycles could be even longer; product depth required may exceed team capacity; competitive landscape may be crowded; support burden of larger customers on a 3-person team |
| **C** | **Horizontal AI support copilot -- move upmarket** | General customer support is expensive and slow at scale | Mid-market e-commerce (same as B but general support, not returns-specific) | Keep the general support copilot but repackage for mid-market with better integrations, analytics, SLAs | "Enterprise-grade AI support at mid-market prices" | **10%** | Larger ACV; mid-market has real support pain; leverages existing product | Mid-market will buy a general support AI from a 3-person startup over established players (Zendesk AI, Intercom); you can differentiate on depth/quality | Competing with well-funded incumbents (Zendesk, Intercom, Ada); no moat; same "broad but shallow" problem at higher ACV; team of 3 cannot provide enterprise-grade support/reliability |
| **D** | **Returns-as-a-Service platform (API)** | E-commerce platforms and 3PLs need returns intelligence embedded in their workflows | Platform/3PL partners who serve e-commerce merchants | API-first returns intelligence: classification, fraud scoring, policy engine; partners embed in their UX | "Plug returns AI into your platform in a day" | **200%** | Leverages partner distribution (one integration = hundreds of merchants); recurring revenue per API call; avoids direct SMB sales; builds a data moat | A platform partner (Shopify app, 3PL, returns logistics company) will integrate your API and drive volume; you can build a credible API product in 4-6 weeks | No existing platform relationships; API adoption is slow; revenue per merchant is tiny unless volume is massive; business development with platforms is notoriously slow |
| **E** | **Refund fraud detection for e-commerce** | Refund fraud costs e-commerce $25B+/year; merchants lose money on fraudulent returns/chargebacks | E-commerce companies of any size (SMB to enterprise) with fraud exposure | AI fraud detection for returns and refund requests: pattern detection, risk scoring, auto-flag | "Stop refund fraud before it costs you" | **200%** | Massive, quantifiable pain ($$$); clear ROI pitch; defensible with data/ML; "stop losing money" sells faster than "save time" | Refund fraud is a top-3 pain point for target merchants; you can build a credible fraud model with limited data; merchants will share data for a pilot | Cold-start data problem (need transaction data to train); competing with Forter, Riskified, Signifyd at the high end; may require deep domain expertise in fraud patterns |
| **F** | **Persevere + optimize (status quo)** | General support for SMBs | Same | Same | Sharpen positioning, fix onboarding, lower price | **0% (no pivot)** | Preserves current learnings and customers; avoids pivot disruption | D30 retention can be raised to 70%+ with onboarding/positioning fixes; sales cycle can be cut to <3 weeks with better targeting; SMB support AI market is large enough | 5 months of runway with $600 MRR; 40% retention suggests a value problem, not just execution; founder must sell at low ACV for months with no guarantee of traction |

### Options analysis summary

- **Option A (returns for SMBs)** is a 10% pivot: sharper focus, same ICP. Low risk, low reward. May not solve the fundamental "SMBs don't have enough volume" problem.
- **Option B (returns for mid-market)** is the strongest 200% pivot: follows real demand signal, changes both persona and product focus, higher ACV justifies sales effort. The biggest question is whether a 3-person team can serve mid-market.
- **Option C (general support, move upmarket)** is a 10% pivot into a red ocean. Competing with Zendesk AI, Intercom, Ada with no differentiation.
- **Option D (returns API/platform)** is a 200% pivot with high potential but long time-to-revenue. Platform business development is slow.
- **Option E (fraud detection)** is a 200% pivot into a large market but has a cold-start data problem and strong incumbents.
- **Option F (persevere)** is the baseline. Possible but risky given runway and retention signals.

---

## 5) Chosen Pivot Thesis + Success Metrics + Kill Criteria

### Recommended pivot: Option B -- Returns/Refunds AI for Mid-Market E-commerce

### Pivot Thesis Card

- **Persona:** Mid-market e-commerce companies (50-500 employees, $10M-$500M revenue) with high returns volume (1,000+ returns/month). Primary buyer: VP of Customer Experience or VP of Operations.
- **Problem:** Processing returns and refunds at scale is expensive (dedicated staff), slow (multi-day resolution), error-prone (wrong refund amounts, missed fraud), and a key driver of customer dissatisfaction. Each return costs $10-30 to process manually.
- **Promise (value):** "AI-powered returns automation that cuts processing cost by 60% and resolution time from days to minutes -- while catching fraud and improving customer satisfaction."
- **Proof (why believe?):** (a) Mid-market companies are already reaching out unprompted asking for returns-specific AI -- this is pull, not push. (b) The existing AI/NLP infrastructure built for general support can be narrowed and deepened for returns classification, policy matching, and auto-resolution. (c) Returns is a P&L line item with clear, quantifiable ROI -- making the business case is straightforward.
- **Price/packaging assumption:** $1,500-3,000/month (base) + volume-based pricing above a threshold. 7.5-15x current ACV. Target: $2,000/month average starting contract.
- **Distribution wedge:** (a) Warm outbound to the mid-market companies who have already expressed interest. (b) LinkedIn/content targeting VPs of CX and Ops at mid-market e-commerce. (c) Shopify Plus and BigCommerce partner ecosystems. (d) Case study from first design partner becomes the sales engine.
- **Risks/unknowns:** (1) Can a 3-person team deliver a credible mid-market product? (2) Will mid-market sales cycles be <4 weeks at this ACV? (3) Is the technical depth required for returns automation achievable in 4 weeks? (4) How many mid-market e-commerce companies have this pain acutely enough to pay $2k/month?

### Success Metrics

#### North Star

- **Metric:** Number of paid mid-market design partners processing returns through the product.
- **Why it reflects value:** A company that connects their returns flow and pays monthly has validated the problem, the product, and the price. This is the single strongest signal of product-market fit for this pivot.
- **Baseline:** 0 (starting fresh with new ICP)
- **8-week target:** 3+ paid design partners

#### Leading indicators (checked weekly)

| Indicator | Week 2 target | Week 4 target | Week 8 target |
|---|---|---|---|
| Discovery calls completed with mid-market e-commerce | 8+ | 15+ | 20+ |
| Companies agreeing to paid pilot / LOI signed | 2+ | 4+ | 6+ |
| Returns processed through product (pilot volume) | N/A | 100+ | 1,000+ |
| Pilot customer D14 retention (still active) | N/A | N/A | 80%+ |
| Average sales cycle (first contact to paid pilot) | N/A | <3 weeks | <3 weeks |

#### Guardrails (must not violate)

1. **Burn rate:** Monthly burn must stay under $36k/month (current rate). No new hires until 3+ design partners are secured.
2. **Existing customer commitment:** Do not abandon the 3 paying SMB customers mid-contract. Provide maintenance-level support but no new feature development for the general copilot.
3. **Scope discipline:** Build only for returns/refunds. Resist mid-market customer requests to expand back to general support until the returns wedge is validated.
4. **Data/privacy:** Handle returns data (order info, customer PII, payment info) with appropriate security. SOC 2 readiness is a future requirement, not a blocker for pilots.

### Kill Criteria (Decision Gates)

| Gate | Date | Condition | Decision |
|---|---|---|---|
| **Gate 1: Demand signal** | Week 2 (Mar 31) | Fewer than 5 qualified discovery calls booked with mid-market e-commerce companies | **Pause:** Re-evaluate whether we can reach this ICP. Consider Option D (API/platform) or Option A (returns for SMBs with stronger positioning). |
| **Gate 2: Willingness to pay** | Week 3 (Apr 7) | Fewer than 2 companies willing to sign a paid pilot LOI ($1,500+/month) | **Stop pivot B:** The ACV hypothesis is wrong. Evaluate whether to lower price (SMB returns) or change approach. |
| **Gate 3: Product viability** | Week 4 (Apr 14) | Cannot demonstrate credible returns auto-processing in a live demo (>50% auto-resolution rate on test data) | **Reassess scope:** Either narrow further (e.g., only apparel returns) or extend timeline by 2 weeks with a revised scope. |
| **Gate 4: Retention signal** | Week 8 (May 12) | Fewer than 2 of 3+ design partners still actively using the product after 2+ weeks | **Kill:** The returns-specific value prop is not strong enough. Convene a strategy session to evaluate remaining options with ~3 months of runway. |

---

## 6) Validation Plan

### Customer Learning Plan

| Learning goal | Method | Sample/target | Success threshold | Decision if fails | Owner | Date |
|---|---|---|---|---|---|---|
| Validate that mid-market e-commerce has acute returns pain | Discovery calls (structured interview: current process, cost, volume, pain ranking) | 10+ mid-market e-commerce ops/CX leaders | 7/10+ rank returns in top 3 operational pains | Pivot thesis weakened; consider fraud angle (Option E) or SMB returns (Option A) | Founder | Week 1-2 |
| Test willingness to pay $1,500-3,000/month | Present pricing in discovery calls; ask for LOI/paid pilot commitment | Same prospects as above | 3+ LOIs signed at $1,500+/month | ACV is wrong; test $500-1,000/month tier or usage-based pricing | Founder | Week 2-3 |
| Validate technical feasibility of 50%+ auto-resolution | Build returns classification + policy-matching prototype; test on anonymized data from design partners | 2-3 design partner datasets | >50% of returns correctly auto-classified and routed | Narrow scope to a single returns category (e.g., "item not as described") or extend build by 2 weeks | Engineers | Week 2-4 |
| Test whether product retains after initial setup | Monitor daily active usage and resolution accuracy for pilot customers over 2 weeks | 3+ pilot customers | 80%+ D14 retention; >90% resolution accuracy | Core value is insufficient; investigate whether the issue is product quality, integration difficulty, or value perception | Engineers + Founder | Week 4-8 |
| **Hard truth test:** Can we get a company to route live returns through our system and keep doing it? | Concierge pilot: manually assist with setup, then observe if they continue using it unassisted for 1 week | 2+ companies | At least 1 company processes 100+ returns through the system with <10% manual override rate | **Kill criterion triggered.** The product does not deliver sufficient automation value. Reassess with 3 months of runway. | Full team | Week 4-6 |

### What would change our mind

- If discovery calls reveal that returns pain is concentrated in enterprise (not mid-market), we may need to adjust the persona upward and accept longer sales cycles.
- If multiple prospects say "we'd use this if it integrated with [specific platform]," that's a signal to consider Option D (API/platform) as a secondary strategy.
- If the technical challenge of returns auto-resolution is harder than expected, we may narrow to a specific returns category (e.g., apparel size/fit returns only).

---

## 7) Execution Plan: 4-Week Pivot Sprint

### Scope (what we will build/do)

1. **Returns/refunds AI product (MVP):**
   - Returns request classifier (reason categorization)
   - Policy matching engine (auto-approve/deny based on configurable rules)
   - Refund amount calculator
   - Integration with 1-2 e-commerce platforms (Shopify Plus priority)
   - Simple dashboard showing returns volume, auto-resolution rate, savings
2. **Sales materials:**
   - New positioning and landing page (returns-focused)
   - ROI calculator for prospects
   - 1-page case study template (to be filled after first pilot)
3. **Customer development:**
   - 15+ discovery calls
   - 3+ signed LOIs/paid pilots

### Cut list (what we stop)

| What we stop | Rationale | Impact |
|---|---|---|
| General support copilot feature development | All engineering effort goes to returns AI | Existing 3 SMB customers get maintenance only (bug fixes, no new features) |
| SMB outbound sales prospecting | Founder switches entirely to mid-market returns outreach | Pipeline of SMB prospects goes cold |
| Multi-channel support features (chat, email, phone routing) | Returns MVP only needs one input channel (returns portal / email) | Simplifies build scope dramatically |
| General NLP training for broad support categories | Retrain models specifically for returns language/classification | Faster iteration on a narrower domain |

### Timeline

#### Week 1 (Mar 17-23): Discovery + Foundation

**Founder (sales/customer dev):**
- Call every churned SMB customer (exit interviews) -- learnings inform pivot
- Call the 3 retained SMB customers -- understand what they love (may reveal returns usage)
- Research and build a target list of 30+ mid-market e-commerce companies
- Begin outreach to the mid-market companies who already expressed interest in returns AI
- Book 8+ discovery calls for Week 1-2

**Engineers:**
- Audit existing codebase: identify what can be reused for returns-specific AI
- Design the returns classification model architecture
- Set up a returns-specific training dataset (use publicly available returns data + synthetic data)
- Begin Shopify Plus integration research

**Deliverables by end of Week 1:**
- Completed churn/retention interviews (minimum 5 calls)
- Target list of 30+ mid-market prospects
- 5+ discovery calls completed or booked
- Technical architecture doc for returns AI MVP

#### Week 2 (Mar 24-30): Validate Demand + Build Core

**Founder:**
- Complete 8+ discovery calls; document pain points, volume, current costs, willingness to pay
- Present pricing ($1,500-3,000/month) to qualified prospects
- Begin LOI conversations with top 3 prospects
- Draft new landing page copy (returns-focused positioning)

**Engineers:**
- Build returns classification model (v1: rule-based + ML hybrid)
- Build policy matching engine (configurable rules per merchant)
- Begin Shopify Plus returns data integration

**Gate 1 check (Mar 31): Do we have 5+ qualified discovery calls completed?**
- YES: Continue.
- NO: Pause and reassess whether we can reach this ICP within runway.

**Deliverables by end of Week 2:**
- Discovery call summary with patterns (pain ranking, volume data, willingness to pay)
- Working returns classifier (tested on synthetic data)
- New landing page live
- Gate 1 decision documented

#### Week 3 (Mar 31 - Apr 6): Close Pilots + Demo-Ready Product

**Founder:**
- Push for 2+ LOI/paid pilot commitments
- Share demo with top prospects (even if rough)
- Continue discovery calls to build pipeline behind initial pilots
- Prepare investor update email (pivot rationale + early signal)

**Engineers:**
- Complete Shopify Plus integration (read returns data, write resolution status)
- Build dashboard (returns volume, auto-resolution rate, cost savings)
- Run classifier on first design partner's historical data to measure accuracy
- Fix critical bugs and polish demo flow

**Gate 2 check (Apr 7): Do we have 2+ LOIs at $1,500+/month?**
- YES: Proceed to live pilots.
- NO: ACV hypothesis is wrong. Strategy session to consider lower pricing or alternative pivot.

**Deliverables by end of Week 3:**
- 2+ signed LOI/paid pilot agreements
- Demo-ready product with Shopify Plus integration
- Accuracy metrics on historical data (target: >50% correct auto-classification)
- Gate 2 decision documented

#### Week 4 (Apr 7-14): Live Pilots + Decision

**Founder:**
- Onboard first 2-3 pilot customers (white-glove setup)
- Monitor usage daily; call pilot customers every 2-3 days for feedback
- Prepare the Pivot Decision Memo for final decision on Apr 14
- Send investor update (pivot progress, early results)

**Engineers:**
- Support live pilot onboarding and integration
- Monitor auto-resolution accuracy in production; iterate on model
- Instrument usage analytics (returns processed, manual overrides, time savings)
- Fix production issues in real-time

**Gate 3 check (Apr 14): Can the product demo >50% auto-resolution on real data?**
- YES: Commit to the pivot for the next 4 weeks (Weeks 5-8 execution).
- NO: Narrow scope (e.g., apparel returns only) or extend by 2 weeks with revised targets.

**Deliverables by end of Week 4:**
- 2+ pilot customers processing live returns
- Week 1 pilot data (volume, auto-resolution rate, customer feedback)
- Final pivot decision documented and communicated
- Weeks 5-8 execution plan based on pilot learnings

### Weeks 5-8 (post-decision): Execution and Gate 4

If the pivot is confirmed at Week 4:
- **Scale pilots:** Onboard 3-5 more design partners.
- **Iterate on product:** Improve auto-resolution rate based on live data.
- **Build case study:** Quantified ROI from first pilot customer.
- **Prepare for fundraising or revenue milestones:** 3+ paid customers, $5k+ MRR target by Week 8.

**Gate 4 check (May 12, Week 8): Are 2+ of 3+ design partners still actively using the product after 2+ weeks?**
- YES: PMF signal. Continue scaling. Begin fundraising preparation.
- NO: Kill. Convene strategy session with ~3 months of runway remaining. Evaluate Option D (API/platform), Option E (fraud), or wind-down.

### Rollback / Exit Plan

If the pivot fails at any gate:
- **Gate 1 or 2 failure (Weeks 2-3):** Return to Option A (returns for SMBs with sharper positioning) or evaluate Option D (API/platform). We've lost 2-3 weeks but have 4+ months of runway.
- **Gate 3 failure (Week 4):** Narrow technical scope or extend by 2 weeks. If still failing, switch to a lower-technical-risk option.
- **Gate 4 failure (Week 8):** With ~3 months of runway, options are: (a) pursue Option D or E with learnings from the returns exploration, (b) seek acqui-hire or soft landing, (c) return remaining capital to investors.
- **At all stages:** The 3 existing SMB customers remain on maintenance. If we fully revert, their revenue ($600/month) provides a small base.

### Comms Plan

- **Team (Week 1):** Founder holds a 1-hour "pivot kickoff" meeting. Share this document. Discuss concerns openly. Align on the 4-week sprint commitment and decision gates. Key message: "We're not abandoning what we built -- we're focusing it on where we see the strongest pull."
- **Existing customers (Week 1-2):** Email to 3 paying SMB customers: "We're improving our product with a focus on returns automation. Your current service continues unchanged. We'd love your feedback on whether returns/refunds is a pain point for you too."
- **Investors/advisors (Week 3):** Send a concise update: what we learned, why we're pivoting, the thesis, early demand signals, timeline to next decision. Frame as disciplined execution, not panic. Ask for introductions to mid-market e-commerce contacts.
- **Prospects (ongoing):** New outreach uses returns-focused messaging. Old SMB pipeline gets a "we've evolved our focus" note with an option to stay in touch.

---

## 8) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Mid-market sales cycles are 8+ weeks even at this ACV | Medium | High (burns runway without revenue) | Use concierge pilots and design partner framing to compress cycles; offer first-month-free pilot to reduce friction |
| Technical complexity of returns auto-resolution is higher than expected | Medium | Medium (delays product readiness) | Start with rule-based system (configurable policies), layer ML on top; narrow to one returns category if needed |
| Mid-market customers need SOC 2 / enterprise security before committing | Medium | Medium (blocker for some prospects) | Target "early adopter" mid-market companies comfortable with startup vendors; begin SOC 2 prep in parallel but don't gate on it |
| Team of 3 cannot support mid-market customers and build product simultaneously | High | High (quality suffers, burns out team) | Strict scope discipline; white-glove onboarding for first 3 only; automate setup as much as possible; hire first support/success person if we hit Gate 2 |
| The mid-market "pull" signal was a mirage (2-3 curious companies, not a market) | Low-Medium | Critical | Gate 1 (Week 2) tests this explicitly. If demand signal is weak, pivot to alternative option early. |
| Existing SMB customers churn during pivot transition | Medium | Low (only $600 MRR at risk) | Maintain basic service; communicate proactively; these customers are low enough in number to manage personally |

### Open Questions

1. **How many mid-market companies have already reached out about returns?** Need exact count, company names, and qualification level before starting outreach.
2. **What e-commerce platforms do mid-market companies use?** Shopify Plus is assumed, but BigCommerce, Magento, or custom platforms may require different integration strategies.
3. **What does the competitive landscape look like for returns-specific AI?** Are there established players (Loop, Returnly/Affirm, Narvar) that already solve this? What's our differentiation?
4. **Should we consider a co-sell or partnership with a returns logistics company** (e.g., Happy Returns, Optoro) rather than going direct?
5. **What is the right legal/privacy framework for handling returns data** (PII, payment info) in pilot agreements?

### Next Steps (This Week)

| Action | Owner | Due |
|---|---|---|
| Compile list of mid-market companies who've expressed interest; qualify them | Founder | Mar 18 |
| Complete exit interviews with churned SMB customers | Founder | Mar 20 |
| Interview retained SMB customers about returns-specific usage | Founder | Mar 20 |
| Audit codebase for returns-reusable components; write technical architecture doc | Engineers | Mar 21 |
| Build outbound prospect list (30+ mid-market e-commerce targets) | Founder | Mar 21 |
| Begin outreach and book first 5 discovery calls | Founder | Mar 23 |
| Set up returns classification training pipeline | Engineers | Mar 23 |
| Send this pack to any advisors/investors for feedback | Founder | Mar 19 |

---

## Pivot Decision Memo (Shareable Summary)

### Decision

**Pivot from general AI support copilot for SMBs to returns/refunds AI for mid-market e-commerce.** Validate over 4 weeks with a design partner sprint. Final commitment decision on April 14, 2026.

### Why now

- D30 retention of 40% and 6-week sales cycles at $200/month ACV indicate a fundamental value-market mismatch, not just an execution problem.
- Mid-market companies are reaching out unprompted for returns-specific AI -- this is organic pull that we are not currently serving.
- With 5 months of runway ($180k), we have exactly enough time for one well-executed pivot attempt with decision gates. Waiting costs us optionality.

### What we learned / evidence

- General AI support is a moderate pain for SMBs; it does not create enough urgency to drive fast sales or sustained retention.
- Returns/refunds processing is a specific, quantifiable pain for larger e-commerce companies with clear ROI (each return costs $10-30 to process manually).
- Our existing AI/NLP infrastructure can be narrowed and deepened for returns rather than rebuilt from scratch.
- The exhaustion check confirmed that while some non-pivot levers remain (positioning, pricing), they are unlikely to solve the core retention problem within our runway.

### Options considered

1. Narrow to returns for SMBs (10% pivot -- preserves ICP, but may not solve volume/ACV problem)
2. **Returns/refunds AI for mid-market (200% pivot -- RECOMMENDED; follows demand, higher ACV, quantifiable ROI)**
3. General support, move upmarket (10% pivot -- red ocean, no differentiation)
4. Returns API/platform play (200% pivot -- high potential but slow time-to-revenue)
5. Refund fraud detection (200% pivot -- large market but cold-start data problem)
6. Persevere with current direction (high risk given retention and runway signals)

### Plan + decision gates

- **4-week validation sprint** with weekly decision gates.
- Gate 1 (Week 2): 5+ qualified discovery calls or pause.
- Gate 2 (Week 3): 2+ paid pilot LOIs or reassess pricing/ACV.
- Gate 3 (Week 4): Working demo with >50% auto-resolution or narrow scope.
- Gate 4 (Week 8): 2+ retained design partners or kill.

### Risks / Open questions / Next steps

- **Top risk:** Team of 3 may struggle to serve mid-market while building. Mitigation: strict scope, white-glove for first 3 only.
- **Top open question:** Is the mid-market pull signal broad or narrow? Gate 1 tests this.
- **Immediate next step:** Qualify existing inbound interest and begin discovery calls this week.

---

**Human checkpoint:** The founder/CEO must review this pack and make the final pivot decision. This document provides the analysis, framework, and plan -- but the commitment to execute must come from the decision owner. Target decision date: **April 14, 2026**.

---

## Self-Assessment: Quality Gate

### Checklist verification

| Checklist | Status | Notes |
|---|---|---|
| **A) Input readiness** | PASS | Decision is explicit and time-bounded (Apr 14); runway stated (5 months / $180k); product/persona/promise stated; evidence listed with gaps labeled; constraints stated. |
| **B) Exhaustion check (Butterfield rule)** | PASS | 6 non-pivot levers evaluated with quality-of-attempt assessment; "last best tries" (churn interviews, positioning) are time-boxed and parallel to pivot; pivot rationale ties to runway and low expected value of remaining levers. |
| **C) Pivot options quality** | PASS | 6 options (exceeds 4-8 minimum); 3 classified as 200% pivots (Options B, D, E); each includes "why this could win," "what must be true," and biggest risks; distribution wedge included for recommended option. |
| **D) Pivot thesis + metrics** | PASS | Thesis is falsifiable (persona/problem/promise); North Star defined with baseline and target; 5 leading indicators with weekly targets; 4 guardrails; 4 dated kill criteria with explicit decisions. |
| **E) Validation + execution plan** | PASS | Hard truth test included (live returns processing with unassisted usage); cut list is concrete (4 items); owners assigned for all workstreams; 4 decision gates with dates; rollback plan for each gate failure. |
| **F) Finalization** | PASS | Risks, open questions, and next steps all present with owners; memo is self-contained and shareable async; human checkpoint reiterated (founder, Apr 14). |

### Rubric scoring

| Criterion | Score | Rationale |
|---|---|---|
| 1) Decision framing | 2 | Owner (founder/CEO), date (Apr 14), and binary decision ("pivot to returns for mid-market vs. persevere vs. alternative pivot") all explicit. |
| 2) Evidence quality | 2 | Evidence inventoried in structured table with fact/assumption/gap tags; 5 evidence gaps named with plans to fill them (discovery calls, churn interviews). |
| 3) Diagnosis clarity | 2 | Top 4 bottlenecks ranked; each has a root cause hypothesis; signal vs. execution clearly separated in a table; specific (40% D30, 6-week cycles, mid-market pull). |
| 4) Exhaustion check integrity | 2 | 6 levers evaluated with quality-of-attempt; 2 "last best tries" time-boxed; pivot rationale links to runway constraints and low expected value of remaining levers. |
| 5) Option set quality | 2 | 6 options across the 4P grid; 3 are 200% pivots; each has "what must be true," distribution path, and risks; meaningfully distinct. |
| 6) Thesis quality | 2 | Persona, problem, promise, proof, pricing, and distribution all specified; falsifiable within 4-week time-box; internally consistent (mid-market + higher ACV + returns-specific depth). |
| 7) Metrics and gates | 2 | North Star with baseline and target; 5 leading indicators with weekly check-ins; 4 guardrails; 4 kill criteria with dates and explicit decisions. |
| 8) Validation plan strength | 2 | Hard truth test (live returns processing, unassisted usage for 1 week); 5 learning goals each mapped to specific decisions if failed. |
| 9) Execution realism | 2 | Plan fits 5-month runway (4-week sprint uses ~$36k x 1 = ~$36k, leaving $144k for execution); cut list names 4 specific items; each week has owner-level assignments; team of 3 allocation is explicit. |
| 10) Shareability + safety | 2 | Self-contained memo section readable without context; risks (6), open questions (5), and next steps (8) all present with owners; human checkpoint prominently stated. |
| **Total** | **20/20** | |
