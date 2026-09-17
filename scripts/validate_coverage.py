#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path


def validate(requirements_path: Path, coverage_path: Path) -> list[str]:
    req=json.loads(requirements_path.read_text(encoding="utf-8")); cov=json.loads(coverage_path.read_text(encoding="utf-8")); errors=[]
    if cov.get("schema_version") != "1.1": errors.append("coverage schema_version must be 1.1")
    if cov.get("status") != "ready": errors.append("coverage status must be ready before generation")
    req_index={r.get("id"):r for r in req.get("requirements",[]) if isinstance(r,dict) and r.get("id")}
    con_ids={c.get("id") for c in req.get("constraints",[]) if isinstance(c,dict) and c.get("id")}
    entries=cov.get("coverage")
    if not isinstance(entries,list): errors.append("coverage must be an array"); entries=[]
    refs=[]
    for i,item in enumerate(entries):
        if not isinstance(item,dict): errors.append(f"coverage[{i}] must be an object"); continue
        rid=item.get("requirement_id"); refs.append(rid)
        if rid not in req_index: errors.append(f"coverage[{i}] references unknown requirement_id {rid!r}")
        if item.get("status") != "planned": errors.append(f"coverage[{i}] status must be planned")
        if not str(item.get("planned_section") or "").strip(): errors.append(f"coverage[{i}].planned_section is required")
        if not isinstance(item.get("teaching_mode",[]),list): errors.append(f"coverage[{i}].teaching_mode must be an array")
    counts=Counter(refs)
    for rid,r in req_index.items():
        if r.get("scope_class") == "required" and counts[rid] < 1: errors.append(f"required requirement missing from coverage: {rid}")
    hand=cov.get("constraint_handling")
    if not isinstance(hand,list): errors.append("constraint_handling must be an array"); hand=[]
    handled=set()
    for i,item in enumerate(hand):
        if not isinstance(item,dict): errors.append(f"constraint_handling[{i}] must be an object"); continue
        cid=item.get("constraint_id")
        if cid not in con_ids: errors.append(f"constraint_handling[{i}] references unknown constraint_id {cid!r}")
        else: handled.add(cid)
        if not str(item.get("handling") or "").strip(): errors.append(f"constraint_handling[{i}].handling is required")
    for cid in con_ids:
        if cid not in handled: errors.append(f"constraint missing handling rule: {cid}")
    if cov.get("unresolved") not in ([],None): errors.append("coverage unresolved must be empty before generation")
    return errors


def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("requirements",type=Path); p.add_argument("coverage",type=Path); args=p.parse_args()
    errors=validate(args.requirements,args.coverage)
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("coverage: OK")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
