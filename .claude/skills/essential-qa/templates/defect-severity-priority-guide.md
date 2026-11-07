# Defect Severity and Priority Guide

Use this guide when a defect needs a consistent triage recommendation. If the project or organization already defines severity and priority levels, follow that taxonomy instead and record any mapping. This guide is a fallback, not a replacement for an incident, security, privacy, or safety-response process.

## Keep severity and priority separate

- **Severity describes impact:** how harmful the defect is when it occurs, considering affected functionality, users, data, security, and business outcomes.
- **Priority describes urgency:** how soon the defect should be investigated, fixed, mitigated, or scheduled, considering severity, exposure, active customer impact, deadlines, workarounds, and release context.

Do not calculate priority from severity, or severity from the risk score. A defect can have high severity but lower immediate priority when exposure is very limited and a safe workaround exists. A lower-severity issue can still need urgent attention because of a fixed deadline or a high-visibility release. Explain any apparent mismatch.

## Severity scale

Rate the credible impact of the defect when it manifests. Record the affected users, workflow, data, and scope that support the rating.

| Level | Name | Rating anchor |
|---|---|---|
| **S1** | Critical | A critical service or journey is unavailable for a broad or essential user group; the defect causes or risks serious data loss/corruption, unauthorized access, significant privacy/security exposure, financial harm, or an irreversible action; no safe workaround exists. |
| **S2** | High | A major feature or important journey is materially impaired for many users or a significant segment; important data or processing may be incorrect but impact is bounded or recoverable; workaround is limited or costly. |
| **S3** | Medium | A specific function or subset of users is affected; core service remains usable; a practical workaround exists; no serious data, security, or financial consequence is evidenced. |
| **S4** | Low | Cosmetic, wording, layout, or minor usability issue with no material effect on core functionality, data integrity, security, or business processing. |

Do not assign S4 simply because a defect is hard to reproduce or affects few known reports. If the possible consequence is serious but scope or evidence is unclear, record the uncertainty and seek triage rather than minimizing the severity.

## Priority scale

Recommend urgency based on current exposure and the decision context. Priority is normally confirmed by the product, engineering, incident, or release owner.

| Level | Name | Rating anchor |
|---|---|---|
| **P1** | Urgent | Immediate investigation or mitigation is warranted: serious impact is active or imminent, a critical journey is broadly blocked, a severe security/privacy/data issue may be exposed, or delay creates unacceptable harm. Follow the applicable incident process. |
| **P2** | High | Address in the current release or next planned fix window; important user workflows are materially affected, exposure is meaningful, or the workaround is inadequate. |
| **P3** | Normal | Schedule in a planned iteration or maintenance window; impact is bounded and a reasonable workaround or acceptable temporary behavior exists. |
| **P4** | Low | Defer to backlog or opportunistic cleanup; impact is minor, exposure is low, and there is no material deadline or operational risk. |

These anchors do not establish a universal response-time SLA. Use the team's agreed service levels and release policy when available. Do not call a defect a release blocker unless an agreed criterion or authorized owner establishes that decision.

## Triage procedure

1. **Confirm the report.** Capture the affected application/build, environment, user role, preconditions, steps, expected behavior, actual observation, and evidence. Separate a reproduced defect from an unverified report.
2. **Establish scope.** Record affected workflows, user groups, frequency or exposure if known, data involved, and whether impact is ongoing. Do not infer population or frequency from a single report.
3. **Rate severity.** Apply the S1–S4 anchors to the demonstrated or credible impact. State the evidence and assumptions.
4. **Recommend priority.** Apply the P1–P4 anchors using current exposure, workaround, deadlines, release context, and operational risk. State why the issue needs that urgency.
5. **Record confidence and ownership.** Mark the classification **CONFIRMED** when supported by sufficient evidence, **PROVISIONAL** when based on incomplete but stated assumptions, or **NEEDS TRIAGE** when essential context is missing. Identify the decision owner when known.
6. **Reassess when facts change.** Update the rating if reproduction, affected scope, workaround, business timing, or impact changes.

If severity cannot be supported, use **UNASSESSED**. If priority cannot be recommended, use **UNASSIGNED**. Do not silently default either to the lowest level.

## Security, privacy, safety, and data incidents

If a report suggests unauthorized access, exposed personal data, active exploitation, safety risk, or serious data corruption:

- follow the organization's security, privacy, safety, or incident-response process;
- preserve relevant evidence without spreading sensitive content;
- do not perform intrusive reproduction or access data beyond the user's authorization; and
- do not disclose exploit details or secrets in a general QA report.

The normal defect rubric does not replace specialist incident handling.

## Record

| Defect ID | Summary | Severity | Severity rationale / evidence | Priority | Priority rationale / deadline | Confidence | Owner / disposition |
|---|---|---|---|---|---|---|---|
| BUG-001 | | UNASSESSED | | UNASSIGNED | | NEEDS TRIAGE | |

Keep severity, priority, confidence, and risk score as separate fields. Severity is impact, priority is urgency, confidence describes how well the classification is supported, and a risk score is a separate test-planning aid.
