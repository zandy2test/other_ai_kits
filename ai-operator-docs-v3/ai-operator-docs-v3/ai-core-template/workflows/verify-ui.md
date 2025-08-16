# Verify UI (run with `/verify-ui.md`)
1) Run tests.
2) If Playwright MCP is connected: open impacted routes; assert with role/text; capture evidence.
3) If Not connected: ask to enable, retry once → propose fallback.
## Example
```ts
import { test, expect } from '@playwright/test';
test('save shows confirmation', async ({ page }) => {
  await page.goto(process.env.E2E_BASE_URL ?? 'http://localhost:3000/settings');
  await page.getByRole('button', { name: /save/i }).click();
  await expect(page.getByRole('status')).toHaveText(/saved/i);
});
```
