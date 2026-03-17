# Sales Qualification Pack

## Context

**Company Profile:** B2B SaaS targeting operations teams at companies with 50-500 employees
**ACV:** $12,000
**Sales Cycle:** ~45 days
**Team Structure:** SDRs qualify inbound leads and hand off to AEs
**Core Problem:** High inbound volume but AEs report low meeting quality

---

## 1. Problem Diagnosis

The gap between high inbound volume and low meeting quality points to a qualification breakdown. Common root causes in this scenario include:

- **Loose or undefined qualification criteria:** SDRs may lack a clear, shared framework for what constitutes a "qualified" lead, leading to inconsistent handoffs.
- **Incentive misalignment:** If SDRs are compensated primarily on meetings booked rather than pipeline generated or deals closed, they are incentivized to pass volume, not quality.
- **Insufficient discovery during qualification:** SDRs may be scheduling meetings after surface-level conversations rather than confirming genuine fit, need, and timing.
- **Inbound lead source quality variance:** Not all inbound channels produce the same quality. Some channels (e.g., content downloads, free tool signups) may attract researchers or non-buyers.
- **Lack of a feedback loop:** AEs may not have a structured way to report meeting quality back to SDR leadership, so the problem persists undiagnosed.

---

## 2. Ideal Customer Profile (ICP) Refinement

Before qualification criteria can work, the team needs a tight ICP. Based on the stated parameters:

### Firmographic Fit

| Dimension | Target | Acceptable | Disqualify |
|---|---|---|---|
| Employee Count | 100-500 | 50-99 | <50 or >500 |
| Industry | Manufacturing, logistics, professional services, healthcare ops | Retail, e-commerce, construction | Government, education, non-profit (unless ops-heavy) |
| Revenue Range | $10M-$100M (estimated) | $5M-$10M | <$5M |
| Geography | Primary market (e.g., US, Canada) | Secondary markets | Markets you don't serve |
| Tech Stack | Uses complementary tools (ERP, project management, HRIS) | Minimal tooling (greenfield) | Locked into competitor with 2+ years remaining |

### Persona Fit

| Dimension | Primary Buyer | Secondary Buyer | Not a Buyer |
|---|---|---|---|
| Title | VP/Director of Operations, Head of Ops, COO | Operations Manager, Process Improvement Lead | Individual contributor, intern, student |
| Reporting Line | Reports to CEO/COO or is the COO | Reports to VP Ops | Reports to non-ops function |
| Budget Authority | Owns or influences $12k+ annual spend | Can champion internally | No purchasing influence |
| Team Size Managed | 5-50 direct/indirect reports | 3-5 reports | No reports |

---

## 3. Qualification Framework

### Recommended: MEDDPICC (Adapted for $12k ACV, 45-day cycle)

Given the ACV and cycle length, a full enterprise qualification framework is overkill. Instead, use a streamlined version focused on the dimensions that most predict conversion:

### SDR Qualification Criteria (BANT+)

SDRs should confirm at least 4 of the following 5 before booking an AE meeting:

**1. Budget Indication**
- The prospect's company can reasonably afford $12k/year (not a tiny bootstrapped startup)
- They are not in a hiring freeze, layoff cycle, or publicly known financial distress
- *SDR question:* "How does your team typically evaluate and budget for tools like this? Is there a budget allocated for operations improvements this year?"

**2. Authority / Access to Power**
- The person on the call holds a relevant title (Manager+ in operations or a closely related function)
- OR they can specifically name the decision-maker and confirm willingness to involve them
- *SDR question:* "Who else would be involved in evaluating a solution like this? Walk me through how your team has made similar decisions in the past."

**3. Need / Pain Confirmed**
- The prospect can articulate a specific operational pain point your product addresses
- The pain is current (not hypothetical, not "someday we might")
- *SDR question:* "What's the biggest operational challenge your team is dealing with right now? How is that impacting the business?"

**4. Timing / Urgency**
- There is a triggering event or deadline creating urgency (new hire, lost customer, compliance requirement, board mandate, broken process)
- They are actively looking for a solution, not just researching the market
- *SDR question:* "What's driving you to look at this now? Is there a timeline you're working toward?"

**5. Fit Confirmation**
- The prospect's use case aligns with your product's core capabilities
- They are not asking for functionality you don't have and won't build
- *SDR question:* "Based on what you've described, let me confirm -- you're looking for [restate their need]. Is that right?"

