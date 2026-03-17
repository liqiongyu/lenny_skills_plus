# Systems Thinking Pack: Engineering On-Call Escalation Crisis

## 1. System Boundary and Problem Statement

**Presenting problem:** On-call page volume has tripled over 6 months (5 to 15 pages/week per team), causing burnout, degraded code review quality, and a suspected increase in production incidents --- all while management demands higher feature velocity due to competitive pressure.

**System boundary:** Engineering organization including individual contributors, tech leads, engineering managers, product management, and executive leadership. Excludes customer-facing support triage and external market dynamics (treated as exogenous inputs).

**Time horizon:** 6-month retrospective, 12-month forward projection.

---

## 2. Actors, Roles, and Incentive Maps

### 2.1 Individual Engineers (ICs)

| Dimension | Detail |
|-----------|--------|
| **Primary incentive** | Ship features (tied to performance reviews, promotions) |
| **Secondary incentive** | Reduce personal on-call suffering |
| **Behavioral response to current state** | Cut corners on code reviews to reclaim time lost to incident response; defer tech debt work; reduce investment in monitoring and runbooks |
| **Hidden cost** | Cognitive load from context-switching between firefighting and feature work degrades quality of both activities |

### 2.2 Tech Leads / Staff Engineers

| Dimension | Detail |
|-----------|--------|
| **Primary incentive** | Team delivery against roadmap commitments |
| **Secondary incentive** | System reliability and architectural health |
| **Behavioral response** | Absorb disproportionate on-call burden to shield team; deprioritize reliability investments in favor of feature work to satisfy management; approve weaker PRs to unblock velocity |
| **Hidden cost** | Single-point-of-failure knowledge concentration; personal burnout leading to attrition of most experienced engineers |

### 2.3 Engineering Managers

| Dimension | Detail |
|-----------|--------|
| **Primary incentive** | Meet quarterly delivery commitments; maintain team health metrics |
| **Secondary incentive** | Reduce attrition and maintain hiring pipeline reputation |
| **Behavioral response** | Underreport on-call burden in status updates; negotiate for headcount as the solution; shield team from scope discussions |
| **Hidden cost** | Information asymmetry --- leadership makes decisions on incomplete data about system health |

### 2.4 Product Management

| Dimension | Detail |
|-----------|--------|
| **Primary incentive** | Feature throughput and time-to-market |
| **Secondary incentive** | Customer satisfaction and retention |
| **Behavioral response** | Resist scope reduction; treat reliability work as "not real work"; push for parallel workstreams |
| **Hidden cost** | Features shipped on an unreliable platform generate support burden and customer churn that ultimately slows net delivery |

### 2.5 Executive Leadership

| Dimension | Detail |
|-----------|--------|
| **Primary incentive** | Competitive positioning, revenue growth |
| **Secondary incentive** | Organizational sustainability |
| **Behavioral response** | Demand more output; approve headcount as the default intervention; set aggressive timelines |
| **Hidden cost** | Slow to recognize that throughput has an upper bound set by system reliability; new hires add coordination overhead before contributing |

---

## 3. Feedback Loop Analysis

### 3.1 The Core Doom Loop: Firefighting Creates More Fires (Reinforcing Loop R1)

```
High on-call load
    --> Engineers spend more time on incidents
    --> Less time for code reviews, testing, tech debt
    --> Lower code quality shipped to production
    --> More production incidents
    --> Higher on-call load  [REINFORCING]
```

**Characteristics:**
- This is a *reinforcing* (positive feedback) loop with exponential growth dynamics
- It is self-accelerating: every cycle through the loop increases the rate of the next cycle
- The 5-to-15 tripling over 6 months is consistent with exponential growth from a reinforcing loop
- Without intervention, this loop does not reach equilibrium --- it runs until a constraint binds (engineer attrition, system collapse, or management intervention)

