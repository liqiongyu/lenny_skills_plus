# Bulk CSV Import for Admins: 4-Week Scoped Plan

## Context

Admins need to bulk-import data via CSV. We have 4 weeks (20 working days). This document cuts scope to a shippable MVP, identifies the riskiest parts, and includes a Wizard-of-Oz validation plan for those risks.

---

## 1. Full Feature Wish List (Unscoped)

Before cutting, here is the universe of things "bulk CSV import" could mean:

1. File upload UI (drag-and-drop, file picker)
2. CSV parsing and validation (encoding, delimiters, escaping)
3. Column mapping (map CSV headers to system fields)
4. Data validation (types, formats, required fields, uniqueness constraints)
5. Duplicate detection and merge/skip/overwrite strategies
6. Relationship resolution (e.g., CSV references a team name that must exist)
7. Dry-run / preview mode (show what will happen before committing)
8. Batch processing for large files (100K+ rows)
9. Progress indicator and background processing
10. Error report generation (downloadable CSV of failed rows with reasons)
11. Undo / rollback capability
12. Import history and audit log
13. Template download (pre-formatted CSV with correct headers)
14. Support for multiple entity types (users, products, orders, etc.)
15. Scheduled / recurring imports
16. API-based import (headless, no UI)

---

## 2. Scope Cut: What Ships in 4 Weeks

### Guiding Principles for Cutting

- **One entity type only.** Pick the highest-value one (likely "users" or "contacts"). Supporting multiple entity types multiplies every decision.
- **Happy path first.** Nail the core flow before handling edge cases.
- **Fail loudly, not silently.** It is better to reject a bad row and tell the admin why than to silently import garbage.
- **Manual beats automated for now.** Anything we can do with a human in the loop for the first 2 months is not worth automating in Week 1.

### In Scope (MVP)

| # | Feature | Week | Notes |
|---|---------|------|-------|
| 1 | **Template CSV download** | 1 | Pre-formatted file with correct headers and 2-3 example rows. Reduces support burden enormously. |
| 2 | **File upload UI** | 1 | Simple file picker. No drag-and-drop. Max file size: 5,000 rows (hard cap). |
| 3 | **CSV parsing** | 1 | UTF-8 only. Comma-delimited only. Reject anything else with a clear error. |
| 4 | **Column auto-mapping** | 1-2 | Auto-match CSV headers to system fields by exact name match. Manual re-mapping via dropdowns for mismatches. |
| 5 | **Row-level validation** | 2 | Type checks, required-field checks, format checks (email regex, phone format). No uniqueness check against DB yet. |
| 6 | **Dry-run preview** | 2-3 | Show first 20 rows with pass/fail status per row. Admin confirms before committing. |
| 7 | **Synchronous import (commit)** | 3 | On confirmation, insert valid rows. Skip invalid rows. No background job needed at 5K row cap. |
| 8 | **Error report download** | 3 | CSV of failed rows with a "reason" column appended. Admin can fix and re-upload. |
| 9 | **Basic import history** | 4 | Log: who imported, when, how many rows succeeded/failed. No undo. |
| 10 | **End-to-end testing and polish** | 4 | Edge cases, error messages, loading states, empty states. |

### Out of Scope (Explicitly Deferred)

| Feature | Why Cut | When to Revisit |
|---------|---------|-----------------|
| Duplicate detection / merge strategies | High complexity, needs product decisions on conflict rules | Month 2, after observing real admin behavior |
| Relationship resolution | Requires foreign-key lookups, error UX for missing refs | Month 2 |
| Large file support (>5K rows) | Needs background jobs, progress UI, failure recovery | Month 2-3, based on demand |
| Drag-and-drop upload | Nice-to-have, file picker works fine | Anytime, low effort |
| Multiple entity types | Multiplies scope by N | After MVP proves value |
| Undo / rollback | Extremely complex (cascading deletes, state restoration) | Month 3+, maybe never |
| Scheduled / recurring imports | Different feature entirely (integration, not import) | Quarter 2 |
| API-based import | No admin UI needed; different user, different flow | Quarter 2 |
| Non-UTF-8 / TSV / Excel support | Encoding detection is a rabbit hole | Month 2, if support tickets demand it |

---

## 3. Week-by-Week Execution Plan

### Week 1: Foundation

- **Backend:** CSV parsing service (UTF-8, comma-only). Column-mapping logic. Validation framework (pluggable per-field validators).
- **Frontend:** Upload page. Template download button. Column-mapping UI (dropdowns).
- **Deliverable:** Admin can upload a CSV, see mapped columns, get parse errors.

