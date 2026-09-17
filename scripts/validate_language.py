#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

PROFILES={"zh-en-teaching","en-full","zh-full"}

def stats(text:str)->tuple[int,int]:
    cjk=len(re.findall(r"[\u3400-\u9fff]",text))
    english=len(re.findall(r"\b[A-Za-z][A-Za-z'-]*\b",text))
    return cjk,english

def validate(run_path:Path, output_path:Path)->list[str]:
    run=json.loads(run_path.read_text(encoding="utf-8")); errors=[]
    profile=run.get("language_profile","zh-en-teaching")
    if profile not in PROFILES: return [f"unknown language_profile: {profile}"]
    if not output_path.is_file(): return ["output file missing"]
    text=output_path.read_text(encoding="utf-8"); cjk,english=stats(text)
    if profile=="zh-en-teaching":
        if cjk < 40: errors.append("zh-en-teaching requires meaningful Chinese navigation/explanation content")
        if english < 60: errors.append("zh-en-teaching requires meaningful English exam/teaching content")
    elif profile=="en-full":
        if english < 100: errors.append("en-full output does not contain enough English content")
    elif profile=="zh-full":
        if cjk < 100: errors.append("zh-full output does not contain enough Chinese content")
    return errors

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("run",type=Path); p.add_argument("output",type=Path); args=p.parse_args()
    errors=validate(args.run,args.output)
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("language: OK")
    return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
