# QA Evidence Record

Use this record for a scoped QA activity. Duplicate the check row for each scenario. Keep evidence traceable and redact secrets or personal data. Replace placeholders with observations; do not fill missing facts by guessing.

## Context

- **Task / feature:**
- **Requirement or source:**
- **Application / build:**
- **Environment:**
- **Role / account type:**
- **Execution date and time (timezone):**
- **Tools / method:**
- **Scope and constraints:**
- **Assumptions:**

## Risk rating guide

Use the anchored scales in the Essential QA skill and its [QA risk assessment guide](risk-assessment-guide.md). Record the reason for material ratings; do not treat an unknown impact or likelihood as a low score.

- **Impact:** 1 = contained/minor; 2 = material but limited or recoverable; 3 = critical, broad, security/privacy, financial, or irreversible consequence.
- **Likelihood:** 1 = unlikely based on available evidence; 2 = plausible due to complexity, change, weak coverage, or related signals; 3 = likely based on observed/repeated failure or a strong known signal.
- **Score:** impact × likelihood. **High:** 6 or 9; **Medium:** 3 or 4; **Low:** 1 or 2. Use **UNASSESSED** if either input is unknown, or mark a score provisional and state the assumption.

## Requirement-to-test map

Use the coverage states defined in the Essential QA skill. A mapped or planned check is not evidence that the requirement passed. Keep risk score and coverage state separate: risk expresses priority; coverage expresses test progress.

| Requirement / risk ID | Requirement or risk | Impact (1–3) | Likelihood (1–3) | Risk score | Priority / rationale | Check IDs | Coverage state | Gap / scope note |
|---|---|---:|---:|---:|---|---|---|---|
| REQ-001 | | | | | | QA-001 | MAPPED | |

## Check design and execution record

| Check ID | Preconditions / data | Action / steps | Expected result | Actual observation | Status | Evidence reference | Notes |
|---|---|---|---|---|---|---|---|
| QA-001 | | | | | NOT RUN | | |

Allowed statuses: **PASS**, **FAIL**, **BLOCKED**, **NOT RUN**, **NEEDS REVIEW**.

- Use **PASS** or **FAIL** only when the check was executed.
- For **BLOCKED**, state the blocker and what is needed to proceed.
- For **NEEDS REVIEW**, explain what is ambiguous and what judgment is required.
- For **NOT RUN**, record why it was not attempted when known.
- Reference screenshots, logs, traces, reports, or URLs where available. Do not paste secrets into the record.

## Defect notes

Complete for each actionable failure. Keep the defect ID linked to its originating check. Use the [defect severity and priority guide](defect-severity-priority-guide.md); follow an existing project taxonomy when supplied.

- **Defect ID / title:**
- **Related check ID:**
- **Environment / build:**
- **Preconditions and reproduction steps:**
- **Expected behavior:**
- **Actual behavior:**
- **Reproducibility:**
- **Affected users / workflow / data:**
- **Severity (S1–S4 or UNASSESSED):**
- **Severity rationale (impact):**
- **Priority (P1–P4 or UNASSIGNED):**
- **Priority rationale (urgency / deadline):**
- **Classification confidence (CONFIRMED / PROVISIONAL / NEEDS TRIAGE):**
- **Triage owner / disposition:**
- **Evidence:**
- **Root-cause hypothesis (if any; label as unconfirmed):**

Keep severity, priority, and the test-planning risk score separate. Severity describes impact; priority describes urgency; the risk score helps decide what to test.

## QA summary

For broad testing or release validation, use the [QA exit decision guide](qa-exit-decision-guide.md). The overall recommendation is evidence-based QA guidance, not release authorization.

- **Overall QA recommendation (NOT READY / INCONCLUSIVE / READY WITH RISKS / READY FOR QA SIGN-OFF REVIEW):**
- **Decision basis / agreed exit criteria:**
- **Scope and approach:**
- **Planned checks:**
- **Attempted checks:**
- **Result counts (PASS / FAIL / BLOCKED / NOT RUN / NEEDS REVIEW):**
- **Critical criteria verified:**
- **Known blocking failures:**
- **Critical checks BLOCKED / NOT RUN / NEEDS REVIEW:**
- **Requirements verified:**
- **Coverage gaps and exclusions:**
- **Open non-critical issues:**
- **Residual risks and disposition / owner:**
- **Key findings:**
- **Evidence references:**
- **Limitations and recommended next action:**

### Reporting integrity

Only report behavior supported by the recorded observations. Distinguish planned coverage from executed coverage. If a criterion, environment, timestamp, or evidence reference is unavailable, mark it unknown or omit it rather than inventing it. Do not infer release approval from a QA recommendation or from a high count of passing checks.
