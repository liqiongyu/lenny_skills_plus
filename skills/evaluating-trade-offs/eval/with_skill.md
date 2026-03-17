# Trade-off Evaluation Pack: SEO Content Infrastructure vs Paid Acquisition Tooling

---

## 1) Trade-off Brief

**Decision (one sentence):**
We are choosing whether to dedicate our sole growth engineer for Q2-Q3 2026 to building SEO content infrastructure or paid acquisition tooling, in order to grow from $80k to $200k ARR by Q4 2026.

**Decision owner:** Head of Growth / CEO (30-person B2B SaaS)

**Decision date:** End of current sprint (before Q2 planning commits the engineer)

**Why now:**
- The growth engineer's Q2-Q3 allocation must be locked this cycle; delay means losing a quarter of execution time.
- $80k to $200k ARR ($120k net new) in ~6 months is aggressive -- wrong bet means missing the target and potentially a funding/runway problem.
- Both options require sustained engineering focus; splitting the engineer across both produces neither outcome well.

**Time horizon:** 6 months (Q2-Q3 2026), with compound effects evaluated over 12-18 months.

**Context:**
- 30-person B2B SaaS company. One growth engineer available (no additional hiring assumed).
- Current ARR: $80k. Target: $200k ARR by end of Q4 2026 (2.5x growth).
- No existing SEO infrastructure or paid acquisition tooling in place (greenfield for both).
- Paid acquisition would require $8k/month ongoing ad spend on top of engineering investment.
- SEO has compounding returns but requires 6+ months before meaningful organic pipeline materializes.

**Constraints / non-negotiables:**
- One growth engineer only (cannot split or hire a second in the timeframe).
- Must hit $200k ARR by Q4 2026 -- this is a hard gate (likely tied to funding/board milestone).
- Total budget for paid media: capped at $8k/month ($48k over 6 months).
- Cannot sacrifice core product stability or current customer retention.

**Options:**
- **Option A: SEO Content Infrastructure** -- Build programmatic content engine, landing pages, internal linking tooling, and keyword-targeted content pipeline.
- **Option B: Paid Acquisition Tooling** -- Build attribution, audience management, landing page optimization, and automated campaign tooling for paid channels.
- **Option C: Sequenced hybrid** -- Paid tooling first (Q2, ~10 weeks), then pivot engineer to SEO infrastructure (Q3). Accept sub-optimal execution on both.
- **Do nothing:** Continue current organic/manual growth channels. Unlikely to close the $120k ARR gap.

**Success metrics:**
1. Net new ARR added by Q4 2026 (target: $120k net new).
2. Customer acquisition cost (CAC) trajectory -- declining or stable, not spiraling.
3. Pipeline-to-close velocity (weeks from first touch to signed contract).

**Guardrails:**
- Customer retention rate must not drop below 90% (no neglecting existing customers).
- Engineering velocity on core product must not degrade more than 10%.
- Brand/reputation: no spammy SEO or low-quality paid placements.
- Total cash outlay (eng time + media spend + tooling) must be survivable on current runway.

---

## 2) Options + Criteria Matrix

| Criterion | Definition (observable) | Weight | Option A: SEO Infra | Option B: Paid Tooling | Option C: Sequenced Hybrid | Notes / Assumptions |
|---|---|---:|---|---|---|---|
| **ARR impact by Q4** | Net new ARR attributable to channel by end of Q4 2026 | High | Low-Med (slow ramp) | Med-High (immediate pipeline) | Med (split focus) | SEO unlikely to produce material ARR in 6 months; paid can produce pipeline in weeks |
| **Time-to-pipeline** | Weeks until first qualified leads appear | High | 12-26 weeks | 4-8 weeks | 4-8 weeks (paid first) | Critical given the Q4 hard deadline |
| **CAC sustainability** | Unit economics trend over 12 months | Med | Excellent (near-zero marginal cost) | Poor-Fair ($8k/mo ongoing) | Fair | SEO compounds; paid is linear with spend |
| **12-month compounding** | Does the channel get better over time without proportional spend increase? | Med | High (content compounds) | Low (stops when spend stops) | Med | Key differentiator beyond the 6-month window |
| **Cash outlay (6 months)** | Total cash required beyond eng salary | Med | Low (~$2-5k tooling) | High (~$50-55k media + tooling) | Med (~$30-35k) | Paid requires $48k media spend alone |
| **Execution risk** | Probability the engineer can deliver a working system in the timeframe | Med | Med (content strategy is harder to get right) | Med-High (paid tooling is more predictable) | High (context switching, two half-baked systems) | SEO requires content + technical SEO expertise; paid is more mechanical |
| **Reversibility** | How easy to change course if it's not working | Low | High (content persists; infra reusable) | Med (tooling reusable; spend is sunk) | Low (lost time on both) | SEO assets persist even if you stop; paid spend is gone |
| **Guardrail: brand quality** | Risk of brand damage from channel | Guardrail | Low (quality content builds trust) | Med (poor ads can harm brand) | Med | B2B buyers are sensitive to quality signals |

