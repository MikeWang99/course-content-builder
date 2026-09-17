# course-content-builder

A source-grounded pipeline for generating one bounded course unit/chapter from syllabus files, with auditable requirement coverage and a practical bilingual teaching mode.

## Core rule

**Prove the syllabus scope before writing teaching prose.**

```text
REQUEST
  ↓
INVENTORY
  ↓
LOCATE → scope.json
  ↓
REQUIREMENTS → requirements.json
  ↓
ENRICH
  ↓
COVERAGE → coverage.json
  ↓
GENERATE with teaching + language profile
  ↓
VALIDATE
  ↓
OUT
```

## Default language profile: `zh-en-teaching`

The output is mixed by function, not translated line by line.

**English-first:** official terminology, definitions, relationships, derivations, graph/vector/spatial language, model conditions, problem cues, worked-example physics reasoning, and exam-style justifications.

**Chinese-first:** section headings, transitions, misconception framing, summary/navigation labels, self-check sections, and teacher-facing commentary.

High-value terms are introduced bilingually when useful, e.g. `displacement（位移）`.

Other supported profiles are `en-full` and `zh-full`.

See `references/language-policy.md` for the detailed contract.

## Inputs

```text
sources/syllabi/
sources/official-supplements/
sources/enrichment/
prompt.md  # optional
```

Files may also be supplied directly to the AI; the same order still applies.

## One run = one bounded target

Examples:

- AP Physics 1 → Kinematics
- CIE IGCSE Physics → Waves
- A Level Physics → Electric Fields

## Initialize

```bash
python scripts/init_workspace.py ./my-course \
  --course "AP Physics 1" \
  --target "Kinematics"
```

This defaults to `zh-en-teaching`. To override:

```bash
python scripts/init_workspace.py ./my-course \
  --course "AP Physics 1" \
  --target "Kinematics" \
  --language-profile en-full
```

## Hard gates

```bash
python scripts/validate_scope.py work/<run>/scope.json
python scripts/validate_requirements.py work/<run>/requirements.json
python scripts/validate_coverage.py work/<run>/requirements.json work/<run>/coverage.json
```

Only after all three pass should generation begin.

## Output

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

See `references/pipeline.md`, `references/language-policy.md`, and the schema references for the full contract.
