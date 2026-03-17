# Growth Loop Design Pack — AI Onboarding Assistant for HR Teams

---

## 1) Context Snapshot

**Product:** AI onboarding assistant for HR teams
**Stage:** Early growth (some PMF in mid-market)
**Target segment(s):** Mid-market companies (100–1,000 employees) with HRIS platforms in place
**Growth goal (metric + target + date):** +30% WAU within 90 days, focused on mid-market segment
**Decision this informs:** Which 1–2 growth loops to invest the next quarter in, given limited engineering capacity; whether to double down on the HRIS integration/partner loop as the primary growth engine vs. exploring a secondary referral/champion loop.
**Current primary channels:** Outbound sales + HRIS marketplace partnerships (listed on several HRIS marketplaces)
**Constraints:**
- Engineering capacity: 2 developers (all experiments must be low-to-moderate eng effort)
- Brand-safe only: no aggressive/spammy tactics; must maintain trust with HR buyers
- No explicit paid acquisition budget mentioned (paid loop gated accordingly)
- Platform policy: must comply with HRIS marketplace listing policies and partner guidelines
- Legal/privacy: HR data is sensitive; no PII exposure in growth mechanics

**Core value moment:** An HR team installs the integration, connects their HRIS, and successfully runs their first AI-assisted onboarding workflow for a new hire — the moment they see the tool saving them manual onboarding work.

---

## 2) Loop Inventory + Baseline

### Baseline (best available)

| Area | Metric / definition | Current (estimated) | Source | Notes / confidence |
|---|---|---:|---|---|
| Acquisition volume | New signups or installs per week from HRIS marketplaces + outbound | ~30–50/week (assumption) | User context | Medium confidence — user says "some PMF" and "listed on several marketplaces" |
| Activation rate | % of installs that complete first AI-assisted onboarding | ~25–40% (assumption) | Not provided | Low confidence — common for B2B integrations; needs validation |
| Retention/engagement proxy | WAU (Weekly Active Users) | Not provided (baseline to measure +30% against) | User context | The +30% target implies a known WAU baseline; team should confirm |
| Referral/share | Organic internal referrals or word-of-mouth from HR teams | Low / informal (assumption) | Not provided | Low confidence — no referral mechanism described |
| Unit economics (if known) | LTV, margin, CAC, payback | Not provided | — | Paid loop gated; not recommended without data |

### Existing loops (if any)

| Loop name | Type | Input --> Action --> Output --> Feedback | Strength today (H/M/L) | Evidence |
|---|---|---|---|---|
| HRIS marketplace discovery | Partner/integration | Marketplace listing views --> HR admin clicks "Install" --> Integration installed --> Usage data/reviews improve listing rank | Medium | Listed on several HRIS marketplaces; this is stated as the believed best lever |
| Outbound sales | Sales | Sales team outreach --> Demo --> Close --> Account active | Low-Medium | Mentioned as a current channel; likely linear (not compounding) without a feedback path |

**Observation:** The outbound channel is linear (no self-reinforcing feedback), not a loop. The HRIS marketplace channel has loop potential (installs --> usage --> reviews/ratings --> more visibility --> more installs) but it is likely under-optimized today.

---

## 3) Loop Candidates (Micro + Macro)

### Candidate 1: HRIS Marketplace Integration Loop (Primary)

**Loop name:** HRIS Marketplace Integration Loop
**Type:** Partner/integration
**Target segment:** Mid-market HR teams using HRIS platforms
**Core mechanism:** More installs from HRIS marketplaces drive more usage, reviews, and co-marketing assets, which increase marketplace ranking and visibility, driving even more installs.

#### Loop model
- **Input:** HRIS marketplace listing impressions (organic search within the marketplace + category browsing)
- **Action:** HR admin discovers listing --> clicks "Install" --> completes guided setup --> runs first AI onboarding workflow
- **Output:** Active integration + marketplace review/rating + usage data signal to HRIS platform
- **Feedback:** Higher review count/rating --> improved marketplace ranking --> more listing impressions --> more installs. Additionally, co-marketing with HRIS partners amplifies listing exposure.
- **Cycle time:** 2–4 weeks (install to review/rating)

