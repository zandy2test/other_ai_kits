# Tool Setup & Detection Guide

---
[← Task Scaffold](08-task-scaffold.markdown) | [↑ README](README.operator.markdown) | [→ Example Run](10-example-run-login.markdown)
---

## Quick Capability Check (30 seconds)

### In VS Code + Cline Environment

```bash
# Check terminal access
echo "test" # If this works, terminal ✓

# Check Node/npm versions
node --version # Need v18+
npm --version  # Need v8+

# Check if Playwright installed locally
npm ls @playwright/test # If found, automation possible

# Check Cline @-mentions work
# Type: @problems 
# If Cline shows problems panel, context gathering ✓

# Check if workflows accessible
# Type: /
# If Cline shows available workflows, workflow system ✓
```

## Cline-Specific Features

### @-Mentions for Context
- `@problems` - Shows current errors/warnings
- `@terminal` - Shows last terminal output
- `@git-changes` - Shows uncommitted changes
- `@/file` - Target specific file
- `@/folder` - Target specific folder

### Running Workflows
- Type `/filename.md` to execute any workflow
- Example: `/startup-checklist.md` runs the startup checklist
- Workflows appear in Cline's autocomplete menu

### MCP Servers in Cline

#### Check Current MCP Status
1. Open VS Code settings (Cmd/Ctrl + ,)
2. Search for "Cline MCP" or check `.vscode/settings.json`
3. Look for `mcpServers` configuration

## Setting Up Playwright MCP (UI Testing)

### Installation for Cline

#### Method 1: Via Settings UI
1. Open VS Code Settings
2. Search "Cline MCP"
3. Add new server with these details:
   - Name: `playwright`
   - Command: `npx`
   - Args: `@playwright/mcp@latest`

#### Method 2: Via settings.json
Add to `.vscode/settings.json`:
```json
{
  "cline.mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

#### Verify It Works
Ask Cline: "Using Playwright MCP, verify there's a button with text 'Submit' on http://localhost:3000"

If it works, you'll see Playwright commands being executed.

### Fallback When Playwright MCP Unavailable

```bash
# Option 1: Use Playwright directly (if installed)
npx playwright test --grep "login"

# Option 2: Manual DOM inspection
1. Open http://localhost:3000 in browser
2. Press F12 for DevTools
3. Console tab → Type:
   document.querySelector('button')?.textContent
   document.querySelector('[role="button"]')?.getAttribute('aria-label')
4. Copy results to evidence log

# Option 3: Use curl + grep for basic checks
curl http://localhost:3000 | grep -o '<button[^>]*>[^<]*</button>'
```

## Setting Up Firecrawl MCP (Web Scraping)

### Installation for Cline

1. Get API key from https://firecrawl.dev/app/api-keys
2. Add to `.vscode/settings.json`:
```json
{
  "cline.mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-YOUR-KEY-HERE"
      }
    }
  }
}
```
3. Restart VS Code
4. Test: Ask Cline to "scrape the title from example.com"

### Fallback When Firecrawl Unavailable

```bash
# Get page content
curl -s https://example.com > page.html

# Extract specific elements
grep '<title>' page.html
grep '<h1' page.html

# Or use Node.js fetch
node -e "fetch('https://example.com').then(r=>r.text()).then(console.log)"
```

## Decision Tree for Cline Users

```
Need to verify something?
├─ UI element on localhost?
│  ├─ Playwright MCP connected?
│  │  └─ Use: page.getByRole('button', {name: 'Login'})
│  └─ Not connected?
│     └─ Open browser → F12 → Copy element text/attributes
│
├─ API endpoint?
│  ├─ Can use terminal?
│  │  └─ Use: curl commands → capture JSON
│  └─ No terminal?
│     └─ Ask for @terminal output from last test run
│
└─ External web content?
   ├─ Firecrawl MCP connected?
   │  └─ Use: scrape/crawl commands
   └─ Not connected?
      └─ Use: curl + text extraction
```

## Common Cline + MCP Issues

| Issue | Solution |
|-------|----------|
| "MCP server not responding" | Restart VS Code, check settings.json |
| "@-mention not working" | Update Cline extension, check workspace trust |
| "/workflow not found" | Ensure .md files are in workspace root |
| "Playwright timeout" | Check if localhost:3000 is running |
| "API key invalid" | Double-check key in settings, no extra spaces |

## Verification Commands for Each Tool

### After setup, verify everything works:

```bash
# 1. Terminal in Cline
echo "Terminal works in Cline"

# 2. @-mentions
# Type: @problems
# Should show problems panel

# 3. Workflows  
# Type: /startup-checklist.md
# Should start the checklist workflow

# 4. Playwright MCP (if connected)
# Ask: "Check if button exists on page"
# Should see Playwright commands

# 5. Git integration
git status
# Should show current repo status
```

## When All Else Fails

**The Universal Fallback**: Manual verification with text evidence

1. Open the page/API/content in any tool you have
2. Copy the relevant text/response/output
3. Paste into `07-evidence-log.markdown`
4. Mark verification method as "manual"

Example:
```markdown
## Evidence (Manual Verification)
Opened http://localhost:3000 in Chrome
Found button element: "<button type='submit'>Login</button>"
Accessible: Yes (keyboard tab worked)
Method: Manual DOM inspection (Playwright MCP not available)
```

Remember: **Evidence is evidence**, whether from automation or manual inspection. The goal is proof, not perfect tooling.

---

*Next: See [Example Run](10-example-run-login.markdown) for this guide in action*
