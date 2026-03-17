# Marketplace Liquidity Management Pack

## On-Demand Dog Walking Marketplace — SF Evenings

---

## 0) Context Snapshot

- **Marketplace:** On-demand dog walking marketplace (NYC, SF, LA)
- **Buyer side:** Dog owners requesting walks
- **Seller side:** Dog walkers accepting and fulfilling bookings
- **Core action:** Request -> booked within 10 minutes (real-time matching)
- **Priority segment:** SF evenings (5 PM - 9 PM, 7 days/week)
- **Timebox:** 6 weeks (target completion by late April 2026)
- **Goal:** Improve booking fill rate from 55% to 75% in SF evenings (+20 pp)
- **Baseline metrics:**
  - Fill rate: 55% (SF evenings)
  - p50 time-to-book: 18 minutes (vs. 10-minute SLA)
  - Cancellation rate: 9%
- **Constraints:**
  - $25k/month incentive budget
  - Limited engineering capacity (assume 1 eng sprint / 2-week cycle available)
  - No stated policy/legal constraints beyond standard marketplace trust & safety
- **Decision this informs:** Whether to invest in supply-side activation, matching mechanics, or demand shaping to close the SF evenings liquidity gap — and how to allocate the $25k/month incentive budget across levers.

---

## 1) Liquidity Definition (Reliability)

### Working definition

Liquidity = the probability that a dog owner who requests a walk in a given local market can get a confirmed booking with a qualified walker within 10 minutes, and that booking is fulfilled without cancellation or no-show.

### Thresholds ("good enough")

| Dimension | Current (SF evenings) | Target (6-week) | Stretch |
|-----------|----------------------|------------------|---------|
| Fill rate (request -> booked) | 55% | 75% | 80% |
| Time-to-book p50 | 18 min | ≤ 10 min | ≤ 7 min |
| Time-to-book p90 | Unknown (assume ~35 min) | ≤ 20 min | ≤ 15 min |
| Cancellation rate (post-booking) | 9% | ≤ 6% | ≤ 4% |
| No-show rate | Unknown (assume ~3%) | ≤ 2% | ≤ 1% |

**Note:** The 10-minute SLA is buyer-facing. If a request is not matched within 10 minutes, it is a liquidity failure even if eventually booked — the user experience degrades sharply after that window.

---

## 2) Liquidity Metric Tree

| Level | Metric | Definition | Segmentable by | Data source | Notes |
|------:|--------|------------|----------------|-------------|-------|
| **North star** | Booking reliability rate | % of walk requests that result in a confirmed booking within 10 min AND are fulfilled (no cancel/no-show) | city, daypart, day-of-week, walker tier | `requests`, `bookings`, `cancellations` tables | Composite: fill rate x (1 - cancel rate) |
| **Driver** | Fill rate | % of walk requests that receive a confirmed booking (any time) | city, daypart, day-of-week | `requests` -> `bookings` join | Primary target metric |
| **Driver** | Time-to-book (p50 / p90) | Elapsed time from request creation to walker acceptance | city, daypart, walker tier | `requests.created_at` -> `bookings.confirmed_at` | Must get p50 under 10 min |
| **Driver** | Availability at intent | % of requests where ≥ 3 eligible walkers are online and within range at request time | city, daypart, neighborhood | `walker_sessions`, `requests` | Proxy for supply depth |
| **Driver** | Offer-to-accept rate | % of booking offers sent to walkers that are accepted | city, daypart, walker tier | `offers` -> `acceptances` | Low acceptance = slow matching |
| **Driver** | Offer response time (p50) | Median time from offer sent to walker response (accept/decline) | city, walker tier | `offers.sent_at` -> `offers.responded_at` | Slow response cascades into time-to-book |
| **Guardrail** | Cancellation rate | % of confirmed bookings cancelled by either side before walk start | city, daypart, cancel reason | `bookings` -> `cancellations` | Breakout by walker-cancel vs owner-cancel |
| **Guardrail** | No-show rate | % of confirmed bookings where walker does not arrive | city, daypart | `bookings` -> `no_shows` | Trust destroyer |
| **Guardrail** | Post-walk rating (p25) | 25th percentile of owner rating after completed walk | city, walker tier | `reviews` | Quality floor signal |

---

## 3) Local Market Definition + Segmentation

### Local market unit

**City x daypart x day-type** (weekday vs weekend)

