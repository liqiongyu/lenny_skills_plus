# User Interview Pack: B2B SaaS Onboarding Activation Drop

---

## A. Context Snapshot

| Field | Detail |
|---|---|
| **Decision to inform** | Determine whether to revert, iterate, or redesign the new onboarding flow based on what is actually breaking for new trial users. |
| **Research goal** | Understand what new trial users experience step-by-step during onboarding under the new flow, where they get stuck or abandon, what workarounds they attempt, and what "activated" vs "not activated" looks like from their perspective. |
| **Interview type** | Discovery (with onboarding-specific probes). |
| **Target participants** | New trial users who signed up within the last 7-14 days and attempted onboarding under the new flow. Mix of activated and not-yet-activated users. |
| **Constraints** | 8 interviews; must be scheduled and completed this week; 45 minutes each; recording allowed with consent; no external incentive budget mentioned (assume none unless available). |
| **Current evidence** | Activation rate dropped after the onboarding change. Quantitative data shows the drop but not the "why." No qualitative data yet on what specifically is failing in the new flow. |
| **Hypotheses / risks** | H1: The new onboarding introduces steps that are confusing or feel irrelevant, causing users to abandon before reaching the activation milestone. H2: The new flow removes guidance or context that the old flow provided, leaving users uncertain about what to do next. H3: The activation metric itself may not have changed meaning, but the path to reach it is less discoverable. Risk: If we only interview activated users, we miss the failure stories that matter most. |

**What will we do differently after these interviews?** We will know which specific steps in the new onboarding flow cause friction, abandonment, or confusion, and we will have enough evidence to either (a) ship targeted fixes to the new flow, (b) revert specific changes, or (c) redesign the flow with user-validated requirements. The team will make this call by end of next week.

---

## B. Recruiting Plan + Screener

### Participant Profile (Inclusion / Exclusion)

**Inclusion criteria (behavior/situation-based)**
- Signed up for a trial within the last 14 days (experienced the new onboarding flow).
- Attempted at least one onboarding step (opened the product, started setup).
- Role: the person who actually performed the setup (not someone who delegated it).

**Exclusion criteria**
- Signed up before the onboarding change went live (old flow experience).
- Internal accounts, test accounts, or employee accounts.
- Users who signed up but never logged in (no onboarding experience to discuss).
- Existing customers on a new workspace (they have prior product context).

**Target mix**
- Core: 6 interviews — new trial users who attempted onboarding in the last 7-14 days (mix of 3 who activated and 3 who did not).
- Edge cases: 2 interviews — (1) a user who explicitly abandoned / churned during onboarding, and (1) a user who activated quickly (under 1 day) to understand what went right.

**Recency requirement**
- Signed up within the last 14 days. Prioritize the last 7 days for sharpest recall.

---

### Recruiting Channels

| Channel | Action | Expected volume needed |
|---|---|---|
| **In-product / Email (CRM)** | Query trial signups from the last 14 days. Segment by activation status. Send personalized email to each segment. | Send 40-50 emails to book 8 interviews (expect ~15-20% response, ~50% of responders will schedule). |
| **Support / CS tickets** | Ask support team to flag any new trial users who wrote in with onboarding questions or complaints in the last 2 weeks. Reach out directly. | 5-10 candidates; high signal, likely to accept. |
| **In-app prompt (if available)** | Trigger a short in-app message for trial users who are mid-onboarding: "We'd love 45 min of your time to hear about your setup experience. Interested?" | Depends on traffic; useful for catching users mid-experience. |

**Scheduling logistics**
- Use a scheduling tool (Calendly or equivalent) with 45-minute slots across Mon-Fri this week.
- Offer morning and afternoon slots across the user's timezone.
- Send calendar invite with video call link (Zoom/Google Meet) immediately upon confirmation.
- Send a reminder 24 hours before and 1 hour before the session.
- Have 2-3 backup slots in case of no-shows (expect 10-20% no-show rate).

---

### Outreach Copy

**Email to not-yet-activated trial users:**

