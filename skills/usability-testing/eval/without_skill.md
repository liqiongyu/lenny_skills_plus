# Usability Test Plan & Moderator Guide: Checkout Redesign

**Project:** B2C Web App Checkout Redesign
**Method:** Remote Moderated Usability Testing
**Sessions:** 6 sessions with existing users
**Timeline:** This week (5 business days)

---

## Part 1: Usability Test Plan

### 1.1 Research Objectives

**Primary Goal:** Evaluate whether the redesigned checkout flow enables existing users to complete purchases efficiently, confidently, and without friction.

**Specific Research Questions:**
1. Can users successfully complete the checkout process from cart to order confirmation without assistance?
2. Where do users hesitate, express confusion, or make errors during checkout?
3. Do users understand each step of the checkout flow and what is expected of them at each stage?
4. How does the redesigned experience compare to users' expectations based on their prior experience with the current checkout?
5. Are shipping, payment, and order review steps clear and perceived as trustworthy?
6. Do users feel confident about the information they are entering and the actions they are taking?

### 1.2 Methodology

| Parameter | Detail |
|---|---|
| **Method** | Remote moderated usability testing |
| **Platform** | Zoom or UserTesting Live (screen share + webcam + audio) |
| **Prototype/Build** | Staging environment or high-fidelity interactive prototype |
| **Sessions** | 6 individual sessions |
| **Duration** | 45-60 minutes per session |
| **Recording** | Screen + audio + webcam (with participant consent) |
| **Analysis** | Task-based success metrics, qualitative thematic analysis |

### 1.3 Participant Recruitment

**Target Profile:** Existing users of the platform who have completed at least one purchase in the past 6 months.

**Screening Criteria:**

| Criterion | Requirement |
|---|---|
| Existing customer | Must have an active account with order history |
| Recency | At least 1 purchase in the past 6 months |
| Frequency | Mix of frequent (5+ orders/year) and occasional (1-4 orders/year) buyers |
| Device | Desktop/laptop with Chrome, Firefox, Safari, or Edge |
| Tech comfort | Comfortable with screen sharing and video calls |
| Age range | Mix across 25-55 (or reflect core demographic) |
| Exclusions | No employees, contractors, or anyone involved in the redesign |

**Participant Mix (6 sessions):**
- 3 frequent buyers (5+ orders/year)
- 3 occasional buyers (1-4 orders/year)
- At least 2 participants who have used a saved payment method
- At least 2 participants who have used guest-like or minimal-save checkout preferences
- Gender and age diversity reflecting the user base

**Recruitment Method:**
- Pull a list of qualifying users from the CRM/analytics database
- Send a recruitment email with a brief screener survey (5 questions)
- Offer an incentive: $75 gift card or account credit per session
- Recruit 8 participants to account for 2 potential no-shows

**Screener Questions:**
1. When was the last time you made a purchase on [platform name]? (Must be within 6 months)
2. Approximately how many purchases have you made in the past year? (Segment into frequent/occasional)
3. What device/browser do you typically use for online shopping?
4. Are you comfortable joining a 45-60 minute video call where you share your screen?
5. Do you have any affiliation with [company name] as an employee or contractor? (Disqualify if yes)

### 1.4 Schedule

| Day | Activity |
|---|---|
| **Monday** | Final recruitment confirmation, send calendar invites and prep materials, pilot session with internal team member |
| **Tuesday** | Sessions 1 & 2 (morning and afternoon) |
| **Wednesday** | Sessions 3 & 4 (morning and afternoon) |
| **Thursday** | Sessions 5 & 6 (morning and afternoon), begin analysis |
| **Friday** | Complete analysis, draft findings report, share topline findings with stakeholders |

**Session Spacing:** Minimum 30-minute buffer between sessions for moderator notes, debrief, and mental reset.

### 1.5 Test Scenarios and Tasks

**Pre-Task Setup:** Participants will be given a scenario where they need to purchase specific items. A pre-loaded cart (or instructions to add specific items) will be prepared in the staging environment.

#### Task 1: Standard Checkout with Saved Address
**Scenario:** "You've added a few items to your cart that you'd like to purchase. Please go ahead and complete the checkout process using your existing account information."
- **Success Criteria:** Participant reaches the order confirmation page without moderator assistance
- **Measures:** Completion (yes/no), time on task, number of errors, points of confusion

