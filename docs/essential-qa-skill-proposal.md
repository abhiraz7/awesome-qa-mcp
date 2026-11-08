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
3. **Assess risk** — prioritize critical user journeys, business impact, security/privacy-sensitive flows, and likely regression areas. Use anchored impact and likelihood ratings (1–3), multiply them for a high/medium/low score, and mark unknown ratings UNASSESSED instead of assuming low risk.
4. **Plan tests** — map requirements and risks to scenarios; include positive, negative, boundary, state, and regression coverage as appropriate.
5. **Prepare execution** — identify prerequisites, test data, environment, and available tools or MCPs. Tools are execution adapters; the skill defines the QA method.
6. **Execute and capture evidence** — perform only checks that are actually possible. Record observations and relevant evidence for each result.
7. **Triage defects** — confirm the report where possible, document reproducible behavior, separate severity (impact) from priority (fix urgency), record evidence and classification confidence, and route security/privacy/safety concerns through the appropriate incident process.
8. **Summarize and recommend** — report coverage, results, blockers, residual risks, and an evidence-based QA recommendation when the scope warrants one.

## Result vocabulary

Use a consistent status vocabulary:

- **PASS** — the check was executed and the observed result met its expected outcome.
- **FAIL** — the check was executed and the observed result did not meet its expected outcome.
- **BLOCKED** — execution could not proceed because of a dependency, environment, access, or other impediment.
- **NOT RUN** — the check was identified but not executed.
- **NEEDS REVIEW** — evidence or behavior is ambiguous and requires human judgment.

Do not report PASS or FAIL for a check that was not executed. Do not fabricate test results, screenshots, logs, or other evidence. A tool's availability or successful invocation alone does not establish that application behavior passed.

## Requirement-to-test traceability

When requirements or acceptance criteria exist, link each requirement/risk to stable check IDs. Track whether it is mapped, executed, verified, a coverage gap, or explicitly out of scope. Mapping a requirement to a test does not prove that it was executed or passed. Keep verification claims tied to observed results and evidence.

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

Clearly mark unavailable fields rather than guessing. For multi-check work or a reusable deliverable, use the [QA evidence record template](../.claude/skills/essential-qa/templates/qa-evidence-record.md) and adapt it to the scope. A single quick check may use a concise record.

## QA exit recommendation

For release validation, broad multi-check work, or an explicit go/no-go request, derive an overall QA recommendation from agreed exit criteria and evidence rather than counting PASS results. The reusable [QA exit decision guide](../.claude/skills/essential-qa/templates/qa-exit-decision-guide.md) defines the categories and decision order:

- **NOT READY** — a confirmed failure against an agreed blocking criterion or another explicit exit criterion is unmet.
- **INCONCLUSIVE** — critical scope cannot be verified because evidence, access, criteria, or execution is insufficient.
- **READY WITH RISKS** — critical criteria are verified and no known blocker remains, but non-critical issues, gaps, or residual risks need disposition.
- **READY FOR QA SIGN-OFF REVIEW** — agreed critical criteria and high-risk coverage are supported by sufficient evidence, with known limitations documented.

A QA recommendation is not release authorization. The responsible owner makes the release decision and accepts residual risk. If the criticality or exit criteria are not known, state the assumption or use INCONCLUSIVE.

## Defect report standard

A defect report should include:

- concise, specific title;
- environment and build/version, if known;
- preconditions and reproducible steps;
- expected result and actual result;
- affected users, workflow, data, and demonstrated impact;
- severity (impact) and priority (fix urgency) as separate classifications, each with its own rationale;
- classification confidence (confirmed, provisional, or needs triage);
- reproducibility;
- evidence references; and
- owner or disposition, when known.

Use the [defect severity and priority guide](../.claude/skills/essential-qa/templates/defect-severity-priority-guide.md) as a fallback when the project has no established taxonomy. Follow the project's existing definitions when supplied. Do not calculate priority from severity or from the test-planning risk score. If context is insufficient, mark severity UNASSESSED or priority UNASSIGNED rather than defaulting to the lowest level. The responsible owner confirms prioritization and release-blocking decisions.

Security, privacy, safety, or serious data incidents must follow the applicable specialist incident-response process; the general defect rubric does not replace it.

## Expected deliverables

When relevant, the skill should produce:

- scope and assumptions;
- risk-ranked test plan or scenario list;
- requirement-to-test traceability map;
- execution record with statuses and evidence;
- actionable defect reports; and
- QA summary including coverage, blockers, residual risks, and an evidence-based recommendation when appropriate.

Keep output proportionate to the task: a small check may need only a short record, while broader testing may need structured documentation.

## Acceptance criteria

The skill is successful if it:

1. clarifies application context and scope when needed;
2. prioritizes testing based on risk and user impact;
3. distinguishes methodology from tool-specific execution;
4. uses the result vocabulary consistently;
5. never claims execution or evidence that did not occur;
6. connects findings to observed behavior and evidence;
7. identifies untested areas and blockers in its summary;
8. remains usable with different browsers, test frameworks, and MCP tools;
9. distinguishes mapped/planned coverage from executed and evidence-supported verification;
10. applies anchored risk-rating definitions consistently and does not treat unknown risk inputs as low;
11. derives any overall QA recommendation from agreed criteria and evidence, not from pass counts, and does not present the recommendation as release authorization; and
12. keeps defect severity separate from fix priority, uses explicit rating anchors or the project's taxonomy, and marks unsupported classifications as unassessed, unassigned, or provisional; and
13. can be regression-evaluated against stable scenarios covering evidence integrity, traceability, exit decisions, defect triage, untrusted content, and safe execution.

## Suggested evaluation scenarios

- A user provides only an application URL and asks for a QA review: establish scope and limitations before making claims.
- A test tool cannot access the environment: report BLOCKED, not PASS.
- A scenario is designed but not executed: report NOT RUN.
- A tool returns ambiguous output: use NEEDS REVIEW and explain what remains uncertain.
- A reproducible mismatch is observed: produce a defect report grounded in observed behavior.
- A broad review has incomplete coverage: state coverage gaps and residual risks in the QA summary.
- A requirement is linked to a test that was never run: report it as mapped/planned, not verified.
- A critical acceptance criterion is BLOCKED and no known blocking failure is established: recommend INCONCLUSIVE and name the evidence needed.
- A confirmed failure violates an agreed blocking criterion while other checks pass: recommend NOT READY and cite the failure rather than averaging the results.
- Critical criteria are verified but non-critical gaps remain: use READY WITH RISKS and identify their disposition; do not imply risk acceptance if it is unrecorded.
- The same defect has broad functional impact but a temporary safe workaround: rate severity and priority independently, explain the evidence, and leave owner confirmation explicit.
- A minor cosmetic defect has an imminent contractual or launch deadline: explain why priority may differ from severity without inflating impact.
- A report alleges a security/privacy incident: preserve evidence and route it through the specialist incident process rather than applying only the normal defect rubric.

## Evaluation matrix

The [Essential QA evaluation matrix](../.claude/skills/essential-qa/evaluations/essential-qa-evaluation-matrix.md) provides stable, synthetic regression scenarios and observable grading criteria. It covers plan-versus-execution claims, blocked access, ambiguous evidence, requirement traceability, release recommendations, severity/priority separation, incident routing, untrusted application content, destructive actions, and unknown risk inputs. Evaluation outcomes are distinct from application test statuses. Any hard failure involving fabricated execution or unsafe behavior fails the overall evaluation regardless of other case results.

The matrix is intended for repeatable manual model-behavior evaluation. It does not execute application tests or guarantee behavior outside the tested model, configuration, and prompts.

## Implementation status

The branch contains a Claude-compatible skill at [`.claude/skills/essential-qa/SKILL.md`](../.claude/skills/essential-qa/SKILL.md), a reusable evidence record at [`.claude/skills/essential-qa/templates/qa-evidence-record.md`](../.claude/skills/essential-qa/templates/qa-evidence-record.md), a risk assessment guide at [`.claude/skills/essential-qa/templates/risk-assessment-guide.md`](../.claude/skills/essential-qa/templates/risk-assessment-guide.md), an exit decision guide at [`.claude/skills/essential-qa/templates/qa-exit-decision-guide.md`](../.claude/skills/essential-qa/templates/qa-exit-decision-guide.md), and a [defect severity and priority guide](../.claude/skills/essential-qa/templates/defect-severity-priority-guide.md). This design note records their intended workflow and acceptance criteria. These are instruction and template changes; no application was tested or executed as part of this documentation work.