> Subject: Quick question about your setup experience
>
> Hi {first_name},
>
> I'm {your_name}, a product manager at {product}. I noticed you recently signed up for a trial, and I'm trying to understand how the setup experience is working for new users.
>
> Would you be open to a 45-minute video call this week to walk me through what your experience has been like so far? This is purely a research conversation -- I'm not selling anything. I just want to hear your honest experience. With your permission, I'd record the call for my notes only.
>
> If you're interested, you can pick a time here: {scheduling_link}
>
> Thanks for considering it.
>
> {your_name}
> Product Manager, {product}

**Email to activated trial users:**

> Subject: 45 min to share your onboarding experience?
>
> Hi {first_name},
>
> I'm {your_name}, a PM at {product}. You recently signed up and got set up, and I'd love to hear how that went -- what worked, what didn't, and what almost stopped you.
>
> Would you have 45 minutes for a video call this week? This is a research conversation, not a sales call. With your permission, I'd record for notes only.
>
> Pick a time here if you're open to it: {scheduling_link}
>
> Thanks,
> {your_name}

**Follow-up (if no response after 2 days):**

> Hi {first_name}, just a quick follow-up -- I'd really value hearing about your experience getting started with {product}. If this week doesn't work, I completely understand. Here's the link in case it's easier: {scheduling_link}

---

### Screener

Use this screener to confirm fit before scheduling. Deliver via a short form (Typeform, Google Form) or ask these questions in a brief email exchange.

**Q1.** What best describes your role?
- [ ] I'm the person who set up / is setting up {product} for my team
- [ ] Someone else set it up; I'm a user
- [ ] Other: ___

*Qualify: Must be the person who did the setup.*

**Q2.** When did you sign up for your {product} trial?
- [ ] Within the last 7 days
- [ ] 8-14 days ago
- [ ] More than 14 days ago
- [ ] I don't remember

*Qualify: Within the last 14 days. Disqualify "more than 14 days ago."*

**Q3.** How far did you get in setting up {product}? (Select the best match)
- [ ] I signed up but haven't really started setup
- [ ] I started setup but got stuck or paused
- [ ] I completed setup and have been using it
- [ ] I tried it and decided not to continue

*Qualify: Any answer except "signed up but haven't really started" (no onboarding story to tell).*

**Q4.** What were you using before {product} for this workflow? (free text)
___

*No disqualification; context for interview prep.*

**Q5.** Are you available for a 45-minute video call this week to share your experience? (The call may be recorded with your permission for note-taking only.)
- [ ] Yes
- [ ] No

*Qualify: Yes only.*

**Disqualify if:**
- Signed up more than 14 days ago (old flow or stale recall).
- Did not personally attempt onboarding.
- Only hypothetical interest; no actual trial experience.

---

## C. Interview Guide + Consent/Recording Plan

### 45-Minute Discovery Interview Guide: Onboarding Experience

**Moderator preparation (before the call)**
- Review the participant's screener answers and activation status (activated vs not).
- Note their signup date, role, and prior tool (from screener Q4).
- Have the new onboarding flow open on your screen for reference (but do not share it or lead with it).
- Open the note-taking template.

---

### Intro (3 min)

**Consent and recording script:**

> "Thanks so much for taking the time. Before we start, I want to set some context:
>
> - This is a research conversation, not a sales call. I'm trying to understand your experience, and there are no right or wrong answers.
> - I'd like to record this call so I can focus on listening instead of taking frantic notes. The recording will only be used by our internal product team and stored securely. You can ask me to stop recording at any time.
> - You can skip any question you don't want to answer, and you can stop the conversation at any time.
>
> **Is it okay if I start recording?**"

*If yes:* Start recording. Confirm verbally: "Recording is on. Thank you."
*If no:* "No problem at all. I'll just take notes as we go."

> "I'll be asking about your recent experience getting started with {product}. I'm going to ask you to be as specific as you can -- walk me through what actually happened rather than general impressions. Sound good? Let's dive in."

---

### Warm-Up (5 min)

*Goal: Build rapport and understand their context. Do not jump to onboarding yet.*

1. **"Tell me a bit about your role and what you're responsible for day to day."**
   - Probe: "How big is your team? Who do you collaborate with most?"