**Not optimizing for:**
- Long-term (3-5 year) channel mix strategy -- this decision is about the next 6 months.
- Perfection of either system -- we need "good enough to produce pipeline," not best-in-class infrastructure.

---

## 3) All-in Cost + Opportunity Cost Table

Assumptions: Growth engineer fully loaded cost ~$180k/year = ~$90k for 6 months. This cost is incurred regardless of option chosen, so we focus on *incremental* costs and the *opportunity cost* of the engineer's time.

| Cost Area | Option A: SEO Infra | Option B: Paid Tooling | Option C: Sequenced Hybrid | Notes |
|---|---:|---:|---:|---|
| **Engineering build (6 months)** | $90k (fully allocated) | $90k (fully allocated) | $90k (fully allocated) | Same engineer cost regardless |
| **Tools / vendors** | $2-5k (CMS, keyword tools, analytics) | $3-8k (attribution, landing page tools, analytics) | $4-10k (both toolsets) | Assumes existing analytics stack is minimal |
| **Media / ad spend** | $0 | $48k ($8k/mo x 6 months) | $24-32k ($8k/mo x 3-4 months paid window) | This is the biggest cash differentiator |
| **Content creation (non-eng)** | $5-15k (freelance writers, design) | $2-5k (ad creative) | $5-12k (both) | SEO needs substantially more content production |
| **Maintenance / on-call** | Low ($1-2k/mo after build) | Med ($2-3k/mo monitoring + optimization) | High ($3-5k/mo, two systems) | Paid requires ongoing campaign management |
| **Coordination / change mgmt** | Low (mostly eng + marketing) | Med (eng + marketing + sales alignment for lead routing) | High (two workstreams, more handoffs) | Paid leads need faster sales follow-up |
| **Risk cost (if fails)** | Low (content assets persist) | Med-High ($48k media spend is unrecoverable) | High (worst of both: time lost + some spend sunk) | SEO failure mode is "slow"; paid failure mode is "expensive" |
| **TOTAL incremental cost (6 months)** | **$7-22k** | **$53-61k** | **$33-54k** | Excluding the engineer salary (sunk either way) |

**Opportunity cost (what gets displaced):**
- **If we pick Option A (SEO):** We defer paid acquisition tooling entirely. No paid pipeline for 6+ months. We rely solely on existing channels + emerging SEO to bridge the $120k gap. High risk of missing Q4 target.
- **If we pick Option B (Paid):** We defer SEO infrastructure. No compounding organic channel being built. After 6 months, we have pipeline but are dependent on continued $8k/mo spend to maintain it. No "earned" channel.
- **If we pick Option C (Hybrid):** We get a partial version of both. Paid tooling is ~60% complete before switching; SEO infra starts late and has even less time to compound. Engineer context-switches, reducing effectiveness by an estimated 20-30%.
- **If we do nothing:** Current growth trajectory continues. If current channels add ~$3-5k ARR/month, we reach ~$98-110k ARR by Q4 -- well short of $200k.

---

## 4) Impact Ranges (Order-of-Magnitude)

| Option | Expected Upside Range (net new ARR by Q4) | Expected Downside Range | Time-to-Impact | Confidence | Key Assumptions (top 2-3) |
|---|---|---|---|---|---|
| **A: SEO Infra** | $10-40k net new ARR by Q4; $60-150k by Q4+6mo | $0-10k by Q4 (too slow to matter) | 12-26 weeks to first leads | Low-Med | (1) Content ranks within 4-6 months; (2) B2B buyer intent keywords exist with sufficient volume; (3) Conversion rate from organic is comparable to other B2B SaaS benchmarks (2-5%) |
| **B: Paid Tooling** | $60-120k net new ARR by Q4 | $20-40k net new ARR by Q4 (poor targeting/conversion) | 4-8 weeks to first leads | Medium | (1) $8k/mo budget is sufficient to generate 15-30 qualified leads/month at ~$300-500 CAC; (2) Sales can close paid leads at current close rate (~15-25%); (3) ACV is ~$3-8k so 15-40 new customers closes the gap |
| **C: Hybrid** | $40-80k net new ARR by Q4 | $15-30k net new ARR by Q4 | 4-8 weeks (paid first) | Low-Med | (1) Engineer can context-switch without major ramp cost; (2) Partial paid tooling (10 weeks) is sufficient for campaign management; (3) Q3 SEO build produces some pipeline by late Q4 |
| **Do Nothing** | $18-30k net new ARR by Q4 | $10-18k net new ARR by Q4 | Ongoing (current pace) | Medium | Current channels continue at $3-5k/month net new ARR |

