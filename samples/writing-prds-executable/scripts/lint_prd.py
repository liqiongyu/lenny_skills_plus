#!/usr/bin/env python3
"""
lint_prd.py — lightweight PRD linter for the Writing PRDs (Executable) skill.

Usage:
  python scripts/lint_prd.py path/to/PRD.md

Checks (heuristic):
- Required sections exist (or close variants)
- "Why now" mentioned
- Out of scope present
- Metrics present
- Open questions present

Exit code:
- 0 = pass
- 1 = warnings found
"""

import re
import sys
from pathlib import Path

REQUIRED_PATTERNS = [
    r"\bTL;DR\b",
    r"\bProblem\b|\bOpportunity\b",
    r"\bGoals\b",
    r"\bNon-goals\b|\bNon goals\b",
    r"\bRequirements\b",
    r"\bOut\s*of\s*scope\b",
    r"\bMetrics\b|\bSuccess\s*metrics\b",
    r"\bRisks\b",
    r"\bRollout\b|\bLaunch\b",
    r"\bOpen\s*questions\b",
]

WHY_NOW_PATTERN = r"why\s*now"

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/lint_prd.py path/to/PRD.md")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    text = path.read_text(encoding="utf-8", errors="ignore")
    warnings = []

    for pat in REQUIRED_PATTERNS:
        if not re.search(pat, text, flags=re.IGNORECASE):
            warnings.append(f"Missing section/pattern: {pat}")

    if not re.search(WHY_NOW_PATTERN, text, flags=re.IGNORECASE):
        warnings.append("Missing: 'Why now' (or equivalent)")

    if warnings:
        print("PRD Lint Warnings:")
        for w in warnings:
            print(f"- {w}")
        return 1

    print("PRD lint passed ✅")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