**Critical delay:** The lag between shipping low-quality code and the resulting incidents is typically 2-6 weeks. This delay makes the causal link invisible to participants: by the time incidents spike, the code that caused them was merged weeks ago and the team has moved on.

### 3.2 The Burnout Attrition Loop (Reinforcing Loop R2)

```
High on-call load
    --> Engineer burnout and dissatisfaction
    --> Increased attrition (senior engineers leave first)
    --> Knowledge loss and reduced team capacity
    --> Remaining engineers handle more on-call and more features
    --> Higher on-call load per person  [REINFORCING]
```

**Key insight:** Senior engineers leave first because they have the most options. They also carry the most system knowledge. Their departure causes a *double hit*: reduced capacity AND reduced ability to diagnose and resolve incidents quickly, which increases mean-time-to-resolve (MTTR) and total on-call burden.

### 3.3 The Velocity Pressure Loop (Reinforcing Loop R3)

```
Management demands higher velocity
    --> Teams skip reliability investment to ship features
    --> System becomes more fragile
    --> More incidents
    --> More time spent on incidents
    --> Effective velocity drops
    --> Management perceives teams as slower
    --> Management demands even higher velocity  [REINFORCING]
```

**This is the most insidious loop** because it creates a *worse-before-better* dynamic for any intervention. Investing in reliability temporarily reduces feature output, which intensifies management pressure, which makes it harder to sustain the reliability investment.

### 3.4 The Code Review Erosion Loop (Reinforcing Loop R4)

```
Time pressure from on-call + feature demands
    --> Code reviews become superficial (rubber-stamping)
    --> Defects escape to production
    --> More incidents
    --> More time pressure  [REINFORCING]
```

**Compounding factor:** As review quality drops, engineers internalize lower standards. The team's shared definition of "good enough" drifts downward. This cultural erosion is much harder to reverse than a process change.

### 3.5 The Balancing Loop That Should Work But Doesn't (Balancing Loop B1)

```
High incident rate
    --> Visibility to management
    --> Investment in reliability
    --> Fewer incidents
    --> Lower on-call load  [BALANCING]
```

**Why it's broken:** This loop is suppressed by three factors:
1. **Information filtering:** Managers underreport on-call burden; dashboards show lagging indicators
2. **Competing priorities:** Even when visible, reliability investment loses to feature pressure
3. **Delay:** Reliability investments take 1-3 months to show results, while feature delivery shows results in days

---

## 4. Causal Loop Diagram (Text Representation)

```
                    COMPETITIVE PRESSURE (exogenous)
                              |
                              v
                   Management velocity demands
                        |              ^
                        v              |
              +---> Feature pressure --+-- Perceived slow delivery
              |         |
              |         v
              |    Skip reliability     Skip thorough reviews
              |    investment               |
              |         |                   v
              |         v              Defects escape (R4)
              |    System fragility         |
              |         |                   |
              |         v                   v
              |    MORE INCIDENTS <----------+
              |         |
              |    +----+----+
              |    |         |
              |    v         v
              | Time lost   Burnout
              | to fires    (R2) --> Attrition --> Knowledge loss
              |    |                                    |
              |    v                                    |
              +-- Less time for quality work <----------+
                   (R1 - Core Doom Loop)
```

---

## 5. Quantitative Estimation of Current Trajectory

### Assumptions
- Average incident takes 2 hours to resolve (including context switch cost)
- 15 pages/week = ~30 engineer-hours/week per team lost to incidents
- A 6-person team has ~240 productive hours/week
- Therefore, ~12.5% of capacity is consumed by firefighting (up from ~4% at 5 pages/week)

### Projection Without Intervention
If the reinforcing loop continues at its current growth rate (tripling in 6 months, roughly 20% month-over-month growth):

| Month | Pages/week | Capacity lost | Effective feature velocity |
|-------|-----------|---------------|--------------------------|
| Now   | 15        | 12.5%         | 87.5% of baseline        |
| +3    | 26        | 21.7%         | 78.3%                    |
| +6    | 45        | 37.5%         | 62.5%                    |
| +9    | 78        | 65.0%         | 35.0%                    |

