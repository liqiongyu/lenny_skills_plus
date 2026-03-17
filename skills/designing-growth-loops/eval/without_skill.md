# Growth Loop Design: AI Onboarding Assistant (Mid-Market HRIS Integration Play)

## Context Summary

- **Product**: AI onboarding assistant for HR teams
- **Stage**: Early growth, some product-market fit
- **Segment**: Mid-market (typically 100-1,000 employees)
- **Goal**: Increase WAU by 30% in 90 days
- **Constraint**: 2 developers, brand-safe tactics only
- **Hypothesized lever**: HRIS marketplace integrations (already listed on several)

---

## 1. Growth Loop Design

### Primary Loop: HRIS Marketplace Integration Loop

This is an **integration-driven acquisition loop** where each new customer acquired through an HRIS marketplace generates usage data and success stories that improve marketplace presence, which in turn drives more discovery and adoption.

```
[HRIS Marketplace Listing]
        |
        v
[Mid-Market HR Buyer Discovers Product]
        |
        v
[Trial / Free Pilot via Marketplace Install]
        |
        v
[Onboarding AI Runs for New Hires → Generates Value]
        |
        v
[HR Admin Becomes Active Weekly User (WAU)]
        |
        v
[Success Metrics Generated (time-to-productivity, completion rates)]
        |
        v
[Reviews/Ratings on HRIS Marketplace + Case Study Content]
        |
        v
[Improved Marketplace Ranking & Social Proof]
        |
        (loops back to top)
```

### Secondary Loop: Internal Viral Expansion Loop

Within each customer account, the product has a natural expansion mechanism:

```
[HR Admin Activates AI Onboarding for Department A]
        |
        v
[New Hires in Dept A Have Great Experience]
        |
        v
[Hiring Manager in Dept A Sees Results]
        |
        v
[Word Spreads to Dept B, C Hiring Managers]
        |
        v
[HR Admin Expands Usage Across Departments]
        |
        v
[More Weekly Active Users (HR admins + hiring managers)]
        |
        (loops back → more departments, more WAU)
```

### Combined Loop Mechanics

The two loops reinforce each other: the external HRIS marketplace loop brings in new accounts, while the internal expansion loop increases WAU within each account. For mid-market companies (100-1,000 employees), a single account can generate 3-15 weekly active users (HR team members, hiring managers, department leads) if expansion is working.

---

## 2. Full Loop Mechanics Map

### Stage 1: Discovery (HRIS Marketplace)

- **Input**: HR buyer searches HRIS marketplace (e.g., BambooHR, Rippling, Workday marketplace) for onboarding solutions
- **Mechanism**: Marketplace search ranking, category placement, reviews/ratings
- **Output**: Click-through to product listing
- **Key metric**: Marketplace listing impressions → click-through rate (CTR)

### Stage 2: Evaluation & Activation

- **Input**: HR buyer views listing, reads reviews, sees integration details
- **Mechanism**: One-click install from marketplace, free trial/pilot offer, pre-built integration means zero engineering effort on buyer side
- **Output**: Product installed and connected to HRIS
- **Key metric**: Listing view → install conversion rate

### Stage 3: First Value (Aha Moment)

- **Input**: Product is installed and connected
- **Mechanism**: AI assistant auto-configures onboarding workflows based on HRIS data (roles, departments, locations), runs first onboarding for a real new hire
- **Output**: HR admin sees AI-generated onboarding plan, first new hire completes AI-assisted onboarding
- **Key metric**: Install → first onboarding workflow completed (time-to-value)

### Stage 4: Habit Formation (WAU Driver)

- **Input**: First onboarding completed successfully
- **Mechanism**: Weekly digest of onboarding progress, pending tasks surface in HRIS dashboard, automated reminders for HR admin actions
- **Output**: HR admin returns weekly to monitor, adjust, and launch onboarding for new cohorts
- **Key metric**: Activated user → WAU retention at Week 4

### Stage 5: Expansion (Internal Virality)

- **Input**: HR admin is an active weekly user
- **Mechanism**: Hiring managers receive onboarding status updates, are invited to customize department-specific flows, see dashboard of their new hires' progress
- **Output**: Additional WAU from hiring managers and department leads
- **Key metric**: WAU per account (target: 3-5 for initial, 8-15 for expanded)

### Stage 6: Advocacy (Loop Closure)

- **Input**: Measurable success (e.g., 40% faster time-to-productivity, 90% onboarding completion)
- **Mechanism**: In-app prompt to leave marketplace review, automated ROI report shareable with leadership, case study co-creation
- **Output**: New reviews on HRIS marketplace, improved ranking, social proof for next buyer
- **Key metric**: NPS, marketplace review rate, referral rate

---

## 3. Key Bottlenecks

### Bottleneck 1: Marketplace Discovery → Install Conversion (HIGHEST PRIORITY)