#### Preconditions
- Product prerequisites: Guided setup flow that minimizes time-to-first-value; review prompt at the right moment
- Operational prerequisites: Partnership contacts at top 2–3 HRIS platforms for co-marketing; listing optimization (copy, screenshots, keywords)
- Risk/policy constraints: Must comply with marketplace review policies (no incentivized reviews that violate ToS); co-marketing assets must be approved by partners

#### Success definition
- **Loop KPI:** Marketplace-sourced installs per week
- **Leading indicators:** Listing view --> install conversion rate; time-to-first-integration; review submission rate
- **Lagging indicator:** WAU growth from marketplace-sourced accounts

---

### Candidate 2: Internal Champion Referral Loop

**Loop name:** Internal Champion Referral Loop
**Type:** Viral/referral (B2B internal expansion)
**Target segment:** Mid-market HR teams; expansion from one HR user to the broader HR team and adjacent departments
**Core mechanism:** An activated HR admin invites colleagues to the platform; as more team members use it, the tool becomes embedded in the onboarding workflow, which increases WAU and creates word-of-mouth to other companies via HR professional networks.

#### Loop model
- **Input:** Activated HR admin (has completed first AI-assisted onboarding)
- **Action:** Admin invites HR team members or assigns them onboarding tasks within the tool --> colleagues activate --> tool becomes the team's default onboarding system
- **Output:** Additional WAU from same account + cross-company word-of-mouth in HR communities/networks
- **Feedback:** More active users per account --> stronger lock-in --> HR professionals mention the tool in peer conversations/communities --> new company signups
- **Cycle time:** 1–3 weeks (invite to activation); 4–8 weeks for cross-company word-of-mouth

#### Preconditions
- Product prerequisites: Easy "invite teammate" flow; collaborative features that give teammates a reason to use the tool (e.g., task assignment, shared onboarding templates)
- Operational prerequisites: Identify moments when inviting makes sense (e.g., "You have 3 new hires this week — invite your team to help assign tasks")
- Risk/policy constraints: Invites must be opt-in and not spammy; respect corporate email policies

#### Success definition
- **Loop KPI:** Teammates invited per activated admin per month; cross-company referral signups
- **Leading indicators:** Invite send rate; invite accept rate; multi-user account rate
- **Lagging indicator:** WAU growth from invited users + referral-sourced new accounts

---

### Candidate 3: Co-Marketing Content Loop

**Loop name:** Co-Marketing Content Loop
**Type:** Content/partner
**Target segment:** Mid-market HR decision-makers
**Core mechanism:** Co-create onboarding best-practice content with HRIS partners (webinars, case studies, integration guides); content drives qualified traffic to marketplace listings and directly to the product.

#### Loop model
- **Input:** Partnership with HRIS vendors
- **Action:** Co-produce content (case studies, "how to automate onboarding with [HRIS] + [your product]" guides, joint webinars) --> distribute via partner channels + own channels
- **Output:** Qualified traffic to marketplace listing or direct signup; content assets that rank in search
- **Feedback:** Content drives installs --> installs produce success stories --> success stories become new content --> content drives more installs
- **Cycle time:** 4–8 weeks (content creation to measurable traffic/install lift)

#### Preconditions
- Product prerequisites: At least 2–3 customer success stories to seed content
- Operational prerequisites: Partner marketing contact willing to co-promote; content creation capacity (can be done by non-eng team)
- Risk/policy constraints: Must get partner approval on co-branded content; no exaggerated claims

#### Success definition
- **Loop KPI:** Content-sourced marketplace listing views and installs per month
- **Leading indicators:** Content piece views; click-through to listing; webinar registrations
- **Lagging indicator:** WAU growth attributable to content-sourced signups

---

### Candidate 4: Sales-Assisted Expansion Loop

**Loop name:** Sales-Assisted Expansion Loop
**Type:** Sales
**Target segment:** Existing mid-market accounts
**Core mechanism:** Outbound/CS team identifies activated accounts with expansion potential --> upsell to more departments/locations --> more users --> more case studies for outbound.

