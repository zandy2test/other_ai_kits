# Risk Register (living)

| Risk | Impact | Mitigation | Owner |
|------|--------|------------|-------|
| Discovery drift (can’t find a workflow/step) | Steps skipped | Keep a plain‑text Startup Checklist in this file set; allow running steps manually | Operator |
| Capability unavailable (no UI inspector/web fetch) | Blocked verification or data | Ask to enable capability; retry once; propose smallest fallback; log what’s skipped | Operator |
| Over‑restriction in rules | Friction; workarounds | Keep evidence bar **flexible**; allow text‑only proof | Operator |
| Lint bypass left in builds | Ship with hidden issues | Keep bypass **out of templates**; if used, record as short‑lived and remove after unblock | Operator |
| Evidence privacy | Sensitive info leaked | Prefer logs/DOM text; redact; avoid screenshots when unnecessary | Operator |
| Link rot in docs | Confusing guidance | Periodically run a link check (any CI or local script) | Operator |
