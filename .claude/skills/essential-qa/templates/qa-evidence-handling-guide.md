# QA Evidence Handling and Redaction Guide

Use this guide before copying, summarizing, storing, attaching, or sharing screenshots, logs, API traffic, traces, browser exports, database output, or other QA evidence. The goal is to preserve enough information to reproduce and investigate a finding while minimizing exposure of secrets and personal or confidential data.

This guide is a handling baseline, not a replacement for the organization's data-classification, privacy, security, incident-response, retention, or evidence-preservation policies. Follow stricter project or organizational requirements when they apply.

## 1. Minimize evidence before capture

- Capture only the screen, request, response, log window, trace spans, fields, and time range needed to support the check or finding.
- Prefer synthetic accounts and data. Use the least-privileged test identity that can demonstrate the behavior.
- Avoid full database dumps, full browser profiles, unrestricted HAR exports, complete log archives, or broad screenshots when a smaller excerpt is sufficient.
- Do not collect unrelated customer records or browse unrelated personal data to make a test more convenient.
- Before capture, close unrelated tabs and hide side panels, notifications, password managers, and account details where practical.
- Record the source, environment, build, time window, and relevant check/defect ID without copying sensitive values into the report.

## 2. Identify sensitive content

Treat the following as sensitive unless the data owner explicitly classifies it otherwise:

| Evidence source | Common sensitive content |
|---|---|
| Screenshots / recordings | Names, email addresses, phone numbers, addresses, account identifiers, payment details, private messages, browser notifications, visible credentials |
| HTTP requests / responses / HAR files | Authorization headers, cookies, session IDs, API keys, signed URLs, reset links, request bodies, personal data, payment or health data |
| Application / server logs | Tokens, passwords, connection strings, request payloads, user identifiers, IP addresses, stack traces containing secrets, internal hostnames |
| Traces / telemetry | Header and baggage values, query parameters, span attributes, database statements, user IDs, email addresses, session identifiers |
| Database / exports | Direct identifiers, free-text fields, credentials, financial records, customer or employee data |
| Filenames / URLs / metadata | Names, tenant IDs, ticket tokens, signed query parameters, local paths, embedded metadata |

Never include real passwords, private keys, access tokens, session cookies, recovery codes, or connection strings in a skill example, commit, issue, pull request, prompt, or ordinary QA report.

## 3. Redact a shareable copy

1. Keep the original evidence unchanged when it must be retained for investigation or audit. Store it only in an approved, access-controlled location.
2. Create a separate working copy for review or sharing.
3. Replace sensitive values with consistent placeholders such as `[REDACTED_TOKEN]`, `[REDACTED_EMAIL]`, or `[TEST_ACCOUNT_01]`. Keep placeholders consistent within one evidence set when correlation is useful.
4. Remove secrets from headers, cookies, query strings, request/response bodies, log messages, trace attributes, screenshots, filenames, and document metadata.
5. Preserve non-sensitive diagnostic context where possible: timestamps and timezone, status/error codes, endpoint templates, field names, sanitized IDs, relevant stack frames, and safe correlation references.
6. Do not over-redact the evidence so far that the behavior can no longer be understood. If a value is needed to reproduce the issue, use an approved synthetic substitute rather than exposing a real value.
7. Verify the redacted copy before sharing. Search text exports for known secret patterns and identifiers; inspect screenshots at full resolution; check hidden layers, annotations, OCR-visible text, metadata, and copied text where applicable.
8. Record what was redacted, the method, who performed the review when known, and where the approved original is retained. Do not claim an artifact is sanitized until it has been checked.

A visual black rectangle or crop is not sufficient if the underlying text remains selectable, recoverable, or present in the file metadata. Use a redaction method that permanently removes the sensitive content from the shareable copy, then verify the result.

## 4. Handle common evidence formats

### Screenshots and recordings

- Capture only the relevant application area and state.
- Redact visible names, contact details, account IDs, balances, payment details, browser tabs, notifications, and secrets that are not necessary to explain the finding.
- Check the full image and each relevant video frame; do not assume a blur or overlay is permanent redaction.
- Remove unnecessary location, device, or account metadata before sharing.