Dayparts:
- Morning (6 AM - 10 AM)
- Midday (10 AM - 2 PM)
- Afternoon (2 PM - 5 PM)
- **Evening (5 PM - 9 PM)** — priority segment
- Late night (9 PM - 12 AM)

### Segment scorecard (baseline)

| Segment | Est. daily requests | Est. walkers online | Fill rate | Time-to-book p50 | Cancel rate | Primary bottleneck | Confidence |
|---------|--------------------:|--------------------:|----------:|------------------:|------------:|-------------------|------------|
| **SF Evening Weekday** | ~120 | ~25 | 50% | 20 min | 10% | Supply-limited | Medium (stated baseline) |
| **SF Evening Weekend** | ~160 | ~30 | 58% | 16 min | 8% | Supply-limited | Medium (estimated) |
| SF Morning Weekday | ~90 | ~35 | 72% | 9 min | 7% | Near-target | Low (assumed) |
| SF Afternoon Weekday | ~60 | ~30 | 68% | 12 min | 8% | Mechanics-limited | Low (assumed) |
| NYC Evening Weekday | ~200 | ~60 | 65% | 14 min | 8% | Mechanics-limited | Low (assumed) |
| NYC Evening Weekend | ~250 | ~70 | 62% | 15 min | 9% | Supply-limited | Low (assumed) |
| LA Evening Weekday | ~80 | ~20 | 58% | 17 min | 10% | Supply-limited | Low (assumed) |
| LA Evening Weekend | ~100 | ~25 | 55% | 18 min | 11% | Supply + Quality | Low (assumed) |

**Assumptions flagged:** Only SF evenings baseline was provided directly. Other segments are estimates based on typical on-demand marketplace patterns. Validation with actual data is required in Week 1.

### Fragmentation notes

- **Evening demand spike:** Evenings concentrate ~40% of daily demand into a 4-hour window. This is when dog owners return from work — demand is highly predictable but supply is constrained because walkers also have evening commitments.
- **Neighborhood concentration:** SF demand likely clusters in SoMa, Mission, Marina, Noe Valley, Hayes Valley. Supply may not be distributed proportionally (walkers may cluster near transit hubs but not near residential demand centers).
- **Uniform needs:** Dog walking is a relatively uniform-need marketplace (low heterogeneity in the service itself), which means liquidity is achievable with adequate supply density. The fragmentation is primarily **temporal** (evening spike) and **geographic** (neighborhood mismatch), not categorical.

---

## 4) Bottleneck Diagnosis

### Primary segment: SF Evenings (Weekday + Weekend)

#### Diagnosis: Supply-limited + slow matching mechanics

**Evidence (metrics):**

| Signal | Value | What it suggests |
|--------|-------|------------------|
| Fill rate | 55% | ~45% of requests go unfulfilled — significant unmet demand |
| p50 time-to-book = 18 min | 1.8x the 10-min SLA | Even matched requests are slow; offers are cascading through multiple walkers |
| Cancel rate = 9% | Above 6% target | Some accepted bookings are unreliable, further eroding net fill |
| Availability at intent | Unknown (assumed low) | If only ~25 walkers are online for ~120 requests, the ratio is ~5:1 request-to-walker — thin |

**Primary failure mode: Supply-limited**
- Not enough walkers are online during the 5 PM - 9 PM window. The request-to-walker ratio is likely too high for real-time matching to work.
- Walkers online may already be occupied with active walks, making effective availability even thinner than the gross number suggests.

**Secondary failure mode: Mechanics-limited (slow acceptance)**
- Even when walkers are available, p50 time-to-book at 18 minutes suggests offers are being declined or timing out before acceptance. The matching algorithm may be sending offers to busy/distant walkers first, or walkers are cherry-picking requests.
- Response time per offer is likely slow (walkers may not see push notifications promptly while on other walks).

**Cancellation breakdown hypothesis:**
- 9% cancellation rate likely splits: ~5-6% walker-initiated (found a better gig, overcommitted, travel time miscalculation) and ~3-4% owner-initiated (waited too long, found alternative).
- Walker cancellations are a quality/trust problem that directly undermines reliability.

**Flip-flop risk:**
- If supply interventions succeed and fill rate jumps above 75%, demand growth may accelerate (word of mouth, repeat rate), potentially re-creating a supply constraint at higher volume. The operating cadence must watch for demand surges following reliability improvements.
- Over-incentivizing supply could attract low-quality walkers who cancel or no-show, worsening the quality guardrail.

