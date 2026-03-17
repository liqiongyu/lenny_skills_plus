# Behavioral Product Design Pack: Checkout Abandonment at Shipping

---

## 1. Context Snapshot

- **Product:** E-commerce store (B2C, web-based checkout flow)
- **Target user segment:** Shoppers who have added items to cart and entered the checkout flow but abandon at the shipping information/options step
- **Decision this supports:** Redesign the shipping step of checkout to reduce abandonment caused by uncertainty about delivery timing and return policies
- **Constraints:**
  - Platform: Web (desktop + mobile responsive)
  - Notification channels: On-page UI changes, transactional email (post-purchase); no push notifications at checkout
  - Brand/tone: Trustworthy, transparent, customer-first
  - Compliance: Standard e-commerce; no regulated goods assumed
- **Baseline (funnel/retention):**
  - Cart-to-checkout initiation: assumed ~60%
  - Checkout initiation to shipping step completion: assumed ~45% (this is the problem step -- significant drop-off here)
  - Shipping step to payment: assumed ~80% of those who pass shipping
  - Overall cart-to-purchase conversion: assumed ~22%
  - Support tickets mention: "not sure when it arrives," "returns are unclear"

**Assumptions (labeled):**
- Exact conversion rates are approximate; the team should validate with actual analytics
- No prior A/B tests on the shipping step have been run (assumption)
- Returns policy exists but is buried in a footer link or FAQ page (assumption based on ticket themes)
- Delivery date estimation is technically feasible via carrier APIs or zone-based lookup (assumption)

---

## 2. Target Behavior Spec

- **Primary target behavior:** Complete the shipping step of checkout (select shipping method and proceed to payment) within 3 minutes of reaching the shipping page
- **Success metric (primary):** Shipping step completion rate (% of users who reach shipping and proceed to payment); target: increase from ~45% to ~55% (+10 pp)
- **Guardrails (must not worsen):**
  - Post-purchase return rate (must not increase by more than 2 pp)
  - Customer support ticket volume related to shipping/returns (must decrease or hold steady)
  - Customer satisfaction (CSAT) on checkout experience (must not decline)
  - Time-to-complete checkout (should not increase meaningfully; minor increase acceptable if completion rate rises)
- **Who benefits (user value):** Users gain clarity and confidence about when their order will arrive and what happens if they need to return it, reducing anxiety and enabling an informed purchase decision
- **Notes/assumptions:** The target behavior is observable (shipping step completion event) and time-bounded (within a single checkout session). Users who abandon and return later via saved cart are tracked separately.

---

## 3. Journey + Moments That Matter

### Journey steps (trigger to action to outcome)

```
1. TRIGGER: User adds item(s) to cart
2. Cart review: User views cart summary, sees subtotal
3. Checkout initiation: User clicks "Checkout" / "Proceed to checkout"
4. Account/contact info: User enters email, name (or logs in)
5. **SHIPPING STEP** (problem zone):
   a. User sees shipping address form
   b. User enters/selects shipping address
   c. User sees shipping options (methods, costs)
   d. User looks for delivery date/timeline -- NOT FOUND or VAGUE
   e. User wonders about returns -- NO CLEAR INFO VISIBLE
   f. User hesitates, feels uncertain --> ABANDONS or goes to support
6. Payment: User enters payment details
7. Order review: User reviews full order summary
8. Confirmation: User places order, sees confirmation
```

### Drop-off points (top 3)

1. **Shipping options display (step 5c-d):** User sees shipping costs but no clear delivery date or date range. Uncertainty about "when will it arrive" causes hesitation. Support tickets directly cite this.
2. **Returns policy gap (step 5e):** User wants reassurance that they can return if the product is wrong/doesn't fit. No returns information is visible in the checkout flow. Perceived risk of a bad purchase with no recourse.
3. **Shipping cost surprise (step 5c):** User may encounter shipping costs they didn't anticipate, adding to the friction of the step. (Secondary issue -- not directly cited in tickets but a common compounding factor.)

### Emotional moments

- **Uncertainty:** "When will it arrive?" -- peak uncertainty at shipping options display
- **Risk/anxiety:** "What if I need to return this?" -- unresolved risk at the moment of commitment
- **Effort/friction:** Form filling + decision fatigue across shipping methods without enough info to choose
- **Waiting:** No sense of when they will have the product in hand

---

## 4. Behavioral Diagnosis

