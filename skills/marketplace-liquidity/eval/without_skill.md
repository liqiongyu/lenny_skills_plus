# Marketplace Liquidity Improvement Plan: SF Evening Dog Walking

## Executive Summary

This plan targets improving the booking fill rate from 55% to 75% for SF evening slots (5-9 PM) within 6 weeks. The core problem is a supply-demand imbalance during peak evening hours, resulting in an 18-minute p50 time-to-book (target: under 10 minutes) and a 9% cancellation rate. We will deploy a combination of supply-side incentives, demand shaping, matching algorithm improvements, and operational changes within the $25k/month incentive budget and limited engineering capacity.

---

## 1. Problem Diagnosis

### Current State
- **Fill rate**: 55% (SF evenings)
- **p50 time-to-book**: 18 minutes (target: <10 min)
- **Cancellation rate**: 9%
- **Markets**: NYC, SF, LA (focus: SF)
- **Core action**: Request to booked within 10 minutes

### Root Cause Hypotheses
1. **Insufficient evening supply**: Not enough walkers available during 5-9 PM peak hours in SF.
2. **Geographic mismatch**: Walkers are concentrated in certain neighborhoods while demand is spread across others.
3. **Pricing doesn't reflect urgency**: Flat or static pricing fails to attract walkers during high-demand windows.
4. **Slow matching**: The current matching algorithm takes too long to find and confirm walkers.
5. **Cancellation drag**: 9% cancellations waste supply and create rebooking delays that inflate time-to-book.

### Key Metrics to Track
| Metric | Baseline | Week 3 Target | Week 6 Target |
|--------|----------|---------------|---------------|
| Fill rate (SF evenings) | 55% | 65% | 75% |
| p50 time-to-book | 18 min | 12 min | <10 min |
| Cancellation rate | 9% | 7% | 5% |
| Active evening walkers (SF) | TBD | +30% | +50% |
| Requests per evening | TBD | Stable or +10% | Stable or +15% |

---

## 2. Strategy Overview

Four parallel workstreams, ordered by expected impact and feasibility:

| Workstream | Expected Impact | Eng Effort | Budget |
|------------|----------------|------------|--------|
| A. Supply Activation & Incentives | High | Low | $18k/mo |
| B. Matching & Booking Speed | High | Medium | $0 |
| C. Cancellation Reduction | Medium | Low | $3k/mo |
| D. Demand Shaping | Medium | Low | $4k/mo |

---

## 3. Workstream A: Supply Activation & Incentives ($18k/month)

### A1. Evening Surge Bonuses (Weeks 1-6)
- **What**: Offer $5-$10 per-walk bonus for walks accepted during 5-9 PM in SF.
- **Tiered structure**:
  - $5 bonus for walks accepted within 5 minutes of request (speed incentive)
  - $8 bonus for walks in underserved zones (geographic incentive)
  - $10 bonus for walkers who complete 4+ evening walks in a week (consistency incentive)
- **Budget**: ~$12k/month (assuming 1,500-2,000 qualifying walks/month)
- **Eng effort**: Low -- configure bonus rules in existing payment system.

### A2. Guaranteed Earnings Floor (Weeks 1-6)
- **What**: Guarantee walkers $25/hour if they commit to being available 5-9 PM at least 3 evenings per week in SF.
- **Mechanism**: If a walker's actual earnings fall below $25/hr during their committed window, we top up the difference.
- **Budget**: ~$4k/month (most walkers will earn above floor; this is insurance against slow nights)
- **Eng effort**: Low -- manual calculation and payout initially, automate later.

### A3. Reactivation Campaign (Weeks 1-2)
- **What**: Identify churned or dormant SF walkers (inactive 30-90 days). Send targeted push/SMS/email with a "$50 comeback bonus for your first 5 evening walks this week" offer.
- **Budget**: ~$2k/month
- **Eng effort**: None -- use existing CRM/messaging tools.

### A4. Walker Referral Burst (Weeks 1-4)
- **What**: Temporarily increase walker referral bonus to $75 (from standard) for SF, specifically for walkers who complete their first evening walk within 7 days of signup.
- **Budget**: Included in A1 envelope.
- **Eng effort**: None -- update referral config.

---

## 4. Workstream B: Matching & Booking Speed ($0 incremental budget)

