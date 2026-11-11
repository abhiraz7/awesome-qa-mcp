# QA Risk Assessment Guide

Use this guide to make risk prioritization consistent and explainable. Score a risk using the impact and likelihood anchors below, record the rationale, and keep risk priority separate from test execution status.

## Impact (1–3)

- **1 — Low:** contained inconvenience or cosmetic issue; no meaningful data, security, or critical-workflow consequence; a practical workaround exists.
- **2 — Moderate:** a feature or journey is materially degraded for some users, or a recoverable data/function issue occurs; a workaround may exist.
- **3 — High:** a critical journey is unavailable, impact is broad, or the scenario could affect security/privacy, financial outcomes, or irreversible actions.

## Likelihood (1–3)

- **1 — Unlikely:** available evidence suggests the failure is uncommon; no known trigger or recent related signal is present.
- **2 — Plausible:** complexity, a recent change, weak coverage, or related behavior gives a credible reason to test for it.
- **3 — Likely:** the failure has been observed, repeatedly reported, or is strongly indicated by a known defect, incident, or direct change.

## Score and priority

Calculate **risk score = impact × likelihood**:

| Score | Priority |
|---:|---|
| 6 or 9 | High |
| 3 or 4 | Medium |
| 1 or 2 | Low |

If impact or likelihood cannot be assessed from available context, mark the rating **UNASSESSED** rather than silently assigning 1. If a provisional score is still useful, state the assumption and keep the rating provisional. This score is a prioritization aid, not an objective guarantee.

## Apply the rating

1. State the risk in terms of a user journey, requirement, failure mode, or business consequence.
2. Assign impact and likelihood using the anchors above; cite the known signal or explain the assumption.
3. Calculate the score and priority.
4. Map the risk to one or more stable check IDs.
5. Revisit the rating when new evidence, a defect, or a scope change changes the assumptions.

Do not use a low score to dismiss security, privacy, financial, or irreversible-action risks without explaining the rationale. Do not treat an unknown rating as low. Risk priority describes what to test first; it does not prove that a check ran or passed.

## Record

| Risk ID | Risk / failure mode | Impact | Likelihood | Score | Priority | Rationale / evidence | Check IDs |
|---|---|---:|---:|---:|---|---|---|
| RISK-001 | | | | | | | |