| Moment | Observed Issue | Likely Barrier | Mechanism Hypothesis | Evidence or Signal | Design Implication |
|---|---|---|---|---|---|
| Shipping options display (5c-d) | No delivery date shown; user doesn't know when order will arrive | **Uncertainty** -- fear of the unknown outcome | **Uncertainty aversion**: People avoid committing when they can't predict the outcome. Without a delivery date, the purchase feels like a gamble on timing. | Support tickets: "not sure when it arrives" | Show estimated delivery date/range prominently next to each shipping option |
| Returns info absent (5e) | Returns policy not visible during checkout; user fears being stuck with a bad purchase | **Uncertainty** -- perceived risk of irreversible loss | **Loss aversion + uncertainty aversion**: The potential loss of money on a product they can't return looms larger than the gain of having the product. Ambiguity about return process amplifies perceived risk. | Support tickets: "returns are unclear" | Surface a clear, concise returns guarantee directly in the checkout flow |
| Shipping cost display (5c) | Shipping costs may appear unexpectedly at this step | **Ability/friction** -- unexpected cost adds decision friction | **Pain of paying (mental accounting)**: An unexpected additional cost triggers re-evaluation of the entire purchase. Even small costs can cause abandonment if they feel like a surprise. | Common e-commerce pattern; no direct ticket evidence (hypothesis) | Show shipping cost estimate earlier in the funnel (cart page); or offer free shipping threshold |
| Overall shipping step (5a-f) | Too many unknowns concentrated in one step; cognitive overload | **Ability/friction** -- decision fatigue from multiple unresolved questions at once | **Choice overload + uncertainty stacking**: Multiple shipping options without enough info to differentiate, combined with missing delivery dates and return info, creates a compound decision burden. | Inferred from the step being the primary drop-off point (hypothesis) | Simplify the step: pre-select best option, show all key info inline, reduce decisions required |

---

## 5. Intervention Map

| # | Idea | Moment in Journey | Mechanism | User Benefit | Metric Impact Hypothesis | Effort | Risk (trust/legal/brand) | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | **Delivery date promise**: Show estimated delivery date range (e.g., "Arrives Mar 21-24") next to each shipping option | Shipping options (5c-d) | Reduces uncertainty aversion | User knows exactly when to expect their order | +5-8 pp shipping step completion | Medium (requires carrier API or zone-based logic) | Low -- increases trust | High priority; directly addresses top ticket theme |
| 2 | **Inline returns guarantee badge**: Show a trust badge ("Free 30-day returns -- no questions asked") with expandable details directly on the shipping step | Returns gap (5e) | Reduces loss aversion / perceived risk | User feels safe that a wrong purchase is reversible | +3-5 pp shipping step completion | Low (copy + UI change) | Low -- reinforces trust | Directly addresses second ticket theme |
| 3 | **Smart default shipping selection**: Pre-select the most popular / best-value shipping option with delivery date visible | Shipping options (5c) | Status quo effect + friction reduction | Reduces decision effort; user can accept default or change | +2-3 pp shipping step completion | Low (logic + UI) | Low | Good complement to intervention #1 |
| 4 | **"Save cart + resume" with email**: If user starts to leave, offer to save their cart and email a resume link | Abandonment moment (5f) | Reduces friction / present bias (lowers commitment needed now) | User doesn't lose their cart; can return when ready | +1-3 pp eventual conversion (longer window) | Medium (exit intent + email trigger) | Low | Recovery mechanism, not primary fix |
| 5 | **Shipping cost preview in cart**: Show estimated shipping cost on the cart page before checkout begins | Cart review (step 2) | Reduces surprise / pain of paying | No sticker shock at shipping step | +2-4 pp shipping step completion (fewer surprise abandonments) | Low-Medium (estimate logic) | Low | Addresses compounding friction |
| 6 | **Order timeline visual**: Replace text-only shipping options with a simple visual timeline (order placed -> shipped -> arrives by DATE) | Shipping options (5c-d) | Reduces uncertainty; makes abstract "3-5 days" concrete | User can visualize the entire delivery journey | +2-4 pp shipping step completion | Medium (UI component) | Low | Enhancement of #1; can be phased |
| 7 | **Social proof on shipping**: "92% of orders in your area arrive within the estimated window" | Shipping options (5c-d) | Social proof + uncertainty reduction | Builds confidence that the estimate is reliable | +1-2 pp shipping step completion | Low (data query + copy) | Low-Medium (must be accurate) | Supplement to #1; requires data validation |
| 8 | **Progress bar with time estimate**: Show checkout progress (step 2 of 4 -- ~2 min left) | Entire checkout flow | Reduces uncertainty about process length | User knows how much effort remains | +1-2 pp overall checkout completion | Low | Low | General improvement, not specific to shipping uncertainty |
| 9 | **Returns policy tooltip on product images**: In the shipping step order summary, add a "returnable" label on each line item | Shipping step order summary (5a) | Reduces loss aversion per item | User sees returnability per product at decision moment | +1-2 pp shipping step completion | Low | Low | Reinforces #2 at item level |
| 10 | **Urgency framing (ethical)**: "Order within 2 hours to get it by [date]" | Shipping options (5c-d) | Present bias (makes "now" more valuable) + scarcity | User understands time-sensitivity of delivery promise | +1-3 pp same-session conversion | Low (logic + copy) | Medium -- must be truthful; never fake scarcity | Only use if delivery dates genuinely shift based on order time |

