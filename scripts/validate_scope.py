#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path


def validate(path: Path) -> list[str]:
    data=json.loads(path.read_text(encoding="utf-8")); errors=[]
    if data.get("schema_version") != "1.1": errors.append("schema_version must be 1.1")
    if not str(data.get("request") or "").strip(): errors.append("request is required")
    if data.get("status") != "ready": errors.append("status must be ready before requirements extraction/generation")
    matches=data.get("matched_sections")
    if not isinstance(matches,list) or not matches: errors.append("matched_sections must be non-empty")
    else:
        for i,item in enumerate(matches):
            if not isinstance(item,dict): errors.append(f"matched_sections[{i}] must be an object"); continue
            if not str(item.get("source_file") or "").strip(): errors.append(f"matched_sections[{i}].source_file is required")
            if not str(item.get("locator") or "").strip(): errors.append(f"matched_sections[{i}].locator is required")
    if not isinstance(data.get("excluded_neighbors",[]),list): errors.append("excluded_neighbors must be an array")
    if data.get("unresolved") not in ([],None): errors.append("unresolved must be empty before continuing")
    if "official_requirements" in data: errors.append("official_requirements belongs in requirements.json in schema 1.1")
    return errors


def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("scope",type=Path); args=p.parse_args()
    errors=validate(args.scope)
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("scope: OK")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