**Graduation problem signals:**
- Top-performing walkers may be building direct client relationships (dog owners exchanging numbers to avoid platform fees). This is a classic services marketplace leakage risk.
- High-earning walkers may leave for competing platforms (Rover, Wag) if they perceive better economics.

---

## 5) Intervention Plan + Prioritized Experiment Backlog

### Strategy overview

The 55% -> 75% fill rate gap in SF evenings requires closing ~20 percentage points. Decomposing the gap:

- **Supply availability gap** (~12 pp): Get more walkers online during 5-9 PM. If we can go from ~25 to ~40 available walkers, fill rate should improve mechanically.
- **Matching speed gap** (~5 pp): Faster offer routing and acceptance to convert available supply into booked walks within the SLA.
- **Cancellation recapture** (~3 pp): Reducing cancellations from 9% to 6% recovers ~3 pp of net fill rate.

### Reallocation ("whac-a-mole") plan

**Weekly levers available:**

| Lever | Owner | Budget/capacity |
|-------|-------|-----------------|
| Walker incentive bonuses (evening surge) | Ops/Growth | Up to $15k/mo of the $25k budget |
| Demand-side credits (apology/retry) | Ops/Growth | Up to $5k/mo |
| Matching algorithm tuning | Eng | 1 sprint per 2-week cycle |
| Ops outreach (walker reactivation) | Ops | 10 hrs/week |
| Marketing spend reallocation | Growth | Up to $5k/mo from budget |

**Reallocation triggers:**

| Trigger | Action |
|---------|--------|
| SF evening fill rate < 55% for 2 consecutive weeks | Increase walker bonuses by 20%; deploy ops outreach blitz |
| SF evening fill rate > 70% but cancel rate > 8% | Shift budget from supply incentives to quality (cancel penalties, walker reliability bonus) |
| SF evening availability > 40 walkers but fill rate still < 65% | Shift focus from supply acquisition to matching mechanics (eng sprint) |
| Demand volume spikes > 150 requests/evening weekday | Add $2k/week to walker bonuses; alert ops for manual matching assist |

### Prioritized experiment backlog