**10x check:**
- Paid (Option B) is plausibly 3-10x better than SEO (Option A) **within the 6-month Q4 window**, because it produces pipeline immediately vs. SEO's 6+ month lag.
- SEO (Option A) is plausibly 3-10x better than Paid (Option B) **in the 12-18 month window**, because it compounds while paid is linear with spend.
- The critical variable is the Q4 hard deadline. If Q4 is truly non-negotiable, the time-to-impact difference dominates all other factors.

**Assumptions that drive the decision:**
1. **Is Q4 a hard gate?** If $200k ARR by Q4 is truly non-negotiable (e.g., tied to funding), paid acquisition is the only option that can plausibly close the gap in time. If Q4 is aspirational and the real deadline is Q2 2027, SEO changes from "too slow" to "clearly better."
2. **Can $8k/month generate sufficient qualified pipeline?** If CAC is $300-500 per customer with $3-8k ACV, paid math works. If CAC is $1,000+ or ACV is lower, the budget cannot close the gap.
3. **Does the team have content/SEO expertise?** If no one on the team can produce high-quality B2B content and keyword strategy, SEO infrastructure without content is an empty pipe.

---

## 5) Thought Experiments (Pre-mortems)

### Pre-mortem: Option B (Paid Tooling) -- "It's Q4 and we're at $130k ARR. What happened?"
- CAC was higher than expected ($800-1,200) because B2B SaaS audiences are expensive on paid channels; $8k/month only generated 7-10 leads/month instead of 20-30.
- Sales couldn't close paid leads at the same rate as inbound -- paid leads had lower intent and required more nurturing, dropping close rate to 8-12%.
- We spent $48k+ on media and $90k on eng time for a channel that only works while we keep spending. Now we need more budget to sustain pipeline AND we haven't built any organic foundation.
- Attribution was messy; we couldn't tell which campaigns worked, so optimization was slow.

### Pre-mortem: Option A (SEO Infra) -- "It's Q4 and we're at $95k ARR. What happened?"
- SEO took exactly as long as expected (6+ months) and by Q4 we had ~50-100 organic visitors/month, converting at 2% = 1-2 leads/month. Not nearly enough.
- We built great infrastructure but didn't have the content volume or domain authority to rank for competitive B2B keywords.
- We missed the Q4 target entirely and now face the consequences of that miss (funding pressure, team morale, board credibility).

### Cheapest evidence to de-risk the biggest assumption:
1. **Paid CAC validation (1-2 weeks, ~$2-4k):** Before committing the engineer, run a $2-4k manual paid campaign (no tooling) using existing landing pages. Measure actual CPL and lead quality. This directly tests whether $8k/month can generate sufficient pipeline.
2. **SEO keyword/volume audit (2-3 days, $0):** Use free/trial keyword tools to assess whether B2B buyer intent keywords in our space have meaningful search volume. If volume is <500 searches/month for our category, SEO ceiling is very low.
3. **Sales close-rate check on paid leads (thought experiment):** Talk to 2-3 peer B2B SaaS founders about their paid-to-close conversion rates. If industry data shows paid leads close at 50-70% the rate of organic/inbound, adjust the model.

---

## 6) Worse-First + Mitigation Plan

**The "worse first" path is Option B (Paid Tooling):**
Choosing paid means we accept that we are building a non-compounding channel that requires ongoing spend. The short-term gain (immediate pipeline) comes at the cost of long-term CAC efficiency. We are trading future organic leverage for near-term ARR.

**Expected dip:**
- Cash burn increases by $8k/month immediately, tightening runway.
- No organic pipeline is being built; if paid stops, pipeline stops.
- After 6 months, we may have hit the ARR target but are dependent on continued ad spend with no path to reducing CAC.

**Why it's worth it:**
- Hitting $200k ARR by Q4 is a hard gate. Missing it has consequences (funding, board, morale) that outweigh the long-term CAC disadvantage.
- Paid tooling infrastructure is reusable; once built, a second engineer or marketer can operate it while the growth engineer pivots to SEO in Q4.
- We can begin SEO investment in Q4 once the immediate ARR pressure is relieved.

