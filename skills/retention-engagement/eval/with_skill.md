# Retention & Engagement Improvement Pack

**Product:** Meditation & Mindfulness App (B2C Subscription)
**Prepared:** 2026-03-17
**Skill:** `retention-engagement`

---

## 1) Context Snapshot

- **Product:** B2C meditation and mindfulness mobile app (subscription model, $9.99/month).
- **ICP / primary user:** Paid subscribers seeking daily meditation and mindfulness practice. Likely adults 25-45 looking for stress reduction, sleep improvement, or mental health support.
- **Segments in scope:**
  - **Segment A:** Paid subscribers who completed at least one guided session in week 1 ("activated paid users").
  - **Segment B:** Paid subscribers who never completed a full guided session ("unconverted paid users").
- **Stage:** Early PMF / Growth (product has paying users, but retention is weak, indicating the value loop is not yet sticky).
- **Goal:** Improve paid D30 retention from 22% to 32% within 90 days (by mid-June 2026). Intermediate target: reduce the week-2 engagement cliff so that daily sessions drop no lower than 2.0/day (from current 1.1) by end of 30-day sprint.
- **Constraints:**
  - 4-week sprint; 1 PM + 2 engineers.
  - No major app redesign allowed (config changes, new screens/modals OK; no navigation overhaul or new core features).
  - Channels: push notifications + in-app only (no email).
  - No dark patterns, coercive streaks, or guilt-based messaging.

---

## 2) Metric Definitions + Guardrails

| Metric | Definition (behavior) | Segment | Window | Baseline | Target | Source | Notes |
|---|---|---|---|---:|---:|---|---|
| D30 Paid Retention | Paid subscriber completes at least 1 meditation session on day 28-32 after subscription start | All paid subs | D28-32 | 22% | 32% | Analytics (assumed: Amplitude/Mixpanel) | Primary outcome metric |
| Daily Session Frequency (Week 3+) | Average sessions/day for paid users who are 15+ days into subscription | All paid subs | Rolling 7-day avg | 1.1 sessions/day (post week 2) | 2.0 sessions/day | Analytics | Leading indicator for engagement cliff |
| D7 Paid Retention | Paid subscriber completes at least 1 session on day 5-9 | All paid subs | D5-9 | ~55% (assumed) | 65% | Analytics | Early retention signal |
| Activation Rate | % of paid subs who reach aha moment (defined in Section 4) within 7 days | All paid subs | First 7 days | Unknown (to be measured) | 60%+ | Analytics | Requires new instrumentation |
| Weekly Active Sessions | Median sessions/week for retained paid users | Retained paid subs | Weekly cohort | 4.2/day wk1 -> 1.1/day wk3 | Flatten curve | Analytics | Engagement decay indicator |

**Guardrails**
- **Revenue / conversion:** Subscription cancellation rate must not increase by more than 2pp during experiments. Trial-to-paid conversion (if applicable) must not decline.
- **User trust:** Push notification opt-out rate must not increase by more than 5pp. App store rating must not drop below current. Zero tolerance for complaints about manipulative UX.
- **Performance / reliability:** App crash rate and session load time must stay within current p95.

---

## 3) Diagnosis (What's Broken, Where, and Why)

### 3.1 Cohort/Curve Snapshot (by segment)

| Segment | Activation Rate | D1 | D7 | D30 | WAU/MAU | Primary Failure Mode | Evidence |
|---|---:|---:|---:|---:|---:|---|---|
| Activated paid users (completed 1+ session in wk 1) | ~70% (assumed) | ~80% (assumed) | ~60% (assumed) | ~30% (assumed) | ~0.35 (assumed) | Engagement decay | Users get value in week 1 (4.2 sessions/day) but drop sharply after week 2 (1.1/day); habit does not form |
| Unconverted paid users (no full session in wk 1) | ~0% | ~40% (assumed) | ~15% (assumed) | ~5% (assumed) | ~0.10 (assumed) | Activation failure | Paid but never experienced core value; likely cancels before D30 |

**Confidence note:** D1/D7 breakdowns by segment are assumed based on the provided D30 = 22% aggregate and the engagement cliff pattern. These should be validated with actual cohort data.

### 3.2 Onboarding Drop-offs

| Step | % Reach | % Complete | Biggest Drop Reason (hypothesis) | Instrumented? |
|---|---:|---:|---|---|
| Subscription confirmed | 100% | 100% | N/A | Yes (payment event) |
| First session started | ~85% (assumed) | ~75% (assumed) | Users browse library but feel overwhelmed by choices; no clear "start here" | Likely partial |
| First session completed | ~75% (assumed) | ~65% (assumed) | Session too long or not matched to mood/goal; users exit mid-session | Unknown |
| Second session (same day or next day) | ~65% (assumed) | ~50% (assumed) | No prompt to return; no clear "what's next" after first session | Unknown |
| Third+ session in first week | ~50% (assumed) | ~40% (assumed) | Initial motivation fades; no habit trigger established | Unknown |
| Any session in week 3 | ~35% (assumed) | ~22% (actual D30 proxy) | Engagement cliff: novelty worn off, no personalization, no progress anchor | Unknown |