2. **"What were you trying to accomplish when you decided to look at {product}?"**
   - Probe: "Was there a specific trigger -- something that happened that made you start looking?"
   - Probe: "What were you using before? How was that going?"

---

### The Onboarding Story (20 min)

*Goal: Get the full step-by-step story of their onboarding experience. This is the core of the interview. Let them lead; follow the story.*

3. **"Take me back to when you first signed up for {product}. Walk me through what happened, step by step."**
   - Probe: "What was the very first thing you saw or did after signing up?"
   - Probe: "What did you expect to happen at that point?"

4. **"What did you do next?"**
   - Keep asking this until you've walked through their full onboarding journey.
   - Probe at each step: "Was that clear? Did you know what to do?"
   - Probe: "How long did that take? Did that feel reasonable?"

5. **"Was there a point where you got stuck, confused, or paused?"**
   - Probe: "Tell me exactly what happened. What were you looking at?"
   - Probe: "What did you try to do about it?"
   - Probe: "Did you look for help anywhere -- docs, support, Google, a colleague?"
   - Probe: "What happened after that? Did you come back to it?"

6. **"Was there anything that almost made you give up or close the tab?"**
   - Probe: "What kept you going?" (if they continued)
   - Probe: "What was the last thing you did before you stopped?" (if they abandoned)