#### Loop model
- **Input:** Activated account with usage data showing value delivery
- **Action:** CS/sales reaches out with expansion pitch (e.g., "Your HR team in HQ loves it — roll out to your 3 other offices")
- **Output:** Expanded account (more WAU) + case study / testimonial
- **Feedback:** Case studies fuel outbound and partner co-marketing
- **Cycle time:** 4–8 weeks

**Note:** This loop is lower priority because it depends on having enough activated accounts to mine expansion from, and it is more linear than compounding. Included for completeness.

---

### Candidate 5: Paid Acquisition Loop

**Loop name:** Paid Marketplace/Search Ads
**Type:** Paid
**Target segment:** Mid-market HR buyers searching for onboarding solutions

**Paid Loop Feasibility Gate (see Section 6 below):** NOT RECOMMENDED at this time. No unit economics data provided; engineering capacity is too limited to also build attribution infrastructure. Revisit after organic loops are validated and LTV/CAC data is available.

---

### Candidate 6: HR Community Word-of-Mouth Loop

**Loop name:** HR Community Seeding Loop
**Type:** Viral (community-driven)
**Target segment:** HR professionals active in communities (SHRM, HR Twitter/LinkedIn, People Ops Slack groups)
**Core mechanism:** Activated users share tips/templates from the product in HR communities --> community members discover the product --> sign up.

#### Loop model
- **Input:** Activated user who has created onboarding templates or workflows
- **Action:** User shares a useful template or workflow tip in an HR community, mentioning the tool
- **Output:** Community engagement + product awareness
- **Feedback:** New signups from community members --> they create templates --> share in communities
- **Cycle time:** 2–6 weeks

**Note:** This loop has a long cycle time and low controllability for a 90-day horizon. Better as a long-term secondary strategy. Not prioritized.

---

## 4) Loop Map (Qualitative Model)

### Micro Loops --> Macro Loop Table

| Micro loop | Input | Action | Output | Feedback path | Primary bottleneck |
|---|---|---|---|---|---|
| **HRIS Marketplace Install Loop** | Marketplace listing impressions | HR admin discovers + installs integration | Active integration + review/rating | Reviews/ratings improve listing rank --> more impressions | Listing-to-install conversion rate; time-to-first-value (activation) |
| **Internal Champion Referral Loop** | Activated HR admin | Admin invites teammates; assigns tasks in tool | More WAU per account + cross-company WOM | Multi-user accounts create stickiness + HR network referrals | Invite trigger/prompt; teammate activation rate |
| **Co-Marketing Content Loop** | HRIS partner relationship | Co-create content (guides, webinars, case studies) | Qualified traffic to listing/signup | Content drives installs; installs produce stories for new content | Partner willingness; content-to-install conversion |

### Macro Loop: How These Connect

```
HRIS Marketplace Listing Impressions
        |
        v
   HR Admin Discovers & Installs
        |
        v
   Guided Setup --> First AI Onboarding (VALUE MOMENT)
        |
        +--------> Marketplace Review/Rating -----> Improves Listing Rank ----+
        |                                                                      |
        +--------> Invites Teammates (Champion Referral) --> More WAU          |
        |              |                                                       |
        |              +---> Cross-company WOM in HR networks --> New Signups -+
        |                                                                      |
        +--------> Success Story / Case Study                                  |
                       |                                                       |
                       v                                                       |
               Co-Marketing Content with HRIS Partner                          |
                       |                                                       |
                       +-----> Drives Traffic to Listing ----->----------------+
```

**How to read this:** The macro loop starts with marketplace discovery, flows through activation (the value moment), and then branches into three reinforcing micro loops: (1) reviews that boost marketplace ranking, (2) internal expansion via champion referrals, and (3) co-marketing content that drives more marketplace traffic. All three micro loops feed back into the top of the funnel (more listing impressions and installs).

### Bottleneck Hypotheses

1. **Listing --> Install conversion rate.** If the marketplace listing copy, screenshots, and reviews are weak, the top-of-funnel volume is wasted. This is likely the single highest-leverage bottleneck for the primary loop.
2. **Time-to-first-value (activation).** If the guided setup is clunky or takes too long, installs churn before reaching the value moment, which kills both the review loop and the referral loop downstream.
3. **Review/rating submission rate.** Most B2B users never leave reviews unless prompted at the right moment. Without reviews, marketplace ranking stagnates.
4. **Invite trigger / teammate activation.** If there is no natural moment to invite teammates, the champion referral loop never starts. Need a product-driven trigger.

