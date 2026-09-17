#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

PROFILES=("zh-en-teaching","en-full","zh-full")

def slug(text:str)->str:
    value=re.sub(r"[^a-z0-9]+","-",text.lower()).strip("-")
    return value or "course"

def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument("root",type=Path)
    p.add_argument("--course",required=True)
    p.add_argument("--target",required=True)
    p.add_argument("--language-profile",choices=PROFILES,default="zh-en-teaching")
    args=p.parse_args()
    course_slug,target_slug=slug(args.course),slug(args.target); run=f"{course_slug}__{target_slug}"
    for rel in ["sources/syllabi","sources/official-supplements","sources/enrichment",f"work/{run}",f"out/{course_slug}"]:
        (args.root/rel).mkdir(parents=True,exist_ok=True)
    config={
        "schema_version":"1.3",
        "course":args.course,
        "target":args.target,
        "run_slug":run,
        "language_profile":args.language_profile,
        "learning_mode_profile":"ABC",
        "output":f"out/{course_slug}/{target_slug}.md",
        "provenance":f"out/{course_slug}/{target_slug}.sources.json"
    }
    (args.root/f"work/{run}/run.json").write_text(json.dumps(config,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(run); return 0

if __name__ == "__main__": raise SystemExit(main())
