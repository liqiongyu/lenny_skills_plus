# Survey Pack: Onboarding Profiling for B2B Analytics Tool

---

## A) Context Snapshot

- **Decision to inform (by date):** Route new signups to the correct onboarding path (self-serve individual vs. team/buyer track) and suppress sales outreach to non-buyers. Decision is operational and continuous -- routing logic should be live as soon as the survey is validated (target: within 2 weeks of pilot completion).
- **Survey type:** Onboarding profiling (buyer vs. user segmentation).
- **Primary audience:** All new signups, triggered during their first in-product session.
- **Distribution channel:** In-product modal / inline flow during first session (post-signup, pre-core-experience).
- **Constraints:**
  - Completion time: under 2 minutes (~4-5 questions, 3-4 screens).
  - No PII beyond what registration already collects (name, email, company domain).
  - Must not block core product experience -- users can skip, but routing defaults to "self-serve individual" if skipped.
- **Known context / existing evidence:** Sales team is contacting signups who are individual contributors with no purchasing authority, wasting outbound capacity and annoying users. No existing profiling mechanism beyond email domain.

---

## B) Survey Brief

- **Goal:** Classify every new signup into one of three routing segments -- (1) Individual IC / self-serve user, (2) Team evaluator / buyer, (3) Enterprise decision-maker -- so that onboarding content is personalized and sales only contacts segments 2 and 3.
- **Hypotheses / unknowns:**
  - H1: A meaningful share of signups are individual ICs who will never buy a team plan; sales outreach to them is wasted.
  - H2: Four profile signals (role, company size, use case, buying intent) are sufficient to separate buyer from user.
  - Unknown: What is the actual segment split? (This survey will establish the baseline.)
- **Target population:** 100% of new signups (census, not sample).
- **Sampling frame:** Triggered automatically for every new account during first session.
- **Segment cuts (must-have comparisons):**
  - Buyer vs. user (evaluating for team vs. self)
  - Company size tier (1-10, 11-100, 101-500, 500+)
  - Role category (analyst/data, engineering, product/PM, leadership/exec, other)