**Leading indicators (watch weekly):**
- Cost per lead (CPL) by channel/campaign -- target: < $400
- Leads generated per week -- target: 4-7 qualified leads/week by week 6
- Lead-to-opportunity conversion rate -- target: > 20%
- Opportunity-to-close rate -- target: > 15%
- Blended CAC -- target: < $2,000 (with $3-8k ACV, payback < 6 months)
- Cash runway impact -- no more than 2 months of runway reduction vs. plan

**Mitigations (managing the dip):**
- Run the $2-4k manual paid test in weeks 1-2 BEFORE committing the engineer full-time. If CPL > $800 or lead quality is poor, reconsider before sinking 6 months.
- Set a hard spend cap at $8k/month with no creep. If the channel can't work within this budget, it won't work at $12k either.
- Have the growth engineer document the paid tooling so a non-engineer (marketing) can operate it by Q3, freeing the engineer to start SEO work earlier.
- Begin lightweight SEO groundwork (keyword research, content briefs, sitemap planning) with marketing team in parallel -- costs nothing and accelerates the eventual SEO build.

**Communication plan:**
- **Who needs to know:** CEO, sales lead, marketing lead, board (if ARR target is a board metric).
- **Message:** "We're investing Q2-Q3 in paid acquisition tooling to hit our $200k ARR target by Q4. This is a deliberate 'worse-first' choice -- we're accepting higher CAC now to generate immediate pipeline, with a plan to layer in SEO infrastructure starting Q4 once the ARR pressure is relieved. We'll review at 6 weeks with clear stop/continue triggers."

---

## 7) Stop/Continue Triggers (Sunk-Cost Reset)

**Sunk-cost reset question:** If we hadn't yet assigned the growth engineer and hadn't spent anything on paid, would we start this today?
**Answer:** Yes -- given the $200k Q4 hard gate, the only channel that can plausibly close a $120k ARR gap in 6 months is one that produces pipeline in weeks, not months. The math strongly favors paid acquisition first, then layering in SEO.

**Review date:** 6 weeks from start of execution (approximately end of Week 6, Q2 2026).

**Owner:** Head of Growth / CEO.

**Continue if (leading indicators):**
- CPL is at or below $500 and trending down with optimization.
- Generating 3+ qualified leads/week by week 4, trending toward 5-7/week by week 6.
- At least 1-2 leads have converted to closed-won or are in late-stage pipeline.
- Sales team confirms lead quality is actionable (not junk leads).
- Cash burn is within planned budget ($8k/month media + tooling costs).

**Stop/pivot if (kill criteria):**
- CPL exceeds $800 after 4 weeks of optimization with no downward trend.
- Fewer than 2 qualified leads/week by week 6 despite full budget deployment.
- Sales rejects > 50% of paid leads as unqualified after initial outreach.
- Close rate on paid leads is < 8% after 6 weeks (indicating fundamental channel-fit problem).
- Cash runway drops below 9 months due to combined spend.

**If we stop, what do we salvage?**
- Paid tooling infrastructure (attribution, landing pages, audience segmentation) is reusable for future paid efforts or for measuring organic channel performance.
- Campaign data and audience insights inform future content strategy and ICP refinement.
- Pivot the growth engineer to SEO infrastructure immediately; the 4-6 weeks of "lost" time means SEO starts later but the remaining ~4 months can still build a foundation for Q1 2027.
- Reduce media spend to $0 immediately; no ongoing commitment.

---

## 8) Recommendation Memo

**Recommendation:** Choose **Option B (Paid Acquisition Tooling)**, with a sequenced plan to begin SEO infrastructure in Q4.

**Confidence:** Medium

**Rationale:**
- The $200k ARR Q4 hard gate eliminates SEO as the primary strategy. SEO's 6+ month lag means even in the best case, it contributes only $10-40k net new ARR by Q4 -- leaving a $80-110k gap. Paid acquisition is the only option with plausible time-to-impact to close a $120k ARR gap in 6 months.
- Order-of-magnitude analysis: paid plausibly delivers $60-120k net new ARR by Q4 vs. SEO's $10-40k. Even in the pessimistic paid scenario ($20-40k), it outperforms SEO's expected case for the Q4 window.
- The $48k media spend is significant but survivable. At $3-8k ACV and 15-40 new customers needed, the math works if CAC stays below ~$1,500. The manual paid test ($2-4k) in weeks 1-2 will validate this assumption before full commitment.
- Paid tooling infrastructure is reusable and can be handed off to marketing, freeing the growth engineer for SEO in Q4. This is a "paid first, SEO second" sequence, not "paid instead of SEO."
- The worse-first dip (higher CAC, cash burn, no organic foundation) is manageable with the defined mitigations, leading indicators, and a 6-week kill switch.