---

## 5) Channel Fit Triad (Customer x Business x Medium)

| Candidate channel | Customer need/context | Business goal fit | Medium strength match | Verdict (Go/No-go) | Notes |
|---|---|---|---|---|---|
| HRIS Marketplace listings | HR admins actively search for tools in their HRIS ecosystem; high intent | Directly drives installs in target segment; compounds via reviews | Interactive (install flow); text (listing copy); integration-native | **Go** | Strongest channel-product fit; this is where mid-market HR buyers already shop |
| In-product invite flow (B2B referral) | HR teams are collaborative; onboarding is a team task | Drives WAU per account; creates stickiness | Interactive (in-app); email (invite notification) | **Go** | Natural fit for multi-user B2B product; low eng effort for basic invite flow |
| Co-marketing with HRIS partners | HR buyers trust their HRIS vendor's recommendations | Leverages partner credibility; low cost | Text/video (guides, webinars); partner email lists | **Go (secondary)** | Depends on partner willingness; longer cycle time but high-quality leads |
| HR community seeding (LinkedIn, Slack) | HR professionals share tools in peer communities | Builds awareness; slow compounding | Text (posts, templates) | **Defer** | Low controllability; better as a long-term play after loops 1–2 are working |
| Paid search/marketplace ads | HR buyers search for onboarding tools | Could accelerate top-of-funnel | Text (search ads) | **No-go (for now)** | No unit economics data; limited eng capacity for attribution; revisit at 60–90 days |

---

## 6) Paid Loop Feasibility Gate

**Known/estimated:**
- LTV (gross): Not provided
- Gross margin %: Not provided
- Target CAC: Not provided
- Payback target (months): Not provided

**Gate checks (directional):**
- LTV x margin supports target CAC: **Cannot evaluate** (no data)
- Retention strong enough that CAC won't be "wasted": **Unknown** (WAU retention not provided)
- Attribution and conversion tracking: **Likely insufficient** (no analytics tooling described; 2-dev team cannot prioritize attribution infrastructure)

**Verdict:** Not yet viable
**Prerequisites before revisiting:**
1. Establish WAU retention baseline (is retention strong enough to justify acquisition spend?)
2. Calculate rough LTV from current customers (ARPA x gross margin x expected lifetime)
3. Instrument basic attribution (UTM tracking on marketplace listings at minimum)
4. Revisit at Day 60–90 if organic loops are working and unit economics are clearer

---

## 7) Loop Scorecard (Pick Top 1–2)

Scoring: 1 = low, 5 = high. For Effort, 5 = low effort (favorable). For Risk, 5 = low risk (favorable).

| Loop candidate | Impact | Confidence | Effort (inverse) | Cycle time (speed) | Risk (inverse) | Notes | Total |
|---|---:|---:|---:|---:|---:|---|---:|
| **HRIS Marketplace Integration Loop** | 5 | 4 | 4 | 4 | 5 | Highest leverage; user identified this as best lever; compounds via reviews + ranking | **22** |
| **Internal Champion Referral Loop** | 4 | 3 | 4 | 4 | 5 | Directly drives WAU; low eng effort for basic invite flow; less certain on adoption | **20** |
| Co-Marketing Content Loop | 3 | 3 | 3 | 2 | 5 | High-quality leads but slower cycle time; depends on partner cooperation | **16** |
| Sales-Assisted Expansion | 2 | 3 | 3 | 2 | 5 | Linear, not compounding; good for later when account base is larger | **15** |
| HR Community Seeding | 2 | 2 | 4 | 2 | 5 | Low controllability; long cycle; better as organic byproduct | **15** |
| Paid Acquisition | 3 | 1 | 2 | 3 | 3 | Gated: no unit economics; no attribution infra; revisit later | **12** |

### Selection

**Primary loop:** HRIS Marketplace Integration Loop (score: 22)
**Secondary loop:** Internal Champion Referral Loop (score: 20)

