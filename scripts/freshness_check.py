#!/usr/bin/env python3
import argparse
import json
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "data/claims.json"


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--today", default=date.today().isoformat())
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    today = parse_date(args.today)
    data = json.loads(CLAIMS.read_text(encoding="utf-8"))
    due = []
    for claim in data.get("claims", []):
        last = parse_date(claim["last_verified_at"])
        max_age = int(claim.get("freshness_days", 30))
        age = (today - last).days
        reasons = []
        if age >= max_age:
            reasons.append(f"stale:{age}d/{max_age}d")
        if not claim.get("source_url"):
            reasons.append("missing_source_url")
        if claim.get("verification_status") != "verified":
            reasons.append(claim.get("verification_status", "not_verified"))
        if reasons:
            due.append((claim, age, reasons))

    if args.report:
        month = today.strftime("%Y-%m")
        path = ROOT / "radar/updates" / f"{month}.md"
        lines = [
            f"# Business Radar Update Due — {month}",
            "",
            f"Generated freshness check: {today.isoformat()}",
            "",
            "## Claims requiring research/re-verification",
            "",
        ]
        if due:
            for claim, age, reasons in due:
                lines.append(
                    f"- **{claim['entity']} / {claim['metric_type']}** — "
                    f"last verified {claim['last_verified_at']}; reasons: {', '.join(reasons)}"
                )
        else:
            lines.append("- None.")
        lines += [
            "",
            "## Required research pass",
            "",
            "1. Prefer official/primary sources.",
            "2. Record exact source URL and as-of date.",
            "3. Separate official claims, media reports, founder claims and estimates.",
            "4. Re-score opportunity/evidence/catalyst only if the new evidence changes a decision variable.",
            "5. Synchronize PROJECT_MASTER.md and CHANGELOG.md.",
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(path.relative_to(ROOT))

    print(f"Claims requiring update: {len(due)}")
    for claim, age, reasons in due:
        print(f"- {claim['id']}: {', '.join(reasons)}")


if __name__ == "__main__":
    main()