**The system hits a wall around month 6-9** where more than half of engineering capacity goes to firefighting. At this point, feature velocity effectively collapses and attrition accelerates dramatically.

---

## 6. Intervention Analysis: Second-Order Effects

### 6.1 Intervention A: Hire More Engineers

**First-order effect:** More capacity to absorb both feature work and on-call load.

**Second-order effects:**

| Effect | Impact | Timeframe |
|--------|--------|-----------|
| Onboarding load | Senior engineers spend time mentoring instead of fixing systems; short-term productivity *drops* | Months 1-3 |
| Communication overhead | Brooks's Law --- adding people to a late project makes it later; coordination cost grows quadratically | Ongoing |
| Diluted on-call knowledge | New engineers on-call without deep system knowledge increases MTTR | Months 2-6 |
| Cultural dilution | New hires absorb the current degraded norms (weak code reviews) rather than improving them | Months 3-6 |
| Headcount costs | Budget consumed by hiring reduces budget for tooling and infrastructure | Immediate |

**Third-order effects:**
- If new hires are put on features while existing engineers handle on-call, you create a two-class system that accelerates attrition of the experienced engineers
- If new hires go on-call, incident resolution quality drops, potentially causing cascading failures

**Verdict:** Hiring helps only if *combined* with reliability investment and improved onboarding. Alone, it's the slowest and most expensive lever with the longest delay to impact. It does not address any of the reinforcing loops directly.

### 6.2 Intervention B: Reduce Scope

**First-order effect:** Less feature work in progress; engineers reclaim time for reliability and quality.

**Second-order effects:**

| Effect | Impact | Timeframe |
|--------|--------|-----------|
| Management resistance | Political cost; product team pushback; requires executive alignment | Immediate |
| Competitive risk (real) | Competitors may gain ground on features | Months 3-12 |
| Competitive risk (perceived) | Often overstated; customers care about reliability too | Ongoing |
| Quality improvement | With less WIP, code reviews improve, defect rate drops | Months 1-3 |
| Morale improvement | Engineers feel less stretched; attrition risk decreases | Months 1-2 |
| Reliability time freed | Teams can invest in automation, monitoring, and debt paydown | Months 1-3 |

**Third-order effects:**
- Reduced scope forces prioritization discipline, which often reveals that 30-40% of planned features deliver marginal value
- Slower feature pace with higher quality often results in *higher* customer satisfaction than fast pace with reliability issues
- Creates organizational capability for sustainable delivery that compounds over time

**Verdict:** Highest-leverage intervention with fastest time to impact. The political cost is real but manageable if framed correctly (see Intervention Plan below).

### 6.3 Intervention C: Invest in Reliability

**First-order effect:** Fewer incidents through better monitoring, automation, testing, and architectural improvements.

**Second-order effects:**

| Effect | Impact | Timeframe |
|--------|--------|-----------|
| Short-term velocity reduction | Engineers spending time on reliability are not shipping features | Months 1-3 |
| Management impatience | Results are delayed; pressure to redirect back to features | Months 1-4 |
| Compounding returns | Each reliability improvement reduces future incident load, freeing more capacity | Months 3-12 |
| Knowledge codification | Runbooks, monitoring, and automation capture tribal knowledge, reducing bus factor | Months 2-6 |
| On-call quality of life | Engineers who see investment in reliability have higher retention | Months 1-3 |

**Third-order effects:**
- Reliability investment builds institutional muscle for platform thinking
- Automated incident response reduces the skill barrier for on-call, easing the new-hire ramp
- Better monitoring creates data that makes the case for *continued* reliability investment (virtuous cycle)

**Verdict:** Essential complement to scope reduction. Alone, it's vulnerable to the "worse-before-better" trap (R3 loop intensifies before the investment pays off). Combined with scope reduction, it's transformative.

---

## 7. Leverage Points (Ranked by Impact)