- **Timing + cadence:** Always-on (every new signup). Review routing accuracy quarterly.
- **Incentive:** None. Value exchange is "we'll personalize your experience."
- **Success criteria:**
  - Completion rate >= 75% of new signups (since it's in-product and short).
  - Routing accuracy: >= 85% of users routed to the correct onboarding path (validated by checking a sample after 30 days).
  - Sales qualification: reduction in sales outreach to non-buyers by >= 50% within first month.
- **Data/privacy notes:** No new PII collected beyond role/company size/use case (non-sensitive firmographic data). Responses stored with account record. Standard product privacy policy applies.

---

## C) Questionnaire

| ID | Section | Question | Type | Options / Scale | Required | Logic | Rationale |
|---:|---|---|---|---|:---:|---|---|
| Q01 | Profile | What best describes your role? | single_choice | Data Analyst / Data Scientist; Data Engineer / Analytics Engineer; Product Manager; Engineering Manager / Director; VP / C-level Executive; Other (please specify) | Y | -- | Determines onboarding content track and signals seniority for sales routing. Leadership/exec roles correlate with buying authority. |
| Q02 | Profile | How large is your company? | single_choice | Just me (freelancer/solo); 2-10 employees; 11-100 employees; 101-500 employees; 500+ employees | Y | -- | Company size is the strongest predictor of team-plan fit and sales-worthiness. Solo/small = self-serve; 101+ = sales-assisted. |
| Q03 | Profile | What will you primarily use [Product] for? | single_choice | Ad-hoc data exploration; Dashboards & reporting for my team; Embedded analytics for customers; Data pipeline monitoring; Other (please specify) | Y | -- | Personalizes onboarding path (e.g., show dashboard templates vs. SQL editor). Also signals product-led vs. sales-led use case. |
| Q04 | Profile | Are you evaluating [Product] for yourself or for a team? | single_choice | Just for myself; For my team (2-10 people); For my department or organization (10+ people) | Y | -- | The core buyer-vs-user signal. "For my team/org" triggers sales routing; "just myself" suppresses outbound. |
| Q05 | Profile | Anything else we should know to get you started? | open_text | Free text (optional, max 200 chars) | N | -- | Catches edge cases (e.g., "migrating from Looker", "need SSO") that can trigger targeted onboarding nudges or sales context. |

**Estimated completion time:** 45-75 seconds (4 required taps + 1 optional text field across 2-3 screens).

**Question design notes:**
- All required questions are single-choice with 5-6 options to keep tap count low.
- "Other (please specify)" included on Q01 and Q03 to avoid forced misclassification.
- Q05 is optional and placed last -- it adds richness without increasing abandonment.
- No double-barreled questions. Each question captures a single dimension.
- No satisfaction/opinion questions -- this is pure profiling.

---

## D) Survey Instrument Table (Implementation-Ready)

```
id,section,question,type,options,required,logic,notes
Q01,Profile,What best describes your role?,single_choice,"Data Analyst / Data Scientist|Data Engineer / Analytics Engineer|Product Manager|Engineering Manager / Director|VP / C-level Executive|Other (please specify)",Y,,Freetext field appears if "Other" selected. Randomize first 5 options to reduce order bias.
Q02,Profile,How large is your company?,single_choice,"Just me (freelancer/solo)|2-10 employees|11-100 employees|101-500 employees|500+ employees",Y,,Do NOT randomize -- options are ordinal. Display vertically.
Q03,Profile,What will you primarily use [Product] for?,single_choice,"Ad-hoc data exploration|Dashboards & reporting for my team|Embedded analytics for customers|Data pipeline monitoring|Other (please specify)",Y,,Freetext field appears if "Other" selected. Randomize first 4 options.
Q04,Profile,Are you evaluating [Product] for yourself or for a team?,single_choice,"Just for myself|For my team (2-10 people)|For my department or organization (10+ people)",Y,,Do NOT randomize -- options are ordinal by scope. This is the primary routing signal.
Q05,Profile,Anything else we should know to get you started?,open_text,"max 200 chars",N,,Optional. Display as single-line input or small textarea.
```

**Screen layout recommendation (3 screens):**
- Screen 1: Q01 + Q02 (role + company size)
- Screen 2: Q03 + Q04 (use case + buying intent)
- Screen 3: Q05 (optional open text + "Get Started" CTA)

**QA checklist items (instrument-specific):**
- [x] All options visible without scrolling on mobile (max 6 options per question, vertical layout).
- [x] Required questions are minimal (4 of 5 required; all are essential for routing).
- [x] Skip logic: none needed (all questions shown to all users; Q05 is optional by design).
- [x] "Other (please specify)" on Q01 and Q03 to capture roles/use cases not listed.
- [x] Randomize non-ordinal option lists (Q01, Q03) to reduce primacy bias.
- [x] Do NOT randomize ordinal lists (Q02 company size, Q04 evaluation scope).

---

## E) Analysis + Reporting Plan

### Primary metric(s)
- **Segment distribution:** % of new signups in each routing segment (Individual IC / Team Evaluator / Enterprise Decision-Maker).
- **Completion rate:** % of new signups who complete the survey vs. skip.
- **Routing accuracy:** % of users correctly routed (validated via 30-day follow-up sample).

### Routing logic (the core output)

| Q04 Answer | Q02 Answer | Routing Segment | Onboarding Path | Sales Action |
|---|---|---|---|---|
| Just for myself | Any | Individual IC | Self-serve onboarding (templates, quick-start guide) | No outbound. Nurture via product emails only. |
| For my team (2-10) | 2-10 or 11-100 | Team Evaluator (SMB) | Team onboarding (invite flow, shared dashboards) | Light-touch: automated email sequence with team-plan info. No phone. |
| For my team (2-10) | 101-500 or 500+ | Team Evaluator (Mid-Market) | Team onboarding + admin setup | Sales-qualified: route to SDR for follow-up within 48h. |
| For my department/org (10+) | Any | Enterprise Decision-Maker | White-glove onboarding (dedicated setup call offer) | High-priority: route to AE for follow-up within 24h. |

### Segment cuts (predefined)
1. **Buyer vs. user** (Q04): Primary cut. Report weekly.
2. **Company size tier** (Q02): Cross-tab with Q04 to refine sales routing thresholds.
3. **Role** (Q01): Identify which roles skew buyer vs. user; adjust onboarding content per role.
4. **Use case** (Q03): Identify which use cases correlate with team/enterprise adoption.

### Open-ended coding plan (Q05)
- **Tag list v0 (12 tags):** migration-from-competitor, need-SSO/security, need-integrations, evaluating-multiple-tools, specific-use-case-request, onboarding-help, pricing-question, team-setup-help, API-access, data-source-question, timeline-pressure, other.
- **Coding rules:** Apply 1-2 tags per response. Code weekly in batches. New tags added if >5 responses don't fit existing tags.
- **Output:** Top themes by segment; surface any high-frequency requests to product and sales teams.

### Decision thresholds
- **If > 40% of signups are "Just for myself":** Validates the hypothesis that sales is over-contacting. Confirm self-serve onboarding path is robust.
- **If "For my team/org" signups have < 20% sales follow-up conversion:** Tighten routing -- add a secondary qualifying signal (e.g., company size threshold) before routing to sales.
- **If completion rate < 60%:** Shorten survey further (consider removing Q05 or combining Q01+Q03). Test whether the modal is too intrusive.
- **If a single role (Q01) dominates > 60%:** Consider splitting that role into sub-roles for more precise onboarding.

### Reporting
- **Format:** Weekly automated dashboard (segment distribution, completion rate, skip rate) + monthly memo with routing accuracy review.
- **Audience:** Product team (onboarding optimization), Sales ops (routing rules), Growth team (conversion by segment).
- **Decisions to capture:** Any routing rule changes, onboarding path updates, sales threshold adjustments.

---

## F) Launch Plan + QA Checklist

### Pilot plan
- **Who:** Internal team members using test accounts + first 50-100 real signups (1-2 days of traffic).
- **n:** 50-100 real responses.
- **What you're looking for:**
  - Completion rate (target >= 75%).
  - Drop-off by screen (any screen with > 15% drop-off needs review).
  - Time to complete (target < 2 minutes; flag if median > 90 seconds).
  - Option coverage: are > 10% of respondents choosing "Other" on any question? If so, add a missing option.
  - Q05 response quality: are free-text responses useful or mostly empty/noise?
- **Changes after pilot:** Adjust option lists, wording, or screen layout based on findings. Remove Q05 if it adds no value.

### Launch schedule
- **Pilot start:** Day 1 (internal) + Day 2-3 (first 50-100 real signups).
- **Review pilot:** Day 4.
- **Full launch:** Day 5 (all new signups).
- **First routing accuracy review:** Day 35 (30 days post-launch).

### Reminder plan
- No reminders needed. The survey is in-product during first session. If a user skips, they are routed to the default path (self-serve individual). Consider a gentle re-prompt on second session if skipped, but do not nag.

### Monitoring plan
- **Response rate target:** >= 75% of new signups complete the survey.
- **Completion rate target:** >= 90% of those who start complete all required questions.
- **Drop-off watchpoints:** Screen 2 (Q03 + Q04) -- if drop-off > 15%, simplify.
- **Segment mix watchpoints:** If > 80% fall into a single segment, investigate whether the questions are differentiating effectively.

### Close the loop
- **What respondents will hear back:** Personalized onboarding experience (immediate). "Based on your answers, here's your recommended setup..." (shown right after survey completion).
- **When:** Immediately upon completion (onboarding path loads based on responses).
- **Channel:** In-product (the onboarding flow itself is the "close the loop").

---

## G) Risks / Open Questions / Next Steps

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Low completion rate if modal feels intrusive | Medium | High -- missing data means default routing, sales still contacts non-buyers | Frame as "personalize your experience" (value exchange), not "tell us about yourself." Keep to 3 screens. Allow skip with sensible default. |
| "Other" responses dominate Q01 or Q03, reducing routing signal quality | Low-Medium | Medium -- weakens automated routing | Monitor "Other" % in pilot. If > 15%, add missing options. Code free-text "Other" responses weekly to identify new categories. |
| Users game responses (e.g., say "just for myself" to avoid sales contact) | Low | Medium -- undercount buyers | Cross-validate with behavioral signals post-onboarding (e.g., user invites teammates within 14 days despite saying "just myself"). Flag mismatches for manual review. |
| Routing rules are too coarse -- some Team Evaluators at small companies don't want sales outreach | Medium | Low-Medium -- minor annoyance | Start with light-touch (email only) for SMB team evaluators. Escalate to phone only for mid-market+ or explicit request. |
| Survey fatigue if combined with other in-product prompts | Low | Medium | Coordinate with other in-product messaging. This survey replaces any generic "welcome" modal, not added on top. |

### Open Questions

1. **What user attributes are available at signup?** If company size or role is already captured during registration, remove the redundant question from the survey and use the existing data.
2. **What is the current signup volume?** Needed to estimate how quickly we'll reach statistical confidence on segment splits and routing accuracy.
3. **Are there compliance/legal requirements for storing profiling data?** Standard product privacy policy likely covers this, but confirm with legal if the data will be shared with third-party sales tools.
4. **What is the current sales outreach process?** Understanding the existing SDR workflow will help define the routing handoff (e.g., auto-create lead in CRM vs. manual list).
5. **Are there existing onboarding paths, or are we building them?** The survey design assumes at least 2-3 distinct onboarding paths exist or will be built concurrently.

### Next Steps

1. **Validate routing logic with Sales and Product.** Share the routing table (Section E) with sales ops and product team. Confirm segment definitions and outreach rules before building.
2. **Build the survey in your in-product survey tool** (e.g., Appcues, Chameleon, Pendo, or custom). Use the instrument table (Section D) as the spec.
3. **Run the pilot** (50-100 signups). Review completion rate, drop-off, option coverage, and time-to-complete.
4. **Adjust and launch.** Refine wording/options based on pilot data. Go live for all new signups.
5. **30-day routing accuracy review.** Sample 50-100 users from each segment. Check whether their actual behavior (e.g., invited teammates, purchased, stayed individual) matches their survey-assigned segment. Adjust routing thresholds if accuracy < 85%.
6. **Quarterly review cadence.** Re-examine segment distribution, routing accuracy, and completion rate. Update option lists as the product and user base evolve.

---

## Quality Gate

### Checklist Results

**A) Decision + scope**
- [x] A specific decision is named and time-bounded.
- [x] The survey has one primary goal (route signups + suppress non-buyer outreach).
- [x] Every question maps to a decision, hypothesis, or segment cut.
- [x] Clear boundary: this survey does NOT measure satisfaction, friction, or feature requests.

