#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("scope", type=Path)
    p.add_argument("coverage", type=Path)
    p.add_argument("output", type=Path)
    args=p.parse_args()
    errors=[]
    scope=json.loads(args.scope.read_text(encoding="utf-8"))
    if scope.get("status") != "ready" or scope.get("unresolved") not in ([], None): errors.append("scope gate is not ready")
    if not args.coverage.is_file() or len(args.coverage.read_text(encoding="utf-8").strip()) < 40: errors.append("coverage plan missing/empty")
    if not args.output.is_file(): errors.append("output file missing")
    else:
        text=args.output.read_text(encoding="utf-8")
        if len(text.strip()) < 200: errors.append("output appears incomplete")
        if re.search(r"\\\(|\\\)|\\\[|\\\]", text): errors.append("output uses non-dollar math delimiters; normalize if the target workflow requires Markdown+LaTeX dollar delimiters")
    for e in errors: print(f"ERROR: {e}")
    if not errors: print("run: OK")
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
