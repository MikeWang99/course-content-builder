# course-content-builder

A source-grounded pipeline for generating one bounded course unit/chapter from syllabus files.

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
GENERATE
  ↓
VALIDATE
  ↓
OUT
```

Version 1.1 adds three explicit hard gates so a long teaching prompt cannot become the de facto syllabus.

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

The pipeline does not generate the full course unless explicitly requested.

## Initialize

```bash
python scripts/init_workspace.py ./my-course --course "AP Physics 1" --target "Kinematics"
```

Then place sources in the workspace and invoke `$course-builder`.

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

See `references/pipeline.md` for the stage contract and `references/prompt-audit.md` for the audit of the original long teaching prompt.
