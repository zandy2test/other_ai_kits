# Verification Standard (no screenshots required)

**UI assertions (accessibility‑first)**
- Prefer **roles**, **labels**, and **visible text** derived from semantic HTML / ARIA. Examples:
  - Button by role + name (e.g., “Save”)
  - Status/alert region by role
  - Form control by associated label
- Avoid brittle selectors (CSS/XPath) as the primary strategy; only use when no semantic hook exists.
- If a visual artefact isn’t possible, capture **console/logs** or **DOM/text** that demonstrates the result.

**Non‑UI assertions**
- Data/CLI outputs that match expectations (invariants), structured logs, or minimal traces.

**Evidence policy**
- Keep it light: UI/non‑UI assertion **plus one** additional artefact (trace **or** logs **or** DOM/text capture).
