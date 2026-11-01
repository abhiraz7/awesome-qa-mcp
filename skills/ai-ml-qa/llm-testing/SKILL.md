---
name: llm-testing
description: help qa engineers design and evaluate tests for llm-powered applications, including response quality, grounding, safety, consistency and regression.
---

# llm testing

help the tester evaluate an llm-powered feature as a probabilistic system. do not assume that one successful response proves the feature is reliable.

## workflow

1. identify the user task, intended behaviour, model or application context and failure impact.
2. define evaluation dimensions appropriate to the feature, such as relevance, correctness, completeness, instruction following, grounding, safety and latency.
3. build representative cases from normal use, edge cases, ambiguous inputs and adversarial inputs.
4. define expected properties and acceptable outcomes. use exact expected strings only when the requirement truly demands them.
5. identify which checks can be deterministic and which require human judgment or calibrated evaluators.
6. consider repeated runs, model/version changes, prompt changes and variation in outputs.
7. report failures with the input, relevant context, output, evaluation criteria and reproducibility information.
8. recommend regression thresholds only when there is a baseline and a defensible evaluation method.

## evaluation guidance

- separate retrieval failures, prompt/context failures, model reasoning failures and application integration failures where evidence allows.
- evaluate the complete user task, not just whether the response sounds plausible.
- test refusal behaviour and safe handling of harmful or out-of-scope requests where relevant.
- check whether claims are supported by supplied context or trusted sources.
- track latency and cost alongside quality when they affect the user experience.
- use representative datasets and document their limitations.

## boundaries

do not treat an llm judge as ground truth. do not claim a model is unbiased, safe or hallucination-free based on a small sample. do not invent evaluation scores or test results. state uncertainty and explain how to improve confidence.
