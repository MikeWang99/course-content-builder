#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

PRIMARY_TYPES={"A","B","C"}

def validate(requirements_path: Path, learning_map_path: Path) -> list[str]:
    req=json.loads(requirements_path.read_text(encoding="utf-8"))
    data=json.loads(learning_map_path.read_text(encoding="utf-8"))
    errors=[]
    if data.get("schema_version") != "1.3": errors.append("learning-map schema_version must be 1.3")
    if data.get("status") != "ready": errors.append("learning-map status must be ready before coverage/generation")
    req_ids={r.get("id") for r in req.get("requirements",[]) if isinstance(r,dict) and r.get("id")}
    required_ids={r.get("id") for r in req.get("requirements",[]) if isinstance(r,dict) and r.get("scope_class")=="required"}
    items=data.get("items")
    if not isinstance(items,list): errors.append("items must be an array"); items=[]
    mapped=set(); seen_ids=set()
    for i,item in enumerate(items):
        if not isinstance(item,dict): errors.append(f"items[{i}] must be an object"); continue
        kid=str(item.get("id") or "")
        if not kid.startswith("KM-"): errors.append(f"items[{i}].id must start with KM-")
        if kid in seen_ids: errors.append(f"duplicate learning-map id: {kid}")
        seen_ids.add(kid)
        if not str(item.get("title") or "").strip(): errors.append(f"{kid or f'items[{i}]'}.title is required")
        refs=item.get("requirement_ids")
        if not isinstance(refs,list) or not refs: errors.append(f"{kid}.requirement_ids must be a non-empty array"); refs=[]
        for rid in refs:
            if rid not in req_ids: errors.append(f"{kid} references unknown requirement_id {rid!r}")
            else: mapped.add(rid)
        primary=item.get("primary_type")
        if primary not in PRIMARY_TYPES: errors.append(f"{kid}.primary_type must be one of A, B, C")
        secondary=item.get("secondary_types",[])
        if not isinstance(secondary,list): errors.append(f"{kid}.secondary_types must be an array")
        else:
            if any(x not in PRIMARY_TYPES for x in secondary): errors.append(f"{kid}.secondary_types may contain only A, B, C")
            if primary in secondary: errors.append(f"{kid}.secondary_types must not repeat primary_type")
            if len(set(secondary)) != len(secondary): errors.append(f"{kid}.secondary_types contains duplicates")
        if not str(item.get("rationale") or "").strip(): errors.append(f"{kid}.rationale is required")
        if not str(item.get("recommended_learning_action") or "").strip(): errors.append(f"{kid}.recommended_learning_action is required")
    for rid in sorted(required_ids):
        if rid not in mapped: errors.append(f"required requirement missing from learning map: {rid}")
    if data.get("unresolved") not in ([],None): errors.append("learning-map unresolved must be empty before coverage/generation")
    return errors


def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("requirements",type=Path); p.add_argument("learning_map",type=Path); args=p.parse_args()
    errors=validate(args.requirements,args.learning_map)
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("learning-map: OK")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
