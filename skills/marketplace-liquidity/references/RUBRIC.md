# Rubric (score 0/1/2)

0 = missing / unusable  
1 = present but incomplete  
2 = clear, executable, reusable

Suggested passing bar: **>= 14/18**.

## 1) Reliability definition (0–2)
- 0: “Liquidity” is vague or purely conceptual; no measurable definition provided (e.g., “we need better liquidity” with no metric or threshold)
- 1: Defined as a metric (e.g., “fill rate”) but missing either time thresholds (acceptable time-to-match) or quality thresholds (cancellation/no-show rate), or defined only from the platform's perspective without tying to user-perceived reliability
- 2: Clear reliability definition from the user's perspective (e.g., “probability a buyer finds and books a qualified cleaner within 4 hours with <10% cancellation rate”) with explicit time + quality thresholds

## 2) Local market segmentation (0–2)
- 0: Uses only global averages (e.g., “our marketplace fill rate is 65%”) with no breakdown by geography, category, or time window
- 1: Some segmentation exists (e.g., by city or category) but the segments are not defined as actionable “local markets” where matches actually occur, or priority segments are not ranked by impact
- 2: Local markets explicitly defined as a cross of relevant dimensions (e.g., city x category x day-of-week); priority segments ranked by volume and liquidity gap; each segment has its own baseline metrics

## 3) Metric tree quality (0–2)
- 0: No metric tree; metrics mentioned ad hoc or not at all
- 1: Partial list of metrics (e.g., fill rate, time-to-match) but missing event-level definitions, guardrail metrics, or segmentation plan; north-star metric not distinguished from drivers
- 2: Explicit north-star metric + 3-6 driver metrics + at least 1 guardrail metric; each metric has an event definition (what triggers it), a data source, and a segmentation plan

## 4) Fragmentation analysis (0–2)
- 0: No mention of fragmentation or thin markets; assumes all segments behave uniformly
- 1: Mentions fragmentation (e.g., “some categories have thin supply”) but without quantified evidence or impact sizing; no distinction between uniform-need and heterogeneous-need markets
- 2: Identifies specific fragmented segments with volume data; quantifies the impact on reliability (e.g., “product design has 3 suppliers vs logo design's 40, driving 5-day vs 1-day match times”); addresses whether the marketplace has uniform or heterogeneous needs

## 5) Bottleneck diagnosis (0–2)
- 0: No diagnosis of root cause; jumps straight to solutions or only describes symptoms
- 1: Labels the bottleneck (e.g., “supply-limited”) but for the marketplace as a whole rather than per-segment, or lacks supporting metric evidence and testable causal hypotheses
- 2: Per-segment diagnosis labeling the primary failure mode (supply / demand / mechanics / quality) with at least 1 metric signal and 1 testable hypothesis per segment; addresses flip-flop dynamics (which side is currently the constraint)

## 6) Interventions + experiments (0–2)
- 0: Generic tactics only (e.g., “acquire more supply,” “improve UX”) with no experiment structure
- 1: Experiments listed with some structure but missing one or more of: hypothesis, primary metric, target effect size, segment scope, or cycle time estimate
- 2: Prioritized backlog where each experiment specifies (a) target segment, (b) hypothesis, (c) primary + guardrail metrics, (d) expected effect size or directional expectation, and (e) estimated cycle time; experiments are ranked by impact/effort

## 7) Whac-a-mole operating plan (0–2)
- 0: No reallocation plan; interventions are static one-time actions
- 1: Mentions reallocation or weekly review but without specific triggers (e.g., “if fill rate drops below X, shift incentives to supply”) or a decision log template
- 2: Weekly reallocation plan with named levers (e.g., incentive budgets, ops attention, marketing spend), explicit triggers for rebalancing (metric thresholds per segment), and a decision log format tracking what was changed and why

## 8) Measurement + instrumentation (0–2)
- 0: No measurement plan; assumes data is available without specifying sources or tracking
- 1: Metrics are listed but without specifying data sources, event definitions, update frequency, or instrumentation gaps; no dashboard/alert design
- 2: Specifies dashboards/alerts with refresh cadence; maps each metric to an event/table and data source; identifies instrumentation gaps with a plan to close them (owner, timeline if known)

## 9) Risks/open questions/next steps (0–2)
- 0: Missing entirely or a single generic line (e.g., “there are risks to consider”)
- 1: Present but generic (e.g., “supply may not respond to incentives”); no second-order effects; next steps are vague (“continue monitoring”)
- 2: At least 3 specific risks including second-order effects (e.g., “subsidizing supply in City A may cannibalize City B”); concrete open questions with owners; an unblocked 2-week plan with specific actions, owners, and dates