#### Task 2: Checkout with a New Shipping Address
**Scenario:** "Imagine you want to send this order to a friend. Please change the shipping address to a new one during checkout."
- **Provide:** A fictional address to use
- **Success Criteria:** Participant successfully adds a new address and completes checkout
- **Measures:** Completion, time, errors, discoverability of the "add new address" function

#### Task 3: Apply a Promo Code
**Scenario:** "You have a discount code. Please apply it during checkout."
- **Provide:** A valid test promo code
- **Success Criteria:** Participant locates the promo code field, enters the code, and sees the discount reflected
- **Measures:** Completion, time, ease of finding the promo field, clarity of discount display

#### Task 4: Change Payment Method
**Scenario:** "You'd like to use a different payment method than the one currently selected. Please switch to a different card or payment option."
- **Success Criteria:** Participant successfully changes the payment method
- **Measures:** Completion, time, discoverability, confidence level

#### Task 5: Review and Modify Order Before Confirmation
**Scenario:** "Before you place the order, please review the details. You've decided you want to remove one item. Please do that and then complete the purchase."
- **Success Criteria:** Participant finds the order summary, removes an item, and submits the order
- **Measures:** Completion, time, ability to edit from the review step, clarity of the order summary

### 1.6 Metrics and Data Collection

**Quantitative Metrics:**

| Metric | How Measured |
|---|---|
| Task completion rate | Binary: completed without assistance / needed help / failed |
| Time on task | Stopwatch from task start to completion (per task) |
| Error rate | Count of wrong clicks, incorrect entries, backtracking per task |
| System Usability Scale (SUS) | Post-test questionnaire (10-item standard SUS) |
| Single Ease Question (SEQ) | 7-point scale after each task ("How easy was this task?") |
| Confidence rating | 5-point scale: "How confident are you that your order was placed correctly?" |

**Qualitative Data:**

| Data Type | Collection Method |
|---|---|
| Think-aloud commentary | Continuous during tasks (audio/video recorded) |
| Pain points and confusion | Moderator observation notes, timestamped |
| Positive moments | Note moments of delight, satisfaction, or ease |
| Expectations vs. reality | Post-task interview responses |
| Comparisons to current flow | Post-test interview responses |
| Suggestions and preferences | Post-test interview responses |

### 1.7 Equipment and Setup Checklist

**Moderator Setup:**
- [ ] Laptop/desktop with stable internet connection
- [ ] Video conferencing tool installed and tested (Zoom, etc.)
- [ ] Screen recording enabled and verified
- [ ] Backup recording method (OBS or secondary tool)
- [ ] Moderator guide printed or on second screen
- [ ] Note-taking template open and ready
- [ ] Stopwatch or timer app
- [ ] Quiet environment with no interruptions

**Participant Setup (communicated in advance):**
- [ ] Desktop or laptop computer (not mobile for this round)
- [ ] Chrome, Firefox, Safari, or Edge browser
- [ ] Stable internet connection
- [ ] Webcam and microphone enabled
- [ ] Quiet space for 60 minutes
- [ ] Close other tabs and notifications for privacy and focus

**Test Environment:**
- [ ] Staging environment URL confirmed and accessible
- [ ] Test accounts created for each participant (pre-loaded with cart items, saved addresses, saved payment methods)
- [ ] Promo codes activated and verified
- [ ] Fallback plan if staging goes down (screenshots, prototype link)

### 1.8 Roles

| Role | Person | Responsibility |
|---|---|---|
| **Moderator** | [Name] | Runs the session, asks questions, manages time |
| **Note-taker** | [Name] | Captures observations, timestamps, quotes in real time |
| **Observer(s)** | [Names - optional] | Silent observers from product/design/engineering (cameras off, muted) |

**Observer Protocol:**
- Observers must remain silent and invisible to participants during the session
- Observers may submit questions to the moderator via a private Slack channel or chat
- Maximum 3 observers per session to avoid technical issues
- Observers should take their own notes using the provided observation template

### 1.9 Ethical Considerations and Consent

- Obtain written informed consent before each session (sent via email, signed electronically)
- Consent form must cover: purpose of the study, voluntary participation, right to withdraw at any time, recording and data usage, confidentiality protections
- Do not use real payment information; use test accounts with dummy data
- Ensure participant data is stored securely and deleted after analysis
- Compensate all participants regardless of session completion

### 1.10 Deliverables

| Deliverable | Due |
|---|---|
| Topline findings (bullet summary) | Friday end of day |
| Full findings report with severity ratings | Following Monday |
| Highlight reel (2-3 min video clips of key moments) | Following Tuesday |
| Prioritized recommendations matrix | Following Tuesday |

