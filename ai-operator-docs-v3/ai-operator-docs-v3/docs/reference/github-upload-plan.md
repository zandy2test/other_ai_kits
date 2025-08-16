# 📋 GitHub Upload Plan - Clean & Simple

## Your Process:
1. **Copy each artifact** above to GitHub (5 files)
2. **Tell the other AI**: "Move these files to their correct folders based on the LOCATION header"
3. **Done!** No bloat, no confusion

## The 5 Essential Files:

| File | Purpose | Folder Path |
|------|---------|-------------|
| manifest.yml | Makes audit work | `ai-operator-docs-v3/` (root) |
| risks.md | Track risks | `ai-operator-docs-v3/ai-context/` |
| evidence.md | Log what worked | `ai-operator-docs-v3/ai-context/` |
| ship-it.md | Deploy in 2 min | `ai-operator-docs-v3/ai-core-template/workflows/` |
| unstuck.md | Recover when stuck | `ai-operator-docs-v3/ai-core-template/workflows/` |

## What Each Does:

### `/ship-it.md` - Your Speed Deployer
- Pre-flight checks (no console.logs, no secrets)
- Quick verify (runs tests if exist)
- Proper commit message
- Push to deploy
- Auto-logs to evidence.md
- **Result**: Deploy in <2 minutes instead of 20

### `/unstuck.md` - Your Recovery Helper
- Saves your WIP to a branch
- Tries progressively simpler approaches
- Common fixes for 80% of problems
- Escalation path if truly stuck
- **Result**: Never waste >15 min being stuck

### `manifest.yml` - Your Audit Enabler
- Documents your entire kit structure
- Makes the audit prompt work
- Central configuration file
- **Result**: Kit is "official" and auditable

### `risks.md` - Your Lightweight Tracker
- Active risks you're managing
- Escalation triggers
- Mitigated items
- **Result**: Never forget what's risky

### `evidence.md` - Your Proof Log
- What you tested
- How you verified it
- Any concerns noted
- **Result**: Can prove what worked

## Instructions for Other AI:

```
"I have 5 files to organize in the ai-operator-docs-v3 repo.
Each file has a LOCATION header showing exactly where it goes.
Please:
1. Create the folder structure if needed
2. Place each file in its specified location
3. Confirm all 5 files are in place"
```

## After Upload:

In Cline, test:
- Type `/ship-it.md` - should appear
- Type `/unstuck.md` - should appear
- Check manifest.yml is at root
- Verify ai-context/ has risks.md and evidence.md

## No Bloat Approach ✅
- Only 5 essential files
- Each under 50 lines
- Clear single purpose
- No duplication
- Total: ~200 lines across all files (not 2000!)

**This is lean, clean, and ready to use!**
