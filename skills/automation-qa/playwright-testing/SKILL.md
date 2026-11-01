---
name: playwright-testing
description: help qa engineers design, review, debug and maintain reliable playwright tests using sound test architecture and observable evidence.
---

# playwright testing

help the user build reliable and maintainable playwright tests. adapt examples to the language, framework and project conventions they provide.

## workflow

1. establish the application under test, language, playwright version, test runner and existing project conventions.
2. understand the user journey and the behaviour that needs verification.
3. recommend stable locators, preferably user-facing roles, labels and accessible names.
4. use assertions that verify observable outcomes rather than implementation details.
5. isolate test data and state; avoid dependencies on test execution order.
6. use fixtures, page objects or helper abstractions only when they improve clarity and maintenance.
7. account for loading, asynchronous behaviour, retries and cleanup without hiding real failures.
8. when debugging, inspect the failure message, trace, screenshot, video or relevant logs before proposing a root cause.

## review checklist

- does the test verify user-visible behaviour?
- are locators resilient and meaningful?
- are assertions specific and useful?
- can the test run independently and repeatedly?
- is test data controlled and cleaned up?
- are waits based on observable conditions rather than arbitrary sleeps?
- could the test pass while the feature is broken?
- does the test create avoidable flakiness or maintenance cost?

## boundaries

do not assume the repository's language, configuration or conventions. ask for relevant files or error output when needed. do not claim a test was run unless execution evidence is available. do not rewrite the framework when a focused test change is sufficient.
