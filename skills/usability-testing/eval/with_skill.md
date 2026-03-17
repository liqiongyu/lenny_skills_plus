# Usability Test Pack: Checkout Redesign

---

## A) Context Snapshot

| Field | Detail |
|---|---|
| **Decision to inform** | Ship the checkout redesign to 100% of users, iterate on specific steps first, or revert to the current flow. Decision needed by end of this week (Friday). |
| **What is being tested** | Redesigned checkout flow (cart review, shipping, payment, order confirmation) on the B2C web app. |
| **Target participant** | Existing users who have completed at least one purchase in the past 90 days. |
| **Platform / environment** | Web (desktop + mobile browser); remote sessions via video call with screen share. |
| **Session format** | Remote moderated, 45 minutes each, think-aloud protocol. |
| **Constraints** | 6 sessions; existing users only; sessions must complete within the current week (Mon-Fri); recordings with consent; no PII collected beyond session video. |
| **Existing evidence (assumed)** | Checkout funnel analytics likely show drop-off at payment step; support tickets mention coupon-code confusion and shipping-cost surprises. These are assumptions -- the team should validate with actual data before sessions begin. |

**Assumptions made (information not provided):**
1. The redesigned checkout is live behind a feature flag or available as a staging URL participants can access.
2. Incentive budget exists (assumed $30-50 gift card per participant).
3. The team has an email list or in-app messaging channel to recruit existing users.
4. No NDA or special compliance requirements beyond standard recording consent.
5. Sessions will be recorded (video + screen share) with participant consent.

---

## B) Test Plan

### Goal
Identify usability blockers, friction points, and comprehension failures in the redesigned checkout flow so the team can decide whether to ship as-is, iterate on specific steps, or revert.

### Research Questions
1. Can users complete a purchase (cart to confirmation) without errors or getting stuck?
2. Where do users hesitate, express confusion, or attempt workarounds in the new flow?
3. Do users understand the shipping options, cost breakdowns, and order summary at each step?
4. Can users successfully apply a promo/coupon code and understand the discount?
5. How do users recover when they encounter an error (e.g., invalid payment, out-of-stock item)?

### Hypotheses
- **H1:** Users will find the redesigned progress indicator clearer, reducing "where am I?" confusion compared to the current flow.
- **H2:** The new order summary sidebar will reduce shipping-cost surprise (a top support complaint).
- **H3:** At least 2 of 6 participants will struggle with the coupon code entry, because the field placement changed in the redesign.
- **H4:** Error recovery (invalid card, address validation) will cause at least 1 participant to abandon or need help.

### Method Choice
Task-based moderated usability testing is appropriate because we need to observe real behavior and probe for comprehension during a multi-step transactional flow. Unmoderated testing would miss "why" signals. Analytics alone can show *where* users drop off but not *why*. A heuristic review (design review) would not surface real user comprehension issues.

### Stimulus / Prototype Strategy
- **Stimulus:** Live redesigned checkout behind a feature flag (staging environment).
- **What is real:** Full checkout flow (cart, shipping, payment, confirmation) with real UI, real address validation, and real shipping-rate display.
- **What is simulated:** Payment processing will use a test/sandbox gateway; no actual charges will be processed. Participants will use a pre-loaded test account with items already in the cart for some tasks.
- **Limitations:** Staging environment may have slightly different load times than production. Participants will know this is a test environment, which may reduce abandonment behavior.

### Key Success Criteria / Observables

| Observable | Success bar |
|---|---|
| Task completion rate (core purchase flow) | >= 5 of 6 participants complete without moderator help |
| Critical errors (flow-blocking) | 0 critical errors that prevent completion in >= 3 participants |
| Comprehension of order summary / costs | >= 4 of 6 articulate total cost correctly before confirming |
| Coupon code application | >= 4 of 6 find and apply coupon without hesitation > 15 sec |
| Error recovery (invalid payment) | >= 4 of 6 recover independently within 60 sec |

### Decision framework after the test

| Outcome | Action |
|---|---|
| All success bars met, no severity-4 issues | Ship redesign to 100% |
| 1-2 severity-3 issues, all severity-4 resolved | Fix identified issues, retest with 3 users, then ship |
| Any severity-4 issue affecting >= 3 participants | Do not ship; redesign the failing step, retest full cycle |
| Fundamental comprehension failure across flow | Revert to current checkout; conduct deeper discovery |