**Key trade-offs (explicit):**
- **We optimize for:** Time-to-pipeline and ARR velocity within the Q4 window.
- **We accept costs:** Higher CAC ($300-500+ per customer vs. near-zero marginal cost for SEO), $48k media spend, and 6 months of no organic channel investment.
- **We are not optimizing for:** Long-term CAC efficiency, organic channel compounding, or sustainable growth economics. These become the focus in Q4+ once the ARR target is secured.

**Risks (with mitigations):**
- **Risk:** B2B paid CAC is higher than modeled ($800-1,200+), making the $8k/month budget insufficient. **Mitigation:** Run $2-4k manual test in weeks 1-2; stop/pivot if CPL > $800 after 4 weeks of optimization.
- **Risk:** Paid leads are lower quality than organic/inbound, dropping close rate below model assumptions. **Mitigation:** Weekly lead quality review with sales; adjust targeting and messaging within first 3 weeks; kill trigger at < 8% close rate by week 6.
- **Risk:** We hit $200k ARR but are dependent on paid spend with no organic flywheel, creating a CAC treadmill. **Mitigation:** Begin SEO infrastructure in Q4; plan for 12-month transition to 50%+ organic pipeline by Q2 2027.
- **Risk:** Growth engineer builds paid tooling but it requires ongoing eng maintenance, preventing the Q4 pivot to SEO. **Mitigation:** Design for handoff from day 1; document tooling for marketing self-service; architect for low-maintenance operation.

**Open questions (that could change the decision):**
1. **How hard is the Q4 $200k gate?** If it is aspirational (not tied to funding/survival), the calculus shifts significantly toward SEO, which is better on every dimension except time-to-impact. This is the single most important question to resolve.
2. **What is the actual B2B paid CAC in our space?** The manual test ($2-4k, 1-2 weeks) will answer this. If CPL > $600, the paid math may not close the gap within budget.
3. **Does the team have any content/SEO capability today?** If a marketing team member can begin content production in parallel (even 1-2 articles/month), the SEO compounding clock starts ticking sooner and reduces Q4+ transition risk.
4. **What is the current ACV and close rate?** The model assumes $3-8k ACV and 15-25% close rate. If ACV is < $2k or close rate is < 10%, neither option closes the $120k gap without more resources.
5. **Can we hire a contract growth marketer to run paid campaigns while the engineer builds SEO?** This would change the "one engineer" constraint and potentially enable a true parallel approach.

**Next steps (owner + date):**

| Action | Owner | Date |
|---|---|---|
| Confirm Q4 $200k ARR is a hard gate (not aspirational) | CEO | This week |
| Run $2-4k manual paid campaign test (no tooling) | Growth engineer + marketing | Weeks 1-2 |
| Complete SEO keyword/volume audit | Marketing | Week 1 (parallel) |
| Review manual test results; make go/no-go on full paid commitment | CEO + Growth lead | End of Week 2 |
| If go: Growth engineer begins paid tooling build | Growth engineer | Week 3 |
| 6-week review against stop/continue triggers | CEO + Growth lead | Week 8 (6 weeks from build start) |
| Begin SEO infrastructure scoping (regardless of paid outcome) | Growth engineer + Marketing | Q4 2026 |

---

## Quality Gate Self-Assessment

| Rubric Category | Score | Notes |
|---|---:|---|
| 1) Framing + options | 2 | Decision is dated, owner identified, 4 options including do-nothing |
| 2) Criteria + horizon | 2 | 8 criteria including guardrails; 6-month and 12-month horizons explicit; "not optimizing for" stated |
| 3) All-in cost + opportunity cost | 2 | Includes hidden costs (maintenance, coordination, risk); opportunity cost per option is explicit |
| 4) Impact ranges + assumptions | 2 | Ranges with confidence; no false precision; 3 key assumptions named and testable |
| 5) Thought experiments + validation | 2 | Specific pre-mortems for top 2 options; cheapest validation tests identified ($2-4k manual test) |
| 6) Recommendation quality | 2 | Explicit recommendation with rationale, trade-offs, risks+mitigations, open questions, next steps, review date, and stop/continue triggers |
| **Total** | **12/12** | |

---

*Generated using the `evaluating-trade-offs` skill pack.*