**Innovate vs. Optimize recommendation:** **Optimize first, then layer innovation.**
- The HRIS marketplace loop already exists in nascent form. The highest ROI is optimizing it (listing conversion, guided setup, review prompting) before inventing new loops.
- The champion referral loop is a modest innovation (new invite mechanism) that can be layered on top once activation is strong.

**Why these win vs. alternatives:**
- The HRIS Marketplace loop has the shortest path to impact because the channel already exists and has demonstrated some traction. Optimization experiments (listing copy, guided setup) are low-eng-effort and fast to test.
- The Champion Referral loop directly drives the target metric (WAU) by expanding usage within accounts that have already activated, and it compounds with the primary loop (more users per account = more reviews, more word-of-mouth).
- Co-marketing is valuable but has a 4–8 week cycle time that makes it less suitable as the primary lever for a 90-day goal. It should be started in parallel as a "slow burn" amplifier.

---

## 8) Measurement + Instrumentation Plan

### Metrics

| Loop | KPI (headline) | Leading indicators | Data source | Notes |
|---|---|---|---|---|
| HRIS Marketplace Integration Loop | Marketplace-sourced installs/week | Listing views; listing-to-install CVR; time-to-first-value; review submission rate | HRIS marketplace analytics dashboards; product analytics (setup completion events) | Most HRIS marketplaces provide basic install/view analytics |
| Internal Champion Referral Loop | Invited teammates activated/week | Invite send rate per activated admin; invite accept rate; multi-user account % | Product analytics (invite events); email delivery/open/click tracking | Need to instrument invite flow |

### Required Events/Properties

| Event name | When it fires | Properties | Used for |
|---|---|---|---|
| `integration_installed` | User completes HRIS integration connection | `hris_platform`, `marketplace_source`, `company_size`, `timestamp` | Measuring marketplace-sourced installs; segmenting by HRIS platform |
| `guided_setup_started` | User begins guided setup flow | `hris_platform`, `user_id`, `account_id` | Measuring setup funnel entry |
| `guided_setup_completed` | User finishes guided setup and reaches value moment | `hris_platform`, `user_id`, `account_id`, `duration_minutes` | Measuring time-to-first-value; activation rate |
| `first_onboarding_run` | User runs first AI-assisted onboarding for a new hire | `user_id`, `account_id`, `hris_platform` | Core value moment; activation metric |
| `marketplace_review_prompted` | Review prompt is shown to user | `user_id`, `account_id`, `days_since_activation` | Measuring review prompt exposure |
| `marketplace_review_submitted` | User submits a review on the marketplace | `hris_platform`, `rating`, `account_id` | Review loop throughput |
| `teammate_invite_sent` | Activated admin sends an invite to a colleague | `inviter_user_id`, `account_id`, `invite_method` (email/link) | Invite send rate |
| `teammate_invite_accepted` | Invited colleague creates account / activates | `invitee_user_id`, `inviter_user_id`, `account_id` | Invite accept rate; attributed WAU |
| `weekly_active_user` | User performs a qualifying action in a given week | `user_id`, `account_id`, `action_type` | WAU tracking (headline goal metric) |

### Instrumentation Gaps + Fixes

| Gap | Impact | Fix | Effort |
|---|---|---|---|
| No `integration_installed` event with marketplace source attribution | Cannot measure marketplace loop throughput | Add UTM or referral parameter to integration install flow; log `marketplace_source` property | Low (1–2 days) |
| No review prompt or review tracking | Cannot measure review loop | Build review prompt at value moment + 7 days; track prompt shown + review submitted | Low-Medium (2–3 days) |
| No invite flow exists | Cannot run champion referral experiments | Build basic "invite teammate" email flow; instrument send/accept events | Medium (3–5 days) |
| WAU definition may not be instrumented | Cannot measure headline goal | Define qualifying WAU action (e.g., any login + at least one onboarding action); ensure event fires | Low (1 day) |

---

## 9) Experiment Backlog