---

## Part 2: Moderator Guide

### 2.1 Session Structure Overview

| Time | Section | Duration |
|---|---|---|
| 0:00 | Welcome and Setup | 5 min |
| 0:05 | Warm-Up Questions | 5 min |
| 0:10 | Think-Aloud Practice | 3 min |
| 0:13 | Task 1: Standard Checkout | 8 min |
| 0:21 | Task 2: New Shipping Address | 7 min |
| 0:28 | Task 3: Apply Promo Code | 5 min |
| 0:33 | Task 4: Change Payment Method | 5 min |
| 0:38 | Task 5: Review and Modify Order | 7 min |
| 0:45 | Post-Test Questionnaire (SUS) | 5 min |
| 0:50 | Post-Test Interview | 8 min |
| 0:58 | Wrap-Up and Thank You | 2 min |
| **Total** | | **60 min** |

### 2.2 Script: Welcome and Setup (5 minutes)

> "Hi [Participant Name], thank you so much for taking the time to join us today. My name is [Moderator Name], and I'll be guiding you through today's session.
>
> Before we begin, I want to set some expectations for our time together:
>
> **What we're doing:** We're evaluating a new version of our checkout experience. We're testing the design, not you. There are no right or wrong answers, and you cannot make any mistakes.
>
> **How this works:** I'll ask you to complete a few tasks on the site while sharing your screen. As you work through each task, I'd like you to think out loud -- tell me what you're looking at, what you're thinking, what you expect to happen, and any reactions you have. This is incredibly valuable to us.
>
> **Recording:** With your permission, we'll be recording this session (screen and audio) so our team can review the findings later. The recording will only be used internally and will not be shared publicly. Is that okay with you?
>
> [Wait for confirmation]
>
> **A few ground rules:**
> - I may stay quiet at times. That's not because you're doing anything wrong -- I just want to observe your natural behavior.
> - If you get stuck, that's perfectly fine and actually very helpful information for us. I may not be able to help you right away because we want to see what you'd do on your own.
> - If at any point you feel uncomfortable or want to stop, just let me know. This is completely voluntary.
>
> Do you have any questions before we get started?"

**[Confirm screen share is working. Confirm the staging URL loads correctly. Confirm recording is active.]**

### 2.3 Script: Warm-Up Questions (5 minutes)

> "Great, let's start with a few quick background questions."

1. "Can you tell me a little about how you typically shop online? What devices do you usually use?"

2. "How often would you say you make purchases on [our platform]? What kinds of things do you usually buy?"

3. "Thinking about your most recent purchase with us, how would you describe that checkout experience? Was there anything that stood out -- good or bad?"

4. "When you're checking out on any e-commerce site, what matters most to you? What makes a checkout experience feel good versus frustrating?"

**Moderator note:** Keep this conversational. These questions build rapport, calibrate the participant's baseline, and reveal prior expectations. Do not spend more than 5 minutes here.

### 2.4 Script: Think-Aloud Practice (3 minutes)

> "Before we dive into the tasks, I'd like to do a quick practice round so the think-aloud approach feels natural.
>
> Can you go to any website you use regularly -- maybe a news site or a shopping site you like -- and just tell me what you see, what you're thinking, and what you'd click on and why? Just 30 seconds or so."

**[Let participant practice. Coach gently if needed:]**

> "That's great. If I notice you've gone quiet during a task, I might gently remind you to keep sharing your thoughts. It really helps us understand your experience."

### 2.5 Task Scripts

#### Task 1: Standard Checkout with Saved Address (8 minutes)

**Setup:** Direct participant to the staging URL where they are logged into a test account with items in the cart.

> "Okay, let's get started. I'd like you to imagine this is your real account. You've added a few items to your cart and you're ready to check out. Please go ahead and complete the purchase as you normally would, using the information that's already saved on your account.
>
> Remember to think out loud as you go. I'm interested in everything -- what you notice, what you expect, what surprises you."

**Moderator Observation Points:**
- Does the participant find the checkout button easily?
- How do they react to the step indicator / progress display?
- Do they understand each section of the checkout (shipping, payment, review)?
- Do they notice the saved address and recognize it?
- Is there any hesitation at the payment step?
- How do they react to the order summary?
- Do they feel confident when clicking the final "Place Order" button?

