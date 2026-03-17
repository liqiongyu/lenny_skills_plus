# Onboarding Redesign Pack: B2B Team Analytics Tool

## Context & Problem Statement

- **Product**: B2B team analytics tool requiring at least one integration (Slack, Jira, or GitHub) before value delivery.
- **Current 7-day activation rate**: 12% (activation = at least one integration connected).
- **Target**: 18% by end of quarter (a 50% relative improvement).
- **Constraint**: Cannot reduce signup completion rate.
- **Volume**: ~5,000 new signups/month.
- **Primary drop-off point**: Integration setup step.

---

## Part 1: First-30-Seconds Experience

### Design Principles

The first 30 seconds must accomplish three things: (1) reinforce the user made a good decision to sign up, (2) make the single most important next action unmistakable, and (3) reduce perceived complexity of that action.

### Recommended Flow

**Second 0-5: Welcome + Identity Confirmation**

- Display: "Welcome, [First Name]. Let's get [Company Name] set up."
- Show a subtle brand moment (animation, confetti, or a short value-reinforcement line like "Teams using [Product] ship 30% faster").
- No navigation chrome, no sidebar, no dashboard. Full-screen focused experience.

**Second 5-15: Single-Choice Integration Selector**

- Headline: "Connect your first tool to see your team's data."
- Show exactly three large cards: Slack, Jira, GitHub. Each card includes:
  - Logo (large, recognizable).
  - One-line value prop specific to that integration (e.g., "See communication patterns across channels" for Slack).
  - Estimated setup time: "Takes about 60 seconds."
  - A "Connect" button.
- Below the cards: "Not sure which one? We recommend starting with [most popular integration based on company size or industry]."
- Smart default: If the signup email domain is on GitHub or the company uses a known Jira instance, pre-highlight that option.

**Second 15-25: OAuth Flow (Inline)**

- On clicking "Connect," launch the OAuth consent screen.
- Keep the parent page visible in the background with a progress indicator.
- If possible, use a modal/popup rather than a full redirect so users don't lose context.

**Second 25-30: Immediate Confirmation + First Data Preview**

- On successful connection: "Connected! We're pulling in your data now."
- Show a loading skeleton of what the dashboard will look like with real data populating in real time.
- Progress indicator: "Syncing 247 messages..." or "Found 18 repositories..."

### What to Remove

- Skip the product tour. Users don't need a tour before they have data. Tours at this stage increase cognitive load and delay the integration step.
- Remove team invitation from the initial flow. This is a post-activation action. Inviting teammates before data exists creates empty-room syndrome.
- Remove profile completion, avatar upload, notification preferences. All of these can happen later.
- Remove "explore the dashboard" CTAs. An empty dashboard is the worst possible first impression.

### Escape Hatches

- If a user dismisses the integration screen, show a persistent but non-blocking banner: "Connect Slack, Jira, or GitHub to unlock your analytics."
- Offer a "Show me a demo workspace" link for users who want to explore before committing. The demo workspace should contain realistic synthetic data and a clear "Connect your own tools" CTA on every page.

---

## Part 2: First-Mile Milestone Map

The first mile spans signup through the user's first "aha moment." Below is a milestone map with target timeframes and success metrics.

### Milestone 0: Signup Complete (T+0)
- **Definition**: User has created an account with email verification complete.
- **Target**: 100% of cohort (this is the entry point).
- **Current state**: Baseline; no changes proposed here per constraint.

### Milestone 1: Integration Screen Reached (T+0 to T+30 seconds)
- **Definition**: User sees the integration selection screen.
- **Target**: 95% of signups (currently unknown; instrument this).
- **Key risk**: Unnecessary intermediate screens (profile setup, team creation) intercepting users before the integration screen.
- **Action**: Make the integration screen the immediate post-signup destination.

### Milestone 2: Integration Attempt Initiated (T+30 seconds to T+3 minutes)
- **Definition**: User clicks "Connect" on any integration.
- **Target**: 60% of signups.
- **Key risk**: Decision paralysis (which integration?), trust concerns (OAuth permissions), or unclear value proposition.
- **Actions**: Smart defaults, permission explanations, social proof ("12,000 teams have connected Slack").