### 3.3 Primary Diagnosis

- **Primary failure mode: Engagement decay (post-activation habit failure)**
  - Users who start meditating do so enthusiastically in week 1 (4.2 sessions/day is very high), but the habit collapses after week 2 (1.1 sessions/day). This is a classic "novelty cliff" pattern: initial enthusiasm is not converted into a sustainable daily routine.

- **Secondary failure mode: Activation failure (subset)**
  - A portion of paid subscribers likely never complete a meaningful session. These users churn fast and pull down the aggregate D30 number.

- **Biggest leak:** Activated paid users x week 2-3 transition x daily sessions dropping from 4.2 to 1.1.
  - This is the highest-leverage fix because these users already demonstrated intent (they paid and they used the product heavily in week 1). The value is proven; the habit is not.

- **Top 3 root-cause hypotheses (ranked):**
  1. **No habit anchor after initial novelty.** Week 1 usage (4.2 sessions/day) is unusually high, suggesting "exploration mode" rather than sustainable practice. Once users explore the library, there is no structured progression, personalized plan, or daily anchor to sustain a routine. The product relies on intrinsic motivation, which fades.
  2. **No accruing value or visible progress.** Users cannot see what they have built (total minutes, streak history, mood trends, skill progression). Without a sense of accumulated investment, there is no "mounting loss" from leaving, and no reason to prefer this app over free alternatives or simply stopping.
  3. **Re-engagement timing and relevance are weak.** Push notifications (if sent) are likely generic ("Time to meditate!") rather than tied to the user's specific practice pattern, missed schedule, or content they care about. After week 2, users who skip a day receive no compelling reason to return.

---

## 4) Activation / "Aha Moment" Definition (Data-Backed)

### Candidate Behaviors

| Candidate "Aha" Behavior | Threshold Window | Why It Represents Value | Expected Link to Retention | Data Available? |
|---|---|---|---|---|
| Completes 3 guided meditation sessions | Within 7 days | Demonstrates repeated engagement beyond curiosity; user has experienced the core product multiple times | Strong: multi-session users likely form initial habit | Likely (session_completed events) |
| Completes 1 session + saves/favorites a program or teacher | Within 7 days | Saving signals intent to return and personal relevance found | Moderate: curation behavior predicts commitment | Unknown (check for save/favorite events) |
| Completes sessions on 3 distinct days | Within 7 days | Multi-day usage is a stronger habit signal than same-day binging | Strong: daily return is the core retention behavior | Likely (session timestamps) |
| Completes a full "beginner" or "starter" program (e.g., 5-day intro) | Within 14 days | Program completion = structured journey + sense of accomplishment | Strong: program completers should retain much better | Unknown (check for program progress tracking) |
| Sets a daily meditation reminder in-app | Within 7 days | Self-selected commitment device; user is designing their own habit trigger | Moderate-strong: reminder setters have external trigger for return | Unknown (check for reminder_set event) |

### Chosen Activation Definition (v1)

- **Definition:** Paid subscriber completes meditation sessions on **3 or more distinct calendar days** within their **first 7 days** of subscription.
- **Segment:** All paid subscribers.
- **Window:** First 7 calendar days from subscription start.
- **Leading indicator(s):**
  - Sessions on day 2 (next-day return after first session).
  - Reminder set within first 3 days.
  - Session completion rate (started vs. completed).

### Validation Plan

- **How to validate:** Run a retrospective cohort analysis: compare D30 retention for users who met the 3-distinct-days threshold vs. those who did not. Test alternative thresholds (2 days, 4 days, 5 days) to find the sharpest separation. Also test "3 sessions + 1 save" and "completed a starter program" as alternatives.
- **Decision rule:** If the chosen definition does not separate retained vs. churned cohorts by at least 15pp in D30 retention, revise the definition. If program completion shows a stronger signal, shift to that as the activation definition.
- **Tracking requirements:**
  - `session_completed` event with properties: `session_id`, `session_type`, `duration_seconds`, `day_number_since_sub`, `calendar_date`
  - `program_progress` event with: `program_id`, `step_number`, `completed_boolean`
  - `reminder_set` event with: `time_of_day`, `frequency`
  - `content_saved` event with: `content_id`, `content_type`

---

## 5) Lever Hypotheses Map (Convert Insights into Tests)