### Scoring System

| Criteria Met | Action |
|---|---|
| 5 of 5 | Book immediately. Flag as high-priority for AE. |
| 4 of 5 | Book the meeting. Note which criterion is missing in the handoff. |
| 3 of 5 | Place in nurture sequence. Re-engage in 2-4 weeks. |
| 2 or fewer | Disqualify or route to self-serve / marketing nurture. |

---

## 4. SDR-to-AE Handoff Protocol

### The Handoff Brief (Required for Every Meeting)

SDRs must complete the following template before an AE meeting is confirmed:

```
HANDOFF BRIEF
=============
Date: [Date]
SDR: [Name]
AE: [Name]
Prospect: [Name, Title, Company]

COMPANY SNAPSHOT
- Company: [Name]
- Employees: [Number]
- Industry: [Industry]
- Website: [URL]
- Inbound Source: [How they found us -- specific channel]

QUALIFICATION SUMMARY
- Budget: [Yes/Partial/Unknown] -- [Notes]
- Authority: [Decision-maker / Champion / Influencer] -- [Notes]
- Need: [Specific pain stated] -- [Verbatim quote if possible]
- Timing: [Active / Exploring / Future] -- [Trigger event if known]
- Fit: [Strong / Moderate / Uncertain] -- [Notes on use case]

SCORE: [X out of 5]

KEY CONTEXT FOR AE
- What the prospect cares about most: [1-2 sentences]
- What they've tried before: [Previous solutions, if discussed]
- Potential objections or concerns raised: [List any]
- Competitors mentioned: [List any]

MEETING DETAILS
- Date/Time: [Scheduled time]
- Format: [Video / Phone / In-person]
- Attendees: [List all confirmed attendees and their roles]
- Suggested AE approach: [Discovery-heavy / Demo-ready / Executive alignment]
```

### Handoff Rules

1. **No blank fields.** If a field is unknown, write "Not discussed -- AE should explore." This forces intentionality.
2. **48-hour freshness rule.** If more than 48 hours pass between the SDR call and the AE meeting, the SDR sends a brief re-engagement email to the prospect confirming the meeting and restating context.
3. **AE pre-read required.** AEs must review the handoff brief before the meeting. No walking in cold.
4. **Warm introduction.** The SDR sends a bridge email introducing the AE to the prospect before the meeting. Template below.

### Bridge Email Template

```
Subject: [First Name], meet [AE First Name] -- your [Company Name] specialist

Hi [Prospect First Name],

Thanks again for our conversation on [day]. As I mentioned, I'm connecting you
with [AE Full Name], who works directly with operations teams like yours on
[brief value prop related to their stated pain].

[AE First Name] -- [Prospect First Name] leads operations at [Company] and is
looking to [restate their specific need in 1 sentence]. They're currently
[brief context on timing/urgency].

You're set to connect on [Date] at [Time]. Looking forward to hearing how it goes.

Best,
[SDR Name]
```

---

## 5. Inbound Lead Scoring Model

Implement lead scoring to pre-filter before SDR outreach and prioritize the queue:

### Behavioral Scoring (0-50 points)

| Action | Points |
|---|---|
| Requested a demo | 25 |
| Started a free trial | 20 |
| Visited pricing page | 15 |
| Attended a webinar (live) | 10 |
| Downloaded a case study | 10 |
| Visited 3+ pages in one session | 8 |
| Opened 3+ emails in 30 days | 5 |
| Downloaded a general whitepaper/ebook | 3 |
| Subscribed to newsletter only | 1 |

### Firmographic Scoring (0-50 points)

| Attribute | Points |
|---|---|
| Employee count 100-500 | 20 |
| Employee count 50-99 | 10 |
| Target industry | 15 |
| Adjacent industry | 5 |
| Title: VP/Director/Head of Ops or COO | 15 |
| Title: Manager of Ops | 10 |
| Title: Non-ops but relevant (e.g., CFO at small co) | 5 |
| Uses complementary tech (from enrichment data) | 5 |

### Scoring Thresholds

| Score | Routing |
|---|---|
| 70-100 | Immediate SDR outreach (within 5 minutes during business hours) |
| 50-69 | SDR outreach within 2 hours |
| 30-49 | Automated nurture sequence; SDR reviews weekly |
| Below 30 | Marketing nurture only; no SDR touch |

