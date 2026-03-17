# Taste Calibration Plan: Fintech Onboarding — Bank Account Connection & Net Worth Dashboard

**Domain:** Fintech onboarding
**Target user:** First-time user connecting their bank account and seeing their net worth dashboard
**Job to be done:** Feel confident data is safe and see value within 2 minutes
**Constraints:** Mobile-first, WCAG AA accessibility, high-trust design
**Time box:** 90 minutes

---

## 1. Benchmark Selection (5 Benchmarks)

### Benchmark 1: Mint (Fintech)
**Why chosen:** Pioneer of the aggregated net worth dashboard. Millions of users trusted Mint with bank credentials before open banking APIs existed. Represents the baseline for "connect and see your finances."

### Benchmark 2: Robinhood (Fintech)
**Why chosen:** Best-in-class mobile-first onboarding in finance. Known for reducing friction in account setup while maintaining regulatory compliance. The portfolio summary screen is a strong analog to a net worth dashboard.

### Benchmark 3: Apple Health (Health/Wellness — Outside Fintech)
**Why chosen:** Handles an analogous trust problem — users grant access to sensitive personal health data and immediately see a consolidated dashboard. Apple Health excels at progressive disclosure, showing value before asking for more permissions. The "trust-then-value" sequencing is directly transferable.

### Benchmark 4: 1Password (Security/Productivity — Outside Fintech)
**Why chosen:** Onboards users into a product whose entire value proposition is security. First-run experience must simultaneously communicate "your data is locked down" and "this is easy to use." The tension between trust signaling and usability mirrors the fintech onboarding challenge precisely.

### Benchmark 5: Stripe Dashboard (Developer Tools / Fintech-Adjacent — Outside Fintech)
**Why chosen:** Handles first-time activation of a financial product with a dashboard that must convey complex data clearly on first load. Stripe's empty-state and first-data-point design patterns are relevant for the moment a user sees their net worth for the first time.

---

## 2. Benchmark Study Notes

### 2.1 Mint

- **Onboarding flow:** Institution search → credential entry → loading/sync screen → net worth dashboard.
- **Trust signals:** Norton security badge on credential screen, "Bank-level encryption" copy, Intuit brand logo prominent.
- **Time to value:** ~90–120 seconds from credential entry to seeing first account balance. Sync screen uses progress animation per account.
- **What works well:** Immediate display of partial data as accounts sync (progressive loading). Net worth number is the hero element — large, centered, unmistakable.
- **What falls short:** Dense UI on dashboard. Accessibility was historically weak (low contrast text, small tap targets). Trust copy felt boilerplate rather than contextual.
- **Mobile experience:** Responsive but designed desktop-first. Mobile onboarding had more steps than necessary.

### 2.2 Robinhood

- **Onboarding flow:** Sign up → identity verification → bank link (Plaid) → first deposit → portfolio view.
- **Trust signals:** Minimal — relies on clean design as implicit trust. SIPC/FINRA disclosures present but not prominent. Brand reputation does heavy lifting.
- **Time to value:** Bank connection via Plaid is fast (~30 seconds). Portfolio screen appears immediately after, even with $0 balance (empty-state design).
- **What works well:** Extreme simplicity. One action per screen. Confetti animation on first purchase creates emotional reward. The green/red portfolio line is instantly legible.
- **What falls short:** Over-gamification has drawn criticism — may not suit a "high-trust" design goal. Sparse trust signaling could feel insufficient for risk-averse users.
- **Mobile experience:** Native mobile-first. Best-in-class tap target sizing and gesture navigation.

### 2.3 Apple Health

