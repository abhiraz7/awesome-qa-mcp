# Performance & Load Testing MCP Servers

- **[k6 MCP Server](https://glama.ai/mcp/servers/@QAInsights/k6-mcp-server)** (QAInsights)
  — Lets an AI client execute a k6 load test (set duration, number of virtual users) and
  pull back the results for analysis, so you can ask things like "run this script at 50
  VUs for 2 minutes and tell me if p95 latency regressed" conversationally instead of
  parsing raw k6 output by hand.

- **MaxoPerf MCP** — Performance-testing-focused MCP server; exposes test execution and
  results as MCP tools for an AI client to drive load tests and interpret output.

## Related tooling (no dedicated MCP wrapper confirmed yet)

- **Grafana k6** itself (the engine behind the k6 MCP server above) — scriptable load
  testing in JavaScript, widely used in CI pipelines for performance regression gates.
- A **Postman → k6 converter** exists, useful if your functional API tests are already in
  Postman and you want to reuse them as load-test scripts.

---
[← Back to index](README.md)