### Milestone 3: Integration Successfully Connected (T+1 to T+5 minutes)
- **Definition**: OAuth completes and first data sync begins.
- **Target**: 45% of signups.
- **Key risk**: OAuth failures, insufficient permissions, IT/admin blocks, wrong account selected.
- **Actions**: Error recovery flows, "try a different integration" prompts on failure, IT admin request email templates.

### Milestone 4: First Data Visible (T+5 to T+30 minutes)
- **Definition**: User sees at least one meaningful data visualization with their real data.
- **Target**: 35% of signups.
- **Key risk**: Slow data sync, empty states if the connected workspace is small.
- **Actions**: Progressive data loading, highlight even small datasets ("We found activity from 3 team members this week").

### Milestone 5: First Insight Discovered (T+30 minutes to T+24 hours)
- **Definition**: User interacts with a specific insight (clicks into a metric, views a trend, or reads an auto-generated summary).
- **Target**: 25% of signups.
- **Key risk**: Data is visible but not meaningful; user doesn't know what to look at.
- **Actions**: Auto-generated "Your first insight" card highlighting the most interesting pattern. Push notification or email: "We found something interesting in your Slack data."

### Milestone 6: Activated (T+0 to T+7 days)
- **Definition**: Integration connected AND user returns at least once after initial session.
- **Target**: 18% of signups (the stated goal).
- **Key risk**: No reason to return; no habit loop established.
- **Actions**: Weekly digest email, Slack bot notifications with insights, invite teammates to create social accountability.

### Milestone 7: Team Expansion (T+7 to T+14 days)
- **Definition**: User invites at least one teammate or connects a second integration.
- **Target**: 10% of signups.
- **Key risk**: Individual user sees value but doesn't expand to team; tool remains single-player.
- **Actions**: "Share this insight with your team" prompts, "Connect Jira too for cross-tool analytics" upsell.

### Milestone Conversion Funnel Summary

| Milestone | Target % | Current Est. % | Gap |
|-----------|----------|----------------|-----|
| M0: Signup Complete | 100% | 100% | -- |
| M1: Integration Screen | 95% | ~70% | 25pp |
| M2: Attempt Initiated | 60% | ~35% | 25pp |
| M3: Successfully Connected | 45% | ~20% | 25pp |
| M4: First Data Visible | 35% | ~17% | 18pp |
| M5: First Insight | 25% | ~14% | 11pp |
| M6: Activated (7-day) | 18% | 12% | 6pp |

---

## Part 3: Experiment Backlog with Prioritization

Experiments are prioritized using an ICE framework (Impact, Confidence, Ease) on a 1-10 scale. Experiments are grouped into tiers.

### Tier 1: High Impact, High Confidence (Ship First)

#### Experiment 1: Remove Pre-Integration Friction Steps
- **Hypothesis**: Moving the integration selector to immediately after signup (removing profile setup, team creation, and product tour) will increase integration attempt rate by 40%.
- **Change**: Post-signup flow goes directly to the three-card integration selector. Profile and team setup deferred to post-activation.
- **Impact**: 9 | **Confidence**: 8 | **Ease**: 7 | **ICE Score**: 24
- **Metric**: Integration attempt rate (M2).
- **Duration**: 2 weeks to build, 2 weeks to measure.
- **Risk**: Some users may feel disoriented without a tour. Mitigate with contextual tooltips.
- **Sample size**: 2,500 per variant (2 weeks at 5,000/month).

#### Experiment 2: Smart Integration Default
- **Hypothesis**: Pre-selecting the most likely integration based on signup signals (email domain, company size, referral source) will increase attempt rate by 15%.
- **Change**: The integration most relevant to the user is highlighted with "Recommended for you" badge.
- **Impact**: 7 | **Confidence**: 7 | **Ease**: 8 | **ICE Score**: 22
- **Metric**: Integration attempt rate, specifically conversion from screen view to click.
- **Duration**: 2 weeks.
- **Risk**: Wrong recommendation could feel intrusive. Mitigate with easy ability to choose a different option.

#### Experiment 3: Inline OAuth with Permission Explainers
- **Hypothesis**: Showing a brief, friendly explanation of what permissions are needed and why (before the OAuth screen) will increase OAuth completion rate by 20%.
- **Change**: Insert a half-second interstitial: "We'll ask for read-only access to your [Slack messages / Jira issues / GitHub repos]. We never post or modify anything." Then launch OAuth.
- **Impact**: 8 | **Confidence**: 7 | **Ease**: 8 | **ICE Score**: 23
- **Metric**: OAuth completion rate (M2 to M3 conversion).
- **Duration**: 2 weeks.

