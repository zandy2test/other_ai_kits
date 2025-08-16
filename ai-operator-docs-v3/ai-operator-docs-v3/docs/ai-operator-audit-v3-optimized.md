# AI-Operator Kit Audit

**Mission**: Rigorous audit of AI-operator kit. Verify against primary sources, test workflows, return copy-pasteable fixes.

## Quick Audit Mode [If time-constrained]
1. Check MCP connections → fix if broken
2. Run `/verify-ui.md` → get text evidence  
3. Scan for `ignoreDuringBuilds` → flag if found
4. Return GO/NO-GO + top 3 issues

---

## Setup & Context [CRITICAL]

### MCP Requirements
```json
{
  "mcpServers": {
    "playwright": {"command": "npx", "args": ["@playwright/mcp@latest"]},
    "firecrawl": {"command": "npx", "args": ["-y", "firecrawl-mcp"], 
                  "env": {"FIRECRAWL_API_KEY": "YOUR_KEY"}}
  }
}
```
If disconnected: ask to enable → retry once → document fallback

### Immediate Actions
1. Parse `/handoff/manifest.yml` for requirements
2. Pull context: @problems → @terminal → @git-changes → @/file
3. Run `/startup-checklist.md` to verify setup
4. Note: Audience = AIs first, humans second

## Verification Standards

### Primary Sources
- **Diátaxis**: diataxis.fr (4-part doc structure)
- **Playwright**: playwright.dev/docs/locators (accessibility-first)
- **Next.js**: nextjs.org/docs/app/api-reference/config/eslint
- **MCP**: modelcontextprotocol.io

### Core Rules [Test These]
| Rule | Trigger | Action | Evidence Required |
|------|---------|--------|-------------------|
| Verify-First | Any task | Test → Assert → Done | Role/text proof |
| Tool-Failures | Error occurs | Name tool+error → retry → fallback | Error log |
| Context-Asker | Need info | Request smallest slice | @-mention used |
| Capability-Gap | Missing MCP | Request minimal server | Gap documented |

### UI Testing Standards
```javascript
// ✅ REQUIRED: Accessibility-first
await page.getByRole('button', { name: 'Submit' });
await page.getByLabel('Email');

// ❌ FORBIDDEN: Brittle selectors  
await page.locator('.btn-primary');  // No CSS
await page.locator('//button[@id="submit"]');  // No XPath
```
**Evidence**: Assertions + (trace OR console OR DOM text)

## Critical Checks

### Configuration
- [ ] NO `eslint.ignoreDuringBuilds` in templates
- [ ] Emergency escape hatch documented with removal reminder
- [ ] CI has markdownlint-cli2 + Lychee link checker

### Hands-On Tests
1. **Now**: Run `/verify-ui.md` on base URL → capture evidence
2. **Document**: Pass/fail for each workflow with citations

## Risk Focus [Top 5 Only]

| Risk | Impact | Quick Mitigation |
|------|--------|------------------|
| MCP disconnect | HIGH | Retry logic + manual fallback |
| Tool unavailable | HIGH | Document workarounds |
| Stale routes | MED | Quarterly audit |
| Over-automation | HIGH | Human checkpoints |
| Secret exposure | CRITICAL | Never print, env names only |

## Deliverables [Priority Order]

### 1. Go/No-Go Verdict
- Status: **GO** or **NO-GO**  
- If NO-GO: List blocking issues + fastest fix path
- Top 3 strengths, Top 3 fixes needed

### 2. Required Changes
```diff
# Unified diffs only for files needing changes
- old_line_that_must_change
+ new_line_with_fix
```

### 3. Verification Results
| Test | Source Link | Pass/Fail | Evidence/Blocker |
|------|------------|-----------|------------------|
| ... | ... | ✅/❌ | ... |

### 4. Next Steps
- Missing MCPs needed: [list]
- Blocked items: [specific asks using @-mentions]
- Optional improvements: [if time permits]

## Constraints
⚠️ **Never**: Print secrets | Over-scrape | Use screenshots as primary evidence  
✅ **Always**: Cite sources | One retry max | Text-first proof | Reversible changes
