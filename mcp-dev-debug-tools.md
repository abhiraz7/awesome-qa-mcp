# MCP Dev / Debug Tools

Not testing tools themselves — tools for building and verifying your own MCP server, which
you'll likely need if your team's tracker/tool isn't covered by an existing server above.

- **MCP Inspector** — The reference debugging tool for MCP servers. Lets you call
  `tools/list` and individual tools directly over stdio or Streamable HTTP, so you can
  verify a server you're building actually returns valid responses before pointing a real
  AI client at it.

- **MCPJam Inspector** — Similar inspector tooling, an alternative to the reference
  MCP Inspector above.

## Example: a working, tested server built this way

This workspace already has one example of a custom MCP server built and smoke-tested end
to end: `content-writer-mcp` (sibling folder) — a Python/FastAPI MCP server exposing a
notes knowledge base to ChatGPT, with a staged-diff-then-apply safety pattern. Useful as a
reference for structure (tool definitions, auth via API key header, running behind an
ngrok tunnel) if you're building a QA-specific one (e.g. wrapping an internal test
tracker).

---
[← Back to index](README.md)