| Failure Mode | Lever | Hypothesis | Leading Indicator | Experiment Ideas |
|---|---|---|---|---|
| Activation failure | Onboarding / time-to-value | If we guide new paid users to a personalized "starter plan" immediately after subscription (instead of dropping them into the full library), more users will complete 3 sessions in 7 days | Activation rate (3 days in 7); first-session start rate | Exp 1: Personalized starter plan onboarding |
| Activation failure | Onboarding / time-to-value | If we prompt users to set a daily reminder during their first session completion, they will be more likely to return on day 2 | Day-2 return rate; reminder set rate | Exp 2: Post-first-session reminder prompt |
| Engagement decay | Habit / daily return | If we introduce a "daily personalized session" that adapts to time of day, mood, and past preferences, users will maintain higher session frequency through weeks 2-4 | Sessions/day in weeks 2-4; session completion rate | Exp 3: Adaptive daily session recommendation |
| Engagement decay | Habit / daily return | If we surface a lightweight "1-minute check-in" option for days when users are busy (instead of only 10-20 min sessions), users who would otherwise skip entirely will maintain their streak of daily practice | % of days with at least 1 session (weeks 2-4); micro-session usage | Exp 4: Micro-session ("1-minute calm") option |
| Engagement decay | Accruing value | If we add a visible "meditation journey" dashboard showing total minutes, current streak, mood trends, and milestones, users will feel accumulated investment and be less likely to disengage | Dashboard view rate; D14/D30 retention; session frequency weeks 3-4 | Exp 5: Progress dashboard + milestone celebrations |
| Engagement decay | Accruing value | If we surface weekly "mindfulness insights" (your most peaceful time of day, sessions this week vs. last, new techniques tried), users perceive growing personal value | Insights view rate; week-over-week session frequency | Exp 6: Weekly mindfulness insights card |
| Engagement decay | Re-engagement | If we send a contextual push notification when a user misses their usual meditation time (personalized to their established pattern), they will return more often than with generic reminders | Push open rate; same-day session after push; weekly retention | Exp 7: Contextual "missed session" push notification |
| Engagement decay | Re-engagement | If we send a "welcome back" in-app message with a curated short session after 3+ days of inactivity (instead of showing the generic home screen), lapsed users will re-engage | Re-engagement session rate; 7-day retention post-return | Exp 8: "Welcome back" re-engagement flow |

---

## 6) Experiment Backlog (Prioritized)

### Prioritization

Scoring: Impact (1-5) x Confidence (1-5) / Effort (1-5). Higher = better.

| # | Experiment | Segment | Hypothesis | Impact | Confidence | Effort | Score | Dependencies |
|---|---|---|---|---:|---:|---:|---:|---|
| 1 | Personalized starter plan onboarding | New paid subs | Guided start -> higher activation | 5 | 4 | 3 | 6.7 | Content: need 3-4 curated starter paths |
| 2 | Post-first-session reminder prompt | New paid subs (first session) | Reminder -> day-2 return | 4 | 5 | 1 | 20.0 | Reminder infrastructure exists |
| 3 | Micro-session ("1-minute calm") | All paid subs, weeks 2+ | Low-effort option -> maintains daily habit | 4 | 4 | 2 | 8.0 | Need 5-10 micro-session audio assets |
| 4 | Contextual "missed session" push | Paid subs with established pattern | Personalized push -> return | 4 | 3 | 3 | 4.0 | Needs pattern detection logic |
| 5 | Adaptive daily session recommendation | All paid subs | Personalized daily pick -> sustained frequency | 5 | 3 | 4 | 3.8 | Needs recommendation logic |
| 6 | Progress dashboard + milestones | All paid subs | Visible progress -> accruing value -> retention | 5 | 4 | 4 | 5.0 | Needs new UI screen (within constraints?) |
| 7 | Weekly mindfulness insights card | Active paid subs | Personal insights -> perceived value | 3 | 3 | 2 | 4.5 | Needs aggregation logic |
| 8 | "Welcome back" re-engagement flow | Lapsed paid subs (3+ days inactive) | Curated return -> re-engagement | 3 | 3 | 2 | 4.5 | Needs lapse detection + content curation |

**Ranked by feasibility within 4-week sprint and impact:**
1. Post-first-session reminder prompt (Score: 20.0 -- very low effort, high confidence)
2. Micro-session ("1-minute calm") (Score: 8.0)
3. Personalized starter plan onboarding (Score: 6.7)
4. Progress dashboard + milestones (Score: 5.0)
5. Weekly mindfulness insights card (Score: 4.5)
6. "Welcome back" re-engagement flow (Score: 4.5)
7. Contextual "missed session" push (Score: 4.0)
8. Adaptive daily session recommendation (Score: 3.8)

---

### Experiment Cards (Top 6)

#### Experiment Card 1: Post-First-Session Reminder Prompt

