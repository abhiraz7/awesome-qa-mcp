---
name: evidence-standards
description: define and assess evidence for qa findings, test outcomes and quality claims across manual, automated and ai/ml testing.
---

# evidence standards

help the tester make claims that are supported by observable evidence. keep facts, interpretations and hypotheses separate.

## evidence model

for each important finding, identify:
- **claim:** what is being asserted.
- **source:** where the evidence came from.
- **observation:** what the evidence directly shows.
- **interpretation:** what the observation may mean.
- **limitations:** what the evidence cannot establish.
- **next check:** what would increase confidence.

## discipline-specific guidance

- manual testing: record steps, environment, test data, expected result, actual result and relevant screenshots or recordings.
- automation: include test name, run context, assertion, logs, trace and failure artifacts where available.
- api and data testing: preserve request/response details, status, relevant headers, schema or query result, with secrets removed.
- ai/ml testing: preserve input, relevant context, model or application version, output, evaluator criteria, run count and scoring method.

## rules

1. never say a test passed or failed unless execution evidence supports that status.
2. distinguish a missing artifact from a failed test.
3. do not infer backend state from a screenshot or infer user-visible correctness from a database row alone.
4. redact credentials, personal data and other sensitive information.
5. preserve enough context to reproduce a finding without collecting unnecessary data.
6. label uncertain root causes as hypotheses.
7. explain when evidence is incomplete, inconsistent or not reproducible.

## reporting

use precise language: **verified** (directly supported), **observed** (seen in a specific run), **suspected** (plausible but unconfirmed), **not checked** (not verified) and **inconclusive** (evidence does not support a reliable conclusion).
