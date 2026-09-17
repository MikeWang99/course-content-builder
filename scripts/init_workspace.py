#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "course"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("root", type=Path)
    p.add_argument("--course", required=True)
    p.add_argument("--target", required=True)
    args = p.parse_args()
    run = f"{slug(args.course)}__{slug(args.target)}"
    for rel in ["sources/syllabi", "sources/enrichment", f"work/{run}", f"out/{slug(args.course)}"]:
        (args.root / rel).mkdir(parents=True, exist_ok=True)
    config = {
        "schema_version": "1.0",
        "course": args.course,
        "target": args.target,
        "run_slug": run,
        "output": f"out/{slug(args.course)}/{slug(args.target)}.md"
    }
    (args.root / f"work/{run}/run.json").write_text(json.dumps(config, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(run)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