| Priority | Segment | Bottleneck | Hypothesis | Intervention | Primary metric | Guardrail metric | Expected effect | Effort | Timebox |
|---------:|---------|------------|-----------|--------------|---------------|-----------------|----------------|--------|---------|
| 1 | SF Evening Weekday | Supply | Walkers who were active in the past 30 days but are not logging on evenings will respond to targeted reactivation outreach (SMS + push + email) with an evening surge bonus ($5-8 per walk premium). | **Evening surge bonus + reactivation campaign**: Offer $5-8 bonus per walk completed 5-9 PM; run ops outreach to 100+ recently active SF walkers who are not covering evenings. | Fill rate (+8 pp); walkers online in evening (+40%) | Cancel rate stays < 10%; unit economics: blended cost per walk stays under $X | +8-12 pp fill rate | Low (ops + config change, no eng) | Weeks 1-3 |
| 2 | SF Evening Weekday | Mechanics | Slow offer cascading is the primary driver of 18-min time-to-book. Sending offers to 3 nearest available walkers simultaneously (instead of sequentially) will reduce time-to-book. | **Parallel offer routing**: Send walk offers to top 3 nearest available walkers simultaneously; first to accept wins. | Time-to-book p50 (target: ≤ 12 min by week 3, ≤ 10 min by week 6) | Walker experience (offer-to-accept rate does not drop below 30%); no double-booking | -6 min on p50 time-to-book | Medium (1 eng sprint) | Weeks 2-4 |
| 3 | SF Evening Weekday + Weekend | Quality | Walker-initiated cancellations are driven by overcommitment (accepting walks they can't reach in time) and lack of penalty. A cancellation fee + reliability score will reduce cancel rate. | **Cancellation penalty + reliability score**: Charge walkers a $10 fee for cancellations < 30 min before walk; surface a "reliability badge" for walkers with < 3% cancel rate (badge = priority in offer queue). | Cancel rate (target: ≤ 6%) | Walker supply (no net churn > 5% of active walkers); walker satisfaction | -3 pp cancellation rate | Low-Medium (product + policy change) | Weeks 2-5 |
| 4 | SF Evening Weekend | Supply | Weekend evenings have higher demand but only marginally more supply. Walkers who are active weekday evenings can be nudged to also cover weekends with a weekend premium. | **Weekend evening premium**: Add $3 weekend-evening kicker on top of the surge bonus for walkers who cover both Friday and Saturday evenings. | Weekend evening fill rate (+5 pp); weekend walker count (+20%) | Budget stays within $25k/mo total | +5-8 pp weekend fill rate | Low (config change) | Weeks 2-4 |
| 5 | SF Evening Weekday | Supply | New walker onboarding takes too long (background check + training). Expediting onboarding for SF-based applicants can add supply within 2 weeks instead of 4. | **Fast-track SF onboarding**: Prioritize SF applicants in background check queue; reduce training to a 30-min video + quiz (from in-person session); assign a "buddy walker" for first 3 walks. | New walkers activated in SF (target: 20+ in 4 weeks) | Quality (new walker rating ≥ 4.2/5; new walker cancel rate ≤ 10%) | +10-15 walkers to evening pool | Medium (ops process change) | Weeks 1-4 |
| 6 | SF Evening Weekday | Mechanics | Walkers decline offers because estimated travel time is too high. Tighter geo-matching (only offer walks within 15-min travel radius) will improve acceptance rate even if it reduces the eligible pool. | **Tighter geo-matching radius**: Reduce offer radius from 25 min to 15 min travel time; accept slightly lower coverage in exchange for faster acceptance. | Offer-to-accept rate (+15 pp); time-to-book p50 (-3 min) | Fill rate does not decrease (monitor for 1 week before expanding) | +10-15 pp acceptance rate | Low (config change) | Weeks 3-5 |
| 7 | SF Evening Weekday | Demand shaping | Some evening demand can be shifted to 4-5 PM (pre-peak) with a small discount, reducing peak-hour pressure. | **Early-evening discount**: Offer $3 off for walks requested between 4-5 PM (pre-peak shaping). | % of demand shifted to 4-5 PM (target: 10-15% of evening requests) | Total evening demand does not drop; fill rate in 4-5 PM stays ≥ 70% | Reduces peak pressure by ~10 requests/evening | Low (promo config) | Weeks 3-6 |
| 8 | SF Evening | Mechanics | Owners whose requests time out (no walker within 10 min) churn. An auto-retry with expanded radius + apology credit will recover some of these. | **Auto-retry + apology credit**: If no match within 10 min, auto-expand search radius by 50% and offer $5 credit; notify owner "still searching, we'll find someone." | Recovery rate (% of timed-out requests that convert on retry); owner retention | Credit cost per recovered booking stays < $8 | Recover 15-20% of timed-out requests | Medium (eng + ops) | Weeks 4-6 |

### Budget allocation plan (Month 1)

| Lever | Monthly allocation | Notes |
|-------|-------------------:|-------|
| Evening surge bonus (Exp #1) | $12,000 | ~$6/walk x ~2,000 evening walks/month |
| Weekend premium (Exp #4) | $3,000 | ~$3/walk x ~1,000 weekend evening walks |
| Early-evening discount (Exp #7) | $2,000 | ~$3 x ~700 shifted walks |
| Auto-retry apology credits (Exp #8) | $3,000 | ~$5 x ~600 retries |
| Contingency / reallocation buffer | $5,000 | Reallocated weekly based on triggers |
| **Total** | **$25,000** | At budget cap |

---

## 6) Measurement + Instrumentation Plan

### Dashboards

| Dashboard | Contents | Refresh | Owner | Tool |
|-----------|----------|---------|-------|------|
| **Liquidity Overview (SF)** | Fill rate, time-to-book p50/p90, cancel rate, availability at intent — by daypart, day-of-week | Real-time (15-min lag) | Data/Ops | Internal dashboard or Looker |
| **Walker Supply Health** | Walkers online by hour, offer-to-accept rate, response time, earnings per hour, churn rate (7-day rolling) | Daily | Ops | Internal dashboard |
| **Experiment Tracker** | Each active experiment: metric trend, cohort comparison, budget spent, guardrail status | Weekly | Growth | Spreadsheet or experiment platform |
| **Segment Scorecard** | All city x daypart x day-type segments: fill rate, time-to-book, cancel rate, volume, bottleneck label | Weekly | Data | Automated report |

### Alerts

| Alert | Trigger | Channel | Escalation |
|-------|---------|---------|------------|
| Fill rate drop | SF evening fill rate < 50% for 2 consecutive days | Slack #liquidity-alerts | Ops lead reviews within 4 hours |
| Cancel rate spike | SF cancel rate > 12% in any 24-hour window | Slack #liquidity-alerts | Ops + Trust & Safety review |
| Supply drought | < 15 walkers online in SF during 5-9 PM | Slack #liquidity-alerts + SMS to ops lead | Emergency incentive boost ($10/walk) |
| Budget overrun | Incentive spend pace > 110% of monthly budget | Email to Growth lead | Pause lowest-priority incentive |

### Event definitions / key tables

| Event | Definition | Key fields | Source |
|-------|-----------|------------|--------|
| `request_created` | Owner submits a walk request | request_id, owner_id, city, neighborhood, timestamp, dog_count | App backend |
| `offer_sent` | System sends a booking offer to a walker | offer_id, request_id, walker_id, timestamp, estimated_travel_time | Matching service |
| `offer_responded` | Walker accepts or declines an offer | offer_id, response (accept/decline/timeout), timestamp | Matching service |
| `booking_confirmed` | Walk is confirmed (offer accepted) | booking_id, request_id, walker_id, timestamp | Booking service |
| `booking_cancelled` | Confirmed booking is cancelled | booking_id, cancelled_by (walker/owner), reason, timestamp | Booking service |
| `walk_completed` | Walk is finished | booking_id, actual_start, actual_end, distance | Walker app |
| `review_submitted` | Owner rates the walk | booking_id, rating (1-5), comment | App backend |
| `walker_session_start/end` | Walker goes online/offline | walker_id, city, lat/lng, timestamp | Walker app |

### Instrumentation gaps (known or suspected)

| Gap | Impact | Remediation | Priority | Owner |
|-----|--------|-------------|----------|-------|
| **Availability at intent** not currently computed | Cannot measure supply depth at moment of request | Build a query: count distinct online walkers within radius at each `request_created` timestamp | High (Week 1) | Data eng |
| **Offer cascade depth** not tracked | Cannot see how many walkers are tried before a match | Add `offer_sequence_number` to `offer_sent` events | Medium (Week 2) | Eng |
| **Walker earnings per hour** not surfaced | Cannot assess walker economics or predict churn | Build a derived metric in warehouse: total earnings / total online hours per walker per week | Medium (Week 2) | Data eng |
| **Neighborhood-level segmentation** not in dashboards | Cannot diagnose intra-city geographic mismatch | Add neighborhood tagging to requests and walker sessions | Low (Week 3-4) | Data eng |

---

## 7) Operating Cadence (Weekly Liquidity Review)

### Meeting structure

- **Cadence:** Weekly, Mondays 10 AM PT
- **Duration:** 30-45 minutes
- **Owner:** Head of Marketplace Operations (or designated Liquidity Lead)
- **Participants:** Ops lead, Growth lead, Data analyst, Eng lead (for experiment weeks), Trust & Safety rep (bi-weekly)

### Agenda

| # | Topic | Time | Output |
|--:|-------|-----:|--------|
| 1 | **Topline reliability trend** — North-star (booking reliability rate) + fill rate + time-to-book + cancel rate for SF evenings, with week-over-week change | 5 min | Shared understanding of direction |
| 2 | **Segment deep dive** — Worst 3 segments this week (by fill rate gap to target); what changed and why | 7 min | Root cause hypotheses |
| 3 | **Experiment readouts** — Status of each active experiment; metric impact vs. expectation; ship / stop / iterate decision | 10 min | Decision per experiment |
| 4 | **Reallocation decisions** — Review triggers; decide: shift budget, add/remove incentives, change matching parameters, deploy ops outreach | 7 min | Specific changes with owners and effective dates |
| 5 | **Quality + trust check** — Cancel rate breakdown, no-show incidents, walker churn, any fraud signals | 5 min | Escalation if guardrails breached |
| 6 | **Next week commitments** — Who does what by when | 5 min | Commitment list in decision log |

### Decision log template

| Date | Segment | Decision | Rationale (metric trigger) | Owner | Follow-up date |
|------|---------|----------|---------------------------|-------|----------------|
| 2026-03-24 | SF Eve Wkday | Launch evening surge bonus at $6/walk | Fill rate = 55%, need supply | Ops lead | 2026-03-31 |
| 2026-03-24 | SF Eve Wkday | Begin parallel offer routing (eng sprint) | p50 TTB = 18 min | Eng lead | 2026-04-07 |

---

## 8) Risks / Open Questions / Next Steps

### Risks

| # | Risk | Likelihood | Impact | Mitigation |
|--:|------|-----------|--------|------------|
| 1 | **Incentive dependency:** Walkers only show up evenings when bonuses are active; removing bonuses collapses supply. | High | High | Gradually taper bonuses over weeks 4-6; track organic (non-bonus) evening sessions as a leading indicator. If organic share < 40% by week 5, extend bonuses but cap at $4/walk. |
| 2 | **Quality dilution from fast onboarding:** Fast-tracked walkers underperform on ratings and cancel rate, eroding owner trust. | Medium | High | Gate: new walkers must maintain ≥ 4.0 rating and ≤ 10% cancel rate through first 10 walks or face deactivation. Buddy walker program provides quality floor. |
| 3 | **Flip-flop to demand-limited:** If fill rate hits 75%+, improved reliability drives demand growth that re-creates the supply gap at higher volume. | Medium | Medium | Monitor demand growth rate weekly. If requests grow > 15% week-over-week, proactively increase supply incentives before fill rate declines. |
| 4 | **Walker cherry-picking with parallel offers:** Parallel offer routing may cause walkers to only accept nearby/easy walks, leaving harder requests (far neighborhoods, large dogs) unfilled. | Medium | Medium | Monitor acceptance rate by neighborhood and dog count. If acceptance becomes skewed, introduce minimum acceptance rate requirement (e.g., > 50%) to remain eligible for surge bonus. |
| 5 | **Budget cannibalization across cities:** Spending $25k/mo on SF may starve NYC/LA of needed interventions if those markets deteriorate. | Low | Medium | Track NYC and LA fill rates weekly as watchlist segments. If either drops > 5 pp, escalate budget discussion to leadership. |
| 6 | **Graduation / disintermediation:** Top walkers build direct relationships with owners, bypassing the platform. | Medium | High (long-term) | Monitor repeat owner-walker pair frequency. If > 30% of bookings are with the same walker, consider loyalty features (guaranteed walker, subscription) that keep the relationship on-platform. |

### Open questions

| # | Question | Owner | Due date |
|--:|----------|-------|----------|
| 1 | What is the actual p90 time-to-book and no-show rate for SF evenings? Need data pull to validate assumptions. | Data analyst | Week 1 (by Mar 24) |
| 2 | What is the offer cascade depth (how many walkers are tried per request)? Needed to size the matching mechanics problem. | Data eng | Week 1 (by Mar 24) |
| 3 | What is the walker-initiated vs. owner-initiated cancellation split? Needed to target cancellation interventions correctly. | Data analyst | Week 1 (by Mar 24) |
| 4 | How many inactive-but-eligible walkers exist in SF who could be reactivated? (Last active 30-90 days ago, passed background check.) | Ops lead | Week 1 (by Mar 24) |
| 5 | What is the current walker earnings-per-hour in SF evenings? Is the economics proposition competitive with Rover/Wag/gig alternatives? | Data analyst + Ops | Week 2 (by Mar 31) |
| 6 | Can eng support parallel offer routing in a single 2-week sprint, or does it require backend refactoring? | Eng lead | Week 1 (by Mar 24) |
| 7 | Is neighborhood-level data already available in the warehouse, or does it require new instrumentation? | Data eng | Week 1 (by Mar 24) |

### Next steps (Weeks 1-2: unblocked actions)

| # | Action | Owner | Due | Dependencies |
|--:|--------|-------|-----|-------------|
| 1 | **Data pull:** Extract SF evening baseline by daypart, day-type, neighborhood. Validate fill rate, time-to-book p50/p90, cancel rate (by initiator), no-show rate, availability at intent, offer cascade depth. | Data analyst | Mar 24 | Access to warehouse |
| 2 | **Reactivation list:** Pull list of SF walkers active in last 90 days but not active in evenings past 2 weeks. Segment by quality (rating, cancel history). | Ops lead | Mar 24 | Walker data access |
| 3 | **Launch evening surge bonus (Exp #1):** Configure $6/walk bonus for SF 5-9 PM. Deploy reactivation SMS/push/email campaign to eligible walkers. | Ops lead + Growth | Mar 26 | Incentive config tool, reactivation list |
| 4 | **Eng scoping:** Eng lead confirms feasibility and timeline for parallel offer routing (Exp #2). If feasible in 1 sprint, begin Week 2. | Eng lead | Mar 24 | Eng capacity confirmation |
| 5 | **Instrumentation:** Data eng builds "availability at intent" metric and adds offer_sequence_number to offer events. | Data eng | Mar 31 | Eng access to matching service |
| 6 | **Set up Liquidity Overview dashboard:** Build or adapt existing dashboard to show SF evening metrics in real-time with daypart breakdowns. | Data analyst | Mar 28 | Metric definitions finalized |
| 7 | **First weekly liquidity review:** Conduct Week 1 review on Mar 31. Agenda: validate baseline data, review reactivation response, decide on Exp #2 launch, set Week 2 commitments. | Liquidity Lead | Mar 31 | Data pull complete |

---

## Quality Gate Self-Assessment

### Checklist verification

**A) Scope + contracts**
- [x] Clearly states the decision this work informs
- [x] Defines the core action and user perspective (buyer/dog owner)
- [x] Defines the local market unit (city x daypart x day-type) and priority segments
- [x] Lists constraints (budget, eng capacity, timebox)

**B) Liquidity definition + metrics**
- [x] Liquidity defined as reliability with explicit thresholds
- [x] Metric tree includes 1 north-star + 6 driver metrics + 3 guardrails
- [x] Each metric has a definition and is segmentable
- [x] Flags instrumentation gaps (4 identified)

**C) Fragmentation + diagnosis**
- [x] Segment scorecard exists with baseline numbers and flagged assumptions
- [x] Identifies fragmentation (temporal evening spike + geographic neighborhood mismatch)
- [x] Bottleneck diagnosis labeled per segment (supply-limited + mechanics-limited)
- [x] Diagnosis includes metric signals + testable hypotheses
- [x] Notes flip-flop risk (demand growth after reliability improvement)
- [x] Checks graduation problem (disintermediation risk)

**D) Interventions + experiments**
- [x] 8 experiments specified with hypothesis, segment, metrics, timebox
- [x] Reallocation plan with weekly levers and explicit triggers
- [x] Includes quality guardrails (cancel penalties, rating gates, budget caps)
- [x] Experiments sequenced (Weeks 1-2 actions are unblocked)

**E) Measurement + operating cadence**
- [x] Dashboards and alerts specified with refresh cadence
- [x] Instrumentation plan ties metrics to events/tables
- [x] Weekly liquidity review cadence with agenda and decision log

**F) Finalization**
- [x] Includes Risks (6), Open questions (7), Next steps (7)
- [x] Risks include second-order effects (incentive dependency, quality dilution, flip-flop, cannibalization)
- [x] Next steps are concrete and unblocked

### Rubric self-score

| Dimension | Score | Rationale |
|-----------|------:|-----------|
| 1) Reliability definition | 2 | Clear buyer-perspective definition with time + quality thresholds |
| 2) Local market segmentation | 2 | City x daypart x day-type; 8 segments with ranked priorities and per-segment baselines |
| 3) Metric tree quality | 2 | North-star + 6 drivers + 3 guardrails; event definitions and data sources specified |
| 4) Fragmentation analysis | 2 | Temporal + geographic fragmentation identified with volume estimates; uniform-need marketplace noted |
| 5) Bottleneck diagnosis | 2 | Per-segment diagnosis (supply + mechanics); metric signals + hypotheses; flip-flop + graduation addressed |
| 6) Interventions + experiments | 2 | 8 prioritized experiments with segment, hypothesis, metrics, expected effect, effort, timebox |
| 7) Whac-a-mole operating plan | 2 | Weekly levers named; 4 explicit triggers with actions; decision log template |
| 8) Measurement + instrumentation | 2 | 4 dashboards, 4 alerts, 8 event definitions, 4 instrumentation gaps with remediation plans |
| 9) Risks / open questions / next steps | 2 | 6 risks with mitigations including second-order effects; 7 open questions with owners/dates; 7 concrete next steps |
| **Total** | **18/18** | Meets passing bar (>= 14/18) |
