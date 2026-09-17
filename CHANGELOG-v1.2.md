# v1.2.0 — Bilingual teaching output

- Added explicit `zh-en-teaching` language profile as the default output mode.
- English-first for exam-facing terminology, definitions, relationships, derivations, representations, conditions, problem cues, and physics reasoning.
- Chinese-first for headings, transitions, misconception framing, summary/navigation labels, and teacher-facing commentary.
- Added selective bilingual rules to avoid wasteful full-paragraph duplication.
- Added `references/language-policy.md`.
- Added run-level `language_profile` configuration with `zh-en-teaching`, `en-full`, and `zh-full` options.
- Updated the bundled teaching prompt and Skill generation/validation rules to enforce the language policy.
