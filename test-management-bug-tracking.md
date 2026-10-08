# Test Management & Bug Tracking MCP Servers

- **[Zephyr MCP](https://smartbear.com/blog/smartbear-mcp-server-zephyr/)** (SmartBear,
  released Aug 2026) — Brings Zephyr test-management data (test plans, cycles, execution
  records, linked Jira issues) into any MCP-compatible client, so you can ask "what's the
  Zephyr test coverage on this Jira issue?" in one agentic session instead of opening both
  Jira and Zephyr separately.

- **[Jira-Zephyr MCP](https://glama.ai/mcp/servers/leorosignoli/jira-zephyr-mcp)**
  (community, by leorosignoli) — Covers test plan/cycle management, test execution, and
  reading/linking Jira issues. A community alternative to the official SmartBear one
  above, worth comparing feature coverage before picking one.

- **Zephyr Squad Server MCP** — Focused on Zephyr-for-Jira test cycle management: creating
  cycles, controlling execution, and updating execution status from an AI client.

- **Qase MCP Server** — Connects an AI client to the Qase test-management platform for
  reading/writing test cases, runs, and results.

## If your team uses something niche

If your test tracker is something not listed here (an internal tool, YouTrack, a custom
system), building a small MCP server yourself is often the fastest path — see
[mcp-dev-debug-tools.md](mcp-dev-debug-tools.md) for how to validate one as you build it.

---
[← Back to index](README.md)