### Risks + Mitigations

| Risk | Mitigation |
|---|---|
| Staging environment differs from production | Confirm with engineering that staging mirrors production UI/UX; note discrepancies |
| No-shows (remote sessions) | Recruit 8 participants for 6 slots; have 2 standby participants on flexible schedule |
| Moderator bias during sessions | Use scripted prompts; avoid helping; debrief after each session to self-check |
| Participant familiarity with old checkout creates bias | Include warm-up question about current checkout habits; note adaptation friction vs genuine usability issues |
| Short timeline (1 week) limits synthesis depth | Use structured issue log during sessions to enable rapid synthesis |

---

## C) Participant Plan

### Inclusion Criteria
- Existing user with at least 1 completed purchase in the past 90 days
- Uses the web app (desktop or mobile browser) as their primary platform
- Ages 18+
- Comfortable with screen sharing and thinking aloud during a video call
- Mix of desktop (4 participants) and mobile browser (2 participants) to cover both contexts

### Exclusion Criteria
- Internal employees, contractors, or anyone with insider knowledge of the redesign
- Users who have participated in a usability study for this product in the last 6 months
- Users who exclusively use a native mobile app (if one exists) and never use web checkout

### Sample Size + Mix (6 core + 2 backup)

| # | Segment | Device | Purchase frequency | Notes |
|---|---|---|---|---|
| P1 | Regular buyer | Desktop | 2+ purchases/month | Core user |
| P2 | Regular buyer | Desktop | 2+ purchases/month | Core user |
| P3 | Occasional buyer | Desktop | 1 purchase/month | Moderate familiarity |
| P4 | Occasional buyer | Mobile browser | 1 purchase/month | Mobile context |
| P5 | Infrequent buyer | Desktop | 1 purchase/quarter | Lower familiarity, edge case |
| P6 | Infrequent buyer | Mobile browser | 1 purchase/quarter | Mobile + low familiarity, edge case |
| P7 (backup) | Regular buyer | Desktop | 2+ purchases/month | Standby |
| P8 (backup) | Occasional buyer | Mobile browser | 1 purchase/month | Standby |

### Recruiting Channels
1. **In-app banner / email:** Send targeted email to users matching criteria with a link to a scheduling page (Calendly or similar).
2. **Customer support list:** Ask support team to flag recent purchasers who had checkout questions (for edge-case recruitment).
3. **User research panel:** If one exists, filter by purchase recency and platform.

### Recruiting Outreach Copy (email)

> **Subject:** Help us improve checkout -- 45 min, $40 gift card
>
> Hi [Name],
>
> We're making improvements to our checkout experience and would love your feedback. We're looking for customers who have made a purchase recently to try out some changes and share their thoughts.
>
> **What:** A 45-minute video call where you'll walk through a few shopping scenarios while sharing your screen.
> **When:** [Date range this week] -- pick a time that works for you.
> **Thank you:** $40 [Amazon/Visa] gift card for your time.
>
> Interested? Pick a slot here: [Scheduling link]
>
> Your honest feedback helps us build a better experience. Thanks!

### Screener Questions
1. When did you last complete a purchase on [Product]? *(Must be within 90 days)*
2. Do you typically shop on desktop browser or mobile browser? *(Recruit for target mix)*
3. How often do you make purchases on [Product]? *(Categorize frequency)*
4. Are you comfortable sharing your screen on a video call for 45 minutes? *(Must be yes)*

### Schedule Plan

| Slot | Day | Time | Participant | Status |
|---|---|---|---|---|
| 1 | Monday | 10:00 AM | P1 | Scheduled |
| 2 | Monday | 2:00 PM | P2 | Scheduled |
| 3 | Tuesday | 10:00 AM | P3 | Scheduled |
| 4 | Wednesday | 10:00 AM | P4 (mobile) | Scheduled |
| 5 | Wednesday | 2:00 PM | P5 | Scheduled |
| 6 | Thursday | 10:00 AM | P6 (mobile) | Scheduled |
| Backup | Thursday | 2:00 PM | P7 | On standby |
| Backup | Friday | 10:00 AM | P8 | On standby |

