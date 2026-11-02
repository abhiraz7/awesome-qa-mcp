---
name: ai-agent-testing
description: help test ai agents that plan tasks, call tools and interact with external systems, focusing on correctness, control, safety and recoverability.
---

# ai agent testing

help evaluate an agent as a system that interprets goals, plans actions, uses tools and responds to changing state. assess both the final result and the path taken to reach it.

## workflow

1. define the task, permitted actions, expected outcome and unacceptable outcomes.
2. map the agent's available tools, permissions, inputs and external dependencies.
3. create representative tasks with clear success criteria and relevant edge cases.
4. inspect planning, tool selection, arguments, call ordering, retries and handling of tool errors.
5. verify that actions are authorized, scoped and proportionate to the user's request.
6. test ambiguous instructions, missing information, conflicting tool results and interrupted workflows.
7. verify final state independently where evidence or an authorized integration permits.
8. record the trace needed to understand the decision and outcome.

## important test areas

test task completion, instruction adherence, correct tool selection and arguments, authorization and confirmation for consequential actions, resistance to prompt injection in untrusted tool output, duplicate actions and idempotency, timeouts and recovery, state consistency, truthful reporting, privacy and secret handling.

## boundaries

do not equate a plausible final response with successful execution. do not test destructive actions against real systems without explicit authorization and a safe environment. distinguish an agent reasoning error, tool failure and external system failure where evidence allows.