---

## 6. Disqualification Criteria

SDRs must be empowered (and expected) to disqualify. Passing unqualified leads wastes AE time and erodes trust.

### Hard Disqualifiers (Immediate)

- Company has fewer than 30 employees
- Prospect is a student, consultant (not buying for a client), or competitor
- No operations function exists at the company
- Prospect explicitly states no budget and no path to budget in the next 6 months
- Prospect needs functionality your product fundamentally does not offer
- Prospect is in a market/geography you do not serve

### Soft Disqualifiers (Route to Nurture)

- Right company profile but wrong persona (e.g., marketing intern filled out the form)
- Timing is 6+ months out with no triggering event
- Prospect is evaluating but has no authority and cannot name the decision-maker
- Company is in ICP but prospect cannot articulate a specific pain

---

## 7. SDR Compensation Alignment

If SDR comp is tied only to meetings booked, quality will suffer. Recommended structure:

### Proposed SDR Compensation Mix

| Component | Weight | Metric |
|---|---|---|
| Base salary | 50% | -- |
| Meetings booked (qualified) | 20% | Meetings that meet 4/5 qualification criteria |
| Pipeline generated | 20% | Dollar value of opportunities created from SDR-sourced meetings |
| Meetings-to-opportunity conversion rate | 10% | Percentage of SDR meetings that AEs convert to active pipeline |

### Key Changes from Typical Models

- **Meetings booked** is only 20%, not 50%+. This discourages volume-chasing.
- **Pipeline generated** connects SDR effort to revenue outcomes.
- **Conversion rate** creates a direct quality signal. If an SDR books 50 meetings but only 10% convert, their comp reflects that.

---

## 8. AE Meeting Quality Feedback Loop

### Meeting Quality Scorecard

After every SDR-sourced meeting, the AE completes a 60-second rating:

```
MEETING QUALITY SCORECARD
=========================
Date: [Date]
Prospect: [Company / Name]
SDR: [Name]
AE: [Name]

1. Was the prospect expecting the call and prepared?
   [ ] Yes  [ ] Partially  [ ] No

2. Did the prospect match the handoff brief?
   [ ] Matched  [ ] Partially matched  [ ] Did not match

3. Was there a real, confirmed pain point?
   [ ] Yes, specific and urgent  [ ] Vague/general  [ ] No pain identified

4. Did the prospect have authority or access to authority?
   [ ] Decision-maker present  [ ] Champion identified  [ ] No authority

5. Is this a viable opportunity?
   [ ] Yes, creating opportunity  [ ] Maybe, needs follow-up  [ ] No, disqualifying

OVERALL QUALITY: [ ] High  [ ] Medium  [ ] Low

NOTES FOR SDR COACHING: [Free text]
```

### Feedback Cadence

| Activity | Frequency | Owner |
|---|---|---|
| Scorecard completion | After every SDR-sourced meeting | AE |
| SDR-AE 1:1 review | Weekly (15 min) | SDR Manager facilitates |
| Quality metrics review | Bi-weekly | Sales leadership |
| Calibration session (SDR + AE alignment on "qualified") | Monthly | SDR Manager + AE Manager |

---

## 9. Inbound Channel Quality Analysis

Since not all inbound is equal, track and act on source quality:

### Recommended Tracking Dimensions

For each inbound channel, measure:

1. **Volume:** Leads generated per month
2. **Qualification Rate:** % of leads that meet 4/5 SDR criteria
3. **Meeting Conversion Rate:** % of qualified leads that become AE meetings
4. **Opportunity Rate:** % of AE meetings that become pipeline opportunities
5. **Win Rate:** % of opportunities that close
6. **Blended CAC:** Cost to acquire a customer through this channel

### Channel Quality Matrix (Example Framework)

| Channel | Volume | Qual Rate | Opp Rate | Action |
|---|---|---|---|---|
| Demo request (website) | Medium | High | High | Invest more; fastest path to revenue |
| G2/review site referrals | Low | High | High | Increase presence and review volume |
| Paid search (branded) | Medium | Medium | Medium | Maintain; optimize landing pages |
| Paid search (non-branded) | High | Low | Low | Audit keywords; tighten targeting or reduce spend |
| Content downloads | High | Low | Very Low | Route to nurture, not SDR queue |
| Webinar registrations | Medium | Medium | Medium | Use as nurture touchpoint; qualify post-event |
| Partner referrals | Low | High | High | Invest in partner program |
| Free trial signups | Medium | Medium | Medium | Implement product-qualified lead (PQL) triggers |