- **Name:** Post-First-Session Reminder Prompt
- **Target segment:** New paid subscribers who just completed their first meditation session.
- **Hypothesis:** If we prompt users to set a personalized daily meditation reminder immediately after their first session (when motivation is highest), day-2 return rate will increase by 15pp, because an external trigger bridges the gap between initial enthusiasm and habit formation.
- **Change / treatment:** After first session completion, show a modal: "Great first session! Pick a time for your daily meditation and we'll gently remind you." Offer time picker with smart default (same time tomorrow). Control group sees the current post-session screen (no reminder prompt).
- **Success metric (primary):** Day-2 return rate (% of users who complete a session on day 2).
- **Leading indicator(s):** Reminder set rate; push notification opt-in rate.
- **Guardrails:** Push opt-out rate must not increase by more than 2pp; app store complaints about notifications must not increase.
- **Required instrumentation:** `reminder_prompt_shown`, `reminder_set` (with `time_selected`), `reminder_dismissed`, `session_completed` with `day_number`.
- **Rollout plan:** 50/50 A/B test for 2 weeks on all new paid subscribers. Evaluate at day 14.
- **Rollback plan:** Feature flag; disable modal if guardrail is breached within first 3 days.
- **Expected decision date:** End of week 2 of sprint.

#### Experiment Card 2: Micro-Session ("1-Minute Calm")

- **Name:** 1-Minute Calm Micro-Sessions
- **Target segment:** All paid subscribers, particularly those in weeks 2-4 of subscription.
- **Hypothesis:** If we offer a "1-minute calm" session option prominently on the home screen (alongside longer sessions), users who would otherwise skip their daily practice entirely will complete the micro-session instead, maintaining their daily practice streak. This will increase the percentage of days with at least 1 session by 20% in weeks 2-4.
- **Change / treatment:** Add a prominent "1-Minute Calm" card at the top of the home screen. Create 10 micro-session audio tracks (breathing exercises, body scans, gratitude moments). Control group sees the current home screen. Treatment group sees the micro-session card.
- **Success metric (primary):** % of days with at least 1 session in weeks 2-4 (per user).
- **Leading indicator(s):** Micro-session completion rate; total sessions/week in weeks 2-4; ratio of micro vs. full sessions.
- **Guardrails:** Full-length session frequency must not decrease (micro-sessions should add to, not substitute for, regular sessions). Revenue/cancellation rate neutral.
- **Required instrumentation:** `session_completed` with `session_type` (micro vs. standard), `session_duration`, `home_screen_card_tapped` with `card_type`.
- **Rollout plan:** 50/50 A/B test for 3 weeks. Minimum 2 weeks of post-treatment observation for users in their week 2-4 window.
- **Rollback plan:** Feature flag; remove micro-session card. Content assets remain available for future use.
- **Expected decision date:** End of week 3 of sprint.

#### Experiment Card 3: Personalized Starter Plan Onboarding

- **Name:** Personalized Starter Plan Onboarding
- **Target segment:** New paid subscribers (first app open after subscription).
- **Hypothesis:** If we replace the current "browse the library" first experience with a short quiz (3 questions: goal, experience level, preferred time) that maps to a curated 7-day starter plan, the activation rate (3 sessions on 3 distinct days in 7 days) will increase by 10pp, because users receive a clear path instead of choice overload.
- **Change / treatment:** After subscription confirmation, show a 3-question quiz, then present a personalized 7-day plan ("Your Calm Start", "Sleep Better in 7 Days", "Stress Relief Essentials", "Mindfulness for Beginners"). Plan appears as the primary home screen element with daily session queued. Control group sees the current library browse experience.
- **Success metric (primary):** Activation rate (3 distinct days with completed session in first 7 days).
- **Leading indicator(s):** Quiz completion rate; first session start rate; day-2 and day-3 return rates.
- **Guardrails:** Library browse sessions must not decrease (plan should complement, not hide, the library). Session completion rate must not decline (plans must be well-curated).
- **Required instrumentation:** `onboarding_quiz_shown`, `onboarding_quiz_completed` (with `goal`, `experience`, `time_preference`), `starter_plan_assigned` (with `plan_id`), `starter_plan_day_completed`, `session_completed` with `source` (plan vs. library).
- **Rollout plan:** 50/50 A/B test for 2 weeks on new paid subscribers. Need 3-4 curated starter plans ready before launch.
- **Rollback plan:** Feature flag; revert to library browse. Quiz data retained for future personalization.
- **Expected decision date:** End of week 2 of sprint (for activation rate); D30 readout at day 30+.

#### Experiment Card 4: Progress Dashboard + Milestone Celebrations