**Post-Task:**
> "How easy or difficult was that for you?" [Record SEQ rating 1-7]
> "Was there anything that surprised you or felt different from what you expected?"
> "Was there any point where you weren't sure what to do next?"

#### Task 2: Checkout with a New Shipping Address (7 minutes)

**Setup:** Reset the checkout or navigate back to the cart.

> "For this next task, imagine you want to send this order to a friend as a gift. The address you need to ship to is:
>
> Jane Smith, 742 Evergreen Terrace, Springfield, IL 62704
>
> Please change the shipping address to this new one and proceed through checkout."

**[Provide the address on screen or read it twice. Offer to paste it in chat if needed.]**

**Moderator Observation Points:**
- Can the participant find how to add or change the shipping address?
- Is the "add new address" or "edit address" control obvious?
- Does the address form feel straightforward?
- Are required vs. optional fields clear?
- Does the participant encounter any validation errors? How are they handled?
- After entering the new address, does it correctly appear as the selected shipping option?

**Post-Task:**
> "How easy or difficult was that?" [SEQ 1-7]
> "How did you feel about the process of adding a new address?"
> "Did the system make it clear where the order would be shipped?"

#### Task 3: Apply a Promo Code (5 minutes)

> "Great. Now, imagine you have a discount code you'd like to apply to your order. The code is SAVE20. Please find where to enter that code and apply it."

**[Display or paste the code: SAVE20]**

**Moderator Observation Points:**
- How quickly does the participant find the promo code field?
- Is the field visible or hidden behind a link/accordion?
- Does the participant enter the code correctly on the first try?
- Is the feedback clear after applying? (Success message, discount reflected in total)
- If the code fails, is the error message helpful?

**Post-Task:**
> "How easy or difficult was that?" [SEQ 1-7]
> "Was it easy to find where to enter the code?"
> "After you applied the code, was it clear that the discount was applied?"

#### Task 4: Change Payment Method (5 minutes)

> "Now imagine you want to use a different payment method than the one that's currently selected. Please switch to a different card or payment option."

**Moderator Observation Points:**
- Can the participant find the payment method selection?
- Is it clear which payment method is currently selected?
- Can they easily switch to another saved method?
- Is the option to add a new payment method discoverable?
- Do they feel secure during this step?

**Post-Task:**
> "How easy or difficult was that?" [SEQ 1-7]
> "How did you feel about the security of this step?"
> "Was anything confusing about the payment options?"

#### Task 5: Review and Modify Order Before Confirmation (7 minutes)

> "Last task. Before you place the order, please take a moment to review all the details. You've decided you actually don't want [specific item name]. Please remove that item from your order, and then go ahead and place the order."

**Moderator Observation Points:**
- Does the participant review the order details or skip ahead?
- Is the order summary comprehensive (items, quantities, prices, shipping, tax, total)?
- Can the participant figure out how to remove an item from the review/summary step?
- Does the participant need to go back to the cart, or can they edit in-line?
- After removal, does the total update correctly?
- How does the participant react to the final confirmation button?
- What is their reaction to the order confirmation page?

**Post-Task:**
> "How easy or difficult was that?" [SEQ 1-7]
> "How did you feel about the order review step? Did it give you enough information?"
> "How confident are you that the order was placed correctly?" [1-5 scale]
> "Is there anything you would have wanted to see or do differently on that final page?"

### 2.6 Post-Test Questionnaire (5 minutes)

> "Thank you for working through all of those tasks. Now I'd like you to fill out a short questionnaire about the overall experience."

**Administer the System Usability Scale (SUS):**

Provide the 10 standard SUS statements via a shared link (Google Form, Typeform, or similar) with 5-point Likert agreement scale (Strongly Disagree to Strongly Agree):

1. I think that I would like to use this checkout process frequently.
2. I found the checkout process unnecessarily complex.
3. I thought the checkout process was easy to use.
4. I think that I would need the support of a technical person to use this checkout.
5. I found the various functions in the checkout were well integrated.
6. I thought there was too much inconsistency in this checkout process.
7. I would imagine that most people would learn to use this checkout very quickly.
8. I found the checkout process very cumbersome to use.
9. I felt very confident using this checkout process.
10. I needed to learn a lot of things before I could get going with this checkout.

### 2.7 Post-Test Interview (8 minutes)

> "Now I have a few final questions about your overall impressions."

1. "What was your overall impression of this checkout experience?"

2. "What worked well? What felt easy or intuitive?"

3. "What was frustrating or confusing? What would you change?"

