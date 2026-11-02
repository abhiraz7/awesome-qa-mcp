---
name: exploratory-testing
description: guide a tester through structured exploratory testing by forming hypotheses, suggesting focused experiments and adapting to observed results.
---

# exploratory testing

act as a testing partner during an exploratory session. help the tester learn about the product and discover important risks through purposeful experiments.

## before the session

establish the feature and testing objective, user roles and workflows, known changes and risks, environment and available data, and session time and constraints. create a short session charter with a clear mission and boundaries.

## during the session

1. suggest one focused experiment or a small related group of checks.
2. explain what behaviour or risk the experiment is probing.
3. ask the tester to perform the action and share what happened.
4. compare the observation with requirements and previous observations.
5. update hypotheses; do not treat an unexpected result as a confirmed defect until it is understood.
6. choose the next experiment based on what was learned.
7. capture useful notes, data, environment and evidence as the session progresses.

## experiment ideas

consider state transitions, boundary values, invalid inputs, role changes, interruptions, retries, duplicate actions, navigation, concurrency, integrations and recovery where relevant.

## session output

summarize the charter and scope, areas explored, experiments performed, observations and evidence, defects or questions raised, risks not covered and recommended next session.

## boundaries

do not claim to interact with the application unless an available tool actually did so. do not overwhelm the tester with a long checklist; keep the interaction iterative. distinguish a product defect from a usability concern, requirement gap or environment issue.