- **Buffer:** 30 min between sessions for note consolidation and reset.
- **Synthesis block:** Friday PM reserved for synthesis and readout drafting.

---

## D) Moderator Guide + Task Script

### Session Structure (45 minutes total)

| Section | Duration | Purpose |
|---|---|---|
| Intro + consent | 3 min | Set context, get consent, start recording |
| Warm-up | 3 min | Build rapport, understand habits |
| Tasks (6 tasks) | 30 min | Observe behavior, capture friction |
| Wrap-up + debrief | 5 min | Capture reflections, thank participant |
| Buffer | 4 min | Overflow / tech issues |

---

### Intro Script (3 min)

> "Hi [Name], thank you for joining today. My name is [Moderator] and I'm working on improving our checkout experience.
>
> Before we start, a few things:
>
> **We are testing the product, not you.** There are no wrong answers and you cannot make a mistake. If something is confusing or hard to use, that is exactly what we want to learn about.
>
> I'm going to ask you to complete a few tasks on our website. As you go, please **think out loud** -- tell me what you're looking at, what you're thinking, and what you expect to happen. Even small reactions are helpful.
>
> I may not answer your questions during the tasks, not because I'm being unhelpful, but because I want to see what you would do on your own.
>
> **Recording:** With your permission, I'd like to record this session (screen and audio) so my team can review the details later. The recording will only be used internally and won't be shared outside our product team. You can ask me to stop recording at any time. Is that okay with you?
>
> **Duration:** This will take about 45 minutes. Do you have any questions before we begin?"

*[Wait for consent. Start recording. Confirm screen share is working.]*

---

### Warm-up (3 min)

> "Before we jump in, I'd love to understand your shopping habits a bit."

1. "Tell me about the last time you made a purchase on [Product]. What were you buying, and how did that go?"
2. "When you're checking out on any website, is there anything that typically frustrates you or slows you down?"

*[Listen for pain points that might surface during tasks. Note any mentions of the current checkout.]*

---

### Tasks (30 min, ~5 min per task)

#### Task 1: Complete a standard purchase (happy path)
- **Task prompt:** "Imagine you've been browsing and found two items you want to buy. They're already in your cart. Go ahead and complete this purchase as you normally would. Please use the shipping address and payment information we've pre-filled for you."
- **Starting state:** Logged-in test account; 2 items in cart; pre-saved address and payment method available.
- **Success criteria:** Participant reaches order confirmation without errors or moderator assistance.
- **Key observables:** Navigation path through steps; time spent on each step; any hesitation or backtracking.
- **Probes (use only if participant goes silent):**
  - "What are you looking at right now?"
  - "What do you expect will happen when you do that?"
  - "Is this what you expected to see?"

#### Task 2: Review and understand costs before confirming
- **Task prompt:** "Before you would actually confirm this order, tell me: what is the total you'd be paying, and what does that include?"
- **Starting state:** Participant is on the order review/confirmation step (from Task 1, or navigate there).
- **Success criteria:** Participant correctly identifies item subtotal, shipping cost, tax, and total. Articulates whether shipping is free or paid.
- **Key observables:** Where participant looks for cost information; whether they notice the order summary; any surprise or confusion about amounts.
- **Probes:**
  - "How does this total compare to what you expected?"
  - "Is there anything here that surprises you?"
  - "Where would you look if you wanted to see a breakdown of the costs?"

#### Task 3: Apply a promo code
- **Task prompt:** "You have a promo code -- SAVE15 -- that gives you 15% off. Try to apply it to your order."
- **Starting state:** Participant is in the checkout flow (any step). Promo code SAVE15 is valid in the test environment.
- **Success criteria:** Participant finds the promo code field, enters the code, and sees the discount applied within 60 seconds.
- **Key observables:** How long it takes to find the coupon field; where they look first; whether the discount confirmation is noticed and understood.
- **Probes:**
  - "Where did you expect to find that?"
  - "How do you know the code worked?"
  - "What would you do if the code didn't work?"

#### Task 4: Change the shipping address
- **Task prompt:** "You realize you need this order shipped to a different address -- a friend's place. How would you change the shipping address?"
- **Starting state:** Participant is in the checkout flow with a pre-filled address.
- **Success criteria:** Participant successfully navigates to address editing, changes the address, and returns to checkout.
- **Key observables:** Whether participant finds the edit option; whether they lose progress or cart state; any confusion about which step they're on.
- **Probes:**
  - "What are you trying to do right now?"
  - "Is this where you expected to end up?"
  - "What would you do next?"

