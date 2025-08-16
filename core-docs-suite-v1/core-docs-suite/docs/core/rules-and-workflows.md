# Rules & Workflows (behavior‑first)

## Rules (always on)
- **Verify‑First**: Run tests or checks before claiming success. For UI, assert by role/text/label.
- **Tool‑Failures**: On any tool/step error: **name the tool + exact error → ask to enable/fix → one retry → propose a safe fallback**. Record what was skipped and why.
- **Context‑Asker**: When unsure, request the **smallest next slice** (problems → recent terminal output → recent changes → targeted file/path).
- **Capability‑Gap**: List needed capabilities (e.g., UI introspection, web data). Request the **smallest** missing capability and retry once.

## Workflows (when to run)
- **Startup Checklist** (start of a task): inventory capabilities → pull minimal context → confirm save/format semantics → define acceptance checks → verify → report (plan, diff, evidence, risks/asks).
- **UI Verification** (when UI changed): apply `verification-standard.md` and attach one additional artefact (trace or logs or DOM/text).

## Best vs. worst timing
- **Best**: Startup at thread/task beginning; UI verification just before “done.”
- **Worst**: Re‑running checklists without change; UI verification on non‑UI work.

## Exit criteria (proof‑of‑done)
- Assertions by role/text/label **+** one artefact (trace/logs/DOM‑text) **+** diff bullets and risks/asks.
