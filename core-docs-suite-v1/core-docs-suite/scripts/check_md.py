import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
bad = []
for p in ROOT.rglob("*.md"):
    text = p.read_text(encoding="utf-8", errors="ignore")
    if text.count("```") % 2 != 0:
        bad.append(str(p.relative_to(ROOT)))
if bad:
    print("Unbalanced code fences in:")
    for f in bad:
        print(" -", f)
    sys.exit(1)
print("All markdown code fences are balanced.")
