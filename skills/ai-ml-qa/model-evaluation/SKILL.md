---
name: model-evaluation
description: plan and interpret evaluations of machine learning model quality, robustness and regression using appropriate datasets, metrics and validation methods.
---

# model evaluation

help design a defensible evaluation for a machine learning model. first establish what the model is intended to predict or generate and what errors matter in its use context.

## workflow

1. define the task, target population, intended use and failure impact.
2. inspect dataset provenance, labeling quality, representativeness, leakage risks and split strategy.
3. select metrics that reflect the task and error costs.
4. establish baselines and, where appropriate, confidence intervals or statistical comparisons.
5. evaluate relevant slices such as user groups, languages, classes, environments and edge cases.
6. assess robustness to distribution shift, noisy inputs, missing values and adversarial examples where relevant.
7. compare model versions using consistent data and evaluation procedures.
8. communicate limitations, uncertainty and deployment risks.

## metric selection

choose metrics based on the task. for classification, consider precision, recall, f1, confusion matrix and calibration. for ranking, consider ranking metrics. for regression, consider error distributions and task-specific tolerances. for generative systems, use task-specific quality criteria and human evaluation where appropriate.

## boundaries

do not recommend a metric without explaining what it measures and what it misses. do not infer real-world performance from a single benchmark. watch for data leakage and unrepresentative test sets. do not claim fairness or robustness from aggregate scores alone.
