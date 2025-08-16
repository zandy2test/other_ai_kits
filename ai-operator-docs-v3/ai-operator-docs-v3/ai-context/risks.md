# Risk Register (Lightweight)

## 🔴 Active Risks

### High Priority
- [ ] **No automated UI tests** → Manual verification slower → Request Playwright MCP each session
- [ ] **No evidence trail** → Can't prove what worked → Update evidence.md after each task

### Medium Priority  
- [ ] **Context window fills** → AI forgets earlier work → Use new_task when >50% full
- [ ] **Secrets in code** → Security breach → Check before every commit

### Low Priority
- [ ] **Documentation drift** → Confusion later → Monthly review reminder

## ✅ Mitigated Risks
- [x] **Tool failures** → One retry + fallback (2024-12-16)
- [x] **Large PRs** → Hard to review → Small commits rule (2024-12-16)

## 🚨 Escalation Triggers
**Stop and escalate if:**
- Production data at risk
- Authentication/security issue
- AI stuck after 3 attempts
- Core functionality broken