- **Name:** Meditation Journey Dashboard
- **Target segment:** All paid subscribers (visible after first completed session).
- **Hypothesis:** If we add a "Your Journey" tab showing total meditation minutes, current streak (non-punitive framing), sessions completed, and milestone badges (10 sessions, 7-day streak, 30 minutes total, etc.), users will perceive accruing value and be 15% less likely to churn in weeks 3-4, because visible progress creates ethical "mounting loss."
- **Change / treatment:** New "Journey" tab in bottom navigation (replacing or augmenting existing). Shows: total minutes, session count, current streak (with encouraging framing, never guilt), milestone badges with celebration animations, and a simple weekly bar chart. Control group does not see the tab.
- **Success metric (primary):** D30 retention (requires longer observation; use D14 retention as early proxy).
- **Leading indicator(s):** Journey tab view rate; milestone celebration view rate; session frequency in weeks 2-4.
- **Guardrails:** Must not introduce guilt/shame framing for missed days (use "welcome back" language, not "you broke your streak"). No competitive/social pressure. Cancellation rate neutral.
- **Required instrumentation:** `journey_tab_viewed`, `milestone_achieved` (with `milestone_type`, `milestone_value`), `milestone_celebration_viewed`, existing session events with cumulative counters.
- **Rollout plan:** 50/50 A/B test. Requires ~1.5 weeks of engineering. Launch mid-sprint, observe for remaining time.
- **Rollback plan:** Feature flag; hide tab. Data aggregation continues in background.
- **Expected decision date:** End of sprint for leading indicators; D30 readout at day 30+.

#### Experiment Card 5: Weekly Mindfulness Insights Card

- **Name:** Weekly Mindfulness Insights
- **Target segment:** Active paid subscribers (at least 2 sessions in the past week).
- **Hypothesis:** If we surface a personalized weekly insights card every Monday (showing "your most peaceful time of day," "minutes this week vs. last," "new techniques explored"), users will perceive ongoing personal value from the data the app accumulates, increasing week-over-week return rate by 10%.
- **Change / treatment:** Every Monday, show a dismissible in-app card at the top of the home screen with 2-3 personalized insights. Push notification: "Your weekly mindfulness insights are ready." Control group does not receive the card or notification.
- **Success metric (primary):** Week-over-week return rate (% of users active in week N who are also active in week N+1).
- **Leading indicator(s):** Insights card view rate; insights card tap-through rate; Monday session rate.
- **Guardrails:** Push notification opt-out rate must not increase. Card must be easily dismissible. No data shared externally.
- **Required instrumentation:** `weekly_insights_generated`, `weekly_insights_card_shown`, `weekly_insights_card_tapped`, `weekly_insights_card_dismissed`, `weekly_insights_push_sent`, `weekly_insights_push_opened`.
- **Rollout plan:** 50/50 A/B test. Requires aggregation logic + card UI (~1 week engineering). Run for 3+ weeks to observe multi-week trends.
- **Rollback plan:** Feature flag; stop generating/showing cards.
- **Expected decision date:** End of week 4 (preliminary); full read at week 6.

#### Experiment Card 6: "Welcome Back" Re-Engagement Flow

- **Name:** Welcome Back Re-Engagement Flow
- **Target segment:** Paid subscribers who have been inactive for 3+ consecutive days but have not cancelled.
- **Hypothesis:** If we show a "Welcome back" in-app screen (when they next open the app) with a curated short session tailored to their past preferences (instead of the generic home screen), re-engaged users will complete a session at 2x the rate of the control, because reducing choice friction at the moment of return lowers the barrier to re-engagement.
- **Change / treatment:** When a 3+-day inactive user opens the app, show a welcome-back screen: "Welcome back! We picked a [5-min / their preferred duration] [their preferred type] session for you." One-tap to start. Option to dismiss and browse normally. Control group sees the standard home screen.
- **Success metric (primary):** Re-engagement session completion rate (% of returning lapsed users who complete a session on their return visit).
- **Leading indicator(s):** Welcome-back screen view rate; one-tap start rate; 7-day retention after return.
- **Guardrails:** Must not feel intrusive; dismiss option must be prominent. Must not block access to other features. No guilt language.
- **Required instrumentation:** `welcome_back_shown` (with `days_inactive`, `recommended_session_id`), `welcome_back_session_started`, `welcome_back_dismissed`, `session_completed` with `source` = "welcome_back".
- **Rollout plan:** Feature flag, 50/50 for returning lapsed users. Sample size depends on lapse rate.
- **Rollback plan:** Feature flag; disable welcome-back screen.
- **Expected decision date:** Ongoing (rolling cohort); first read at week 3 of sprint.

---

## 7) Measurement + Instrumentation Plan

### Key Events

