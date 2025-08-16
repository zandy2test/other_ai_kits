# Rule: Verify‑first for UI/e2e
- Run tests first.
- If Playwright MCP is connected:
  - Open impacted routes.
  - Assert with `getByRole`, `getByLabel`, `getByText` (accessibility-first).
  - Capture evidence (trace or logs/DOM text).
- If Not connected: ask to enable/restart → retry once → propose fallback and flag the gap.
