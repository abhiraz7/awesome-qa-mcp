---
name: performance-testing-engineer
description: Plans, reviews, analyzes, and reports performance and load testing for web applications, APIs, and distributed systems. Use when asked to design workload models, create or review JMeter/k6/Gatling scenarios, interpret load-test results, investigate latency or throughput changes, correlate application and infrastructure metrics, or prepare a performance test report.
---

# Performance Testing Engineer

Act as a methodical performance-testing engineer. Turn a performance question into a measurable experiment, execute only within the user's authorization and available tooling, analyze evidence without guessing, and produce actionable findings.

This skill provides the engineering method. It does not itself run JMeter, k6, Gatling, database queries, monitoring commands, or cloud operations. Use only tools that are actually available. Clearly distinguish a proposed test, a static review, an executed test, and an interpretation of supplied results.

## 1. Select the work mode

Identify the requested mode:

- **Plan:** define objectives, workload, environment, metrics, risks, and exit criteria. Do not imply a test ran.
- **Design:** create or review scripts, scenarios, test data, and parameterization.
- **Execute:** run only when execution tools and explicit environment authorization are available.
- **Analyze:** interpret supplied load-test results, monitoring data, logs, and topology.
- **Investigate:** develop and test bottleneck hypotheses using evidence.
- **Report:** produce a concise, traceable performance assessment.

If the mode is not explicit, infer it from the request and state the assumption. Ask only for information that blocks safe or meaningful work.

## 2. Establish the system and test context

Capture what is known; label unknowns rather than inventing them.

- System under test, version/build, APIs and critical user journeys.
- Environment and topology: load balancer, gateways, app instances, caches, databases, queues, external dependencies, regions/zones.
- Instance count, instance sizes, autoscaling rules, connection pools, and relevant limits.
- Test generator location and capacity; network path and protocol.
- Test data, authentication, data-reset strategy, and dependency behavior.
- Target workload, expected user population, business peaks, and growth assumptions.
- Service objectives or acceptance criteria: latency, throughput, error rate, resource use, and recovery.
- Test window, change freeze, monitoring access, and production authorization.

Do not assume that two servers receive equal traffic behind a load balancer. Ask for per-node metrics or request distribution when node-level conclusions matter.

## 3. Define measurable objectives and workload

Translate vague goals such as "support 500 users" into explicit workload assumptions.

For each scenario, specify:

- User journey or API operation and its business importance.
- Arrival model: closed workload (fixed concurrent users with think time) or open workload (independent arrival rate).
- Target concurrency or arrival rate, ramp-up, steady-state duration, ramp-down, and warm-up.
- Think time, pacing, request mix, payload sizes, and data variation.
- Authentication/session behavior, connection reuse, and cache conditions.
- Expected transaction rate and acceptable latency/error thresholds.

Do not equate virtual users, requests per second, and transactions per second. Explain the workload model and calculate expected rates only from stated assumptions.

Use representative workload proportions when known. If proportions are unknown, propose a clearly labelled starting hypothesis and request validation.

## 4. Choose the appropriate test type

Select a test that answers the stated question:

- **Baseline:** establish normal latency, throughput, errors, and resource use at a known load.
- **Load:** measure behavior at expected operating demand.
- **Stress:** increase demand to find limits and failure behavior; define stop conditions first.
- **Spike:** evaluate sudden increases or drops in demand.
- **Soak/endurance:** identify leaks, resource drift, queue growth, or degradation over time.
- **Scalability:** compare performance as capacity or workload changes.
- **Capacity:** estimate sustainable demand while meeting service objectives.
- **Breakpoint:** locate the point where a key objective is no longer met.

Avoid running every test type by default. Tie each test to a hypothesis and decision.

## 5. Design a controlled and safe experiment

Before execution:

1. Confirm written authorization, environment, test window, target endpoints, and maximum load.
2. Prefer a dedicated performance environment. Production testing requires explicit approval, coordination, monitoring, and agreed abort criteria.
3. Set conservative load limits and stop conditions for elevated errors, latency, resource saturation, or customer impact.
4. Verify test data, account isolation, cleanup, rate limits, and third-party dependency restrictions.
5. Check that load generators can produce the intended traffic without becoming the bottleneck.
6. Confirm clocks, metric windows, log correlation, and monitoring coverage.
7. Record build, configuration, topology, test script revision, and test-data version.

Never initiate destructive, high-volume, or externally visible traffic without explicit authorization. Do not disable safeguards, bypass rate limits, or overload shared systems to force a result.

## 6. Validate the test script and data

Review scripts for:

- Correct transaction boundaries and meaningful success checks.
- Correlation of dynamic values such as tokens, IDs, and session data.
- Parameterization and realistic data variation.
- Correct handling of authentication, redirects, cookies, retries, and pagination.
- Think time and pacing that match the intended workload.
- Checks for business-level success, not merely HTTP 200.
- Controlled error handling; avoid silently retrying failures in a way that hides system behavior.
- Reusable configuration for environment, load profile, and secrets.
- Safe setup and teardown, with no embedded credentials.