| Event Name | Description | Required Properties | Used For |
|---|---|---|---|
| `session_started` | User taps play on any meditation session | `session_id`, `session_type` (micro/standard), `source` (plan/library/welcome_back/push), `user_id`, `timestamp` | Engagement, activation, all experiments |
| `session_completed` | User finishes a meditation session (reaches end) | `session_id`, `session_type`, `duration_seconds`, `source`, `day_number_since_sub`, `calendar_date`, `user_id` | Activation, retention, engagement decay analysis |
| `session_abandoned` | User exits session before completion | `session_id`, `duration_listened`, `total_duration`, `abandon_point_pct` | Session quality, content-market fit |
| `reminder_set` | User configures a daily reminder | `time_of_day`, `frequency`, `source` (onboarding_prompt / settings), `user_id` | Exp 1, activation |
| `reminder_prompt_shown` | Post-first-session reminder modal displayed | `user_id`, `variant` | Exp 1 |
| `onboarding_quiz_completed` | User finishes the starter plan quiz | `goal`, `experience_level`, `time_preference`, `user_id` | Exp 3 |
| `starter_plan_assigned` | User is assigned a personalized 7-day plan | `plan_id`, `plan_name`, `user_id` | Exp 3 |
| `starter_plan_day_completed` | User completes a day in their starter plan | `plan_id`, `day_number`, `user_id` | Exp 3, activation |
| `journey_tab_viewed` | User views the Journey/Progress tab | `user_id`, `total_minutes`, `current_streak`, `milestones_earned` | Exp 4 |
| `milestone_achieved` | User earns a milestone badge | `milestone_type`, `milestone_value`, `user_id` | Exp 4 |
| `weekly_insights_card_shown` | Weekly insights card displayed on home screen | `user_id`, `week_number`, `insights_count` | Exp 5 |
| `weekly_insights_push_opened` | User opens app from weekly insights push | `user_id`, `week_number` | Exp 5 |
| `welcome_back_shown` | Welcome-back screen displayed to lapsed user | `user_id`, `days_inactive`, `recommended_session_id` | Exp 6 |
| `welcome_back_session_started` | User taps "start" on welcome-back recommendation | `user_id`, `session_id` | Exp 6 |
| `push_sent` | Any push notification sent | `user_id`, `push_type`, `content_id`, `timestamp` | All push experiments, guardrails |
| `push_opened` | User opens app from push notification | `user_id`, `push_type`, `content_id`, `timestamp` | All push experiments |
| `subscription_cancelled` | User cancels subscription | `user_id`, `days_since_sub`, `reason` (if captured) | Guardrail: churn rate |
| `content_saved` | User saves/favorites a session, teacher, or program | `content_id`, `content_type`, `user_id` | Activation validation |
| `home_screen_card_tapped` | User taps a card on home screen | `card_type`, `card_position`, `user_id` | Exp 2, 5 |

### Dashboards to Create

| Dashboard | Audience | Metrics | Refresh |
|---|---|---|---|
| Retention Cohort Tracker | PM, Growth team | D1/D7/D14/D30 paid retention by weekly cohort; split by activated vs. not | Daily |
| Engagement Cliff Monitor | PM, Engineering | Daily sessions/user by subscription week (1, 2, 3, 4+); session completion rate; micro vs. standard sessions | Daily |
| Activation Funnel | PM, Growth team | Activation rate (3-day threshold); reminder set rate; starter plan completion; first-session-to-second-session conversion | Daily |
| Experiment Scorecard | PM, Engineering, Leadership | Primary metric + leading indicators + guardrails for each active experiment; statistical significance indicators | Daily (auto-refresh) |
| Push Health | PM | Push sent volume, open rate, opt-out rate, by push type; frequency per user per week | Daily |
| Weekly Insights | PM (weekly review) | Week-over-week retention, session frequency trends, top content, cohort movement | Weekly (Monday) |

---

## 8) 30/60/90 Execution Plan