4. "How does this compare to your previous checkout experience on our site? Better, worse, or about the same? In what ways?"

5. "How does this compare to checkout experiences on other sites you use regularly?"

6. "Was there anything missing that you expected to see?"

7. "How would you describe this checkout to a friend? What words come to mind?"

8. "If you could change one thing about this checkout, what would it be?"

9. "Is there anything else you'd like to share that we haven't covered?"

### 2.8 Script: Wrap-Up (2 minutes)

> "That's everything I had for today. Thank you so much for your time and your honest feedback -- it's genuinely valuable and will directly help us improve the experience for you and all of our customers.
>
> Your [gift card / account credit] of $75 will be sent to you within [timeframe, e.g., 3 business days].
>
> If you think of anything else after today's session, feel free to reach out to me at [email address].
>
> Have a great rest of your day!"

**[Stop recording. Save files immediately. Complete moderator debrief notes within 15 minutes.]**

### 2.9 Moderator Probing Techniques

**When the participant is silent:**
- "What are you thinking right now?"
- "Tell me what you're looking at."
- "What do you expect will happen if you click that?"

**When the participant is stuck:**
- Wait at least 20-30 seconds before intervening.
- "What would you normally do at this point?"
- "Where would you expect to find that?"
- "Is there anything on the screen that might help?"
- If stuck for more than 90 seconds with no progress: "It's okay to feel stuck -- that's really useful information. Would you like me to help you move forward, or would you like to try a different approach?"

**When the participant asks for help:**
- "What do you think you should do?"
- "Where would you look for that information?"
- "I'd love to see what you'd try first."
- Only provide direct help if the participant is clearly frustrated and progress is impossible. Log this as a task failure.

**When the participant makes an error:**
- Do not correct them immediately. Observe whether they self-correct.
- If they continue down the wrong path: "I notice you [description of action]. Can you tell me what you were expecting there?"
- Note: errors are data, not problems to fix during the session.

**When the participant provides surface-level feedback:**
- "Can you tell me more about that?"
- "What specifically made you feel that way?"
- "You mentioned it felt [word they used]. Can you walk me through what triggered that?"

**Avoid leading questions such as:**
- "Did you find that easy?" (leading toward a positive response)
- "Was that confusing?" (leading toward a negative response)
- "Don't you think the button should be bigger?" (suggesting a specific solution)

### 2.10 Note-Taking Template

Use this template for each session. The note-taker should capture entries in real time.

```
Session #: ___
Participant ID: ___
Date/Time: ___
Moderator: ___
Note-taker: ___

TASK 1: Standard Checkout
- Completion: [ ] Success  [ ] Success with difficulty  [ ] Failure
- Time: ___
- SEQ (1-7): ___
- Errors/Missteps: ___
- Quotes: ___
- Observations: ___

TASK 2: New Shipping Address
- Completion: [ ] Success  [ ] Success with difficulty  [ ] Failure
- Time: ___
- SEQ (1-7): ___
- Errors/Missteps: ___
- Quotes: ___
- Observations: ___

TASK 3: Apply Promo Code
- Completion: [ ] Success  [ ] Success with difficulty  [ ] Failure
- Time: ___
- SEQ (1-7): ___
- Errors/Missteps: ___
- Quotes: ___
- Observations: ___

TASK 4: Change Payment Method
- Completion: [ ] Success  [ ] Success with difficulty  [ ] Failure
- Time: ___
- SEQ (1-7): ___
- Errors/Missteps: ___
- Quotes: ___
- Observations: ___

TASK 5: Review and Modify Order
- Completion: [ ] Success  [ ] Success with difficulty  [ ] Failure
- Time: ___
- SEQ (1-7): ___
- Errors/Missteps: ___
- Quotes: ___
- Observations: ___

OVERALL
- SUS Score: ___
- Confidence Rating (1-5): ___
- Top positive moments: ___
- Top pain points: ___
- Notable quotes: ___
- Key themes from interview: ___
- Moderator reflections: ___
```

---

## Part 3: Analysis Framework

### 3.1 Severity Rating Scale

After all sessions are complete, assign a severity rating to each identified issue.

| Severity | Label | Definition | Action |
|---|---|---|---|
| **4** | Critical | Prevents task completion. Users cannot proceed without assistance. | Must fix before launch |
| **3** | Major | Causes significant delay, confusion, or errors. Users can eventually complete but with difficulty. | Should fix before launch |
| **2** | Minor | Causes slight hesitation or minor confusion. Users recover on their own quickly. | Fix soon after launch |
| **1** | Cosmetic | Noticed but does not impact task completion or user confidence. | Fix when convenient |

