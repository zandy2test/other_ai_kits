# Navigation Updates for All Files

*Add these navigation headers to the top of each file (right after the title):*

## README.operator.markdown
```markdown
---
Start Here | [→ Context Pack](01-context-pack.markdown) | [Tool Setup](09-tool-setup-guide.markdown) | [Example](10-example-run-login.markdown)
---
```

## 01-context-pack.markdown
```markdown
---
[← README](README.operator.markdown) | [→ Operating Contract](02-operating-contract.markdown)
---
```

## 02-operating-contract.markdown
*(Already updated - see separate artifact)*

## 03-startup-checklist.markdown
```markdown
---
[← Operating Contract](02-operating-contract.markdown) | [↑ README](README.operator.markdown) | [→ Verify Checklist](04-verify-checklist.markdown)
---
```

## 04-verify-checklist.markdown
```markdown
---
[← Startup Checklist](03-startup-checklist.markdown) | [↑ README](README.operator.markdown) | [→ Risk Register](05-risk-register.markdown)

*After verification, record evidence in [→ Evidence Log](07-evidence-log.markdown)*
---
```

## 05-risk-register.markdown
```markdown
---
[← Verify Checklist](04-verify-checklist.markdown) | [↑ README](README.operator.markdown) | [→ Decision Template](06-ADR-0001.markdown)
---
```

## 06-ADR-0001.markdown
```markdown
---
[← Risk Register](05-risk-register.markdown) | [↑ README](README.operator.markdown) | [→ Evidence Log](07-evidence-log.markdown)

*Use when making non-trivial decisions. See [Example Run](10-example-run-login.markdown) for sample ADR.*
---
```

## 07-evidence-log.markdown
```markdown
---
[← Decision Template](06-ADR-0001.markdown) | [↑ README](README.operator.markdown) | [→ Task Scaffold](08-task-scaffold.markdown)

*Fill this after completing [Verify Checklist](04-verify-checklist.markdown)*
---
```

## 08-task-scaffold.markdown
```markdown
---
[← Evidence Log](07-evidence-log.markdown) | [↑ README](README.operator.markdown) | [→ Tool Setup](09-tool-setup-guide.markdown)

*Start all tasks with [Startup Checklist](03-startup-checklist.markdown)*
---
```

## 09-tool-setup-guide.markdown
*(Already included in its artifact)*

## 10-example-run-login.markdown
*(Already included in its artifact)*

---

## Quick Copy-Paste Instructions

1. Open each file (01 through 08)
2. Add the navigation header right after the main title
3. Save all files
4. Test navigation by clicking links

## Verification

After adding navigation, you should be able to:
- Start at README and reach any file in 2 clicks max
- Navigate sequentially through the workflow
- Jump back to README from anywhere
- See related files mentioned in context