- **Onboarding flow:** App opens → summary dashboard pre-populated with phone sensor data (steps, etc.) → prompts to connect additional sources.
- **Trust signals:** Apple's privacy brand. On-device processing messaging. Granular permission controls shown inline ("This app can read your heart rate data").
- **Time to value:** Instant. Dashboard shows step count and activity data from day one with zero user effort. Value is visible before any permission is granted.
- **What works well:** Progressive disclosure — starts with data the phone already has, then invites deeper engagement. Permission requests are contextual (asked when relevant, not upfront). Dashboard uses large, clear typography with strong color coding.
- **What falls short:** Information density can overwhelm. Some data categories feel buried. Not all cards are equally actionable.
- **Accessibility:** Strong. Dynamic type support, VoiceOver labels on charts, high-contrast mode.

### 2.4 1Password

- **Onboarding flow:** Account creation → master password setup → browser extension install → first password save → vault dashboard.
- **Trust signals:** Encryption explanation (shown visually, not just text). "Zero-knowledge" architecture explained in plain language. Security audit badges. Secret Key concept introduced with clear rationale.
- **Time to value:** ~60 seconds to save first password. Watchtower security score appears after a few items are added, providing immediate actionable value.
- **What works well:** Trust education is woven into the flow, not bolted on. Each step teaches a security concept while advancing setup. Empty states in vault have clear CTAs. Watchtower score gamifies security improvement without feeling reckless.
- **What falls short:** Master password + Secret Key is conceptually heavy for non-technical users. Desktop-first design legacy shows on mobile.
- **Accessibility:** Good — keyboard navigation, screen reader support, sufficient contrast ratios.

### 2.5 Stripe Dashboard

- **Onboarding flow:** Account creation → business verification → API key display → first test transaction → live dashboard.
- **Trust signals:** PCI compliance badges. "Test mode" toggle clearly separates sandbox from live. Real-time webhook logs show transparency.
- **Time to value:** Test mode provides instant dashboard interaction with fake data. Live dashboard populates with first real transaction.
- **What works well:** Empty states are exceptional — they show what the dashboard *will* look like with sample data, not a blank screen. Progressive complexity: simple metrics first, detailed breakdowns available on drill-down. Status indicators (green dots, checkmarks) provide constant system-health feedback.
- **What falls short:** Information density is high (developer audience). Typography hierarchy could be stronger on mobile. Not designed for consumer audiences.
- **Accessibility:** Moderate. Functional but not exemplary — some charts lack alt text.

---

## 3. Taste Rules

These are the design principles extracted from studying the benchmarks. Each rule has a clear "do this / not that" framing.

### Rule 1: Show Value Before Asking for Trust
**Do:** Display useful information (even partial or illustrative) before requesting sensitive credentials.
**Don't:** Gate the entire experience behind a credential wall with nothing but a promise on the other side.
**Source:** Apple Health shows step data before asking for health device permissions. Stripe shows sample dashboard data before requiring live API credentials.

### Rule 2: Trust Signals Must Be Contextual, Not Decorative
**Do:** Place encryption/security messaging at the exact moment the user is handing over sensitive data (e.g., on the bank credential screen).
**Don't:** Dump all trust badges on the landing page where they feel like marketing rather than assurance.
**Source:** 1Password explains encryption at the moment of master password creation. Mint places Norton badge on the credential entry screen specifically.

### Rule 3: One Primary Action Per Screen on Mobile
**Do:** Each screen in the onboarding flow has exactly one thing the user needs to do, with a single prominent CTA.
**Don't:** Combine bank selection, credential entry, and terms acceptance on one scrolling mobile page.
**Source:** Robinhood's one-action-per-screen flow. Apple Health's single permission prompt per data type.

### Rule 4: The First Number Must Be a Hero
**Do:** When the net worth (or key metric) first appears, make it the largest, most prominent element on screen. Use at least 32pt type. Center it. Give it breathing room.
**Don't:** Bury the net worth figure in a data table or sidebar among twelve other metrics.
**Source:** Mint's hero net worth number. Robinhood's portfolio value as the dominant visual element. Apple Health's large step count.

### Rule 5: Progressive Loading Beats a Spinner
**Do:** Show accounts/data as they sync, one by one. Let the user see partial results building toward the complete picture.
**Don't:** Show a generic spinner for 45 seconds with no indication of progress or what is happening.
**Source:** Mint's per-account sync progress. Stripe's real-time webhook logs showing each event as it arrives.