**B) Audience + sampling**
- [x] Primary audience defined (all new signups, first session).
- [x] Sampling frame is realistic (census -- 100% of signups, in-product trigger).
- [x] Segment cuts are explicit (buyer vs. user, company size, role).
- [x] Plan for low response rate (skip defaults to self-serve; re-prompt on second session considered).
- [N/A] Recall not relevant (profiling current state, not past experience).

**C) Measurement + question quality**
- [x] Core "metric" is segment classification, not a score -- appropriate for profiling.
- [N/A] Scales not used (all single-choice profiling questions).
- [N/A] NPS not used.
- [N/A] Forced ranking not used (profiling, not diagnostics).
- [x] No double-barreled questions; no leading language; no jargon.
- [x] Completion time within target (< 2 minutes).

**D) Instrument QA (mobile + logic + bias)**
- [x] All options visible on mobile (max 6 options, vertical layout).
- [x] Required questions are minimal and justified (4 of 5).
- [x] No skip logic needed (all questions shown to all users).
- [N/A] "Not applicable" not needed (all questions apply to all signups).
- [x] "Other (please specify)" on Q01 and Q03.
- [x] Option randomization on non-ordinal lists (Q01, Q03).

**E) Launch + operations**
- [x] Pilot plan exists (50-100 signups, clear review criteria).
- [x] Launch schedule defined.
- [x] Monitoring plan: completion rate, drop-off, segment mix.
- [x] Close-the-loop: personalized onboarding experience loaded immediately.

