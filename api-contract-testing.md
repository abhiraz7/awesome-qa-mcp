# API & Contract Testing MCP Servers

- **Apidog Tests MCP** — Connects an AI client to Apidog's test management/execution
  features: create, run, and inspect results of API test cases that live in Apidog,
  without leaving the chat/agent session.

- **Generic API/HTTP MCP servers** — Several lightweight servers exist that simply expose
  "send an HTTP request, set headers, read the response" as MCP tools. Useful for ad hoc
  contract/smoke checks (e.g. "call this endpoint with this payload and tell me if the
  response matches the schema") without a full API-testing platform in the loop.

## Underlying tools without a dedicated MCP wrapper yet (confirmed active in 2026 tooling
## roundups, worth building a wrapper around if you need one)

- **Postman** — the de facto API client/collection-runner; a Postman MCP would let an
  agent run a saved collection and read results.
- **Bruno** — open-source, git-friendly Postman alternative.
- **Hoppscotch** — open-source API client, browser-based.
- **Insomnia** — API client with environment/collection support, similar niche to Postman.
- **Karate** — BDD-style API test framework (Java), can also do performance/mocking.
- **REST Assured** — Java DSL for testing REST APIs, common in JVM test suites.
- **Schemathesis** — property-based testing for APIs from an OpenAPI/GraphQL schema; finds
  edge cases a hand-written test suite wouldn't think to check.
- **Pact** — contract testing between services (consumer-driven contracts), useful when
  your QA scope spans multiple microservices owned by different teams.

---
[← Back to index](README.md)