### Rule 6: Empty and First-Data States Are Designed, Not Defaulted
**Do:** Design a specific experience for the moment before data arrives and the moment the first data point appears. Use sample/illustrative data, skeleton screens, or guided overlays.
**Don't:** Show a blank white screen, a zero balance, or "No data available" with no context.
**Source:** Stripe's sample-data empty states. Robinhood's $0 portfolio view with clear "Add funds" CTA.

### Rule 7: Accessibility Is Structure, Not Remediation
**Do:** Use semantic HTML/native components, minimum 44x44pt tap targets, 4.5:1 contrast ratios, and screen reader labels from the start.
**Don't:** Build the visual design first and "add accessibility later" — that approach systematically fails.
**Source:** Apple Health's Dynamic Type and VoiceOver support. WCAG AA as a constraint, not a checklist item.

---

## 4. Falsifiable Hypotheses

Each hypothesis is structured as a testable prediction with a clear pass/fail threshold.

### H1: Trust-Contextual Security Messaging Increases Completion Rate
**Hypothesis:** Placing a brief, plain-language encryption explanation (e.g., "Your credentials are encrypted and never stored on our servers") directly on the bank credential entry screen will increase bank-connection completion rate by at least 15% compared to placing the same message only on the landing/marketing page.
**Measurement:** A/B test. Metric: % of users who reach credential screen and successfully complete bank connection.
**Falsified if:** Completion rate difference is less than 5% or negative.

### H2: Progressive Account Loading Reduces Perceived Wait Time
**Hypothesis:** Showing each bank account's name and balance as it syncs (progressive loading) will result in users rating the wait as "acceptable" at a rate 20% higher than a generic spinner, even if actual sync time is identical.
**Measurement:** Post-sync single-question survey ("How acceptable was the wait?") on a 5-point scale. Compare % rating 4 or 5.
**Falsified if:** No statistically significant difference between progressive and spinner groups (p > 0.05).

### H3: Hero Net Worth Display Drives Return Visits
**Hypothesis:** Users who see their net worth as a single large hero number (32pt+, centered, with positive/negative color coding) on first dashboard load will return to the app within 48 hours at a rate at least 10% higher than users who see a multi-widget dashboard where net worth is one of several equally-weighted elements.
**Measurement:** A/B test. Metric: % of users who open the app again within 48 hours of first bank connection.
**Falsified if:** Return rate difference is less than 3%.

### H4: Two-Minute Value Threshold Is Achievable
**Hypothesis:** 80% of users can go from tapping "Connect Bank" to seeing their net worth number in under 2 minutes, given a Plaid-based connection flow with progressive loading and pre-fetched institution list.
**Measurement:** Instrumented timer from "Connect Bank" tap to net worth number render. Measure P80 latency.
**Falsified if:** P80 exceeds 2 minutes, or fewer than 70% of users complete within 2 minutes.

### H5: AA-Compliant Design Does Not Reduce Perceived Visual Appeal
**Hypothesis:** A dashboard designed to WCAG AA standards from the ground up (4.5:1 contrast, 44pt tap targets, semantic structure) will score within 5 points of a "visually optimized" non-AA design on a visual appeal survey (1–100 scale), among the general user population.
**Measurement:** Between-subjects study. Show AA-compliant and non-compliant mockups to 100+ users. Collect visual appeal ratings.
**Falsified if:** AA-compliant version scores more than 10 points lower on visual appeal.

---

## 5. Validation Plan

### Phase 1: Benchmark Immersion (0–30 minutes)

| Time | Activity |
|------|----------|
| 0–10 min | Walk through Mint and Robinhood onboarding flows on a mobile device. Screen-record. Note trust signals, time to first value, and friction points. |
| 10–20 min | Walk through Apple Health and 1Password first-run experiences. Document permission sequencing and trust education patterns. |
| 20–30 min | Walk through Stripe dashboard activation. Focus on empty-state and first-data design. Capture screenshots of key moments. |

