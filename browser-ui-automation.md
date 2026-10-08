# Browser / UI Automation MCP Servers

Each entry below was confirmed to exist (checked via web search, Oct 2026) before being
listed. "What it does" describes the actual tool capability, not marketing copy.

- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** (Microsoft, official)
  — Exposes browser control as MCP tools: navigate, click, type, take a page snapshot.
  Drives the browser through the accessibility tree instead of screenshots/pixel
  coordinates, so an AI client can run an end-to-end web flow (e.g. "log in, add an item
  to cart, check out") by calling structured tools rather than parsing images — faster,
  cheaper on tokens, and less flaky than vision-based clicking.

- **Selenium MCP** (by Angie Jones) — Wraps Selenium WebDriver as MCP tools: find an
  element by locator, click it, type into it, take a screenshot, run a script. Lets an AI
  client reuse your existing Selenium grid/driver setup instead of switching stacks to get
  MCP support.

- **kogiQA MCP Web Browser** — A browser tool an AI coding agent can call to visit a real
  website and look at it, intended for bug-hunting and drafting UI test cases from what it
  observes on the page, rather than from a spec alone.

## Related (not MCP yet, but what these servers build on)

If you want to build your own MCP wrapper around a framework not listed above, these are
the underlying tools people are already using successfully in agent-driven testing:
Cypress, WebdriverIO, Puppeteer.

---
[← Back to index](README.md)