**Why it matters**: Being listed on HRIS marketplaces is necessary but not sufficient. Mid-market HR buyers are overwhelmed with options. If your listing doesn't convert browsers to installers, the entire loop stalls at the top.

**Evidence signals to look for**:
- Low CTR on marketplace listings relative to category average
- High listing views but low install rate
- Competitors with more reviews/higher ratings capturing disproportionate share

**Root causes likely at play**:
- Listing copy doesn't speak to mid-market-specific pain points (compliance complexity, multi-department coordination)
- Few or no reviews/ratings (cold start problem)
- Unclear value proposition vs. native HRIS onboarding features

### Bottleneck 2: Install → First Value (Time-to-Aha)

**Why it matters**: Mid-market HR teams are busy. If the product requires significant configuration before it delivers value, trial users will abandon before becoming WAU. This is especially critical because mid-market buyers expect enterprise-grade readiness but have SMB-level patience for setup.

**Evidence signals to look for**:
- High install rate but low activation (first workflow created)
- Long time between install and first real onboarding run
- Support tickets clustered around initial setup

**Root causes likely at play**:
- Configuration requires too many manual steps after HRIS connection
- Product doesn't auto-detect enough from HRIS data to pre-build workflows
- First onboarding run requires a real new hire (can't demo with synthetic data)

### Bottleneck 3: Single-User → Multi-User Expansion Within Account

**Why it matters**: WAU growth in mid-market comes disproportionately from expanding active users within existing accounts, not just acquiring new accounts. If only the HR admin uses the product weekly, you're capping WAU at 1 per account instead of 5-15.

**Evidence signals to look for**:
- WAU/account ratio stuck at 1-2
- Hiring managers not logging in after initial invitation
- Department-level customization features unused

**Root causes likely at play**:
- No compelling reason for hiring managers to engage weekly (HR admin acts as bottleneck/proxy)
- Hiring manager experience is not differentiated from HR admin experience
- No notifications or triggers pulling hiring managers back into the product

---

## 4. First 2-3 Experiments

### Experiment 1: Marketplace Listing Optimization + Review Generation Campaign

**Targets Bottleneck**: #1 (Discovery → Install Conversion)

**Hypothesis**: By optimizing our top 2 HRIS marketplace listings with mid-market-specific messaging and generating 10-15 authentic reviews, we can increase install conversion rate by 40%, which translates to ~15-20% more new activated accounts feeding into WAU.

**Design**:
- **Week 1-2**: Audit top 2 performing HRIS marketplace listings. Rewrite copy to emphasize mid-market pain points: multi-department onboarding coordination, compliance across states/regions, reducing HR admin manual work from 8 hrs/new hire to under 1 hr. Add a "Built for 100-1,000 employee companies" positioning line.
- **Week 2-4**: Launch a review generation campaign with existing happy customers. Offer a 30-minute "onboarding optimization session" (high-value, no discount needed = brand-safe) in exchange for an honest marketplace review. Target 5 reviews per marketplace.
- **Week 3-6**: A/B test listing screenshots — version A showing the HR admin dashboard, version B showing a new hire's AI-guided first-day experience.

**Engineering cost**: Minimal (0.25 dev-weeks). This is primarily a marketing/customer success motion. Dev involvement limited to generating screenshots and possibly adding an in-app review prompt.

**Success metric**: Install conversion rate on HRIS marketplace (baseline → +40%). Secondary: new account activations per week.

**Kill criteria**: If after 4 weeks, install rate hasn't moved by at least 15%, pivot to direct outbound instead of marketplace optimization.

---

### Experiment 2: Auto-Magic First Onboarding (Zero-Config Activation)

**Targets Bottleneck**: #2 (Install → First Value)

**Hypothesis**: By auto-generating a complete onboarding workflow from HRIS data at the moment of install (instead of requiring manual configuration), we can reduce time-to-first-value from days to minutes and increase install-to-activation rate by 50%.

**Design**:
- **Week 1-3 (Dev Sprint)**: Build an "auto-magic setup" flow that triggers on HRIS connection. The system reads company data (departments, roles, locations, upcoming start dates) and auto-generates: (a) a department-specific onboarding template for the 2-3 largest departments, (b) a pre-populated onboarding workflow for the next upcoming new hire, and (c) a simulated "preview" onboarding experience the HR admin can walk through in 5 minutes.
- **Week 3-4**: Ship to all new installs. Existing un-activated installs get a "We've set things up for you" re-engagement email.
- **Week 4-6**: Measure activation rate and time-to-value. Iterate on the auto-generated templates based on which departments and roles activate most.

**Engineering cost**: ~3-4 dev-weeks across 2 developers (primary investment). This is the highest-leverage engineering bet because it directly unblocks the loop.

**Success metric**: Install → first-onboarding-completed rate (baseline → +50%). Time-to-first-value (target: under 10 minutes from install). WAU impact: faster activation means more users reaching habit stage within the 90-day window.

**Kill criteria**: If install-to-activation doesn't improve by at least 20% after 3 weeks of deployment, the bottleneck is elsewhere (possibly product-market fit in the segment, not activation friction).

---

### Experiment 3: Hiring Manager Weekly Pulse (Expansion Wedge)

**Targets Bottleneck**: #3 (Single-User → Multi-User Expansion)

**Hypothesis**: By sending hiring managers a personalized weekly "New Hire Pulse" report (with one clear action item) and giving them a lightweight dashboard, we can increase average WAU per account from ~1.5 to ~4, contributing significantly to the 30% WAU goal without acquiring a single new account.

**Design**:
- **Week 1-2 (Dev Sprint)**: Build a weekly automated email to hiring managers with active new hires. Content: new hire onboarding completion %, one specific action item ("Review [Name]'s Week 2 check-in responses"), and a link to a simple hiring-manager-specific dashboard (read-only, focused on their direct reports' onboarding progress).
- **Week 2-3**: Build the lightweight hiring manager dashboard — not the full HR admin view, but a focused "my new hires" view showing progress bars, upcoming milestones, and a comment/feedback mechanism.
- **Week 3-6**: Roll out to top 20 accounts first (highest new-hire volume). Measure hiring manager engagement: email open rate, click-through rate, dashboard WAU.

**Engineering cost**: ~2-3 dev-weeks. The email is straightforward; the dashboard is a simplified view of existing data.

**Success metric**: WAU per account (baseline → target 3-4x increase in participating accounts). Hiring manager weekly return rate > 40%.

**Kill criteria**: If hiring manager email open rates are below 25% after 2 weeks, the content isn't compelling enough — pivot to testing different triggers (e.g., real-time notifications when a new hire completes a milestone instead of weekly digests).

---

## 5. Prioritized Execution Roadmap (90 Days)

| Week | Experiment 1 (Marketplace) | Experiment 2 (Auto-Setup) | Experiment 3 (HM Expansion) |
|------|---------------------------|--------------------------|------------------------------|
| 1-2  | Audit & rewrite listings  | Dev: auto-magic setup    | Design HM email + dashboard  |
| 3-4  | Launch review campaign    | Ship auto-setup          | Dev: build email + dashboard |
| 5-6  | A/B test screenshots      | Measure & iterate        | Roll out to top 20 accounts  |
| 7-8  | Scale to more marketplaces| Re-engage dormant installs| Expand to all accounts       |
| 9-10 | Measure full-loop impact  | Measure activation lift  | Measure WAU/account lift     |
| 11-12| Decide: double down or pivot| Optimize auto-templates | Iterate on HM experience     |

### Resource Allocation (2 Developers)

- **Weeks 1-4**: Both devs on Experiment 2 (auto-setup) — this is the highest-leverage technical investment. Experiment 1 is marketing-led and can run in parallel without dev resources.
- **Weeks 3-6**: Dev 1 continues Experiment 2 iteration; Dev 2 starts Experiment 3 (HM dashboard).
- **Weeks 7-12**: Split between iterating on Experiments 2 and 3 based on results.

---

## 6. WAU Impact Model

Rough estimation of how the 30% WAU increase could break down:

| Lever | Mechanism | Estimated WAU Lift |
|-------|-----------|-------------------|
| Marketplace optimization (Exp 1) | More new accounts entering the loop | +8-12% WAU |
| Auto-setup activation (Exp 2) | Higher % of installs becoming active | +8-10% WAU |
| HM expansion (Exp 3) | More WAU per existing account | +10-15% WAU |
| **Combined** | | **+26-37% WAU** |

The three experiments are designed to be complementary: Experiment 1 widens the top of the funnel, Experiment 2 fixes the activation bottleneck so new users convert, and Experiment 3 multiplies the WAU impact of every activated account. Together, they target the 30% WAU goal with some margin for experiments that underperform.

---

## 7. Key Risks and Mitigations

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| HRIS marketplace algorithm changes reduce visibility | Medium | Diversify across 3+ marketplaces; don't over-index on one |
| Auto-setup generates poor-quality workflows from messy HRIS data | High | Build a "review and customize" step after auto-generation; start with well-structured HRIS platforms |
| Hiring managers see emails as spam | Medium | Ensure first email delivers clear, specific value; include one-click unsubscribe; test subject lines |
| 2-developer bandwidth insufficient for all 3 experiments | Medium | Experiment 1 is marketing-led; stagger Experiments 2 and 3; use off-the-shelf email tooling for Experiment 3 |
| Reviews feel inauthentic or incentivized | Low | Offer value (optimization session) not discounts; never script reviews; comply with marketplace review policies |
