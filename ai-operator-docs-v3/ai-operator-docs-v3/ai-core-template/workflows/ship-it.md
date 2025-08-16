# Ship It Workflow (run with `/ship-it.md`)

**For:** Solo founder rapid deployment

## Pre-Flight Checks
1) Run tests if they exist
2) Check @problems panel (0 critical)
3) No console.log or API keys

## Ship Sequence

### 1. Quick Verification
- UI changed → Run `/verify-ui.md`
- API changed → Test one endpoint
- Logic only → Check tests pass

### 2. Commit
git add -A
git commit -m "feat: <what changed>"

### 3. Deploy
git push origin main
# Auto-deploys on Vercel/Netlify

### 4. Post-Deploy (2 min)
- Check production URL works
- Test one critical path
- Update risks.md if issues

## Auto-Proceed If:
- ✅ Only UI text/style changes
- ✅ No database changes
- ✅ No auth/payment changes
- ✅ Tests pass

## Rollback:
git revert HEAD && git push