**F) Analysis + reporting**
- [x] Segment cuts predefined (buyer/user, company size, role, use case).
- [x] Open-ended coding plan for Q05 (12-tag list + rules).
- [x] Decision thresholds defined (completion rate, segment distribution, routing accuracy).
- [x] Reporting format chosen (weekly dashboard + monthly memo).
- [x] Insights translate to actions (routing rule updates, onboarding path changes).

**G) Privacy + ethics**
- [x] Data minimization: only collecting role, company size, use case, evaluation scope.
- [x] No sensitive PII beyond registration data.
- [x] Consent: standard product privacy policy applies.
- [ ] Storage/retention policy: flagged as open question for legal confirmation.

### Rubric Scores

| Dimension | Score | Notes |
|---|:---:|---|
| 1) Decision clarity | 5 | Clear decision (route signups, suppress non-buyer outreach), continuous operational deadline, explicit "what we'll do if..." scenarios for each result range. |
| 2) Audience + sampling quality | 5 | Census of all new signups (no sampling bias); segment cuts planned; skip-default behavior documented; response rate target set. |
| 3) Measurement design | 4 | Profiling survey -- classification rather than metric. Routing logic is well-defined. Slight gap: no secondary behavioral validation signal built into the instrument itself (addressed in risks). |
| 4) Questionnaire quality | 5 | Neutral, single-concept questions; consistent format; < 2 min completion; "Other" options included; randomization specified. |
| 5) Instrument QA | 4 | Mobile layout specified; randomization rules set; pilot planned with clear criteria. Not yet tested on actual devices (pending implementation). |
| 6) Analysis + reporting plan | 5 | Routing logic table, predefined cuts, open-ended coding plan, decision thresholds, weekly + monthly reporting cadence. |
| 7) Actionability + close-the-loop | 5 | Immediate personalized onboarding as the close-the-loop mechanism; routing feeds directly into sales ops workflow; quarterly review cadence with clear owners. |
| 8) Privacy + ethics | 4 | Data minimization practiced; no sensitive PII; consent via standard policy. Retention policy flagged as open question. |

**Overall: 4.6 average, no dimension below 4 -- Excellent.**
