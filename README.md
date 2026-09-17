# course-builder

A source-grounded pipeline for generating one requested course unit/chapter from syllabus files.

## Core idea

Do not ask an LLM to "write Kinematics" first. Make it prove the syllabus scope first.

```text
REQUEST
  ↓
INVENTORY
  ↓
LOCATE exact syllabus section
  ↓
EXTRACT official requirements
  ↓
ENRICH (separate provenance)
  ↓
COVERAGE PLAN
  ↓
GENERATE with teaching prompt
  ↓
VALIDATE against scope/boundaries
  ↓
OUT
```

## Inputs

Put official syllabi/specifications in `sources/syllabi/`, optional supplements in `sources/enrichment/`, and optionally add `prompt.md`. Files may also be supplied directly to the AI; the same stage order still applies.

## One run = one bounded target

Examples:

- AP Physics 1 → Kinematics
- CIE IGCSE Physics → Waves
- A Level Physics → Electric Fields

The pipeline does not generate the entire course unless explicitly requested.

## Initialize a workspace

```bash
python scripts/init_workspace.py ./my-course --course "AP Physics 1" --target "Kinematics"
```

Then add source files and invoke `$course-builder`.

## Output

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

See `references/pipeline.md` for the full contract and `references/prompt-audit.md` for the audit of the original long AP Physics 1 prompt that motivated this pipeline.