### Week 2: Validation + Preview

- **Backend:** Wire up field-level validators (email, phone, required, max-length). Return structured validation results.
- **Frontend:** Dry-run preview table (first 20 rows, color-coded pass/fail, per-cell error tooltips).
- **Deliverable:** Admin sees exactly what will import and what won't before committing.

### Week 3: Import + Error Report

- **Backend:** Commit endpoint (insert valid rows, skip invalid). Error report generation (CSV).
- **Frontend:** Confirm button, success summary screen, error CSV download link.
- **Deliverable:** End-to-end working import flow.

### Week 4: Polish + History + Ship

- **Backend:** Import history table and API. Hardening (rate limiting, file size enforcement, timeout protection).
- **Frontend:** Import history page. Error message polish. Empty states. Loading states.
- **QA:** Edge case testing (empty file, all-invalid file, 5K row file, unicode content, quoted commas in fields).
- **Deliverable:** Shippable MVP.

---

## 4. Risk Register

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|------------|--------|------------|
| R1 | Admins upload files with unexpected encodings / delimiters | High | Medium | Hard-cap to UTF-8 + comma. Provide template. Clear error on mismatch. |
| R2 | Column mapping is confusing; admins map fields wrong | High | High | **Wizard-of-Oz validation target.** See below. |
| R3 | Validation rules are incomplete; bad data gets in | Medium | High | **Wizard-of-Oz validation target.** See below. |
| R4 | Admins expect duplicate detection that doesn't exist | High | Medium | Clear messaging in UI: "This import will create new records. It will not update existing ones." |
| R5 | Performance at 5K rows is too slow for synchronous processing | Low | Medium | Benchmark by end of Week 2. If >10s, add a simple polling mechanism in Week 3. |
| R6 | Admins need to import >5K rows | Medium | Low | Communicate limit clearly. Offer to split files. Revisit in Month 2. |

---

## 5. Wizard-of-Oz Validation Plan

The idea: before building the expensive/risky parts, simulate them with a human behind the curtain to validate that our design actually solves admin problems.

### WoZ Test 1: Column Mapping UX (Targets Risk R2)

**What we're testing:** Can admins correctly map their CSV columns to our system fields without help? Is auto-mapping sufficient, or do they get confused?

**Setup (do in Week 1, before building the real UI):**
1. Create a clickable Figma prototype of the column-mapping screen.
2. Prepare 3 sample CSVs with varying header names:
   - **Easy:** Headers exactly match system fields ("First Name", "Email", "Phone").
   - **Medium:** Close but not exact ("fname", "email_address", "tel").
   - **Hard:** Ambiguous ("Column A", "Column B", "Column C").
3. Recruit 5 admins (existing customers, or internal ops team as proxy).

**Test protocol:**
1. Give each admin a CSV and ask them to "import these users."
2. Show them the Figma prototype with auto-mapped columns.
3. For the "Medium" and "Hard" CSVs, a human operator behind the scenes manually adjusts the auto-mapping suggestions in real time (simulating a smarter matching algorithm).
4. Observe: Do admins notice the mapping? Do they verify it? Do they change anything? Where do they get stuck?

**Success criteria:**
- 4/5 admins complete mapping correctly within 60 seconds for the Easy CSV.
- 3/5 admins complete mapping correctly within 2 minutes for the Medium CSV.
- If the Hard CSV stumps everyone, we know we need better instructions, not a smarter algorithm.

**Decision this informs:**
- If auto-mapping + dropdowns works well: build as planned.
- If admins ignore the mapping step entirely: make it a required confirmation step with a "does this look right?" prompt.
- If admins struggle with non-exact headers: invest in fuzzy matching (Week 2 stretch goal) or improve the template download to reduce the problem.

### WoZ Test 2: Validation & Error Resolution (Targets Risk R3)

**What we're testing:** When rows fail validation, can admins understand why and fix them? Is our error report useful?

**Setup (do in Week 2, before building error report download):**
1. Take a real-ish CSV with 50 rows. Seed 10 rows with intentional errors:
   - Missing required fields (2 rows)
   - Invalid email format (2 rows)
   - Phone number with wrong format (2 rows)
   - Value too long for field (2 rows)
   - Ambiguous errors (duplicate-ish data, edge case formats) (2 rows)
