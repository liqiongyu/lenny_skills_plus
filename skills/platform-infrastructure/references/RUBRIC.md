# Rubric (score 1–5 each)

Target: average **≥ 4.0** with no critical 1s in Scope/Contracts or Execution Readiness.

## 1) Scope clarity
1 = vague; boundaries missing; no distinction from platform-strategy or technical-roadmaps
2 = scope stated but overlaps with neighboring skills are not addressed; “not in scope” is absent or generic
3 = mostly clear; some scope creep risk; at least one adjacent-skill redirect present
4 = clear scope with explicit “not in scope” items and redirects to 2+ neighboring skills
5 = crisp scope; clear “not in scope”; correct adjacent-skill routing for all confusable neighbors (platform-strategy, technical-roadmaps, managing-tech-debt, engineering-culture)

## 2) Actionability of deliverables
1 = generic advice; no concrete artifacts; output reads like a blog post
2 = some artifacts present but lack specifics (e.g., "improve reliability" without numbers or owners)
3 = artifacts exist but are thin or underspecified; tables/templates used but cells are vague
4 = artifacts are specific and structured; most have owners and measurable criteria
5 = artifacts are detailed enough to execute without a meeting; every deliverable has concrete numbers, owners, and acceptance criteria

## 3) Platformization rigor
1 = “make a platform” hand-waving; no specific capabilities named
2 = capabilities listed but without consumer count, API contract sketch, or migration approach
3 = identifies candidates but weak contracts/migration plan; consumers named but contracts are vague
4 = each candidate has consumers, a contract sketch, and a migration approach; some gaps in rollback or compatibility
5 = clear contracts, ownership, and migration/compat strategy per shared capability; rollback plan and backward-compatibility guarantees explicit

## 4) Quality attributes + measurability
1 = aspirational goals only ("be more reliable"); no numbers, no measurement plan
2 = some numeric targets stated but no measurement method or owner; privacy/safety absent
3 = some metrics/SLOs but gaps remain; measurement method exists for some but not all; at least one of privacy/safety/cost addressed
4 = most quality attributes have measurable targets, measurement methods, and owners; minor gaps in one area
5 = measurable targets, measurement method, and ownership for all dimensions (reliability, performance, privacy/safety, operability, cost); error budget policy defined

## 5) Scaling readiness
1 = reactive; no triggers/lead time; scaling discussed only in generalities
2 = a few limits named but no thresholds, no lead time estimates, no mitigation projects
3 = some limits listed; triggers unclear; lead times missing or generic (e.g., "weeks")
4 = doomsday clock present with thresholds and lead times for most limits; some mitigation projects lack owners
5 = doomsday clock with lead-time-aware triggers, owners, and mitigation projects for each limit; thresholds tied to monitoring/alerting

## 6) Instrumentation + analytics integrity
1 = client-SDK-centric without data-quality plan; no event schema or naming convention
2 = some events defined but no identity strategy, no QA checks, and no delivery guarantees
3 = mixed approach; identity/QA gaps; event naming exists but schemas are incomplete or not enforced
4 = server-side events defined with schemas and identity strategy; QA checks exist but are manual
5 = server-side canonical events, identity strategy, and automated data-quality checks; delivery guarantees and schema enforcement documented

## 7) Execution readiness
1 = no roadmap; no owners; no rollout/rollback; output is a wish-list
2 = roadmap present but milestones are vague, owners missing, and no dependency mapping
3 = roadmap exists but weak acceptance criteria/dependencies; some milestones have owners
4 = sequenced milestones with owners and dependencies; acceptance criteria present for most; rollout plan exists but rollback is thin
5 = sequenced milestones with owners, acceptance criteria, dependencies, and rollout/rollback; first milestone is executable this sprint