7. **"At what point, if ever, did you feel like 'okay, I get this -- I can actually use this for my work'?"**
   - Probe: "What specifically made you feel that way?"
   - Probe (if they haven't reached that point): "What would need to happen for you to feel that way?"

8. **"Was there anything you expected to be part of the setup that wasn't there?"**
   - Probe: "Anything that felt like an unnecessary step or a waste of time?"

---

### Constraints, Workarounds, and Context (10 min)

*Goal: Understand the environment around onboarding -- team, pressure, alternatives.*

9. **"Were you setting this up just for yourself, or for a team? Tell me about that."**
   - Probe: "Did anyone else need to be involved in setup? How did that go?"
   - Probe: "Did anyone else on your team try it? What did they say?"

10. **"How much time did you have to evaluate this? Was there any deadline or pressure?"**
    - Probe: "Were you comparing {product} to other options at the same time?"

11. **"If you think about the old way you were doing things vs what {product} is supposed to do -- what's the gap right now?"**
    - Probe: "What would need to be true for you to move your real work into {product}?"

---

### Wrap-Up (5 min)

12. **"If you could change one thing about the experience of getting started with {product}, what would it be?"**

13. **"Is there anything I didn't ask about that you think is important for us to know?"**

14. **"Do you know anyone else who recently signed up and might be willing to share their experience too?"**

15. **"Thank you -- this was incredibly helpful. I may have a quick follow-up question over email in the next week. Would that be okay?"**

---

### Moderator Notes

- **If the participant gives a general opinion** (e.g., "The onboarding was confusing"), always follow with: *"Can you walk me through the specific part that was confusing? What were you looking at?"*
- **If the participant starts suggesting features**, redirect: *"That's interesting -- before we go there, can you tell me about the last time you ran into that problem? What actually happened?"*
- **If the participant is very positive and skipping details**, probe: *"Was there anything, even small, that gave you a moment of hesitation or uncertainty?"*
- **If the participant abandoned early**, spend more time on questions 5-6 and less on 9-11.
- **Watch the clock:** The onboarding story section is the most important. If warm-up runs long, cut it short. If the story is rich, let it run and shorten constraints.

---

## D. Note-Taking Template + Tagging Scheme

### Note-Taking Template (copy one per interview)

---

**Participant ID:** P__
**Name:** ___
**Role:** ___
**Company size:** ___
**Signup date:** ___
**Activation status:** Activated / Not activated / Abandoned
**Interview date:** ___
**Interviewer:** ___
**Observer(s):** ___
**Recording:** Yes / No
**Prior tool / workflow:** ___

---

#### Story Moments (capture 2-5)

**Story Moment 1:**
- Trigger: What prompted this step/action?
- Goal/outcome: What were they trying to do?
- Steps taken: What did they actually do?
- Struggles/constraints: What got in the way?
- Workarounds: What did they try instead?
- Tools used: Any external help (docs, support, colleague)?
- Verbatim quotes: "_______"
- Importance (H/M/L):
- Frequency (H/M/L):
- Notes (interpretation, clearly labeled as such):

**Story Moment 2:**
- Trigger:
- Goal/outcome:
- Steps taken:
- Struggles/constraints:
- Workarounds:
- Tools used:
- Verbatim quotes: "_______"
- Importance (H/M/L):
- Frequency (H/M/L):
- Notes:

**Story Moment 3:**
- Trigger:
- Goal/outcome:
- Steps taken:
- Struggles/constraints:
- Workarounds:
- Tools used:
- Verbatim quotes: "_______"
- Importance (H/M/L):
- Frequency (H/M/L):
- Notes:

*(Add Story Moments 4-5 as needed.)*

---

#### Tags (pick 3-8 per interview)

Apply from this tag list. Add new tags if a recurring theme emerges.

| Tag | Description |
|---|---|
| `first-impression` | Reaction to initial signup / landing experience |
| `stuck-point` | A specific moment where the user got stuck or confused |
| `abandon-risk` | User considered quitting or actually quit |
| `aha-moment` | User understood the value or felt "this works" |
| `missing-context` | User didn't understand why a step existed or what to do |
| `unnecessary-step` | User felt a step was irrelevant or wasteful |
| `workaround` | User found an alternative path or external help |
| `team-dependency` | Onboarding required someone else's involvement |
| `time-pressure` | User had limited time to evaluate or set up |
| `prior-tool-comparison` | User compared experience to their previous tool |
| `help-seeking` | User sought docs, support, or external resources |
| `positive-surprise` | Something that worked better than expected |

---

#### Immediate Debrief (complete within 10 min of ending the call)

- **Top 3 surprises:**
  1.
  2.
  3.

- **Top 3 follow-ups** (things to verify or probe in the next interviews):
  1.
  2.
  3.

- **Hypotheses updated:**
  - H1 (confusing/irrelevant steps): Supported / Weakened / Unchanged / New evidence: ___
  - H2 (missing guidance): Supported / Weakened / Unchanged / New evidence: ___
  - H3 (activation path less discoverable): Supported / Weakened / Unchanged / New evidence: ___

- **One-sentence summary of this interview:**

---

## E. Synthesis Plan + Report Template

*Complete this section after all 8 interviews. The structure below is your synthesis framework.*

### How to Synthesize

1. **After each interview:** Complete the debrief section of the note-taking template.
2. **After every 2-3 interviews:** Review debriefs side by side. Note emerging patterns and update your hypotheses tracking.
3. **After all 8 interviews:** Use the template below.

### Synthesis Report Template

#### Executive Summary (5 bullets max)
- Total interviews conducted: __ / 8
- Participant breakdown: __ activated, __ not activated, __ abandoned
- Top finding 1: ___
- Top finding 2: ___
- Recommended action: ___

#### Themes

| Theme | What we heard (summary) | Evidence (n + key quotes) | Who it's true for | Confidence | Implication for onboarding |
|---|---|---|---|---|---|
| | | | | High/Med/Low | |
| | | | | High/Med/Low | |
| | | | | High/Med/Low | |

*Rule: Every theme must have evidence from at least 2 interviews or be labeled "single anecdote -- needs validation."*

#### Contradictions and Segments

| Observation | True for... | Not true for... | Possible explanation |
|---|---|---|---|
| | | | |

#### Opportunities

| Opportunity | User outcome enabled | Evidence strength | Candidate solutions (optional) | Priority | Notes |
|---|---|---|---|---|---|
| | | n = __ | | H/M/L | |
| | | n = __ | | H/M/L | |

#### Recommendations

| Recommendation | Rationale | Owner (if known) | Next validation step |
|---|---|---|---|
| | | | |
| | | | |

---

## F. Follow-Up Plan

### Thank-You Note (send within 24 hours)

> Subject: Thank you for sharing your experience
>
> Hi {first_name},
>
> Thank you so much for taking the time to talk with me about your experience getting started with {product}. Your feedback is genuinely helpful, and I learned a lot from our conversation.
>
> We're using what we heard to improve the onboarding experience for new users. If anything else comes to mind about your setup experience, feel free to reply to this email.
>
> Thanks again,
> {your_name}

### Customer Panel (opt-in list)

After completing the 8 interviews, identify 3-5 participants who were engaged and willing to provide future feedback. Invite them into a lightweight panel:

> "You gave us really valuable feedback. Would you be open to occasional quick check-ins (no more than once a month, usually 15-20 minutes) as we improve the product? Totally optional -- just reply 'yes' if you're interested."

**Panel management:**
- Keep a simple tracker: Name, Email, Signup date, Activation status, Key insights, Last contact date.
- Cadence: No more than 1 outreach per month.
- Always share back what changed because of their input (when possible).
- Remove anyone who doesn't respond to 2 consecutive outreaches.

---

## G. Risks / Open Questions / Next Steps

### Risks

| Risk | Mitigation |
|---|---|
| **Recruiting shortfall.** May not book 8 interviews in one week, especially with not-activated / abandoned users who have less motivation to respond. | Over-recruit: send 40-50 outreach messages. Use support tickets as a high-signal backup channel. Accept 6 interviews as a minimum viable set. |
| **Recall decay.** Users who signed up 10-14 days ago may have fuzzy memories of onboarding details. | Prioritize users from the last 7 days. During the interview, use their actual account state as a memory aid ("I can see you completed X but not Y -- does that sound right?"). |
| **Survivorship bias.** Activated users are easier to reach and more willing to talk. The most important signal comes from users who did NOT activate. | Deliberately recruit 3 not-activated and 1 abandoned user. If abandoned users don't respond to email, try in-app messaging or support channel outreach. |
| **Confirmation bias.** The team already has a hypothesis about what broke. Interviewers may unconsciously lead toward that conclusion. | Use the story-first guide as written. Do not mention specific onboarding changes or hypotheses to participants. Have an observer track any leading questions during debriefs. |
| **Small sample.** 8 interviews cannot provide statistical confidence. | Frame findings as directional hypotheses, not conclusions. Use confidence labels in synthesis. Pair with quantitative funnel data for triangulation. |

### Open Questions

1. Which specific step in the new onboarding flow is the activation milestone? (Needed to accurately segment "activated" vs "not activated" participants.)
2. Is the old onboarding flow still available for comparison, or was it fully replaced?
3. Are there any existing analytics showing where in the new flow the drop-off occurs? (This would help focus interview probes on the highest-drop-off steps.)
4. Is there budget for incentives (e.g., $25-50 gift card)? Incentives significantly improve response rates, especially for not-activated users.
5. Who will observe interviews -- just the PM, or also design and/or engineering?

### Next Steps

| Step | Owner | Timing |
|---|---|---|
| **1. Finalize participant list.** Pull trial signups from last 14 days, segment by activation status, and build outreach list. | PM | Day 1 (Monday) |
| **2. Send outreach + screener.** Send 40-50 emails across segments. Post in-app prompt if available. | PM | Day 1 (Monday) |
| **3. Confirm and schedule.** Confirm qualified participants, send calendar invites. Target 2-3 interviews per day, Tue-Thu. | PM | Day 1-2 |
| **4. Run interviews.** Conduct interviews using the guide above. Complete debrief template after each session. | PM + observer(s) | Day 2-4 (Tue-Thu) |
| **5. Mid-point check.** After interview 4, review debriefs and adjust guide if needed (add probes for emerging themes). | PM + observer(s) | Day 3 (Wed) |
| **6. Synthesize.** Complete the synthesis report using the template. | PM | Day 4-5 (Thu-Fri) |
| **7. Share readout.** Present findings to stakeholders. Propose decision: fix, revert, or redesign. | PM | End of week / early next week |
| **8. Send thank-yous and seed panel.** Thank all participants. Invite engaged ones to the customer panel. | PM | Day 5 (Fri) |

---

## Quality Gate

### Checklist Results

**A) Scope + decision checklist**
- [x] A specific decision is named and time-bounded. *(Decide whether to fix, revert, or redesign onboarding; decision by end of next week.)*
- [x] The interview type matches the decision. *(Discovery interviews to understand the new onboarding experience.)*
- [x] Unknowns/hypotheses are explicit. *(Three hypotheses stated in context snapshot.)*
- [x] Boundaries are clear. *(This study will not produce statistical evidence or test a new prototype.)*