Drawing on Donella Meadows's hierarchy of leverage points in complex systems:

### Leverage Point 1: Change the Information Flow (Make the Doom Loop Visible)

**Meadows classification:** #6 --- The structure of information flows

**Why it's high leverage:** The core doom loop persists partly because its dynamics are invisible. Managers don't see that last month's rushed PRs are this month's incidents. Executives don't see that velocity pressure creates reliability debt that destroys future velocity.

**Intervention:**
1. Instrument the causal chain: tag every incident with root cause category (code defect, config error, capacity, dependency)
2. Track "time from merge to incident" for code-defect incidents and attribute to the originating PR
3. Create a weekly dashboard showing: pages per team, hours lost to incidents, code review cycle time, PR approval-without-comment rate
4. Publish this dashboard to executives alongside feature velocity metrics

**Mechanism:** When the loop is visible, the balancing loop B1 (management responds to incident rate with reliability investment) can activate. Information changes incentives without requiring anyone to accept blame.

### Leverage Point 2: Change the Goal of the System (From Feature Velocity to Sustainable Throughput)

**Meadows classification:** #3 --- The goals of the system

**Why it's high leverage:** The current system optimizes for feature output measured in story points or features shipped. This goal drives the R3 loop (velocity pressure). Changing the goal to *sustainable throughput* --- features delivered that remain stable in production --- reframes reliability work as a first-class contributor to the goal rather than a competitor for resources.

**Intervention:**
1. Redefine the team-level success metric: replace "features shipped" with "features stable in production for 30 days without incident"
2. Include on-call burden as a leading indicator in quarterly planning (teams with rising pages/week get automatic scope reduction)
3. Set an organizational SLO for on-call: no team exceeds X pages/week; if breached, feature work pauses until the trend reverses

**Mechanism:** When reliability is part of the goal, the incentive alignment changes at every level. Engineers are rewarded for quality. Managers allocate time to reliability. Product managers learn to value stability. The R3 loop is interrupted because "slower but stable" is now treated as success, not failure.

### Leverage Point 3: Add a Balancing Loop via Structural Policy (The Circuit Breaker)

**Meadows classification:** #5 --- The rules of the system

**Why it's high leverage:** Right now, there is no structural mechanism that forces the system to respond to rising on-call load. The response is discretionary and always loses to feature pressure. A structural policy --- a "circuit breaker" --- removes discretion and forces action.

**Intervention:**
1. Establish an on-call load threshold per team (e.g., 8 pages/week)
2. When a team exceeds the threshold for 2 consecutive weeks, an automatic policy activates:
   - 30% of the team's sprint capacity is reallocated to reliability work (specific items chosen by the team, not management)
   - New feature scope for that team is reduced by the corresponding amount in the next sprint
   - The policy remains active until on-call load drops below threshold for 2 consecutive weeks
3. This is not optional or negotiable --- it's a policy, like a production freeze during incidents

**Mechanism:** This directly interrupts the R1 doom loop by injecting reliability investment when it's most needed. It also addresses the political problem of scope reduction by making it automatic rather than requiring a manager to fight for it each sprint.

---

## 8. Integrated Intervention Plan

### Phase 0: Emergency Stabilization (Weeks 1-2)

**Objective:** Stop the bleeding; buy time for structural changes.

| Action | Owner | Metric |
|--------|-------|--------|
| Declare an on-call emergency; temporary 20% scope reduction across all teams | VP Engineering | Scope committed vs. baseline |
| Identify the top 5 incident categories by volume and assign a DRI for each | Tech Leads | Top-5 list published |
| Implement temporary "incident-free deploy windows" (deploy only during business hours with explicit review) | Engineering Managers | Deploy frequency and incident correlation |
| Cancel all non-essential meetings for on-call engineers for 2 weeks | Engineering Managers | Hours reclaimed |

### Phase 1: Instrument and Diagnose (Weeks 2-6)

