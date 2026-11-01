---
name: requirement-analysis
description: analyze user stories, requirements and acceptance criteria to find ambiguity, missing rules, dependencies, risks and useful clarification questions before testing.
---

# requirement analysis

help the tester understand what the system is expected to do and what needs clarification before test design begins.

## workflow

1. identify the feature, user, business goal and stated scope.
2. extract explicit requirements and acceptance criteria without changing their meaning.
3. identify ambiguous terms, missing states, contradictory rules and unstated assumptions.
4. consider roles, permissions, data, integrations, error handling, boundaries and state transitions where relevant.
5. identify risks if the requirement is misunderstood or implemented incorrectly.
6. prepare focused questions for the product owner or business analyst.
7. when asked to proceed without answers, record assumptions and explain how they affect coverage.

## output

organize findings into:
- understood behaviour
- acceptance criteria and rules
- ambiguities and gaps
- assumptions
- dependencies and affected areas
- risk areas
- clarification questions
- suggested testing focus

do not invent expected behaviour to fill gaps. distinguish a requirement defect from a possible implementation defect. do not generate a full test suite unless the user asks for test design.
