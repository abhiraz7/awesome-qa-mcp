---
name: risk-based-testing
description: identify, compare and prioritize software testing risks so qa effort focuses on the failures that matter most.
---

# risk-based testing

help the team decide what deserves testing first and why. do not use risk labels as decoration or treat a score as objective truth.

## workflow

1. define the feature, system boundary, users and business purpose.
2. identify credible failure modes across behaviour, data, permissions, integrations, operations and user experience as relevant.
3. estimate impact if each failure occurs. consider users affected, financial or operational loss, safety, privacy, compliance and reputation.
4. estimate likelihood using available evidence such as complexity, change size, defect history, usage, dependencies and uncertainty.
5. consider exposure: how often the path is used and how easily the failure can be triggered.
6. prioritize risks using a simple, explained scale. state when ratings are subjective or information is missing.
7. map high-priority risks to verification activities and evidence.
8. revisit priorities when new information, defects or changes emerge.

## useful output

use a concise table with risk or failure scenario, affected users or process, impact, likelihood and rationale, priority, suggested verification and evidence needed.

## guidance

- explain the reasoning behind priority rather than presenting unexplained numbers.
- avoid false precision. do not imply that a 1–5 score is a measured probability.
- include low-frequency, high-impact failures where appropriate.
- distinguish product risk from delivery risk and test execution risk.
- account for what is not known.
- do not equate high test-case count with high risk coverage.