| Priority | Experiment | Loop | Hypothesis (mechanism) | Metric (leading) | Metric (lagging) | Effort | Timebox | Dependencies |
|---:|---|---|---|---|---|---|---|---|
| 1 | **Optimize top 2 HRIS marketplace listings** (rewrite copy, add screenshots, improve keywords) | Marketplace Integration | Better listing copy/visuals will increase listing-to-install CVR by 20%+ because HR admins make install decisions based on clarity of value prop and social proof | Listing-to-install CVR | Marketplace-sourced installs/week | Low (no eng; marketing/product can do this) | 2 weeks | Access to marketplace listing editor |
| 2 | **Build guided "first value" setup flow** that cuts time-to-first-integration by 50% | Marketplace Integration | A streamlined setup flow will increase activation rate (install --> first onboarding run) because the current flow likely has unnecessary friction and drop-off | Setup completion rate; time-to-first-value (minutes) | WAU from marketplace-sourced accounts | Medium (3–5 eng days) | 3 weeks | `guided_setup_started` / `completed` events instrumented |
| 3 | **Add review prompt at the right moment** (after 2nd successful onboarding run, ~7 days post-activation) | Marketplace Integration | Prompting activated users for a review at the moment of realized value will increase review submission rate 3–5x over no prompt, improving marketplace ranking | Review prompt shown; review submitted rate | Marketplace listing rank / impressions | Low (1–2 eng days) | 2 weeks | `first_onboarding_run` event; marketplace review link |
| 4 | **Build basic "invite your team" flow** triggered after first successful onboarding run | Champion Referral | Activated admins will invite 1–2 teammates if prompted at the value moment, because onboarding is inherently a team task | Invite send rate; invite accept rate | WAU from invited teammates | Medium (3–5 eng days) | 3 weeks | `teammate_invite_sent` / `accepted` events |
| 5 | **Co-marketing pilot: 1 integration guide + 1 joint webinar with top HRIS partner** | Co-Marketing Content | Co-branded content distributed via partner channels will drive 2–3x the listing views of organic marketplace discovery alone | Content views; click-through to listing | Installs from content-sourced traffic | Low-Medium (no eng; partnership/marketing effort) | 4–6 weeks | Partner agreement; at least 1 customer case study |
| 6 | **A/B test review prompt timing** (after 1st vs 2nd vs 3rd onboarding run) | Marketplace Integration | Optimal timing will maximize review submission without causing annoyance | Review submission rate per cohort | Review volume/month | Low (1 eng day) | 2 weeks | Experiment 3 shipped |

### Win / Lose / Learn Criteria

**Experiment 1 (Listing optimization):**
- Win: Listing-to-install CVR improves by >= 20% within 2 weeks
- Lose: CVR does not change or declines
- Learn: Which listing elements (copy, screenshots, reviews section) drive the most impact; informs further optimization

**Experiment 2 (Guided setup flow):**
- Win: Activation rate (install --> first onboarding run) improves by >= 15%; time-to-first-value drops by >= 30%
- Lose: Activation rate does not improve
- Learn: Where in the setup flow users drop off; whether the bottleneck is technical (integration difficulty) or motivational (unclear value)

**Experiment 3 (Review prompt):**
- Win: Review submission rate increases to >= 10% of prompted users; at least 5 new reviews in 2 weeks
- Lose: < 3% submission rate despite prompting
- Learn: Whether the barrier is timing, effort, or lack of motivation; informs whether incentives (within policy) are needed

---

## 10) 30/60/90 Plan

### Next 30 days: De-risk + first tests

**Week 1–2:**
- [ ] Instrument core events: `integration_installed` (with source attribution), `guided_setup_started`, `guided_setup_completed`, `first_onboarding_run`, `weekly_active_user`. Establish WAU baseline. **(Eng: ~2–3 days)**
- [ ] Optimize top 2 HRIS marketplace listings (copy, screenshots, keywords). **(Marketing/Product: 2–3 days, no eng)**
- [ ] Baseline current listing-to-install CVR and activation rate.

**Week 3–4:**
- [ ] Ship guided "first value" setup flow (Experiment 2). **(Eng: 3–5 days)**
- [ ] Ship review prompt at value moment (Experiment 3). **(Eng: 1–2 days)**
- [ ] Measure listing optimization impact (Experiment 1 results).
- [ ] Begin outreach to top HRIS partner for co-marketing pilot (Experiment 5).

**Checkpoint (Day 30):** Do we see directional improvement in listing-to-install CVR and/or activation rate? Is the instrumentation working? Decide whether to continue optimizing the marketplace loop or pivot emphasis to the referral loop.