2. Create a mock preview screen (spreadsheet or simple HTML page) showing the validation results.
3. Create a mock error CSV with a "reason" column.

**Test protocol:**
1. Show admin the preview screen with 10 flagged rows.
2. Ask: "What would you do next?"
3. Give them the error CSV. Ask them to fix the errors and describe what they would re-upload.
4. A human operator watches and notes where admins get confused, misunderstand error messages, or give up.

**Success criteria:**
- 4/5 admins can identify and fix at least 7/10 errors without asking for help.
- Average time to understand an error message is under 15 seconds.
- No admin misinterprets an error message in a way that would make the data worse.

**Decision this informs:**
- If error messages are clear: ship as designed.
- If admins struggle with specific error types: rewrite those messages, add examples in the error CSV, or add inline help.
- If admins don't understand the error CSV concept at all: consider an in-app "fix and retry" flow instead (scope increase, but important to know early).

### WoZ Test 3: "What Happens to Duplicates?" (Targets Risk R4)

**What we're testing:** Do admins understand that this import creates new records only? What do they actually expect?

**Setup (do in Week 1-2, lightweight):**
1. Interview 5 admins (can overlap with WoZ Test 1 participants).
2. Scenario: "You imported 100 users last week. You now have an updated CSV with 120 users, including the original 100 with some field changes. What do you expect to happen when you import it?"

**Test protocol:**
1. Open-ended question first. Let them describe their expectation.
2. Then show them the proposed behavior: "The system will create 120 new records. The original 100 will remain, resulting in duplicates."
3. Observe reaction. Ask: "Is this acceptable? What would you do instead?"

**Success criteria:**
- This is a learning test, not a pass/fail. We want to know the distribution of expectations.

**Decision this informs:**
- If most admins expect "create only" behavior: our MVP is fine, ship it.
- If most admins expect "upsert" (update existing, create new): we need to either (a) build basic duplicate detection sooner, or (b) add very prominent warnings and documentation.
- If admins are split: add a clear modal before import that says "This will create N new records" with a "What about existing records?" help link.

---

## 6. Key Technical Decisions (Pre-Decided to Save Time)

| Decision | Choice | Rationale |
|----------|--------|-----------|
| File size limit | 5,000 rows | Keeps processing synchronous. Covers 95% of real admin use cases. |
| Encoding | UTF-8 only | Avoids encoding detection complexity. Template download ensures compliance. |
| Delimiter | Comma only | Excel and Google Sheets both export comma-delimited CSV by default. |
| Processing model | Synchronous (request/response) | At 5K rows, processing takes <5 seconds. No need for background jobs. |
| Error handling | Skip invalid rows, import valid ones | Admins want partial success, not all-or-nothing. Confirmed by common patterns. |
| Entity type | Users/Contacts (pick one) | Highest admin request volume. Most standardized field set. |

---

## 7. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Admin adoption | 30% of admins who currently submit bulk data via support tickets use self-serve import within 60 days | Analytics + support ticket volume |
| Import success rate | >80% of rows in a typical upload pass validation on first attempt | Backend logging |
| Time to complete import | <5 minutes from upload to confirmation for a 500-row file | Analytics |
| Support ticket reduction | 40% reduction in "please import this data for me" tickets within 60 days | Support system metrics |
| Error resolution rate | >70% of admins who get an error report re-upload a corrected file | Analytics |

---

## 8. What "Done" Looks Like at Week 4

An admin can:

1. Download a CSV template with the correct headers and example data.
2. Fill in their data (up to 5,000 rows).
3. Upload the file through a simple file picker.
4. See their CSV columns auto-mapped to system fields (and manually adjust if needed).
5. Preview the first 20 rows with clear pass/fail indicators and error explanations.
6. Confirm the import and see a summary (X succeeded, Y failed).
7. Download a CSV of failed rows with reasons, fix them, and re-upload.
8. See a history of past imports.

What an admin cannot do (yet): update existing records, import more than 5,000 rows at once, import non-user entity types, undo an import, or schedule recurring imports.

---

## 9. Open Questions to Resolve in Week 1

1. **Which entity type ships first?** (Recommendation: Users/Contacts. Validate with product lead.)
2. **What are the exact required vs. optional fields?** (Need the field spec from the data model owner.)
3. **Who are our 5 WoZ test participants?** (Need to recruit by end of Day 2.)
4. **What is the current volume of "import this for me" support tickets?** (Need baseline from support team.)
5. **Is there an existing admin UI framework/design system we must use?** (Affects frontend timeline.)