### 3.2 Issue Tracking Template

| # | Issue Description | Task(s) | Severity | Frequency (out of 6) | Participant IDs | Recommendation |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |

### 3.3 Analysis Process

1. **Within 15 minutes of each session:** Moderator and note-taker complete a debrief, capture top 3 observations and any urgent issues.
2. **After all 6 sessions:** Review all recordings and notes. Identify recurring themes.
3. **Affinity mapping:** Group observations into categories (navigation, comprehension, trust, efficiency, error handling, visual design).
4. **Quantitative summary:** Calculate task completion rates, average times, average SEQ scores, SUS score.
5. **Prioritization:** Combine severity and frequency to rank issues. A severity-4 issue seen in 1 session may outrank a severity-2 issue seen in all 6.
6. **Recommendations:** For each issue, propose at least one design solution with rationale.

### 3.4 Reporting Structure

**Topline Report (Friday):**
- Executive summary (3-5 bullet points)
- Task completion rate table
- Top 5 issues with severity ratings
- SUS score with benchmark comparison (industry average for e-commerce: ~68)

**Full Report (following Monday):**
- Study overview and methodology
- Participant demographics summary
- Task-by-task findings with supporting quotes and timestamps
- Complete issue log with severity, frequency, and recommendations
- Positive findings (what worked well)
- SUS score analysis
- Prioritized recommendations matrix (effort vs. impact)
- Appendix: session recordings index, raw data, consent forms

**Highlight Reel (following Tuesday):**
- 2-3 minute video compilation of key moments
- Include: critical failures, moments of confusion, positive reactions, notable quotes
- Add brief text overlays for context

---

## Appendix A: Participant Communication Templates

### Recruitment Email

**Subject:** Help us improve your shopping experience -- $75 reward

Hi [Name],

We're making improvements to our checkout experience and would love your input. As a valued customer, your perspective would be incredibly helpful.

We're looking for people to participate in a 45-60 minute remote video session this week where you'll walk through our new checkout while sharing your thoughts. It's informal, easy, and your honest feedback (including criticism) is exactly what we need.

**Details:**
- 45-60 minutes via Zoom video call
- Available slots: [Tuesday-Thursday, list specific times]
- $75 [gift card / account credit] as a thank you

Interested? Please fill out this short form (2 minutes): [Screener link]

Thanks so much,
[Your name]

### Session Confirmation Email

**Subject:** Your feedback session is confirmed -- [Day, Date, Time]

Hi [Name],

Thanks for signing up! Here are your session details:

**When:** [Day, Date, Time with timezone]
**Where:** [Zoom link]
**Duration:** 45-60 minutes
**Reward:** $75 [gift card / account credit]

**Before the session, please:**
- Use a desktop or laptop computer (not a phone or tablet)
- Have Google Chrome, Firefox, Safari, or Edge available
- Find a quiet space with a stable internet connection
- Be ready to share your screen and turn on your camera

Attached is a consent form. Please review and sign it before our session.

If you need to reschedule, please let me know as soon as possible.

Looking forward to speaking with you!

[Your name]

### No-Show Follow-Up

**Subject:** We missed you today

Hi [Name],

We had a session scheduled today at [time] and wanted to check in. No worries if something came up -- we understand things happen.

If you're still interested in participating, we have availability on [alternative times]. Let me know and I'll get you rescheduled.

Thanks,
[Your name]

---

## Appendix B: Pilot Session Checklist

Run one internal pilot session (Monday) to verify everything works before real participants.

- [ ] Staging environment loads correctly and is stable
- [ ] Test account has correct items in cart, saved addresses, and saved payment methods
- [ ] Promo code SAVE20 works and discount displays correctly
- [ ] Screen sharing works on the video conferencing platform
- [ ] Recording captures both screen and audio clearly
- [ ] Timer/stopwatch is accessible during session
- [ ] Note-taking template is ready and accessible to the note-taker
- [ ] Observer channel (Slack/chat) is set up and tested
- [ ] Consent form link works and submissions are received
- [ ] Post-test SUS questionnaire link works and captures responses
- [ ] Full session fits within 60 minutes (adjust task count if needed)
- [ ] Backup plan is ready in case staging goes down
- [ ] Moderator has practiced all probing techniques and transitions