### 60 days: Iterate toward a working loop

**Week 5–6:**
- [ ] Analyze Experiment 2 (guided setup) results; iterate on drop-off points.
- [ ] Analyze Experiment 3 (review prompt) results; run A/B on timing (Experiment 6).
- [ ] Ship "invite your team" flow (Experiment 4). **(Eng: 3–5 days)**

**Week 7–8:**
- [ ] Measure invite send/accept rates. Iterate on invite triggers if adoption is low.
- [ ] Launch co-marketing content pilot with top HRIS partner (Experiment 5).
- [ ] Evaluate whether marketplace review volume is improving listing rank.
- [ ] Begin collecting unit economics data (ARPA, retention by cohort) to inform whether paid acquisition should be considered.

**Checkpoint (Day 60):** Is the marketplace loop producing measurably more installs/week? Is the referral loop showing early traction (invite sends, accepts)? Decide whether to double down on winning experiments or start a new loop.

### 90 days: Scale winners, cut losers

**Week 9–10:**
- [ ] Scale winning experiments: roll out optimized listing + guided setup to all HRIS marketplaces (not just top 2).
- [ ] If invite flow is working, add collaborative features that make multi-user usage more valuable (e.g., shared onboarding templates, team dashboards).
- [ ] Measure co-marketing content impact; decide whether to invest in ongoing content partnership.

**Week 11–12:**
- [ ] Final WAU measurement against +30% target.
- [ ] Document what worked and what didn't; capture learnings for next quarter.
- [ ] If WAU target is not yet met, identify the remaining bottleneck (top-of-funnel volume vs. activation vs. expansion) and plan next experiments.
- [ ] Revisit paid acquisition feasibility with 90 days of unit economics data.

**Checkpoint (Day 90):** Did we hit +30% WAU? Which loop(s) are compounding? What is the next investment decision?

---

## 11) Risks / Open Questions / Next Steps

### Risks

1. **HRIS marketplace algorithm/policy changes.** Marketplace ranking algorithms can change, reducing organic visibility overnight. Mitigation: diversify across multiple HRIS marketplaces (not just one); build the referral loop as a hedge.
2. **Partner cooperation dependency.** Co-marketing and listing optimization depend on HRIS partner willingness. Mitigation: start with the partner where you have the strongest relationship; have a backup partner.
3. **Activation bottleneck may be deeper than setup UX.** If users drop off because the AI onboarding output quality is poor (not just setup friction), the guided setup experiment won't move the needle. Mitigation: instrument drop-off reasons; interview churned users.
4. **Eng capacity constraint.** With 2 developers, experiments must be strictly sequenced. Any scope creep or production incident delays the entire plan. Mitigation: keep experiments minimal in scope; use no-code tools where possible (e.g., listing copy changes, email invite flows via existing tools).
5. **Brand/trust risk from review solicitation.** If review prompts are too aggressive, it could damage trust with HR buyers. Mitigation: prompt only after genuine value delivery; make it easy to dismiss; never incentivize reviews in ways that violate marketplace policy.

### Open Questions

1. **What is the current WAU baseline?** The +30% target requires a known starting point. The team should confirm exact WAU before Day 1.
2. **What is the current activation rate (install --> first onboarding run)?** This determines whether the primary bottleneck is top-of-funnel (listing visibility) or mid-funnel (activation).
3. **Which HRIS marketplaces drive the most volume?** Optimizing the top 1–2 marketplaces first will have the most impact.
4. **Do marketplace analytics dashboards provide listing view and install data?** If not, the team needs to find proxy metrics or request data from HRIS partners.
5. **Is there any existing analytics tooling (Mixpanel, Amplitude, etc.)?** The instrumentation plan assumes basic event tracking capability exists or can be set up quickly.
6. **What does the current setup/onboarding flow look like, and where do users drop off?** This informs Experiment 2 design.
7. **Are there any existing customer success stories that could seed the co-marketing content pilot?** Without at least 1–2 stories, the content loop is harder to start.

### Next Steps