#### Experiment 4: Integration Failure Recovery Flow
- **Hypothesis**: Users who fail the OAuth flow and see a dead-end error page never retry. Offering an alternative integration and a "request IT access" email template will recover 25% of failed attempts.
- **Change**: On OAuth failure: (a) show what went wrong in plain language, (b) offer "Try [different integration] instead," (c) provide a pre-written email to IT requesting access.
- **Impact**: 7 | **Confidence**: 8 | **Ease**: 7 | **ICE Score**: 22
- **Metric**: Recovery rate (users who fail M3 and eventually succeed).
- **Duration**: 2 weeks.

### Tier 2: Medium Impact, Worth Testing

#### Experiment 5: Demo Workspace as Fallback
- **Hypothesis**: Offering a "See a demo first" option for hesitant users will not reduce integration rates but will increase 7-day activation by giving users a reason to return and connect later.
- **Change**: Add "Explore with sample data" link below the integration cards. Demo workspace has realistic synthetic data with persistent "Connect your tools" CTAs.
- **Impact**: 6 | **Confidence**: 6 | **Ease**: 6 | **ICE Score**: 18
- **Metric**: 7-day activation rate for users who choose demo first vs. direct integration.
- **Duration**: 3 weeks to build, 3 weeks to measure.
- **Risk**: Could become a crutch; users might stay in demo indefinitely. Mitigate with a 3-day expiry on demo access.

#### Experiment 6: Progress-Based Email Sequence
- **Hypothesis**: Triggered emails based on where the user dropped off will re-engage 10% of users who left during integration setup.
- **Change**: Behavioral email sequence:
  - T+1 hour (no integration attempt): "Pick up where you left off. Connecting takes 60 seconds."
  - T+24 hours (attempt but failure): "Looks like [Integration] didn't connect. Here's a quick fix. Or try [Alternative]."
  - T+48 hours (connected but no return): "We found [N] insights in your data. Come take a look."
  - T+5 days (not activated): "Your team's data is ready. Here's a preview of what we found."
- **Impact**: 7 | **Confidence**: 6 | **Ease**: 5 | **ICE Score**: 18
- **Metric**: Re-engagement rate, 7-day activation rate for email-touched users.
- **Duration**: 2 weeks to build, 4 weeks to measure full sequence.

#### Experiment 7: Social Proof on Integration Screen
- **Hypothesis**: Showing "[X] teams connected [Integration] this week" and logos of recognizable companies will increase trust and attempt rate by 10%.
- **Change**: Add dynamic social proof counters and 2-3 customer logos to each integration card.
- **Impact**: 5 | **Confidence**: 6 | **Ease**: 9 | **ICE Score**: 20
- **Metric**: Integration attempt rate.
- **Duration**: 1 week to build, 2 weeks to measure.

#### Experiment 8: Estimated Time and Difficulty Label
- **Hypothesis**: Adding "Takes ~60 seconds" and "No technical skills required" to each integration card will reduce hesitation and increase attempt rate by 8%.
- **Change**: Add time estimate and difficulty label to each card.
- **Impact**: 4 | **Confidence**: 7 | **Ease**: 9 | **ICE Score**: 20
- **Metric**: Integration attempt rate.
- **Duration**: 1 week.

### Tier 3: Lower Confidence, Longer-Term

#### Experiment 9: Reverse Trial (Show Value Before Integration)
- **Hypothesis**: Showing users anonymized/aggregated insights from similar companies before they connect will increase motivation to connect by 15%.
- **Change**: Before the integration screen, show a 10-second "preview" of what insights look like for similar-sized engineering teams. "This is what [similar company] sees. Connect to see yours."
- **Impact**: 7 | **Confidence**: 4 | **Ease**: 4 | **ICE Score**: 15
- **Metric**: Integration attempt rate, time to attempt.
- **Duration**: 4 weeks to build (requires benchmark data), 3 weeks to measure.

#### Experiment 10: In-App Chat Support During Integration
- **Hypothesis**: Live chat or chatbot support during the integration step will help users who encounter technical issues and increase M3 conversion by 12%.
- **Change**: Add a persistent chat widget on the integration screen with pre-loaded FAQs about common integration issues.
- **Impact**: 6 | **Confidence**: 5 | **Ease**: 4 | **ICE Score**: 15
- **Metric**: M3 conversion, chat engagement rate, resolution rate.
- **Duration**: 2 weeks with existing chat vendor, 4 weeks to measure.