### Logs and traces

- Filter to the relevant time range, request, service, and check/defect ID.
- Remove credentials, tokens, cookies, personal data, and sensitive payload fields.
- Preserve safe timestamps, severity, error codes, sanitized trace/span IDs, and the minimum stack context needed to diagnose the issue.
- Treat trace baggage, span attributes, SQL parameters, and query strings as possible sources of sensitive data.

### API traffic and browser exports

- Prefer a minimal sanitized request/response example over a complete HAR or proxy-session export.
- Remove authorization headers, cookies, API keys, signed URL parameters, and sensitive request/response fields.
- Preserve the method, sanitized endpoint path, status code, content type, relevant schema fields, and representative synthetic values.
- Treat browser exports as highly sensitive by default because they may contain credentials and session state.

### Database and test-data evidence

- Prefer synthetic or purpose-built records and a small query result over production extracts.
- Do not attach database dumps or broad exports to ordinary QA reports.
- Mask or replace direct identifiers and free-text values; check joins and combined fields for re-identification risk.
- If production data is essential for an authorized investigation, follow the data owner's approved access and handling process.

## 5. Store and reference evidence safely

- Use only organization-approved repositories, ticket attachments, artifact stores, or evidence systems with appropriate access controls.
- Reference an artifact by ticket/check ID and an access-controlled location. Do not create public links or copy restricted artifacts into a general-purpose chat, issue, or pull request.
- Keep evidence permissions limited to people who need it. Avoid embedding sensitive values in filenames, commit messages, branch names, or URLs.
- Follow the applicable retention and deletion schedule. Do not keep local copies longer than necessary.
- For reports and templates, include a short sanitized excerpt or finding summary plus a safe evidence reference rather than embedding the raw artifact.
- Do not upload sensitive evidence to an AI assistant, external tool, or third-party service unless the data owner and applicable policy explicitly permit that destination.

## 6. Suspected security, privacy, or data incidents

If evidence suggests exposed credentials, unauthorized access, personal-data disclosure, payment-data exposure, or another serious incident:

- Stop unnecessary copying, sharing, and analysis of the sensitive material.
- Do not paste the raw secret or personal data into the QA report or assistant conversation.
- Preserve the original evidence in the approved restricted location when required; do not overwrite, casually redact, or delete the sole original.
- Record a safe reference and a minimal description of the suspected exposure.
- Follow the organization's security/privacy incident-response process and notify the designated owner promptly.
- Let the incident owner direct credential revocation, rotation, containment, legal/privacy assessment, and evidence retention.

Do not treat this guide as authorization to investigate beyond the assigned scope or to access additional records.

## 7. Record evidence handling in the QA record

For each artifact, record:

- evidence ID and related check/defect ID;
- source type and a short description;
- data classification, if known;
- whether the artifact is original, a working copy, or a redacted shareable copy;
- redaction status and the categories removed;
- verification performed before sharing;
- approved storage reference and access owner, when known; and
- retention or incident-handling reference, when applicable.

Use `NOT REVIEWED`, `REDACTION REQUIRED`, `REDACTED — NOT VERIFIED`, or `REDACTED — VERIFIED` as appropriate. If the artifact remains sensitive, label it `RESTRICTED — DO NOT SHARE` and reference only its approved restricted location.

Never invent a data classification, approval, redaction action, verification result, storage location, or retention decision. Mark unknown information explicitly.

## 8. Final sharing check

Before attaching or sharing an evidence artifact, confirm:

- [ ] The artifact is necessary and limited to the stated QA purpose.
- [ ] No credentials, tokens, cookies, secrets, or unnecessary personal data remain.
- [ ] Redaction is permanent in the shareable copy and has been verified.
- [ ] The original is preserved separately when required.
- [ ] The destination is approved and access-controlled.
- [ ] The evidence reference is safe to include in the report.
- [ ] Retention and incident-handling requirements have been followed.

If any required check cannot be confirmed, do not share the artifact. Record the limitation and request the approved handling path from the data or security owner.