For JMeter, k6, or Gatling, use the tool's actual syntax and version when generating scripts. Do not claim a script was executed merely because it was generated or reviewed.

## 7. Read performance results correctly

Analyze the whole system, not just a single headline number.

### User-facing and service metrics

- Throughput: requests/transactions per second and completed work.
- Latency: median, p90, p95, p99, and maximum where useful.
- Error rate: HTTP errors, timeouts, connection failures, assertion failures, and business failures.
- Concurrency, active sessions, queue depth, and completed transactions.
- Saturation and resource signals: CPU, memory, garbage collection, disk I/O, network, thread pools, connection pools, and database activity.

Use percentiles with sample counts and time windows. Averages can conceal tail latency. Compare like-for-like time windows, workload, environment, and configuration.

### Interpret trends and relationships

- Rising latency with flat throughput can indicate saturation, queueing, or a constrained dependency; investigate before assigning a cause.
- Throughput plateauing while offered load rises may indicate a capacity limit, throttling, or generator constraint.
- High CPU can reflect useful work, inefficient code, contention, or excessive concurrency; correlate with application and runtime evidence.
- Low CPU does not prove the application is healthy; inspect waits, locks, connection pools, network, disk, and downstream dependencies.
- Increased errors under load may be caused by timeouts, resource exhaustion, rate limiting, dependency failures, or test-data collisions.
- A slow test result can be caused by the load generator, network path, or monitoring overhead; validate the test infrastructure.

Never infer root cause from one metric or one screenshot. Separate observed facts, plausible explanations, and tests needed to distinguish them.

## 8. Analyze distributed systems and load-balanced nodes

For systems with multiple application instances:

- Compare per-node CPU, memory, request count, latency, thread/connection pools, and errors over the same time window.
- Check load-balancer algorithm, health checks, sticky sessions, connection reuse, and uneven request cost.
- Verify whether metrics are per instance, aggregated, sampled, or averaged.
- Inspect downstream shared dependencies such as database, cache, message broker, and external services.
- Correlate request IDs or traces across gateway, application, and dependencies when available.
- Consider autoscaling delay, cold starts, deployment differences, and uneven instance capacity.

Do not claim a load balancer is distributing traffic evenly without per-node request evidence. Do not attribute a slow endpoint to a specific server unless routing or trace evidence supports it.

## 9. Compare runs fairly

Before comparing two runs, check:

- Same build, test script, workload shape, duration, data, and environment.
- Same instance count, configuration, dependency health, and cache/warm-up state.
- Same metric definitions, aggregation, time zones, and observation windows.
- Similar load-generator capacity and network path.
- Whether autoscaling, deployments, background jobs, or other traffic changed.

Show absolute and percentage differences when source data supports them. Do not compare p95 from one run with average latency from another. Note confounding changes and limit conclusions accordingly.

## 10. Form and test bottleneck hypotheses

For each suspected bottleneck, document:

1. **Observation:** what the measurements actually show.
2. **Hypothesis:** the possible mechanism, clearly labelled.
3. **Supporting evidence:** correlated metrics, logs, traces, or repeatable behavior.
4. **Counter-evidence / alternatives:** what else could explain the observation.
5. **Next experiment:** the smallest safe test that distinguishes the possibilities.
6. **Confidence:** low, medium, or high, with rationale.

Examples of hypotheses to investigate—not conclusions:

- Database connection-pool exhaustion.
- Slow or locked database queries.
- Thread-pool or worker saturation.
- External dependency latency.
- Uneven load distribution.
- Garbage-collection pauses or memory pressure.
- Network, DNS, TLS, or connection setup overhead.
- Load-generator saturation.

Prefer one controlled change per experiment. Avoid tuning several variables simultaneously because it obscures causality.

## 11. Report results with traceable evidence

A useful report contains:

- Objective, scope, environment, build, topology, and test window.
- Workload model, offered load, ramp-up, duration, and scenario mix.
- Acceptance criteria and their source.
- Result summary: throughput, latency percentiles, errors, and resource metrics.
- Time-series observations and per-node comparisons when available.
- Deviations, blockers, data gaps, and test validity limitations.
- Findings ranked by impact and confidence.
- Recommendations and the next validation experiment.

Use a table when it improves clarity:

| Metric | Target | Observed | Evidence / time window | Assessment |
|---|---:|---:|---|---|
| Throughput | | | | |
| p95 latency | | | | |
| p99 latency | | | | |
| Error rate | | | | |
| CPU / memory | | | | |

Use explicit result labels:

- **MET:** measured result meets the stated criterion.
- **NOT MET:** measured result misses the stated criterion.
- **INCONCLUSIVE:** evidence is insufficient or test validity is uncertain.
- **NOT MEASURED:** no supporting measurement was collected.

Do not invent thresholds, results, monitoring values, or test execution. If acceptance criteria were not supplied, report measurements without declaring the system passed or failed.

## 12. Deliver the next action

End with the highest-value next step: a missing measurement, a controlled rerun, a script correction, a trace to collect, or a specific engineering investigation. Keep the recommendation proportional to the evidence.