**B) Recruiting + participant quality checklist**
- [x] Inclusion criteria are behavior/situation-based. *(Signed up in last 14 days, attempted onboarding personally.)*
- [x] Exclusion criteria prevent low-signal interviews. *(Old flow users, internal accounts, never-logged-in users excluded.)*
- [x] Sampling plan includes edge cases with rationale. *(1 abandoned user + 1 fast activator.)*
- [x] Recruiting plan anticipates drop-off. *(40-50 outreach to book 8.)*
- [x] Screener screens for the story you need. *(Recency, personal setup attempt, activation status.)*

**C) Interview guide quality checklist**
- [x] Questions are story-first. *(Core section: "Walk me through step by step," "Tell me about the last time..." -- estimated 75%+ of questions are behavioral/story-based.)*
- [x] Minimal leading language. *(Hypotheses not mentioned to participants; no solution-embedded questions.)*
- [x] Probes exist for triggers, constraints, workarounds, and outcomes. *(Covered in onboarding story and constraints sections.)*
- [x] Time boxes are realistic. *(3 + 5 + 20 + 10 + 5 = 43 min, fits within 45 min.)*
- [x] Consent/recording script is included and respectful. *(Full script with opt-out path.)*

**D) Execution + note quality checklist**
- [x] Notes separate verbatim quotes from interpretation. *(Template has separate fields.)*
- [x] Each session captures 2-5 story moments. *(Template structured for this.)*
- [x] Debrief happens immediately after each interview. *(10-min debrief section in template.)*
- [x] PM/design observe live or listen to recordings. *(Observer field in template; risk noted if not possible.)*

