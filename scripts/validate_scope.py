#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED_REQ_KEYS = ["topics", "learning_objectives", "essential_knowledge", "skills_or_practices", "equations", "boundary_statements", "weighting"]

def validate(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    if data.get("schema_version") != "1.0": errors.append("schema_version must be 1.0")
    if not str(data.get("request") or "").strip(): errors.append("request is required")
    if data.get("status") != "ready": errors.append("status must be ready before generation")
    matches = data.get("matched_sections")
    if not isinstance(matches, list) or not matches: errors.append("matched_sections must be non-empty")
    else:
        for i, item in enumerate(matches):
            if not isinstance(item, dict): errors.append(f"matched_sections[{i}] must be an object"); continue
            if not item.get("source_file"): errors.append(f"matched_sections[{i}].source_file is required")
            if not item.get("locator"): errors.append(f"matched_sections[{i}].locator is required")
    req = data.get("official_requirements")
    if not isinstance(req, dict): errors.append("official_requirements must be an object")
    else:
        for key in REQUIRED_REQ_KEYS:
            if key not in req: errors.append(f"official_requirements.{key} is required (use [] when absent in source)")
            elif not isinstance(req[key], list): errors.append(f"official_requirements.{key} must be an array")
    unresolved = data.get("unresolved")
    if unresolved not in ([], None): errors.append("unresolved must be empty before generation")
    return errors

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("scope", type=Path); args=p.parse_args()
    errors=validate(args.scope)
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("scope: OK")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