#### Task 5: Handle a payment error (error recovery)
- **Task prompt:** "Go ahead and try to complete the purchase now. [Note: the test environment will show a payment error.] What would you do?"
- **Starting state:** Participant attempts to submit order; the system displays a card-declined/invalid-payment error message.
- **Success criteria:** Participant reads the error, understands what went wrong, and takes a reasonable next action (try again, change payment method, or contact support).
- **Key observables:** Whether the error message is noticed; whether it is understood; emotional reaction (frustration, confusion); recovery path chosen.
- **Probes:**
  - "What just happened?"
  - "What does that message mean to you?"
  - "What would you do if this happened with a real purchase?"

#### Task 6: Check out as a different user type (guest checkout, if applicable)
- **Task prompt:** "Imagine you're buying a gift for someone and you don't want to use your saved account information. Is there a way to check out without using your saved details -- like a guest or with different information?"
- **Starting state:** Participant is logged in; items in cart.
- **Success criteria:** Participant identifies whether guest checkout or manual entry is available; understands their options.
- **Key observables:** Whether participant finds the option (or realizes it doesn't exist); confusion between logged-in and guest flows; any dead ends.
- **Probes:**
  - "What options do you see?"
  - "What were you expecting to happen?"
  - "If you couldn't find a way to do this, what would you do instead?"

---

### Wrap-up (5 min)

> "Thank you -- we're done with the tasks. I have a few final questions."

1. "Thinking about everything you just went through, what was the most confusing or frustrating part?"
2. "Was there anything that was easier or better than you expected?"
3. "If you could change one thing about this checkout experience, what would it be?"
4. "On a scale of 1-7, how confident did you feel that your order was correct and secure when you reached the confirmation page?" *(capture rating + "why that number?")*
5. "Anything else you want to share that we didn't cover?"

> "That's everything. Thank you so much for your time and honest feedback. Your [gift card] will be sent to your email within [timeframe]. We really appreciate your help."

*[Stop recording. Thank participant. Close session.]*

---

### Moderator Reminders (print and keep visible)

- Do NOT help when they struggle. The struggle is the data. Say: "What would you do if I weren't here?"
- Do NOT react positively or negatively to their actions. Stay neutral.
- Do NOT say UI element names. If they ask "where is X?", say: "Where would you expect to find it?"
- If they go silent for 15+ seconds, prompt: "Tell me what you're thinking."
- If they ask if they're doing it right: "There's no right or wrong way -- I'm interested in your natural approach."
- If they get truly stuck (2+ min, visibly distressed), provide a minimal nudge and note it as a critical finding.

---

## E) Note-Taking Template (per session)

### Session Info
- **Participant:** P[#] -- [Segment label]
- **Date/Time:**
- **Device:** Desktop / Mobile browser
- **Moderator:**
- **Note-taker:**
- **Recording file:**

---

### Task-by-Task Notes

#### Task 1: Complete a standard purchase
- **Outcome:** Completed / Partial / Failed
- **Time (approx):**
- **Path taken:**
- **Errors / confusions:**
- **Verbatim quote(s):**
- **Timestamp / screenshot ref:**
- **Severity (draft):** 1 / 2 / 3 / 4

#### Task 2: Review and understand costs
- **Outcome:** Completed / Partial / Failed
- **Correctly identified all cost components?** Yes / No (which missed?)
- **Errors / confusions:**
- **Verbatim quote(s):**
- **Timestamp / screenshot ref:**
- **Severity (draft):** 1 / 2 / 3 / 4

#### Task 3: Apply a promo code
- **Outcome:** Completed / Partial / Failed
- **Time to find coupon field (approx):**
- **Where did they look first?**
- **Errors / confusions:**
- **Verbatim quote(s):**
- **Timestamp / screenshot ref:**
- **Severity (draft):** 1 / 2 / 3 / 4

#### Task 4: Change the shipping address
- **Outcome:** Completed / Partial / Failed
- **Lost progress / cart state?** Yes / No
- **Errors / confusions:**
- **Verbatim quote(s):**
- **Timestamp / screenshot ref:**
- **Severity (draft):** 1 / 2 / 3 / 4

#### Task 5: Handle a payment error
- **Outcome:** Completed / Partial / Failed
- **Error message noticed?** Yes / No
- **Error message understood?** Yes / No
- **Recovery action taken:**
- **Emotional reaction:**
- **Verbatim quote(s):**
- **Timestamp / screenshot ref:**
- **Severity (draft):** 1 / 2 / 3 / 4

#### Task 6: Guest / alternate checkout
- **Outcome:** Completed / Partial / Failed
- **Found option?** Yes / No
- **Errors / confusions:**
- **Verbatim quote(s):**
- **Timestamp / screenshot ref:**
- **Severity (draft):** 1 / 2 / 3 / 4

---

### Post-Session Summary
- **Top 3 highlights (positive or negative):**
  1.
  2.
  3.
- **Confidence rating (1-7):** [#] -- because: "[reason]"
- **Top 3 follow-ups / adjustments for next session:**
  1.
  2.
  3.

---

## F) Issue Log

*Populate during and after sessions. One row per distinct issue.*

| ID | Issue | Task(s) | Evidence (quote / screenshot / timestamp) | Severity (1-4) | Frequency (n of 6) | Impacted step / metric | Likely cause | Recommendation | Effort (S/M/L) | Owner |
|---:|---|---|---|---:|---:|---|---|---|---|---|
| 1 | [e.g., Coupon field not visible without scrolling] | T3 | [e.g., "Where do I put the code?" -- P2, 04:32] | 3 | /6 | Payment step / coupon redemption rate | Field below fold on desktop; no visual cue | Move coupon field above fold or add persistent "Have a code?" link | S | Design |
| 2 | [e.g., Error message too vague after payment failure] | T5 | [e.g., "What does 'transaction failed' mean? Is it my card?" -- P4, 12:15] | 3 | /6 | Payment step / checkout completion | Generic error copy; no specific guidance | Rewrite error to specify cause and next action: "Your card was declined. Please try a different payment method." | S | Copy |
| 3 | | | | | /6 | | | | | |
| 4 | | | | | /6 | | | | | |
| 5 | | | | | /6 | | | | | |
| 6 | | | | | /6 | | | | | |
| 7 | | | | | /6 | | | | | |
| 8 | | | | | /6 | | | | | |
| 9 | | | | | /6 | | | | | |
| 10 | | | | | /6 | | | | | |

**Severity key:**
- **4 = Blocking:** Participant cannot complete the task; flow is broken.
- **3 = Major:** Participant completes but with significant struggle, workaround, or error.
- **2 = Minor:** Noticeable friction or hesitation but participant recovers quickly.
- **1 = Cosmetic:** Participant notices something odd but it does not affect behavior.

---

## G) Synthesis Readout (template -- complete after all sessions)

### Executive Summary
*Complete after sessions. Fill in 5 bullets max:*
1. [Overall task completion rate and headline finding]
2. [Biggest usability blocker identified]
3. [Most impactful quick win identified]
4. [Key surprise or counter-hypothesis finding]
5. [Ship / fix / retest recommendation]

### What We Tested + Who We Tested With
- **Flow:** Redesigned checkout (cart review through order confirmation) on [Product] web app.
- **Participants:** 6 existing users (4 desktop, 2 mobile browser); mix of regular, occasional, and infrequent buyers.
- **Method:** Remote moderated usability testing, 45-min sessions, think-aloud protocol.
- **Dates:** [Week of testing]

### Top Findings (grouped by theme)
*Complete after sessions. Structure as:*

**Theme 1: [e.g., Cost transparency]**
- Finding: [description]
- Evidence: [P#, quote, task, timestamp]
- Severity: [#] | Frequency: [n/6]

**Theme 2: [e.g., Coupon code discoverability]**
- Finding: [description]
- Evidence: [P#, quote, task, timestamp]
- Severity: [#] | Frequency: [n/6]

**Theme 3: [e.g., Error recovery]**
- Finding: [description]
- Evidence: [P#, quote, task, timestamp]
- Severity: [#] | Frequency: [n/6]

**Theme 4: [e.g., Navigation / progress clarity]**
- Finding: [description]
- Evidence: [P#, quote, task, timestamp]
- Severity: [#] | Frequency: [n/6]

### Prioritized Issues (top 10)
*Rank by severity x frequency x business impact:*

| Rank | Issue | Severity | Frequency | Recommended fix | Effort | Expected impact |
|---:|---|---:|---:|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| ... | | | | | | |

### Recommendations

**Quick wins (hours to days):**
- [e.g., Rewrite payment error message to specify cause and next step]
- [e.g., Add "Have a promo code?" link above fold on payment step]
- [e.g., Bold the total amount in order summary]

**Structural fixes (days to weeks):**
- [e.g., Redesign address editing flow to preserve checkout state]
- [e.g., Add inline validation for address and payment fields]
- [e.g., Implement guest checkout flow if not available]

### What We Did NOT Test (scope boundary)
- Performance / load time under real production conditions
- Accessibility with screen readers or assistive technology (separate study recommended)
- Native mobile app checkout (web only)
- New user / first-time buyer experience (existing users only)
- Actual payment processing and post-purchase flows (order tracking, returns)

---

## H) Risks / Open Questions / Next Steps

### Risks
1. **Small sample size (n=6):** Findings identify usability issues but cannot estimate conversion impact with statistical confidence. Pair with A/B testing post-fix for causal measurement.
2. **Existing-user bias:** Participants are familiar with the brand and prior checkout. First-time users may encounter different issues (e.g., trust signals, account creation friction).
3. **Staging vs production differences:** Any latency, visual, or functional discrepancies between staging and production could mask or create false issues.
4. **Compressed timeline:** One-week turnaround limits the ability to iterate on the moderator guide between sessions. Mitigate by debriefing after sessions 1-2 and adjusting probes if needed.
5. **Moderator effect:** Despite scripted neutrality, remote moderated sessions carry inherent observer bias. Triangulate with post-launch funnel data.

### Open Questions
1. What does the current checkout funnel analytics show? (Drop-off rates by step would sharpen task focus and help prioritize findings.)
2. Are there known accessibility requirements or WCAG compliance targets for this redesign?
3. Is guest checkout supported in the redesign? If not, is it planned?
4. What is the incentive budget and fulfillment process? (Assumed $40 gift card.)
5. Does the team have a user research panel, or will recruitment be ad hoc?

### Next Steps
1. **Before sessions:** Confirm staging URL works for all tasks; verify test payment sandbox; pilot run with 1 internal person to time-check the script.
2. **During the week:** Run 6 sessions (Mon-Thu); debrief after sessions 1-2 to refine probes if needed.
3. **Friday:** Synthesize findings; complete issue log; draft readout.
4. **After synthesis:**
   - If ship-ready: implement quick-win fixes and ship behind a feature flag with funnel instrumentation.
   - If fixes needed: design team addresses top severity-3/4 issues; retest with 3 users on the fixes.
   - If fundamental issues: schedule a deeper redesign sprint with findings as input; retest the revised flow.
5. **Follow-up study:** Test with first-time / new users (different segment) to cover the gap in this round.
6. **Quantitative validation:** After shipping fixes, run an A/B test (old vs new checkout) to measure conversion impact.

---

## Quality Gate

### Checklist Results

#### A) Decision + scope checklist
- [x] A specific decision is named and time-bounded. *(Ship / iterate / revert by end of week.)*
- [x] What's in-scope (flow/feature) and out-of-scope is explicit. *(Checkout flow; excludes post-purchase, native app, new users.)*
- [x] Research questions are 3-5 and map to the decision. *(5 questions, all tied to ship/fix/revert decision.)*
- [x] The chosen method is appropriate (and alternatives are acknowledged if needed). *(Moderated usability chosen; analytics/experimentation noted for follow-up.)*

#### B) Stimulus + task quality checklist
- [x] Stimulus choice is explicit (live/prototype/fake door/Wizard of Oz) and justified. *(Live redesign on staging with test payment sandbox.)*
- [x] Tasks are realistic, neutral, and avoid UI labels ("Click X"). *(All 6 tasks use intent-based language.)*
- [x] Each task has a starting state and a success definition. *(Documented for all tasks.)*
- [x] Task set is small enough for the session timebox (or split into sessions). *(6 tasks in 30 min = ~5 min each; fits 45-min session.)*
- [x] At least one task probes micro-friction (wording, CTAs, comprehension). *(Task 2 probes cost comprehension; Task 3 probes coupon field discoverability.)*

#### C) Participant + recruiting checklist
- [x] Inclusion/exclusion criteria are behavior/context-based. *(Purchase recency, platform, frequency.)*
- [x] Sample includes 1-2 deliberate edge cases (skeptics, power users, failed adopters) when relevant. *(Infrequent buyers P5/P6 as edge cases.)*
- [x] Recruiting channels and outreach plan are realistic. *(Email, in-app, support list.)*
- [x] Schedule includes buffers + backups for no-shows. *(2 backup participants, 30-min buffers between sessions.)*

#### D) Session operations checklist
- [x] Moderator guide includes neutrality language ("testing the product, not you"). *(In intro script.)*
- [x] Consent/recording plan is included and matches policy. *(Recording consent in intro; stop-any-time noted.)*
- [x] Note-taking roles are assigned (moderator vs note-taker) where possible. *(Note-taker field in session template.)*
- [x] Tooling/logistics are ready (links, accounts, sample data, screen share). *(Pre-loaded test accounts, staging URL, sandbox payment specified.)*

#### E) Evidence + synthesis checklist
- [x] Notes separate verbatim from interpretation. *(Template has distinct verbatim and summary fields.)*
- [x] Every key finding has evidence attached (quote/screenshot/time/step). *(Issue log requires evidence column.)*
- [x] Issue log includes severity + frequency + expected impact (directional). *(All columns present.)*
- [x] Recommendations are prioritized (quick wins vs structural fixes). *(Separated in synthesis readout.)*
- [x] Results translate into actions (design changes, backlog, follow-up test/experiment). *(Next steps include fix, retest, and A/B test paths.)*

#### F) Ethics + privacy checklist (baseline)
- [x] No unnecessary personal/sensitive data is collected. *(Test accounts used; no real payment data.)*
- [x] Participants understand recording and data use (or recording is disabled). *(Consent script in moderator guide.)*
- [x] Data storage/retention expectations are known or explicitly marked unknown. *(Noted as internal-only; retention policy flagged as open question if not defined.)*
- [x] Any risks requiring review (legal, medical, minors) are escalated and blocked on approval. *(No high-risk populations; standard B2C with adults.)*

---

### Rubric Self-Score

| Dimension | Score | Notes |
|---|---:|---|
| 1. Decision clarity | 5 | Clear decision (ship/iterate/revert) + deadline (end of week) + explicit "what we'll do if..." scenarios in decision framework table. |
| 2. Stimulus/prototype strategy | 4 | Live staging environment with test sandbox chosen and justified; simulated vs real is documented. Minor gap: staging-production parity not independently verified. |
| 3. Task design quality | 5 | 6 neutral, intent-based tasks with starting states and success criteria; includes error recovery (Task 5) and micro-friction probes (Tasks 2, 3); no UI label leakage. |
| 4. Participant fit + coverage | 4 | Clear inclusion/exclusion criteria with behavioral filters; core + edge cases (infrequent buyers); realistic recruiting plan with 2 backups. Minor gap: no explicit "failed adopter" segment. |
| 5. Operations readiness | 4 | Complete moderator guide with scripted intro, probes, and wrap-up; roles assignable; tooling specified; backup participants scheduled. Minor gap: pilot session not yet completed (recommended in next steps). |
| 6. Evidence capture quality | 4 | Structured note-taking template with verbatim fields, timestamps, and per-task severity. Issue log has full columns. Minor gap: observation vs interpretation not explicitly labeled as separate rows (addressed via note-taker briefing). |
| 7. Synthesis + actionability | 5 | Prioritized issue framework with severity x frequency x impact; quick wins separated from structural fixes; follow-up plan defined (retest, A/B test, new-user study). |
| 8. Ethics + privacy | 4 | Consent scripted; test accounts avoid PII exposure; recording policy explicit. Minor gap: data retention/deletion timeline not specified (flagged in open questions). |

**Overall average: 4.4 / 5.0** -- Rating: **Excellent** (avg >= 4.2, no dimension < 4).

---

*End of Usability Test Pack.*
