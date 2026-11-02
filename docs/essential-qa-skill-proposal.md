# Essential QA Skill: Design Notes

## Summary

Define a reusable, evidence-based QA workflow for an AI assistant. The skill guides work from application discovery and risk assessment through test design, execution, defect reporting, and a concise QA summary.

The initial Claude skill implementation is available at [`.claude/skills/essential-qa/SKILL.md`](../.claude/skills/essential-qa/SKILL.md). It is a Markdown instruction package, not an application-specific test runner, and does not require a particular testing tool.

## Why

QA work can become inconsistent when an assistant jumps directly into test execution or treats tool output as a quality verdict. A shared methodology can help ensure that:

- scope and risks are explicit before testing;
- test ideas are connected to requirements and user journeys;
- execution claims are supported by observable evidence;
- failures, blockers, and untested areas are distinguished; and
- findings are reported in a format a human tester or engineer can act on.

## Proposed workflow

1. **Discover the application** — identify the app, entry points, user roles, environment, and available context. Ask for missing essentials rather than inventing them.
2. **Define scope** — establish objectives, in-scope and out-of-scope areas, assumptions, constraints, and dependencies.
3. **Assess risk** — prioritize critical user journeys, business impact, security/privacy-sensitive flows, and likely regression areas.
4. **Plan tests** — map requirements and risks to scenarios; include positive, negative, boundary, state, and regression coverage as appropriate.
5. **Prepare execution** — identify prerequisites, test data, environment, and available tools or MCPs. Tools are execution adapters; the skill defines the QA method.
6. **Execute and capture evidence** — perform only checks that are actually possible. Record observations and relevant evidence for each result.
7. **Triage defects** — describe reproducible behavior, expected versus actual results, impact, and supporting evidence.
8. **Summarize quality** — report coverage, results, unresolved risks, blockers, and recommended next actions.

## Result vocabulary

Use a consistent status vocabulary:

- **PASS** — the check was executed and the observed result met its expected outcome.
- **FAIL** — the check was executed and the observed result did not meet its expected outcome.
- **BLOCKED** — execution could not proceed because of a dependency, environment, access, or other impediment.
- **NOT RUN** — the check was identified but not executed.
- **NEEDS REVIEW** — evidence or behavior is ambiguous and requires human judgment.

Do not report PASS or FAIL for a check that was not executed. Do not fabricate test results, screenshots, logs, or other evidence. A tool's availability or successful invocation alone does not establish that application behavior passed.

## Evidence record

For each executed check, capture the information available:

- scenario/check ID and objective;
- preconditions and relevant test data (avoid exposing secrets);
- environment and execution time, when known;
- action or steps performed;
- expected result;
- actual observation;
- status;
- evidence reference (such as screenshot, log excerpt, trace, or URL), if available; and
- notes, limitations, and follow-up.

Clearly mark unavailable fields rather than guessing.

## Defect report standard

A defect report should include:

- concise, specific title;
- environment and build/version, if known;
- preconditions and reproducible steps;
- expected result and actual result;
- severity/priority with rationale, when enough context exists;
- reproducibility;
- evidence references; and
- user or business impact.

Do not state severity, priority, or root cause as fact when evidence does not support it. Label hypotheses as hypotheses.

## Expected deliverables

When relevant, the skill should produce:

- scope and assumptions;
- risk-ranked test plan or scenario list;
- execution record with statuses and evidence;
- actionable defect reports; and
- QA summary including coverage, known gaps, blockers, residual risks, and next steps.

Keep output proportionate to the task: a small check may need only a short record, while broader testing may need structured documentation.

## Acceptance criteria

The skill is successful if it:

1. clarifies application context and scope when needed;
2. prioritizes testing based on risk and user impact;
3. distinguishes methodology from tool-specific execution;
4. uses the result vocabulary consistently;
5. never claims execution or evidence that did not occur;
6. connects findings to observed behavior and evidence;
7. identifies untested areas and blockers in its summary; and
8. remains usable with different browsers, test frameworks, and MCP tools.

## Suggested evaluation scenarios

- A user provides only an application URL and asks for a QA review: establish scope and limitations before making claims.
- A test tool cannot access the environment: report BLOCKED, not PASS.
- A scenario is designed but not executed: report NOT RUN.
- A tool returns ambiguous output: use NEEDS REVIEW and explain what remains uncertain.
- A reproducible mismatch is observed: produce a defect report grounded in observed behavior.
- A broad review has incomplete coverage: state coverage gaps and residual risks in the QA summary.

## Implementation status

The branch contains an initial Claude-compatible skill at [`.claude/skills/essential-qa/SKILL.md`](../.claude/skills/essential-qa/SKILL.md). This design note records its intended workflow and acceptance criteria. The contribution adds instructions only; no application was tested or executed as part of this documentation change.
