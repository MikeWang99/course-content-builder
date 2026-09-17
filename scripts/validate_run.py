#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, re
from pathlib import Path

ROOT=Path(__file__).parent

def load(name:str):
    spec=importlib.util.spec_from_file_location(name,ROOT/f"{name}.py"); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

VS=load("validate_scope"); VR=load("validate_requirements"); VC=load("validate_coverage"); VL=load("validate_language")

def validate(scope:Path, requirements:Path, coverage:Path, output:Path, run:Path|None=None) -> list[str]:
    errors=[]
    errors += [f"scope: {e}" for e in VS.validate(scope)]
    errors += [f"requirements: {e}" for e in VR.validate(requirements)]
    errors += [f"coverage: {e}" for e in VC.validate(requirements,coverage)]
    if not output.is_file(): return errors+["output file missing"]
    text=output.read_text(encoding="utf-8")
    if len(text.strip()) < 200: errors.append("output appears incomplete")
    if re.search(r"\\\(|\\\)|\\\[|\\\]",text): errors.append("output uses non-dollar math delimiters")
    cov=json.loads(coverage.read_text(encoding="utf-8"))
    req=json.loads(requirements.read_text(encoding="utf-8"))
    planned={x.get("requirement_id") for x in cov.get("coverage",[]) if isinstance(x,dict)}
    required={x.get("id") for x in req.get("requirements",[]) if isinstance(x,dict) and x.get("scope_class")=="required"}
    if not required.issubset(planned): errors.append("coverage does not include every required requirement")
    run_path=run or (scope.parent/"run.json")
    if run_path.is_file(): errors += [f"language: {e}" for e in VL.validate(run_path,output)]
    else: errors.append("run.json missing; cannot validate language profile")
    return errors


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("scope",type=Path); p.add_argument("requirements",type=Path); p.add_argument("coverage",type=Path); p.add_argument("output",type=Path)
    p.add_argument("--run",type=Path)
    args=p.parse_args(); errors=validate(args.scope,args.requirements,args.coverage,args.output,args.run)
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("run: OK")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