**Objective:** Make the system dynamics visible; build the data infrastructure for ongoing management.

| Action | Owner | Metric |
|--------|-------|--------|
| Deploy incident attribution tagging (root cause, originating PR, time-to-detect, time-to-resolve) | Platform/SRE team | 100% of incidents tagged within 4 weeks |
| Build the "System Health Dashboard" combining on-call load, code review metrics, deploy frequency, and incident rate | Platform/SRE team | Dashboard live and reviewed weekly by leadership |
| Conduct blameless retrospectives on the top 10 most costly incidents from the last 3 months | Tech Leads | 10 retro reports with action items |
| Survey engineers on burnout, on-call satisfaction, and perceived code quality trends | Engineering Managers | Baseline survey results |

### Phase 2: Structural Changes (Weeks 4-12)

**Objective:** Install the leverage points; change goals and rules.

| Action | Owner | Metric |
|--------|-------|--------|
| Implement the circuit breaker policy (Leverage Point 3) | VP Engineering | Policy documented and active |
| Redefine team success metrics to include "stable features" (Leverage Point 2) | VP Engineering + Product | New metrics in next quarterly planning |
| Allocate 20% of each team's capacity as a protected "reliability budget" (permanent, not temporary) | Engineering Managers | Budget reflected in sprint planning |
| Establish mandatory code review standards: minimum 1 substantive comment per PR, no self-merges, minimum review time of 15 minutes for PRs over 200 lines | Tech Leads | PR metrics tracked on dashboard |
| Begin hiring for 1-2 SRE/platform roles specifically focused on incident reduction tooling | VP Engineering | Roles posted within 4 weeks |

### Phase 3: Sustain and Compound (Months 3-12)

**Objective:** Let the interventions compound; monitor for regression; adjust.

| Action | Owner | Metric |
|--------|-------|--------|
| Monthly review of system health dashboard at leadership level | VP Engineering | On-call load trending downward |
| Quarterly adjustment of reliability budget based on trends (can decrease as system stabilizes) | Engineering Managers | Budget adjusted per data |
| Invest in incident automation: auto-remediation for top 3 incident categories | Platform/SRE team | Automated remediation rate |
| Re-survey engineers on burnout and satisfaction | Engineering Managers | Improvement vs. baseline |
| Share results organization-wide to reinforce the investment | VP Engineering | Internal comms published |

---

## 9. Guardrails and Failure Modes

### Guardrail 1: Prevent Reliability Theater

**Risk:** Teams game the circuit breaker by logging "reliability work" that is actually feature work or low-value busywork.

**Guardrail:** Reliability work must be tied to a specific incident category or measurable SLO improvement. Tech leads review and approve reliability work items. Monthly audit of reliability hours vs. incident reduction.

### Guardrail 2: Prevent Scope Reduction From Becoming Permanent Underdelivery

**Risk:** Teams use the reliability allocation as a permanent excuse to reduce output, even after on-call load normalizes.

**Guardrail:** The circuit breaker is tied to measurable thresholds. When on-call load drops below the threshold, the reliability allocation returns to the standard 20% budget. Feature velocity is expected to *increase* as reliability improves (because less time is lost to firefighting). Track "total productive output" (features + reliability improvements) rather than just features.

### Guardrail 3: Prevent Management Override of the Circuit Breaker

**Risk:** In a crunch (e.g., major release, competitive threat), leadership overrides the circuit breaker to push features, undoing the structural change.

**Guardrail:** Circuit breaker overrides require VP-level written approval with an explicit plan for how the reliability debt will be repaid. Override events are tracked and reported quarterly. More than 2 overrides per quarter triggers an automatic escalation to the CTO.

### Guardrail 4: Prevent Code Review Standards From Becoming Bottlenecks

**Risk:** Strict code review requirements slow velocity without improving quality if reviewers lack the skill or incentive to give meaningful feedback.