### Reinforcement + resilience notes (Step 5 of workflow)

Since this is a checkout conversion problem (not a habit/retention loop), formal streak/habit resilience patterns do not apply. However:

- **Resilience via save-and-resume (Intervention #4):** Acts as a "bend not break" mechanism for checkout -- if the user can't complete now, they don't lose their progress.
- **Reinforcement via confirmation:** Post-purchase confirmation should reinforce the delivery promise and returns guarantee, creating a positive "pause moment" that builds trust for repeat purchases.
- **Ethics notes:** All interventions are designed to reduce genuine uncertainty, not to pressure or manipulate. Delivery dates must be accurate (not artificially optimistic). Returns guarantee must reflect actual policy. Social proof stats must be real. Urgency framing (#10) must only be used when order timing genuinely affects delivery date.

---

## 6. Prioritized Shortlist (Top 3 Bets)

### Bet #1: Delivery Date Promise

- **Intervention:** Show estimated delivery date range next to each shipping option
- **Why this:** Directly addresses the #1 support ticket theme ("not sure when it arrives"). Uncertainty aversion is the primary diagnosed barrier. High impact, medium effort.
- **Hypothesis:** If we show a concrete delivery date range on the shipping step, then shipping step completion will increase by 5-8 pp, because users' primary uncertainty ("when will it arrive?") is resolved at the moment of decision.
- **Metric:** Shipping step completion rate

### Bet #2: Inline Returns Guarantee Badge

- **Intervention:** Show a trust badge with returns guarantee + expandable details on the shipping step
- **Why this:** Directly addresses the #2 support ticket theme ("returns are unclear"). Reduces perceived risk/loss aversion. Low effort, high confidence.
- **Hypothesis:** If we surface a clear returns guarantee on the shipping step, then shipping step completion will increase by 3-5 pp, because users' fear of being stuck with a bad purchase is mitigated at the moment of hesitation.
- **Metric:** Shipping step completion rate

### Bet #3: Smart Default Shipping Selection

- **Intervention:** Pre-select the best-value shipping option (with delivery date visible) so the user has a clear recommended choice
- **Why this:** Reduces decision friction and choice overload on the shipping step. Low effort, complements Bet #1. Leverages status quo effect.
- **Hypothesis:** If we pre-select the recommended shipping option with a visible delivery date, then shipping step completion will increase by 2-3 pp, because users face less decision effort and have a clear default path.
- **Metric:** Shipping step completion rate

**Combined expected impact:** +10-16 pp shipping step completion (with interaction effects, conservatively +8-12 pp).

**Why these three together:** They address different failure modes:
- Bet #1 solves **uncertainty about timing** (the primary barrier)
- Bet #2 solves **uncertainty about risk/reversibility** (the secondary barrier)
- Bet #3 solves **decision friction/overload** (the compounding barrier)

---

## 7. Behavioral Design Specs

### Spec #1: Delivery Date Promise

- **Target moment:** Shipping options display (step 5c-d)
- **Target behavior:** User selects a shipping option and proceeds to payment
- **Hypothesis:** If we show an estimated delivery date range (e.g., "Arrives Thu, Mar 20 - Mon, Mar 24") next to each shipping option, then shipping step completion rate will increase by 5-8 pp, because users can make an informed timing decision instead of abandoning due to uncertainty.
- **Behavioral mechanism(s):** Uncertainty aversion reduction; concrete framing replaces abstract "3-5 business days" with a specific date the user can plan around
- **User benefit:** "I know exactly when my order will arrive, so I can decide if the timing works for me."

#### UX + copy

- **Entry point:** Shipping options section of the checkout page, immediately visible when the step loads
- **Core interaction:**
  - Each shipping option displays: [Method name] -- [Price] -- **Arrives [Date range]**
  - Example: "Standard Shipping -- $5.99 -- **Arrives Thu, Mar 20 - Mon, Mar 24**"
  - Example: "Express Shipping -- $12.99 -- **Arrives Wed, Mar 19 - Thu, Mar 20**"
  - Delivery date is bold and uses the user's local day-of-week + date format
  - If exact date cannot be calculated (e.g., international, remote address), show: "Estimated 7-12 business days" with a note: "We'll email you a tracking link with a more precise estimate once shipped."
- **States:**
  - **Loading:** Skeleton placeholder where delivery dates will appear ("Calculating delivery dates...")
  - **Success:** Dates displayed as above
  - **Error/unavailable:** Fallback to "Estimated [X-Y] business days" with an explanatory note
  - **Address not yet entered:** Show "Enter your address to see delivery dates" as a prompt
- **Copy (draft):**
  - Delivery date label: "Arrives [Day, Mon DD - Day, Mon DD]"
  - Fallback: "Estimated delivery: [X-Y] business days after shipping"
  - Subtext (optional): "Most orders in [region] arrive within the estimated window."
- **Accessibility:** Delivery dates are in text (not images), associated with the correct radio button via aria-describedby. Screen readers announce the full option including date.

#### Controls + ethics

- **Transparency:** Delivery dates are estimates based on carrier data and shipping address. If we cannot provide a reliable estimate, we say so rather than fabricate one.
- **User control:** User can select any available shipping option; no forced upsell to express.
- **Potential harms + mitigations:**
  - Harm: Delivery date is inaccurate, eroding trust. Mitigation: Use carrier API data; display ranges not single dates; monitor actual vs. estimated delivery accuracy as a guardrail metric.
  - Harm: Slow estimated dates discourage purchase. Mitigation: This is an informed decision -- better than post-purchase disappointment. Consider offering express option prominently.

#### Measurement

- **Primary success metric:** Shipping step completion rate (% of users who see shipping options and proceed to payment)
- **Guardrails:**
  - Post-purchase "where is my order" support tickets (must not increase)
  - Delivery date accuracy (% of orders arriving within estimated window; target >90%)
  - Cart abandonment at shipping step (should decrease)
- **Instrumentation/events needed:**
  - `shipping_options_viewed` -- fired when shipping options (with dates) render; properties: `{shipping_options_count, has_delivery_dates: bool, address_entered: bool}`
  - `shipping_option_selected` -- fired when user selects an option; properties: `{method, price, estimated_delivery_range, is_default: bool}`
  - `shipping_step_completed` -- fired when user proceeds to payment; properties: `{method_selected, time_on_shipping_step_ms}`
  - `shipping_step_abandoned` -- fired when user leaves checkout from shipping step; properties: `{time_on_shipping_step_ms, shipping_options_viewed: bool}`

#### Rollout / rollback

- **Rollout plan:** Feature flag (`show_delivery_dates`); start with 10% of checkout traffic for 3 days to validate date accuracy, then ramp to 50% for the A/B test over 2 weeks.
- **Stop-the-line triggers:**
  - Shipping step completion rate drops by >3 pp vs. control
  - "Where is my order" tickets increase by >20% in treatment group
  - Delivery date API error rate exceeds 10%
- **Rollback plan:** Disable feature flag; revert to current shipping options display (method + price + "X-Y business days" text)

---

### Spec #2: Inline Returns Guarantee Badge

- **Target moment:** Shipping step (step 5e), visible alongside shipping options
- **Target behavior:** User proceeds past the shipping step to payment without hesitating over return concerns
- **Hypothesis:** If we display a clear, concise returns guarantee directly on the shipping step, then shipping step completion rate will increase by 3-5 pp, because users' perceived risk of an irreversible purchase is neutralized at the moment of maximum hesitation.
- **Behavioral mechanism(s):** Loss aversion reduction (the "loss" of money on an unreturnable product); uncertainty aversion reduction (clarity about what happens if something goes wrong)
- **User benefit:** "I know I can return this easily if it doesn't work out, so I can buy with confidence."

#### UX + copy

- **Entry point:** A trust badge/banner positioned directly below the shipping options section (or beside the order summary on desktop), visible without scrolling once shipping options are displayed
- **Core interaction:**
  - A compact trust element: [Return icon] **"Free 30-day returns"** -- [expandable "Learn more"]
  - On click/tap "Learn more," an inline expansion (not a new page) shows:
    - "Changed your mind? Return any item within 30 days for a full refund. Free return shipping included."
    - "Start a return from your order confirmation email or your account page."
    - Link to full returns policy for edge cases
  - Badge remains visible (does not collapse) throughout the shipping step
- **States:**
  - **Default:** Collapsed badge with headline copy
  - **Expanded:** Inline details as above
  - **Items with exceptions:** If certain items are final-sale or have different return windows, show per-item returnability labels in the order summary (e.g., "Final sale" or "60-day return window")
  - **No returns policy:** If the business has no returns policy, do NOT show this badge -- this intervention requires a genuine policy to surface
- **Copy (draft):**
  - Badge headline: "Free 30-day returns -- hassle-free"
  - Expanded: "Not the right fit? Return any item within 30 days for a full refund. Free return shipping. No questions asked."
  - Subtext: "Start a return anytime from your order page."
  - CTA: "See full policy" (links to returns policy page in new tab)
- **Accessibility:** Badge text is readable, not image-only. Expandable section uses `aria-expanded` and `aria-controls`. Sufficient color contrast for the trust badge.

#### Controls + ethics

- **Transparency:** The returns guarantee copy must accurately reflect the actual policy. If there are exceptions (final-sale items, time limits), they must be stated.
- **User control:** No action required from the user; the information is passively available. Expansion is optional.
- **Potential harms + mitigations:**
  - Harm: Increased return rate due to more awareness. Mitigation: Monitor return rate as a guardrail; a moderate increase may be acceptable if it's offset by higher conversion and better customer LTV.
  - Harm: Misleading if the actual policy is restrictive. Mitigation: Work with operations/legal to ensure the displayed policy matches reality exactly.

#### Measurement

- **Primary success metric:** Shipping step completion rate
- **Guardrails:**
  - Return rate (% of orders returned; acceptable increase threshold: +2 pp)
  - Returns-related support tickets (should decrease)
  - CSAT on checkout experience
- **Instrumentation/events needed:**
  - `returns_badge_viewed` -- fired when badge enters viewport; properties: `{page: "shipping_step"}`
  - `returns_badge_expanded` -- fired when user clicks "Learn more"; properties: `{page: "shipping_step"}`
  - `returns_policy_link_clicked` -- fired when user clicks full policy link; properties: `{source: "shipping_step_badge"}`

#### Rollout / rollback

- **Rollout plan:** Feature flag (`show_returns_badge_checkout`); can deploy to 50% immediately (low technical risk -- it's a UI/copy addition). Run A/B test for 2 weeks.
- **Stop-the-line triggers:**
  - Return rate increases by >5 pp (well above the +2 pp acceptable threshold)
  - Shipping step completion rate drops (unexpected negative effect)
- **Rollback plan:** Disable feature flag; remove badge from shipping step

---

### Spec #3: Smart Default Shipping Selection

- **Target moment:** Shipping options display (step 5c)
- **Target behavior:** User accepts the pre-selected shipping option (or makes a quick, confident switch) and proceeds to payment
- **Hypothesis:** If we pre-select the best-value shipping option with delivery date visible, then shipping step completion rate will increase by 2-3 pp, because users experience less decision friction and can accept a sensible default rather than evaluating all options from scratch.
- **Behavioral mechanism(s):** Status quo effect (pre-selected option is "chosen" by default); friction reduction (fewer active decisions required); anchoring (recommended option sets the reference point)
- **User benefit:** "The best option is already selected for me; I just need to confirm or adjust."

#### UX + copy

- **Entry point:** Shipping options section; the recommended option is pre-selected when the step loads
- **Core interaction:**
  - The most popular or best-value option (e.g., standard shipping) is pre-selected via radio button
  - A small "Recommended" or "Most popular" label appears next to the pre-selected option
  - All options remain visible and selectable; the default is not hidden or hard to change
  - The pre-selected option shows its delivery date prominently (integrates with Spec #1)
  - Example layout:
    ```
    (*) Standard Shipping -- $5.99 -- Arrives Mar 20-24  [Recommended]
    ( ) Express Shipping -- $12.99 -- Arrives Mar 19-20
    ( ) Economy Shipping -- Free -- Arrives Mar 26-Apr 2
    ```
- **States:**
  - **Default:** Most popular option pre-selected
  - **User changes selection:** New selection is immediately reflected; no "are you sure" friction
  - **Only one option available:** Option is pre-selected and labeled "Your shipping option"
  - **Address not entered:** Show "Enter address to see options" (same as Spec #1)
- **Copy (draft):**
  - Label: "Recommended" or "Most popular"
  - If using popularity: "Most popular" (requires data to back this up; otherwise use "Recommended")
- **Accessibility:** Pre-selected radio button has correct `checked` state. "Recommended" label is associated via `aria-label` or visible text.

#### Controls + ethics

- **Transparency:** The default is based on popularity or value (not on highest margin). If the business selects the default based on revenue, disclose this: "We recommend based on [criteria]."
- **User control:** All options are visible and one click to switch. No friction to change from the default.
- **Potential harms + mitigations:**
  - Harm: Users unthinkingly accept a shipping option that doesn't suit them (e.g., too slow). Mitigation: Show delivery date prominently on the default; ensure the default is genuinely the best value/most popular, not the most expensive.
  - Harm: "Recommended" label feels manipulative. Mitigation: Base on real data (most chosen by customers); avoid labeling the most expensive option as recommended unless it genuinely is most popular.

#### Measurement

- **Primary success metric:** Shipping step completion rate
- **Secondary:** % of users who accept the default vs. change shipping option (to understand default influence)
- **Guardrails:**
  - "Wrong shipping method" support tickets (must not increase)
  - Distribution of shipping methods selected (monitor for over-indexing on default)
- **Instrumentation/events needed:**
  - `shipping_default_presented` -- fired when default is pre-selected; properties: `{default_method, default_price}`
  - `shipping_option_changed` -- fired when user changes from default; properties: `{from_method, to_method}`
  - `shipping_step_completed` -- (already defined in Spec #1); add property: `{accepted_default: bool}`

#### Rollout / rollback

- **Rollout plan:** Feature flag (`smart_shipping_default`); deploy to 50% alongside or after Spec #1. Run A/B test for 2 weeks.
- **Stop-the-line triggers:**
  - "Wrong shipping method" tickets increase by >10%
  - Shipping step completion rate drops vs. control
- **Rollback plan:** Disable feature flag; revert to no pre-selection (all radio buttons unselected, or previous default behavior)

---

## 8. Experiment + Instrumentation Plan

### Experiment Plan

- **Experiment type:** A/B test (randomized at user/session level)
- **Population/cohorts:**
  - Control: Current shipping step (no delivery dates, no returns badge, no smart default)
  - Treatment A: Delivery Date Promise only (Spec #1) -- to isolate the effect of delivery date information
  - Treatment B: Full bundle (Specs #1 + #2 + #3) -- to measure combined effect
  - Optional Treatment C: Returns badge only (Spec #2) -- if traffic allows, to isolate returns guarantee effect
- **Primary metric + expected direction:**
  - Shipping step completion rate: expect +5-8 pp for Treatment A, +8-12 pp for Treatment B
- **Guardrails:**
  - Post-purchase return rate (must not increase by >2 pp)
  - "Where is my order" support tickets (must decrease or hold steady)
  - Returns-related support tickets (must decrease or hold steady)
  - CSAT on checkout experience (must not decrease)
  - Overall cart-to-purchase conversion rate (must increase or hold steady)
  - Delivery date accuracy (>90% of orders arrive within estimated window)
- **Duration / sample considerations:**
  - Minimum 2 weeks to capture weekday/weekend patterns
  - Target: 80% power to detect a 3 pp lift in shipping step completion rate
  - Sample size depends on current traffic; estimate ~5,000 users per variant for this effect size at typical checkout volumes
- **Risks/limitations:**
  - Delivery date accuracy depends on carrier API reliability; monitor API error rates
  - Novelty effect may inflate initial results; plan a follow-up read at 4 weeks
  - If traffic is insufficient for 3-4 variants, run sequentially: Treatment A first, then add B
- **Decision rule:**
  - **Ship:** Primary metric improves by >= 3 pp with statistical significance (p < 0.05), no guardrail violations
  - **Iterate:** Primary metric improves by 1-3 pp; refine copy/UX and re-test
  - **Kill:** No improvement or guardrail violations; investigate qualitative feedback before fully abandoning

### Instrumentation Spec (Events)

| Event Name | Trigger | Properties | Used for Metric | Owner | Notes |
|---|---|---|---|---|---|
| `checkout_started` | User initiates checkout | `{cart_value, item_count, user_id, session_id}` | Funnel baseline | Frontend | May already exist |
| `shipping_step_viewed` | Shipping step page/section loads | `{variant: control/A/B, has_delivery_dates: bool, has_returns_badge: bool, has_smart_default: bool}` | Funnel denominator | Frontend | New event |
| `shipping_options_loaded` | Shipping options render with data | `{options_count, has_delivery_dates: bool, default_method, load_time_ms}` | UX performance | Frontend | New event |
| `delivery_date_displayed` | Delivery date(s) successfully render | `{methods_with_dates: int, methods_without_dates: int, address_region}` | Date availability rate | Frontend | New; Spec #1 |
| `returns_badge_viewed` | Returns badge enters viewport | `{page: "shipping_step"}` | Badge visibility | Frontend | New; Spec #2 |
| `returns_badge_expanded` | User clicks "Learn more" on returns badge | `{page: "shipping_step"}` | User engagement with returns info | Frontend | New; Spec #2 |
| `returns_policy_link_clicked` | User clicks through to full returns policy | `{source: "shipping_step_badge"}` | Deep engagement | Frontend | New; Spec #2 |
| `shipping_option_selected` | User selects/changes a shipping option | `{method, price, estimated_delivery_range, is_default: bool, accepted_default: bool}` | Option preference | Frontend | New/updated |
| `shipping_step_completed` | User proceeds from shipping to payment | `{method_selected, price, time_on_step_ms, accepted_default: bool, returns_badge_expanded: bool, variant}` | **Primary metric** | Frontend | New event |
| `shipping_step_abandoned` | User leaves checkout from shipping step (exit/back/close) | `{time_on_step_ms, last_interaction, variant}` | Drop-off analysis | Frontend | New event |
| `delivery_date_api_error` | Carrier API fails to return delivery estimate | `{carrier, error_type, address_region}` | Operational health | Backend | New; Spec #1 |
| `order_delivered` | Order confirmed delivered by carrier | `{estimated_range, actual_delivery_date, within_estimate: bool}` | Delivery accuracy guardrail | Backend | May need new tracking |
| `return_initiated` | User starts a return | `{order_id, days_since_purchase, reason}` | Return rate guardrail | Backend | May already exist |

---

## 9. Risks / Open Questions / Next Steps

### Risks

1. **Delivery date accuracy:** If carrier APIs are unreliable or the business cannot calculate accurate delivery estimates, Spec #1 could backfire -- inaccurate dates erode trust more than no dates. **Mitigation:** Use date ranges (not single dates); monitor accuracy as a guardrail; have a graceful fallback for unreliable estimates.
2. **Returns rate increase:** Surfacing the returns policy more prominently may increase return volume. **Mitigation:** Set a guardrail threshold (+2 pp); monitor closely; this may be a worthwhile trade-off if conversion lift and customer LTV justify it.
3. **Implementation complexity for delivery dates:** Integrating carrier APIs for real-time delivery estimates may require more than 1 sprint. **Mitigation:** Start with zone-based static estimates (e.g., "East Coast: 3-5 days") as an MVP; iterate to real-time carrier data in a follow-up.
4. **Smart default ethics:** If the "recommended" option is chosen for revenue reasons rather than customer value, this becomes a dark pattern. **Mitigation:** Base default on most popular or best value; document the selection criteria; audit regularly.

### Open Questions

1. What is the actual current shipping step completion rate? (Assumed ~45% -- needs validation.)
2. Does the current checkout already show any delivery timeline information (even "3-5 business days" text)?
3. What is the actual returns policy? Is it genuinely generous enough to feature prominently?
4. Are carrier API integrations already available, or is this new infrastructure?
5. What is the current event instrumentation coverage for the checkout funnel? Which events above already exist?
6. Is there sufficient traffic to run a multi-variant A/B test, or should we test sequentially?
7. Are there specific product categories or price thresholds where shipping abandonment is disproportionately high?
8. Has the team tried any previous interventions on the checkout flow? What were the results?

### Next Steps

1. **Validate baseline metrics:** Pull actual shipping step completion rate and checkout funnel data to confirm the ~45% assumption and size the opportunity.
2. **Audit existing returns policy:** Confirm the policy is customer-friendly enough to feature. If restrictive, work with operations to improve before surfacing.
3. **Technical discovery for delivery dates:** Assess carrier API availability and accuracy; decide between real-time API vs. zone-based static estimates for MVP.
4. **Design + copy review:** Create mockups for all three specs; run a quick internal review (product, design, legal) before development.
5. **Implement instrumentation:** Add the new events defined above to the checkout flow (can start before the interventions ship -- baseline data is valuable).
6. **Build and launch Spec #2 first** (returns badge -- lowest effort, highest confidence, no API dependency), then **Spec #3** (smart default), then **Spec #1** (delivery dates -- highest impact but most effort).
7. **Run the A/B test:** 2-week minimum; monitor guardrails daily for the first week.
8. **Post-experiment:** Analyze results, decide ship/iterate/kill per the decision rule, and plan follow-up iterations.

---

## Quality Gate: Checklist Verification

### 1) Target behavior checklist
- [x] Target user segment is explicit. (Shoppers who reach the shipping step of checkout.)
- [x] Primary target behavior is observable (action + context + frequency). (Complete shipping step within 3 minutes of reaching it.)
- [x] Success metric and baseline are stated (even if approximate). (Shipping step completion rate, ~45% baseline.)
- [x] Guardrail metrics are defined. (Return rate, support tickets, CSAT, delivery accuracy.)
- [x] User benefit is stated. (Clarity and confidence about delivery timing and return options.)

### 2) Diagnosis checklist
- [x] Top drop-off moments are tied to specific journey steps/states. (Steps 5c-d, 5e, 5c.)
- [x] For each moment, the likely barrier type is named. (Uncertainty, loss aversion, friction.)
- [x] Mechanism hypotheses are plausible and labeled when speculative. (Shipping cost surprise labeled as hypothesis.)
- [x] At least one piece of evidence per priority moment. (Support tickets for top 2; hypothesis label for #3.)

### 3) Intervention quality checklist
- [x] Each intervention maps to a specific barrier and mechanism. (All 10 ideas mapped.)
- [x] At least one intervention reduces friction and one reduces uncertainty. (Friction: #3, #4, #5, #8; Uncertainty: #1, #2, #6, #7.)
- [x] "Pause moments" -- not applicable for checkout flow (no habit loop).
- [x] "Bend not break" -- addressed via save-cart-and-resume (#4).
- [x] Interventions include user controls. (All options remain selectable; badge is optional to expand; save cart is opt-in.)

### 4) Ethics / trust checklist
- [x] No deception: no hidden costs, forced continuity, or misleading UI. (All info surfaced is factual.)
- [x] No coercion: user can opt out without penalty. (All interventions are informational or default-based with easy override.)
- [x] No exploitation of vulnerable cohorts. (Standard e-commerce; no special populations.)
- [x] Framing respects autonomy. (Helps users make informed decisions.)
- [x] Risks and potential harms are listed with mitigations. (See each spec + Risks section.)

### 5) Experiment readiness checklist
- [x] Each top bet has a clear hypothesis and measurable metric movement. (All three specs have explicit hypotheses.)
- [x] Instrumentation requirements are listed. (12 events defined with properties.)
- [x] Rollout plan is safe with stop-the-line triggers. (Feature flags, phased rollout, explicit triggers.)
- [x] Decision rule is stated. (Ship/iterate/kill criteria defined.)

### Rubric Self-Assessment

| Dimension | Score | Rationale |
|---|---|---|
| 1) Problem + behavior clarity | **5** | Clear behavior spec (shipping step completion within 3 min), baseline stated, success + guardrails defined, user benefit articulated |
| 2) Diagnosis quality | **4** | Top friction points mapped to specific steps with evidence from support tickets; one barrier labeled as hypothesis; minor gap: no session replay or analytics data available to confirm |
| 3) Intervention-mechanism fit | **5** | Interventions map to diagnosed mechanisms across uncertainty (Specs #1, #2), friction (#3), and loss aversion (#2); multiple barrier types covered |
| 4) Ethics + user trust | **5** | Transparency designed into every spec; opt-out/override is trivial; harms listed with mitigations; no dark patterns |
| 5) Experimentation + measurement | **4** | Events defined for primary and guardrail metrics; A/B test feasible; rollout plan exists; minor gap: exact sample size depends on traffic data we don't have |
| 6) Execution readiness | **4** | Three specs have UX/copy, states, edge cases, and rollout plans; an engineer could start on Specs #2 and #3 immediately; Spec #1 requires technical discovery for carrier API |

**Overall: 27/30** -- Pack is execution-ready for Specs #2 and #3; Spec #1 requires one technical discovery spike before build.
