from pathlib import Path
import re

root = Path(__file__).parent
html = (root / "index.html").read_text()
refs = set(re.findall(r"assets/[A-Za-z0-9_ ./&'—×–-]+\.(?:webp|gif|mp4|png|jpg|jpeg)", html))
missing = sorted(ref for ref in refs if not (root / ref).exists())
size = sum(p.stat().st_size for p in root.rglob("*") if p.is_file())
print(f"asset refs: {len(refs)}")
print(f"missing: {len(missing)}")
for ref in missing:
    print(ref)
print(f"deploy size: {size / 1024 / 1024:.1f} MB")
raise SystemExit(bool(missing))