### B1. Reduce Matching Radius Dynamically (Weeks 1-3)
- **What**: During evening hours, pre-position the matching algorithm to prioritize walkers who are already nearby rather than waiting for the "best" match.
- **Current likely behavior**: Algorithm searches for optimal walker (rating, distance, preference). This takes time.
- **Change**: During peak hours, switch to "first available within 0.5 miles" mode. Expand radius only if no match in 2 minutes.
- **Expected impact**: Reduce p50 time-to-book by 4-6 minutes.
- **Eng effort**: Medium -- requires algorithm change, but likely a configuration/flag approach.

### B2. Pre-Matching / Predictive Dispatch (Weeks 3-6)
- **What**: Use historical request patterns to pre-alert walkers 15-30 minutes before expected demand spikes in their zone.
- **Mechanism**: Push notification: "High demand expected near Marina District at 6 PM -- go online to earn bonus."
- **Eng effort**: Medium -- requires basic demand forecasting model + notification trigger.

### B3. Auto-Accept for Trusted Walkers (Weeks 2-4)
- **What**: Allow top-rated walkers (4.8+ stars, 50+ walks, <3% cancel rate) to opt into auto-accept mode. When a request comes in, it's instantly confirmed without requiring manual acceptance.
- **Expected impact**: Eliminates the walker-side acceptance delay (often 3-8 minutes).
- **Eng effort**: Medium -- new opt-in flow + matching logic change.

### B4. Parallel Dispatch (Week 1)
- **What**: Instead of sequentially offering a walk to one walker at a time (waiting for timeout before trying the next), send the request to 3 walkers simultaneously. First to accept wins.
- **Expected impact**: Reduces time-to-book by eliminating sequential timeout delays.
- **Eng effort**: Low-Medium -- depends on current architecture.

---

## 5. Workstream C: Cancellation Reduction ($3k/month)

### C1. Cancellation Fee Enforcement (Week 1)
- **What**: Enforce a $10 cancellation fee for walker-side cancellations within 30 minutes of a booked walk. Customer-side cancellations: $5 fee if cancelled within 15 minutes of walk start.
- **Current state**: Likely lenient or no enforcement, contributing to the 9% rate.
- **Eng effort**: Low -- policy change + update in app.

### C2. Cancellation Replacement Priority Queue (Weeks 2-4)
- **What**: When a cancellation occurs, immediately re-enter the request into matching with "urgent" priority and offer the replacement walker a $5 rescue bonus.
- **Budget**: ~$3k/month (assuming ~300 cancellations/month needing rescue)
- **Eng effort**: Low -- priority flag in matching queue.

### C3. Walker Reliability Score (Weeks 3-6)
- **What**: Introduce a visible reliability score that factors into walker ranking and bonus eligibility. Walkers with high cancel rates get deprioritized in matching.
- **Expected impact**: Behavioral nudge to reduce cancellations over time.
- **Eng effort**: Low -- add score calculation, surface in walker app.

---

## 6. Workstream D: Demand Shaping ($4k/month)

### D1. Off-Peak Discounts (Weeks 1-6)
- **What**: Offer $3-$5 discount for customers who book walks at 4-5 PM or 9-10 PM (shoulder hours) instead of the 6-8 PM core peak.
- **Goal**: Flatten the demand curve so supply can serve more requests without adding walkers.
- **Budget**: ~$3k/month
- **Eng effort**: Low -- discount code or automatic pricing rule.

### D2. Scheduled Walks Promotion (Weeks 1-4)
- **What**: Encourage customers to schedule recurring evening walks (e.g., every weekday at 6 PM) rather than on-demand requests. Offer a 10% discount for weekly recurring bookings.
- **Benefit**: Predictable demand allows pre-committed supply; walkers can plan their evenings.
- **Budget**: ~$1k/month in discounts
- **Eng effort**: Low -- if scheduling feature exists; Medium if it needs to be built.

### D3. Wait Time Transparency (Week 1)
- **What**: Show customers estimated wait time before they request. "Current wait: ~15 min. Book for 7:30 PM instead for instant confirmation."
- **Expected impact**: Reduces failed bookings and sets expectations; nudges demand to available slots.
- **Eng effort**: Low -- surface existing matching data in UI.

---

## 7. Implementation Timeline

### Week 1: Quick Wins
- Launch evening surge bonuses (A1)
- Activate reactivation campaign (A3)
- Enable parallel dispatch (B4)
- Enforce cancellation fees (C1)
- Show wait time transparency (D3)
- Launch off-peak discounts (D1)

