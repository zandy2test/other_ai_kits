# Unstuck Workflow (run with `/unstuck.md`)

**For:** When stuck after 2+ attempts

## 1. Save State
git add -A
git stash
git checkout -b "stuck-$(date +%Y%m%d)"
git stash pop
git commit -m "WIP: stuck on X"

## 2. Progressive Recovery

### Level 1: Fresh Context
- New Cline chat
- Run `/startup-checklist.md`
- Try once more

### Level 2: Simpler Approach
- Hardcode temporarily?
- Skip for now?
- Use third-party service?

### Level 3: Different Tool
- Cline → Claude Code
- Claude Code → Direct Claude
- AI → Stack Overflow

### Level 4: Escalate
After 3 attempts with no progress

## 3. Common Fixes

| Problem | Quick Fix |
|---------|-----------|
| Build error | rm -rf node_modules && npm install |
| Type error | Add // @ts-ignore temporarily |
| CSS broken | Use inline styles temporarily |
| API failing | Hardcode mock data |

## 4. Continue
git checkout main
git checkout -b "new-feature"
# Move to next task
