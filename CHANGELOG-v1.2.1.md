# v1.2.1 — Enforced bilingual output gate

- Added `scripts/validate_language.py`.
- `zh-en-teaching` now requires meaningful Chinese navigation/explanation content and meaningful English exam/teaching content.
- `en-full` and `zh-full` are also validated against their requested primary language.
- `validate_run.py` now reads `run.json` (or `--run`) and applies the selected language profile as part of the final hard gate.
- Updated the Skill contract so English carries exam-facing terminology, relationships, derivation logic, representation language, conditions, problem cues, and worked-example reasoning, while Chinese carries headings, transitions, misconception framing, navigation, and reading-load reduction.
- Added regression tests that reject Chinese-only or English-only output when `zh-en-teaching` is selected.