### Week 2: Supply & Speed
- Launch guaranteed earnings floor (A2)
- Launch walker referral burst (A4)
- Ship auto-accept opt-in for trusted walkers (B3)
- Launch scheduled walks promotion (D2)

### Week 3: Matching Intelligence
- Deploy dynamic matching radius (B1)
- Launch cancellation replacement priority queue (C2)
- Begin demand forecasting model work (B2)

### Week 4: Iterate
- Analyze Week 1-3 data. Adjust bonus amounts based on elasticity.
- Tune matching radius thresholds.
- Launch walker reliability score (C3)

### Week 5: Scale
- Deploy pre-matching / predictive dispatch (B2)
- Optimize incentive spend: shift budget from underperforming levers to top performers.

### Week 6: Stabilize & Measure
- Full measurement against targets.
- Document playbook for replication in NYC and LA.
- Plan incentive taper to find sustainable equilibrium.

---

## 8. Budget Allocation

| Category | Monthly Budget | % of Total |
|----------|---------------|------------|
| Evening surge bonuses | $12,000 | 48% |
| Guaranteed earnings floor | $4,000 | 16% |
| Reactivation & referral bonuses | $2,000 | 8% |
| Cancellation rescue bonuses | $3,000 | 12% |
| Demand-side discounts | $4,000 | 16% |
| **Total** | **$25,000** | **100%** |

---

## 9. Measurement & Decision Framework

### Weekly Review Cadence
Every Monday, review the following dashboard:
1. **Fill rate** by hour (5 PM, 6 PM, 7 PM, 8 PM, 9 PM)
2. **p50 and p90 time-to-book** by hour
3. **Active walkers online** by hour and zone
4. **Cancellation rate** (walker-side vs. customer-side)
5. **Incentive spend per incremental booking**
6. **Unit economics**: Revenue per walk vs. cost (including incentives)

### Decision Rules
- If a lever shows <5% improvement after 2 weeks, reallocate its budget.
- If fill rate hits 70% by Week 3, begin tapering bonuses by 20% to test sustainability.
- If cancellation rate doesn't drop below 7% by Week 3, escalate enforcement (ban repeat offenders).
- If time-to-book doesn't improve with parallel dispatch, prioritize B1 (dynamic radius) engineering work.

### Kill Criteria
- Abort a workstream if cost-per-incremental-booking exceeds $15 (not sustainable at typical walk margins).
- If overall fill rate regresses below 50%, pause demand-side promotions to avoid worsening the experience.

---

## 10. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Incentives attract low-quality walkers | Medium | High | Gate bonuses behind minimum rating (4.5+) and background check completion |
| Walkers game the system (go online but decline requests) | Medium | Medium | Track accept rate; require >80% accept rate for bonus eligibility |
| Demand increases faster than supply (incentives attract customers too) | Low | High | Pause demand-side discounts if fill rate drops |
| Engineering delays on matching improvements | High | Medium | Front-load no-eng changes (Weeks 1-2); matching improvements are additive, not blocking |
| Budget overrun from higher-than-expected bonus qualifying rate | Medium | Medium | Set weekly budget caps with automatic bonus reduction triggers |
| Walker fatigue / churn after incentives end | Medium | High | Taper gradually; build habit through recurring bookings; improve non-monetary walker experience |

---

## 11. Success Criteria

**Primary**: SF evening fill rate reaches 75% by end of Week 6.

**Secondary**:
- p50 time-to-book < 10 minutes
- Cancellation rate < 6%
- Incentive cost per booking < $10
- No degradation in walker or customer NPS

**Stretch**: Develop a repeatable playbook that can be applied to NYC and LA evening slots within the following quarter.

---

## 12. Post-Campaign Sustainability Plan

Reaching 75% is necessary, but sustaining it without $25k/month in perpetual incentives is the real goal.

1. **Taper incentives gradually** (Weeks 7-10): Reduce bonuses by 25% every 2 weeks. Monitor fill rate elasticity.
2. **Lock in recurring supply**: Convert bonus-motivated walkers into habitual evening walkers through scheduling commitments and reliability rewards.
3. **Dynamic pricing**: Replace flat incentives with algorithmic surge pricing that self-adjusts based on real-time supply-demand ratio.
4. **Expand the walker base permanently**: The referral and reactivation campaigns should yield a structurally larger supply pool that persists beyond the incentive period.
5. **Product improvements stick**: Matching algorithm changes, auto-accept, parallel dispatch, and wait time transparency are permanent improvements with zero ongoing cost.
