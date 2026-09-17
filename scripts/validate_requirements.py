#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

ALLOWED_SCOPE_CLASSES={"required","optional_official","supporting"}

def validate(path: Path) -> list[str]:
    data=json.loads(path.read_text(encoding="utf-8")); errors=[]
    if data.get("schema_version") != "1.1": errors.append("schema_version must be 1.1")
    if not str(data.get("request") or "").strip(): errors.append("request is required")
    reqs=data.get("requirements")
    if not isinstance(reqs,list): errors.append("requirements must be an array"); reqs=[]
    cons=data.get("constraints")
    if not isinstance(cons,list): errors.append("constraints must be an array"); cons=[]
    seen=set()
    for kind,items,prefix in (("requirements",reqs,"REQ-"),("constraints",cons,"CON-")):
        for i,item in enumerate(items):
            if not isinstance(item,dict): errors.append(f"{kind}[{i}] must be an object"); continue
            rid=str(item.get("id") or "")
            if not rid.startswith(prefix): errors.append(f"{kind}[{i}].id must start with {prefix}")
            if rid in seen: errors.append(f"duplicate id: {rid}")
            seen.add(rid)
            for key in ("category","text","source_file","locator"):
                if not str(item.get(key) or "").strip(): errors.append(f"{rid or kind+'['+str(i)+']'}.{key} is required")
            if kind == "requirements" and item.get("scope_class") not in ALLOWED_SCOPE_CLASSES:
                errors.append(f"{rid}.scope_class must be one of {sorted(ALLOWED_SCOPE_CLASSES)}")
    if data.get("unresolved") not in ([],None): errors.append("unresolved must be empty before coverage/generation")
    if not reqs and not cons: errors.append("requirements packet is empty; extract source-supported content or keep run unresolved")
    return errors


def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("requirements",type=Path); args=p.parse_args()
    errors=validate(args.requirements)
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("requirements: OK")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
