#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_FILES = [
    ROOT / "data/business_idea_success_filter.json",
    ROOT / "data/source_registry.json",
    ROOT / "data/claims.json",
    ROOT / "data/opportunity_radar.json",
]

errors = []
for path in JSON_FILES:
    try:
        with path.open("r", encoding="utf-8") as f:
            json.load(f)
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")

master = ROOT / "master/PROJECT_MASTER.md"
if not master.exists() or master.stat().st_size < 1000:
    errors.append("master/PROJECT_MASTER.md missing or unexpectedly small")

claims = json.loads((ROOT / "data/claims.json").read_text(encoding="utf-8"))
required = {"id", "entity", "metric_type", "value", "as_of_date", "source_grade", "claim_type", "confidence", "last_verified_at"}
for i, claim in enumerate(claims.get("claims", []), start=1):
    missing = required - claim.keys()
    if missing:
        errors.append(f"claims[{i}] missing: {sorted(missing)}")
    if claim.get("source_grade") not in {"A", "B", "C", "D"}:
        errors.append(f"claims[{i}] invalid source_grade")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("Repository validation OK")