#### Experiment 11: Gamified Onboarding Checklist
- **Hypothesis**: A visible progress bar and checklist ("Step 1 of 3: Connect a tool") will increase completion through the Zeigarnik effect (desire to complete incomplete tasks).
- **Change**: Add a persistent sidebar checklist during onboarding with steps: Connect tool -> See first insight -> Invite a teammate. Show progress percentage.
- **Impact**: 5 | **Confidence**: 5 | **Ease**: 6 | **ICE Score**: 16
- **Metric**: Overall activation rate, checklist completion rate.
- **Duration**: 2 weeks to build, 3 weeks to measure.

#### Experiment 12: Admin-Specific Onboarding for IT-Blocked Users
- **Hypothesis**: Providing a "Request access from IT" flow with a pre-written justification email and ROI calculator will convert 15% of IT-blocked users within 7 days.
- **Change**: When a user's OAuth is blocked by organization policy, offer: (a) a pre-drafted email to their IT admin, (b) a one-pager PDF on security and compliance, (c) a link to the product's SOC2/security page.
- **Impact**: 5 | **Confidence**: 5 | **Ease**: 5 | **ICE Score**: 15
- **Metric**: IT-blocked user activation rate at 14 days.
- **Duration**: 2 weeks to build, 4 weeks to measure.

### Prioritized Execution Roadmap

| Week | Experiment | Expected Impact on Activation |
|------|-----------|-------------------------------|
| 1-2 | #1 (Remove friction) + #8 (Time labels) | +2-3pp |
| 3-4 | #3 (Permission explainers) + #7 (Social proof) | +1-2pp |
| 5-6 | #2 (Smart defaults) + #4 (Failure recovery) | +1-2pp |
| 7-8 | #6 (Email sequence) | +0.5-1pp |
| 9-10 | #5 (Demo workspace) + #11 (Checklist) | +0.5-1pp |
| 11-12 | #9 (Reverse trial) or #10 (Chat support) | +0.5pp |

**Estimated cumulative impact**: +5.5-9.5pp, bringing activation from 12% to 17.5-21.5%, bracketing the 18% target.

---

## Part 4: Measurement Plan

### Primary Metric

**7-Day Activation Rate**: Percentage of users who sign up and successfully connect at least one integration within 7 days of account creation.

- Formula: `(Users with >= 1 connected integration within 7 days of signup) / (Total signups in cohort) * 100`
- Current: 12%
- Target: 18%
- Measurement cadence: Weekly rolling cohort.
- Cohort definition: All users who complete signup (email verified, account created) in a given calendar week.

### Secondary Metrics (Guardrails)

These must not degrade as we optimize the primary metric.

| Metric | Definition | Current | Guardrail |
|--------|-----------|---------|-----------|
| Signup completion rate | % of users who start signup and complete it | Baseline TBD | Must not decrease |
| Time to first integration attempt | Median time from signup to first "Connect" click | Baseline TBD | Should decrease |
| OAuth completion rate | % of users who start OAuth and complete it | Baseline TBD | Should increase |
| Integration error rate | % of integration attempts that fail | Baseline TBD | Should decrease |
| 30-day retention | % of activated users who return in days 8-30 | Baseline TBD | Must not decrease |
| Support ticket volume | Tickets per 1,000 signups related to onboarding | Baseline TBD | Should not increase >20% |

### Funnel Instrumentation

Every transition in the milestone map must emit a tracking event. Required events:

```
Event Name                          Properties
----------------------------------  ------------------------------------------
signup_completed                    user_id, signup_method, referral_source
integration_screen_viewed           user_id, timestamp, variant_id
integration_card_clicked            user_id, integration_type, is_recommended
oauth_started                       user_id, integration_type
oauth_completed                     user_id, integration_type, success (bool)
oauth_failed                        user_id, integration_type, error_code
integration_connected               user_id, integration_type, time_from_signup
first_data_synced                   user_id, integration_type, records_count
first_insight_viewed                user_id, insight_type, time_from_signup
demo_workspace_entered              user_id
demo_to_real_converted              user_id, time_in_demo
recovery_flow_shown                 user_id, failure_type
recovery_action_taken               user_id, action (retry/switch/email_it)
onboarding_email_sent               user_id, email_type, trigger
onboarding_email_clicked            user_id, email_type
user_returned                       user_id, days_since_signup, session_number
teammate_invited                    user_id, invite_count
second_integration_connected        user_id, integration_type
```