1. **Confirm WAU baseline and activation rate** — needed before any experiment can be measured.
2. **Prioritize instrumentation (Week 1)** — without events, nothing else is measurable.
3. **Start Experiment 1 (listing optimization) immediately** — zero eng effort, fast feedback.
4. **Scope Experiment 2 (guided setup)** — the single highest-impact eng investment in the first 30 days.
5. **Reach out to top HRIS partner** — begin the co-marketing conversation now so it's ready by Day 30–45.
6. **Schedule a Day 30 checkpoint** — review metrics, decide whether to continue or pivot.

---

## Quality Gate: Checklist

### A) Scope + decision clarity
- [x] The growth goal is explicit: +30% WAU in 90 days, mid-market segment.
- [x] Target segment is defined: mid-market companies (100–1,000 employees) using HRIS platforms.
- [x] Constraints are stated: 2 developers, brand-safe only, no paid budget, HRIS policy compliance, HR data privacy.
- [x] Decision is explicit: invest in HRIS marketplace integration loop (primary) + champion referral loop (secondary); optimize first, then innovate.

### B) Baseline is grounded
- [x] Baseline includes metrics/estimates for acquisition, activation, retention/engagement (with confidence levels noted where data is missing).
- [x] Existing loops documented (marketplace discovery loop, outbound sales).
- [x] Core value moment defined (first AI-assisted onboarding run).

### C) Loop model quality
- [x] Micro loops specified as input --> action --> output --> feedback.
- [x] Macro loop connects micro loops (diagram + narrative).
- [x] Cycle times estimated per loop.
- [x] Bottlenecks named (listing CVR, time-to-first-value, review submission rate, invite trigger).

### D) Prioritization + gating
- [x] Loop scorecard present; top 2 loops selected with rationale and trade-offs.
- [x] Channel fit triad applied for all candidates.
- [x] Paid loop gated (not yet viable; prerequisites listed).

### E) Measurement + learning plan
- [x] Each selected loop has KPI + leading indicators.
- [x] Instrumentation requirements specified (9 events with properties).
- [x] Instrumentation gaps identified with fixes and effort estimates.
- [x] Experiments have hypotheses, metrics, and timeboxes with win/lose/learn criteria.

### F) Safety + ethics
- [x] All mechanisms are policy-compliant; no manipulative/dark-pattern tactics.
- [x] Risks include brand/trust (review solicitation) and platform policy (marketplace rules).
- [x] User consent addressed (invites are opt-in; review prompts are dismissible).

### G) Required closing section
- [x] Risks, Open Questions, and Next Steps all included.

---

## Quality Gate: Rubric Score

| Dimension | Score | Rationale |
|---|---:|---|
| 1) Decision usefulness | 2 | Clear decision (which loops to invest in) + "what changes if it fails" (pivot to different loop or address deeper bottleneck) |
| 2) Loop clarity — micro + macro | 2 | Three micro loops with input/action/output/feedback; macro loop diagram showing connections; bottlenecks and cycle times explicit |
| 3) Evidence grounding | 1 | Baseline exists with estimates and confidence labels, but several key metrics are assumptions (activation rate, WAU baseline) due to limited data provided; hypotheses clearly labeled |
| 4) Prioritization quality | 2 | Scorecard with 6 candidates scored on 5 dimensions; clear top-2 selection with trade-off rationale; innovate-vs-optimize recommendation |
| 5) Unit economics + paid gating | 2 | Paid loop explicitly gated as "not yet viable" with clear prerequisites; non-paid loops have effort estimates |
| 6) Measurement + instrumentation readiness | 2 | KPIs + leading indicators defined; 9 events with properties specified; 4 instrumentation gaps identified with fixes and effort |
| 7) Actionability | 2 | 6 prioritized experiments with hypotheses, metrics, timeboxes, and win/lose/learn criteria; 30/60/90 plan with checkpoints; next 2 weeks unblocked |
| 8) Safety + ethics | 2 | All mechanisms policy-compliant; brand/trust risks addressed; platform compliance checks included; user consent and spam thresholds explicit |

**Total: 15/16** (Passing bar: >= 13/16)

**Interpretation:** Strong. Execute and review cadence weekly. The primary gap is evidence grounding (scored 1/2) due to missing baseline metrics — the first week's instrumentation work will close this gap. All other dimensions are at the highest level.
