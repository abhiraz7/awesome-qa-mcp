---
name: automation-debugging
description: investigate automated test failures and flaky behaviour using failure artifacts, execution context and controlled experiments.
---

# automation debugging

help determine why an automated test failed. do not assume every failure indicates a product defect or that every intermittent failure is harmless flakiness.

## workflow

1. identify the test, framework, language, environment, build and run context.
2. classify the observed failure: assertion, locator, timeout, setup, test data, environment, network, dependency or runner.
3. inspect available evidence such as logs, stack traces, screenshots, traces, videos, network records and recent changes.
4. compare passing and failing runs when available.
5. form competing hypotheses and identify the smallest experiment that can distinguish them.
6. check whether the failure reproduces locally, in isolation, in parallel and in ci where practical.
7. recommend a focused fix and a regression check.

## common causes

examine unstable selectors, race conditions, inadequate synchronization, shared test data, order dependence, parallel execution, retries masking defects, environment drift, external service instability, resource limits and network variability.

## output

summarize the failure signature, evidence reviewed, plausible causes, confidence, next diagnostic step and recommended fix.

## boundaries

do not label a test flaky from one failure. do not recommend arbitrary sleeps as a default fix. do not weaken assertions or increase retries merely to make a pipeline green. state clearly when logs or artifacts are missing.
