# ADR‑0001 — Foundational Choices

**Context**: We need safe defaults that don’t depend on any specific IDE/plugin or vendor tool.

**Decision**
- Prefer accessibility‑first assertions (roles/labels/text) for UI verification.
- Keep “lint bypass during builds” **out of templates**; if used, it must be short‑lived and documented.
- Use lightweight rules (verify‑first; fail‑loudly; smallest‑next‑slice) and a flexible evidence bar.

**Consequences**
- Works in plain environments (no screenshots required).
- Lower risk of silent failures; easier reviews; fewer brittle tests.
