# QA Exit Decision Guide

Use this guide to turn check-level results into a transparent overall QA recommendation. It is for release validation, broad multi-check work, or an explicit request for a go/no-go assessment; do not force a formal decision record onto a single quick check.

An overall QA recommendation is not release authorization. The responsible product, engineering, or risk owner makes the release decision and accepts residual risk.

## Evidence required before deciding

Review the following before assigning a recommendation:

- Agreed scope, build/environment, and acceptance or exit criteria.
- Requirement-to-test map, especially critical journeys and high-risk items.
- Individual check statuses and the evidence supporting each PASS or FAIL.
- Confirmed defects, unresolved issues, and their demonstrated impact.
- BLOCKED, NOT RUN, and NEEDS REVIEW checks.
- Coverage gaps, explicit exclusions, assumptions, and residual risks.

If criteria or criticality were not supplied, state the assumption or mark the decision INCONCLUSIVE. Do not silently invent a release gate.

## Decision categories

Apply the categories in the precedence order below. A known blocking failure takes precedence over missing evidence; absent a known blocker, insufficient evidence for critical scope prevents a readiness recommendation.

### NOT READY

Use when there is a confirmed failure against an agreed release-blocking criterion, a confirmed issue that materially prevents a critical user journey, or another explicit exit criterion is unmet.

- Name the failed criterion/check and cite the observation or evidence.
- Distinguish a confirmed failure from a suspected cause.
- Do not label an issue release-blocking solely from an inferred severity; use the agreed criterion or record who must make that decision.

### INCONCLUSIVE

Use when no confirmed blocking failure is established, but available evidence cannot support a readiness recommendation—for example:

- a critical acceptance criterion is BLOCKED, NOT RUN, or NEEDS REVIEW;
- critical requirements are ambiguous or unmapped;
- the environment, data, or test access prevents a meaningful check; or
- evidence is missing, contradictory, or too weak to verify critical behavior.

State exactly what evidence or decision is needed to resolve the uncertainty. A test being unavailable is not a PASS.

### READY WITH RISKS

Use when the agreed critical acceptance criteria are verified and no known release-blocking failure remains, but non-critical defects, coverage gaps, exclusions, or residual risks remain.

- List each remaining issue or risk and its impact.
- Identify the required disposition, risk owner, or acceptance decision when known.
- If risk acceptance has not been recorded, say that it is pending; do not imply it has been accepted.

### READY FOR QA SIGN-OFF REVIEW

Use only when all of the following are supported by the record:

- agreed critical acceptance criteria are verified;
- agreed high-risk coverage is completed, or any exception is explicitly dispositioned;
- no known release-blocking failure remains;
- the evidence is sufficient and traceable; and
- residual risks, exclusions, and limitations are documented.

This means the evidence is ready for the responsible person to review. It does not mean the application is defect-free or that release approval has been granted.

## Decision procedure

1. Check for a confirmed failure against an agreed blocking criterion. If present, recommend **NOT READY**.
2. Otherwise, check whether critical scope can be verified from the available evidence. If not, recommend **INCONCLUSIVE** and identify the missing evidence.
3. If critical criteria are verified but non-critical issues, gaps, or residual risks remain, recommend **READY WITH RISKS** and state their disposition.
4. Recommend **READY FOR QA SIGN-OFF REVIEW** only when its conditions above are met.
5. If none of these conditions can be established, use **INCONCLUSIVE** rather than guessing.

Do not calculate an overall status by counting PASS/FAIL results or averaging risk scores. One critical failure can outweigh many passing checks, and a large number of PASS results does not compensate for an untested critical criterion.

## Record the recommendation

Include a short decision record in the QA summary:

- **Overall QA recommendation:**
- **Decision basis / agreed exit criteria:**
- **Critical criteria verified:**
- **Known blocking failures:**
- **BLOCKED / NOT RUN / NEEDS REVIEW in critical scope:**
- **Open non-critical issues or coverage gaps:**
- **Residual risks and disposition / owner:**
- **Evidence references:**
- **Limitations and next action:**

Use only the evidence actually available. Mark unknown fields as unknown or omit them.