| Timeframe | Outcomes | Work Items | Owner | Dependencies |
|---|---|---|---|---|
| **Days 1-7 (Week 1)** | Instrumentation in place; Exp 1 and Exp 2 live | 1. Instrument all key events listed above (prioritize: `session_completed` properties, `reminder_set`, `home_screen_card_tapped`). 2. Build Retention Cohort Tracker and Engagement Cliff Monitor dashboards. 3. Run retrospective activation analysis (validate 3-day-in-7 definition). 4. Build and launch Exp 1: Post-first-session reminder prompt (low effort, feature flag). 5. Create micro-session audio assets (5-10 tracks, 1 min each -- content team). 6. Build and launch Exp 2: Micro-session card on home screen. | PM: instrumentation spec + dashboards. Eng 1: event instrumentation + dashboards. Eng 2: Exp 1 (reminder prompt) + Exp 2 (micro-session card). | Micro-session audio content must be ready by day 5. |
| **Days 8-14 (Week 2)** | Exp 3 live; Exp 1 early read; activation analysis complete | 1. Read Exp 1 results (day-2 return rate for first cohort). 2. Complete activation validation analysis; confirm or revise aha definition. 3. Build and launch Exp 3: Personalized starter plan onboarding (quiz + plan assignment). 4. Begin building Exp 4: Progress dashboard (design + engineering). 5. Design weekly insights card (Exp 5). | PM: activation analysis + experiment reads. Eng 1: Exp 3 (quiz + plan). Eng 2: Exp 4 (progress dashboard). | Need 3-4 curated starter plans assembled by day 8. |
| **Days 15-21 (Week 3)** | Exp 4 and Exp 5 live; Exp 2 early read | 1. Read Exp 2 results (micro-session adoption, session frequency in weeks 2-3). 2. Launch Exp 4: Progress dashboard + milestones. 3. Build and launch Exp 5: Weekly insights card. 4. Build Exp 6: Welcome-back re-engagement flow. 5. Design contextual push logic (Exp 7, for later sprint). | PM: experiment reads + next sprint planning. Eng 1: Exp 5 (insights card). Eng 2: Exp 4 launch + Exp 6 build. | Exp 4 requires cumulative session data; ensure aggregation is working from Week 1 instrumentation. |
| **Days 22-28 (Week 4)** | Exp 6 live; sprint retrospective; 30-day plan for next sprint | 1. Launch Exp 6: Welcome-back re-engagement flow. 2. Full read on Exp 1 (2-week data: day-2 return, D7 retention). 3. Interim read on Exp 2 and Exp 3 (leading indicators). 4. Sprint retrospective: which experiments show signal? 5. Prioritize next sprint backlog (Exp 7: contextual push, plus scale winners). 6. Document learnings and update activation definition if needed. | PM: retro + next sprint plan. Eng 1 + 2: Exp 6 launch + cleanup. | D30 retention outcomes for Exp 1-3 cohorts will not be available until days 42-58; plan for delayed reads. |
| **Days 31-60 (Sprint 2)** | D30 reads on Sprint 1 experiments; scale winners; run Exp 7-8 | 1. D30 retention read on Exp 1 and Exp 2 cohorts. 2. Scale winning experiments to 100% rollout. 3. Kill or iterate on underperforming experiments. 4. Build and launch Exp 7: Contextual "missed session" push (requires pattern detection). 5. Iterate on Exp 3 (starter plans) based on data: test different plan lengths, content types. 6. Build second iteration of progress dashboard based on usage data. 7. Begin D30 reads on Exp 3-6 cohorts. | PM + Eng team (plan for similar capacity). | Pattern detection logic for Exp 7 may need data science support. |
| **Days 61-90 (Sprint 3)** | Full D30 reads on all experiments; retention target assessment; long-term roadmap | 1. Complete D30 retention reads on all 6 experiments. 2. Aggregate impact: has D30 paid retention moved from 22% toward 32% target? 3. Identify compounding effects (e.g., reminder + micro-session + progress dashboard together). 4. Plan long-term retention investments: content strategy, deeper personalization, community features, adaptive difficulty. 5. Publish retention playbook for the team. 6. Decide: continue optimizing (more experiments) or shift to adjacent levers (monetization, acquisition). | PM: analysis + roadmap. Eng: scaling + technical debt from experiments. | Full D30 data requires cohorts that started experiments in weeks 1-4. |

---

## 9) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Instrumentation gaps delay experiment reads.** Current event tracking may be incomplete; instrumenting all required events in week 1 is ambitious. | Medium | High | Prioritize the 5 most critical events in days 1-3. Accept partial data for lower-priority experiments. |
| **Micro-session content quality is low.** If 1-minute sessions feel rushed or unfulfilling, they may hurt brand perception rather than help retention. | Low-Medium | Medium | Have content team create and internally test micro-sessions before launch. Include user feedback mechanism. |
| **Push notification fatigue.** Running Exp 1 (reminder), Exp 5 (weekly insights push), and Exp 7 (missed session push) simultaneously could overwhelm users. | Medium | High | Implement a push frequency cap (max 1 push/day per user across all experiment types). Monitor opt-out rate daily. |
| **4.2 sessions/day baseline may be inflated.** If week 1 data includes "free trial exploration" behavior, the engagement cliff may be partly an artifact of trial-to-paid transition timing. | Medium | Medium | Segment analysis: compare session patterns for users on free trial vs. immediately-paid. Adjust baseline if needed. |
| **"No major redesign" constraint limits Exp 3 and Exp 4.** Personalized onboarding quiz and progress dashboard may be considered "too big" by stakeholders. | Low-Medium | Medium | Design minimal versions first (quiz = 3 questions on a single screen; dashboard = single scrollable view, not a new navigation tab). Get stakeholder alignment in week 1. |
| **Small team bandwidth.** 1 PM + 2 engineers running 6 experiments in 4 weeks is aggressive. | Medium | High | Strict prioritization: Exp 1 and 2 must ship in week 1. Exp 3-6 are stretch goals. Use feature flags to manage rollout timing. |

### Open Questions

| Question | How to Answer | Priority |
|---|---|---|
| What is the current activation rate using the proposed 3-day-in-7 definition? | Run retrospective cohort analysis on existing data (Week 1 task). | P0 -- blocks validation of aha moment |
| What % of paid subscribers never complete a single session? | Query `session_completed` events for paid user cohorts. | P0 -- sizes the activation failure segment |
| Is the engagement cliff at week 2 consistent across all content types, or is it driven by specific program/session types? | Segment session frequency by content category (guided meditation, sleep, breathing, etc.). | P1 -- may reveal content-specific interventions |
| What is the current push notification opt-in rate, and what is the baseline open rate? | Pull from push notification platform (e.g., OneSignal, Firebase). | P1 -- determines ceiling for push-based experiments |
| Are there existing reminder features in the app? If so, what is current adoption? | Product audit / check existing feature flags and usage data. | P1 -- determines if Exp 1 is "new feature" or "better surfacing" |
| What does the cancellation flow look like today, and do we capture a reason? | Product audit + check for `subscription_cancelled` event properties. | P2 -- informs monetization churn understanding |
| Is there a content pipeline for new meditation content, and how frequently is the library refreshed? | Check with content team. | P2 -- "content freshness" may be a factor in engagement decay |

