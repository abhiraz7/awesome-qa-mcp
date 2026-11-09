# QA Environment Readiness Checklist

Use this checklist before executing a defined set of QA checks. It is a preflight record for environment, access, data, dependencies, observability, and safety. It does not prove that the application works or replace the organization's change, security, or release approvals.

Readiness is **scope-specific**: record the target build, environment, user role, test data, and actions covered. A staging URL responding successfully is not, by itself, evidence that the environment is ready for every test.

## Record context

- **Work item / feature:**
- **Checks in scope (IDs):**
- **Application / service:**
- **Build / version / commit:**
- **Target environment and region:**
- **Test window:**
- **Operator / QA owner:**
- **Environment or service owner:**

Use `READY`, `BLOCKED`, `NOT CHECKED`, or `N/A` for each item. Add a short evidence reference or explanation. Use N/A only with a reason.

## Preflight checks

| Area | Readiness question | Status | Evidence / owner / notes |
|---|---|---|---|
| Target identity | Is the exact application, API base URL, tenant, region, and environment confirmed? Is there any risk of confusing production with a test environment? | NOT CHECKED | |
| Build and configuration | Is the deployed build/version recorded? Are relevant feature flags and configuration known? | NOT CHECKED | |
| Scope and expected behavior | Are the intended checks, acceptance criteria, roles, and in-scope actions clear enough to judge results? | NOT CHECKED | |
| Authorization | Is the activity within the user's and operator's authorization? Is explicit approval recorded for production, destructive, irreversible, high-volume, or externally visible actions? | NOT CHECKED | |
| Identity and access | Are the required test accounts and roles available, least-privileged, and safe to use? Are credentials handled through approved secret storage? | NOT CHECKED | |
| Test data | Is data synthetic or approved, isolated from real customers, and in a known starting state? Is cleanup or reset understood? | NOT CHECKED | |
| External effects and dependencies | Are payment, email, SMS, webhooks, queues, third-party services, and rate limits understood? Are sandboxes or safe stubs configured where needed? | NOT CHECKED | |
| Observability and evidence | Are the required logs, metrics, traces, and correlation IDs available? Can evidence be captured without exposing secrets or personal data? | NOT CHECKED | |
| Test tools and generators | Are tool versions, connectivity, permissions, and configuration known? For load tests, is generator capacity verified and is the maximum offered load bounded? | NOT CHECKED | |
| Safety and recovery | Are stop/abort conditions, cleanup, rollback, and recovery ownership defined for any state-changing test? Is a backup or restore path required and confirmed? | NOT CHECKED | |
| Change coordination | Is the test window agreed with affected owners? Are deployments, maintenance, background jobs, and competing tests known? | NOT CHECKED | |
| Environment deviations | Are relevant differences from production or the target reference environment recorded, including unavailable integrations or reduced capacity? | NOT CHECKED | |

## Readiness decision

Apply the decision to the specific checks listed in the record:

- **READY** — every mandatory item is READY, or explicitly N/A with a reason. The approved scope and safety limits are understood.
- **BLOCKED** — a mandatory prerequisite is not met, including missing authorization, unsafe data, an uncontrolled external effect, or an unresolved recovery requirement. Do not execute the affected checks.
- **NOT ASSESSED** — one or more mandatory prerequisites remain NOT CHECKED and there is not enough evidence to determine readiness. Do not execute checks whose safety or validity depends on those prerequisites.

A non-critical gap may be accepted only by the appropriate owner and only when it does not undermine authorization, safety, data isolation, or the validity of the affected check. Record the decision and limitation; do not silently convert a gap to READY.

Readiness is not a test result. It does not mean the application passed, and it does not authorize activity outside the stated scope.

## Execution handoff

- **Readiness decision:** NOT ASSESSED
- **Checks allowed to proceed:**
- **Checks held / not run:**
- **Mandatory blockers or unknowns:**
- **Approver / owner and approval reference, if required:**
- **Abort conditions:**
- **Cleanup / rollback owner:**
- **Next action:**

If a prerequisite prevents an attempted check, report the check as BLOCKED. If execution was never attempted because preflight was incomplete, report it as NOT RUN and state that readiness is BLOCKED or NOT ASSESSED. Reassess after a build, configuration, access, data, dependency, or test-scope change.