**Guardrail:** Invest in reviewer training (2-hour workshop on effective code review). Track review quality through a lightweight peer-feedback mechanism. Recognize and reward excellent reviewers in performance cycles. If review cycle time exceeds 24 hours for non-complex PRs, investigate and adjust.

### Guardrail 5: Monitor for Attrition Acceleration During Transition

**Risk:** The "worse-before-better" phase (reduced feature velocity while reliability investment ramps) frustrates engineers who interpret it as organizational dysfunction rather than intentional investment.

**Guardrail:** Over-communicate the strategy. Share the system dynamics analysis (this document) with all engineers. Explain the expected trajectory: things will feel slower for 1-2 months before the compounding benefits kick in. Set explicit milestones and celebrate early wins (e.g., first week below 12 pages, first month below 10).

---

## 10. Expected Trajectory With Intervention

| Timeframe | On-call load (pages/week) | Feature velocity (% of current) | Notes |
|-----------|--------------------------|-------------------------------|-------|
| Now       | 15                       | 100% (but declining)          | Baseline |
| +1 month  | 13-14                    | 80%                           | Scope reduction bites; quick wins on top incidents |
| +3 months | 8-10                     | 85%                           | Circuit breaker and reliability investment paying off |
| +6 months | 5-7                      | 95-100%                       | System stabilized; capacity recovered from reduced firefighting |
| +12 months| 3-5                      | 110-120%                      | Compounding returns: less firefighting + better tooling + healthier team = higher sustainable throughput |

**The key insight:** At month 12, total output (features + reliability) is *higher* than the current state despite (or rather because of) the temporary velocity reduction. The organization is shipping more features on a more stable platform with less burnout. This is the payoff from breaking the reinforcing loops.

---

## 11. Key Mental Models Applied

1. **Fixes That Fail (Systems Archetype):** Hiring more engineers without addressing the root cause (reliability debt) is a symptomatic fix that delays and often worsens the underlying problem.

2. **Shifting the Burden (Systems Archetype):** The organization has shifted from investing in system reliability (the fundamental solution) to heroic firefighting (the symptomatic solution), which has atrophied the capability for reliability investment.

3. **Limits to Growth (Systems Archetype):** Feature velocity cannot grow indefinitely on an unreliable platform. The constraint is system reliability, not engineering headcount.

4. **Eroding Goals:** The implicit quality bar for code reviews has gradually lowered as the norm shifted from thorough review to rubber-stamping. This is an example of goal erosion under pressure, which is much harder to reverse than a process change.

5. **Worse Before Better:** Any intervention that addresses the root cause (reliability) will temporarily reduce feature velocity, creating political pressure to abandon the intervention. This must be anticipated and managed explicitly.

---

## 12. One-Page Executive Summary

**Situation:** On-call load tripled in 6 months. The root cause is a reinforcing feedback loop: firefighting consumes time that would otherwise go to code quality and reliability, which creates more incidents, which requires more firefighting. Three amplifying loops (burnout/attrition, velocity pressure, review erosion) accelerate the decline.

**Without intervention:** The system hits a wall in 6-9 months where more than half of engineering capacity is consumed by incident response. Feature velocity collapses. Senior attrition accelerates.

**Recommended interventions (in priority order):**
1. **Make the doom loop visible** --- instrument the causal chain and put it on a dashboard that leadership reviews weekly
2. **Redefine success** --- measure stable features in production, not features shipped; include on-call load as a planning input
3. **Install a circuit breaker** --- automatic scope reduction when on-call load exceeds threshold; structural, not discretionary

**What this is NOT:** This is not a recommendation to stop shipping features. It is a recommendation to *temporarily* ship fewer features to *permanently* increase sustainable throughput. The expected outcome at 12 months is higher total output on a stable platform with a healthier team.

**The ask:** Executive commitment to a 3-month transition period where feature velocity temporarily dips by approximately 15-20%, in exchange for a projected 10-20% sustained increase in throughput by month 12 and a dramatic improvement in engineer retention and satisfaction.