### Next Steps (Immediate -- This Week)

1. **PM:** Share this pack with engineering; align on week 1 scope (instrumentation + Exp 1 + Exp 2). Confirm micro-session content timeline with content team.
2. **PM:** Run the retrospective activation analysis (3-day-in-7 definition) using existing data. Share results by end of day 3.
3. **Eng 1:** Begin instrumenting the top 5 priority events (`session_completed` enrichment, `reminder_set`, `reminder_prompt_shown`, `home_screen_card_tapped`, `push_sent`/`push_opened`). Target: production by day 4.
4. **Eng 2:** Build Exp 1 (post-first-session reminder prompt) behind feature flag. Target: live by day 5.
5. **PM:** Set up Retention Cohort Tracker dashboard (even with partial data) to establish real baseline segmented by activated vs. not. Target: live by day 5.

---

## Appendix: Quality Gate Self-Assessment

### Checklist Pass/Fail

- [x] The request is primarily retention/engagement/activation (not ICP/value-prop definition).
- [x] Segment(s) and time horizon are explicit (activated paid users vs. unconverted paid users; 90-day horizon).
- [x] Retention metric definition is explicit ("completes at least 1 session on day 28-32").
- [x] Baseline numbers exist (D30 = 22%, sessions/day cliff from 4.2 to 1.1). Segment-level breakdowns are assumptions, labeled as such.
- [x] Constraints are captured (4-week sprint, 1 PM + 2 eng, push + in-app only, no major redesign).
- [x] Cohort snapshot includes 2 segments.
- [x] Primary failure mode is named (engagement decay).
- [x] Biggest leak is explicit (activated paid users x week 2-3 transition).
- [x] Root-cause hypotheses are ranked and testable.
- [x] Diagnosis points to one primary lever (habit formation / daily return).
- [x] 5 candidate value behaviors were considered.
- [x] Chosen activation definition is behavioral + measurable.
- [x] Threshold window is defined (3 distinct days within 7 days).
- [x] Validation plan exists (retrospective cohort comparison + decision rule).
- [x] Tracking requirements are specified.
- [x] Each experiment is tied to a failure mode and hypothesis.
- [x] Each experiment has a primary success metric + leading indicators.
- [x] Guardrails are defined for each experiment.
- [x] Instrumentation needs and rollout/rollback are included.
- [x] Top 3 experiments are feasible within stated constraints.
- [x] Every metric has a clear event definition and data source.
- [x] Dashboards are specified.
- [x] Plan distinguishes leading indicators vs. long-term outcomes.
- [x] No dark patterns.
- [x] Messaging frequency is capped with opt-out.
- [x] No secrets/PII requested.
- [x] Mounting loss is ethical (progress dashboard with transparent framing, no guilt).
- [x] Pack includes: diagnosis, activation spec, lever map, backlog, measurement plan, 30/60/90.
- [x] Includes: Risks / Open questions / Next steps.
- [x] Ready for team to execute next 2 weeks without additional clarification.

### Rubric Score

| Dimension | Score | Rationale |
|---|---:|---|
| 1. Problem fit | 2 | Scope is retention/engagement for paid subscribers; boundaries with onboarding and growth loops are clear. |
| 2. Input contract | 2 | Inputs captured; assumptions (segment-level metrics) are labeled with confidence notes throughout. |
| 3. Metric clarity | 2 | Retention, engagement, activation defined with behavior, segment, window, and guardrails. |
| 4. Diagnosis quality | 2 | Primary failure mode (engagement decay) identified with evidence; 2 segments analyzed; diagnosis drives lever selection. |
| 5. Activation/aha definition | 2 | Behavioral definition with threshold (3 days in 7), validation plan, and decision rule to revise. |
| 6. Insight-to-action mapping | 2 | Every hypothesis ties to a failure mode and a measurable leading indicator; 8 hypotheses across 4 levers. |
| 7. Experiment design | 2 | 6 experiment cards with hypothesis, success metric, guardrails, instrumentation, rollout/rollback. |
| 8. Prioritization | 2 | ICE scoring; top 3 are feasible within 4-week sprint; rationale is transparent. |
| 9. Execution plan | 2 | 30/60/90 plan is sequenced and dependency-aware; week 1 work is unblocked; measurement checkpoints included. |
| 10. Safety + trust | 2 | No dark patterns; push frequency cap; ethical mounting loss framing; user control emphasized. |
| **Total** | **20/20** | |

---

*End of Retention & Engagement Improvement Pack.*