---

## 10. Recommended Process Changes -- 90-Day Implementation Plan

### Month 1: Foundation

- [ ] Finalize and document ICP (firmographic + persona fit criteria)
- [ ] Train SDR team on updated qualification framework (BANT+ with scoring)
- [ ] Implement handoff brief template as a required step in CRM
- [ ] Launch AE meeting quality scorecard
- [ ] Audit current lead scoring model; implement or update in marketing automation platform

### Month 2: Optimization

- [ ] Analyze first 30 days of meeting quality scorecards; identify patterns
- [ ] Run first SDR-AE calibration session to align on "qualified"
- [ ] Review inbound channel quality data; make initial budget reallocation recommendations
- [ ] Adjust SDR compensation structure (phase in over current quarter)
- [ ] Implement automated lead routing based on scoring thresholds

### Month 3: Scaling

- [ ] Measure impact: compare meeting quality scores, opp conversion rates, and cycle times vs. baseline
- [ ] Refine qualification criteria based on data (which criteria most predict closed-won?)
- [ ] Formalize disqualification as a tracked, positive SDR behavior
- [ ] Publish internal "What Good Looks Like" examples -- best handoff briefs, highest-quality meetings
- [ ] Set targets for Month 4-6 based on learnings

---

## 11. Key Metrics to Track

### Leading Indicators (Weekly Review)

| Metric | Current Baseline | 90-Day Target |
|---|---|---|
| SDR qualification score (avg across meetings) | Establish baseline | 4.0+ out of 5 |
| AE meeting quality rating (% rated "High") | Establish baseline | 60%+ |
| Meetings-to-opportunity conversion rate | Establish baseline | 50%+ |
| Average SDR response time (inbound leads) | Establish baseline | <5 min for 70+ score leads |

### Lagging Indicators (Monthly Review)

| Metric | Current Baseline | 90-Day Target |
|---|---|---|
| Average deal size (ACV) | $12,000 | $12,000+ (maintain or grow) |
| Sales cycle length | ~45 days | ~40 days (modest improvement) |
| Win rate (opportunity to close) | Establish baseline | Improve 10-15% relative |
| Disqualification rate (SDR stage) | Establish baseline | 25-35% of inbound (healthy rejection) |
| AE productive selling time | Establish baseline | Increase 20%+ (fewer wasted meetings) |

---

## 12. Quick-Reference: Top 5 SDR Discovery Questions

For SDRs to use on every qualification call:

1. **"What's the biggest operational challenge your team is facing right now?"**
   *Purpose:* Confirm a real, specific pain exists.

2. **"How is that impacting the business? Can you put a number on it?"**
   *Purpose:* Quantify the pain; urgency and budget justification follow from this.

3. **"What have you tried so far to solve this?"**
   *Purpose:* Understand competitive landscape, prior solutions, and sophistication level.

4. **"Who else would be involved in evaluating and deciding on a solution?"**
   *Purpose:* Map the buying committee; confirm authority or path to authority.

5. **"What's driving you to look at this now, and what does your timeline look like?"**
   *Purpose:* Identify trigger events and urgency; distinguish active buyers from browsers.

---

## Summary

The core issue -- high inbound volume with low meeting quality -- is a qualification and handoff problem, not a demand generation problem. The fixes are:

1. **Tighten qualification criteria** with a structured, scored framework (BANT+ with 4/5 threshold).
2. **Standardize the handoff** with a required brief that forces SDRs to confirm fit before booking.
3. **Realign incentives** so SDRs are rewarded for quality (pipeline generated, conversion rate), not just volume.
4. **Close the feedback loop** with AE meeting quality scorecards and regular calibration sessions.
5. **Score and route inbound leads** so SDR time goes to the highest-potential prospects, and low-quality leads go to automated nurture.
6. **Track channel quality** to identify which inbound sources produce real pipeline and which produce noise.

These changes should be implementable within 90 days and measurable within the first 60.