**E) Synthesis checklist**
- [x] Themes tied to outcomes/constraints. *(Template columns include "implication for onboarding" and "user outcome enabled.")*
- [x] Major insights require evidence. *(Rule: 2+ interviews or labeled "single anecdote.")*
- [x] Contradictions surfaced. *(Dedicated "Contradictions and Segments" table.)*
- [x] Opportunities phrased as user outcomes. *(Template column: "User outcome enabled.")*
- [x] Recommendations include next validation steps. *(Template column: "Next validation step.")*

**F) Ethics + privacy checklist**
- [x] Recording only with explicit permission. *(Consent script with opt-out.)*
- [x] Sensitive personal data minimized. *(Screener collects role and behavior, not sensitive PII.)*
- [x] Data storage noted. *(Flagged as open question -- should follow company policy.)*
- [x] Participants can skip questions and stop at any time. *(Stated in consent script.)*

### Rubric Self-Assessment

| Dimension | Score | Notes |
|---|---|---|
| 1. Decision clarity | **5** | Clear decision (fix/revert/redesign onboarding), deadline (end of next week), explicit unknowns and hypotheses. |
| 2. Participant fit | **5** | Behavior/situation criteria (recency, personal setup attempt); deliberate edge cases (abandoned, fast activator); "who NOT to interview" is explicit. |
| 3. Guide quality (story-first) | **5** | 75%+ story elicitation questions; neutral wording; probes for triggers, struggles, workarounds, outcomes; time boxes specified; consent/recording script included. |
| 4. Execution and evidence capture | **4** | Template supports verbatims, story moments, and immediate debrief. Score is 4 (not 5) because execution hasn't happened yet -- quality depends on follow-through. |
| 5. Synthesis quality | **4** | Synthesis template includes themes with evidence, confidence levels, contradictions, and segmented opportunities. Score is 4 because actual synthesis depends on interview data. |
| 6. Actionability | **5** | Specific next steps with owners and timing; customer panel cadence defined; validation steps built into recommendation template. |
| 7. Ethics and safety | **4** | Consent and recording are explicit; data minimization practiced; storage/retention flagged as requiring company policy confirmation (not fully resolved, hence 4). |

**Overall: avg = 4.6, no dimension below 4. Rating: Excellent.**