### Experiment Framework

**Statistical Requirements**:
- Minimum detectable effect (MDE): 2 percentage points (from 12% to 14%).
- Significance level: 95% (alpha = 0.05).
- Power: 80%.
- Required sample size per variant: ~2,400 users (approximately 2 weeks at 2,500/variant given 5,000 signups/month).
- Sequential testing: Use a sequential testing framework (e.g., always-valid p-values) to allow for early stopping if effects are large, since we have limited traffic.

**Experiment Execution Rules**:
1. Run no more than 2 experiments simultaneously to avoid interaction effects (with 5,000 signups/month, each experiment needs ~50% of traffic).
2. Each experiment runs for a minimum of 2 full weeks (to capture weekday/weekend variation).
3. Segment results by: integration type, company size, referral source, and geography.
4. Ship winners immediately; failed experiments get a post-mortem within 48 hours.
5. Compound winners: when experiment A wins, it becomes the new control for experiment B.

**Reporting Cadence**:
- Daily: Automated funnel dashboard with event counts and conversion rates per step.
- Weekly: Cohort-level activation rate by signup week, broken down by variant.
- Bi-weekly: Experiment readout with statistical significance, segment analysis, and go/no-go decision.
- Monthly: Executive summary with cumulative activation rate trend, experiments shipped, and learnings.

### Dashboard Requirements

**Real-Time Funnel Dashboard** (updated hourly):
- Signup -> Integration Screen -> Attempt -> OAuth Complete -> Data Synced -> Insight Viewed -> Returned
- Filterable by: date range, integration type, experiment variant, user segment.
- Anomaly alerts: If any funnel step drops >15% day-over-day, trigger a Slack alert.

**Weekly Cohort Dashboard**:
- Activation rate by signup week (line chart, trailing 12 weeks).
- Activation rate by integration type (stacked bar).
- Median time-to-activation trend.
- Drop-off analysis: Which step lost the most users this week vs. last week?

**Experiment Dashboard**:
- Current experiments: variant allocation, sample sizes, conversion rates, confidence intervals.
- Historical experiments: win/loss record, cumulative impact on activation rate.

### Success Criteria for the Quarter

| Criterion | Measurement | Target |
|-----------|------------|--------|
| Primary goal met | 7-day activation rate (4-week rolling average) | >= 18% |
| No regression on signup | Signup completion rate (4-week rolling average) | >= current baseline |
| Statistical confidence | At least 3 experiments reach significance | 95% confidence |
| Instrumentation complete | All funnel events firing correctly | 100% coverage |
| Sustained improvement | Activation rate holds for 3+ consecutive weeks | >= 18% |

---

## Appendix: Quick Wins (Can Ship Without A/B Testing)

These are low-risk changes that can be shipped directly without experimentation:

1. **Fix known OAuth error messages**: Audit current error states and replace technical error codes with human-readable messages and clear next steps.
2. **Add integration status page link**: If an integration's API is down, show a status indicator so users know it's not their fault.
3. **Pre-fill company name from email domain**: Reduce one more form field during signup.
4. **Add "why we need these permissions" tooltip**: Inline explanation next to each OAuth permission request.
5. **Remove "Skip" button prominence**: If there's currently a prominent "Skip" or "Do this later" option on the integration screen, reduce its visual weight (smaller text, lower contrast, bottom of page).

---

## Appendix: Qualitative Research Recommendations

To increase confidence in the experiment backlog, conduct the following research within the first 2 weeks:

1. **5 user interviews with recent drop-offs**: Recruit users who signed up in the last 30 days, reached the integration screen, and did not connect. Ask: What stopped you? What would have helped?
2. **Session recordings review**: Watch 20 session recordings of users on the integration screen. Code for: hesitation patterns, error encounters, back-button usage, time spent reading.
3. **Support ticket analysis**: Categorize the last 100 onboarding-related support tickets by failure type (OAuth error, permission issue, wrong account, IT block, confusion about which integration).
4. **Competitive teardown**: Sign up for 3 competitor products and document their integration onboarding flow. Note what they do differently.

These research activities will help refine hypotheses and may reorder experiment priorities.
