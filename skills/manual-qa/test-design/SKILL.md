---
name: test-design
description: turn understood requirements and risks into clear, prioritized manual test conditions and test cases with observable expected results.
---

# test design

design tests that provide useful coverage of the stated behaviour and its risks. do not generate repetitive cases just to make the list look complete.

## workflow

1. confirm the requirement, acceptance criteria, scope and known assumptions.
2. identify behaviours, states, roles, data conditions, integrations and important transitions.
3. derive test conditions from normal use, invalid use, boundaries, permissions, error handling and recovery.
4. apply relevant techniques such as equivalence partitioning, boundary-value analysis, decision tables, state transitions and pairwise combinations.
5. prioritize tests using risk and explain the ordering.
6. define preconditions, data, actions and observable expected results.
7. identify dependencies, setup needs and areas that cannot be verified with the available access.
8. review for gaps, overlap and tests that do not produce a meaningful observation.

## output

choose a format suited to the request. a practical test case may include a short title, priority, requirement or risk covered, preconditions, test data, steps and expected result.

## quality checks

- expected results must be observable and traceable to a requirement or explicitly stated assumption.
- include negative and boundary conditions where relevant.
- avoid vague expectations such as "works correctly".
- avoid combining multiple unrelated assertions in one test.
- identify where exploratory testing is more useful than exhaustive scripted cases.
- do not invent product rules to fill requirement gaps.