**Output:** Annotated screenshot deck (10–15 screens) with callouts mapped to the 7 taste rules.

### Phase 2: Design Audit & Rule Application (30–55 minutes)

| Time | Activity |
|------|----------|
| 30–40 min | Sketch 3 key screens for fintech onboarding: (1) Bank connection screen, (2) Sync/loading state, (3) Net worth dashboard first view. Apply taste rules directly. |
| 40–50 min | Audit each sketch against the 7 taste rules using a simple checklist (rule met / not met / partially met). Revise any screen that fails more than 1 rule. |
| 50–55 min | Run WCAG AA spot-check: contrast ratios on primary text, tap target sizes, heading hierarchy, screen reader flow order. |

**Output:** 3 annotated mobile wireframes with rule-compliance checklist.

### Phase 3: Hypothesis Testing Plan (55–75 minutes)

| Time | Activity |
|------|----------|
| 55–60 min | Prioritize hypotheses by effort-to-learn ratio. Recommended order: H4 (instrumentation only), H1 (A/B test), H2 (A/B test with survey), H3 (cohort analysis), H5 (study). |
| 60–70 min | Define test plan for H4 and H1 (highest priority). Specify: user segment, sample size (minimum 200 per variant for H1), test duration (2 weeks), success criteria, and abort criteria. |
| 70–75 min | Draft instrumentation requirements: events to log (credential_screen_viewed, bank_connection_started, bank_connection_completed, net_worth_displayed, app_return_48h). |

**Output:** One-page test plan document covering H4 and H1 with timelines and sample sizes.

### Phase 4: Taste Rule Stress Test (75–90 minutes)

| Time | Activity |
|------|----------|
| 75–80 min | Devil's advocate session: for each taste rule, write one scenario where the rule might be wrong or counterproductive. Example: "Rule 1 (show value before trust) might backfire if pre-credential data feels fake or patronizing." |
| 80–85 min | Identify 2–3 edge cases that the benchmarks didn't cover: users with 5+ bank accounts (sync time), users with negative net worth (emotional design), users on assistive technology (screen reader flow for progressive loading). |
| 85–90 min | Write a "taste rule update trigger" — specific user research findings that would cause each rule to be revised. Example: "Revise Rule 4 if usability testing shows >30% of users want to see account breakdown immediately instead of a single hero number." |

**Output:** Stress-test memo with edge cases, counterarguments, and revision triggers for each taste rule.

---

## Summary of Deliverables

| # | Deliverable | Format |
|---|-------------|--------|
| 1 | Annotated benchmark screenshot deck | 10–15 annotated mobile screenshots |
| 2 | 7 Taste rules with do/don't guidance | Documented rules with benchmark sources |
| 3 | 3 Mobile wireframes with rule-compliance audit | Sketches + checklist |
| 4 | 5 Falsifiable hypotheses with measurement plans | Structured hypothesis cards |
| 5 | Test plan for H4 and H1 | One-page plan with sample sizes and timelines |
| 6 | Stress-test memo | Edge cases and rule revision triggers |

---

## Appendix: Benchmark × Taste Rule Matrix

| Taste Rule | Mint | Robinhood | Apple Health | 1Password | Stripe |
|------------|------|-----------|-------------|-----------|--------|
| 1. Value before trust | Partial | Weak | Strong | Moderate | Strong |
| 2. Contextual trust signals | Moderate | Weak | Strong | Strong | Moderate |
| 3. One action per screen | Weak | Strong | Strong | Moderate | Weak |
| 4. Hero first number | Strong | Strong | Strong | N/A | Moderate |
| 5. Progressive loading | Strong | Moderate | N/A | Weak | Strong |
| 6. Designed empty states | Weak | Moderate | Moderate | Strong | Strong |
| 7. Accessibility as structure | Weak | Moderate | Strong | Moderate | Moderate |
