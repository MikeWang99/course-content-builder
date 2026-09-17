# course-content-builder

A source-grounded pipeline for generating one bounded course unit/chapter from syllabus files, with auditable requirement coverage, A/B/C learning-mode classification, and practical bilingual teaching output.

## Core rule

**Prove the syllabus scope before writing teaching prose, then classify how each knowledge point should be learned.**

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
LEARNING MAP → learning-map.json
  ↓
COVERAGE → coverage.json
  ↓
GENERATE with teaching + language profile
  ↓
VALIDATE
  ↓
OUT
```

## Learning Mode Map

Every chapter classifies its knowledge using a course-general model:

- **A · Must Recall** — retrieve accurately.
- **B · Explain / Reconstruct from a Model** — rebuild from mechanism, causal chain, representation, or principle.
- **C · Apply** — transfer to problems, graphs, data, experiments, model selection, and unfamiliar contexts.

Classification uses one `primary_type` plus optional `secondary_types`, so knowledge does not have to fit one rigid box.

The generated chapter shows this map near the beginning, then derives three revision assets near the end: **Must Recall Bank**, **Model Reconstruction Chains**, and **Application & Recognition Targets**.

## Default language profile: `zh-en-teaching`

The output is mixed by function, not translated line by line.

**English-first:** official terminology, definitions, relationships, derivations, graph/vector/spatial language, model conditions, problem cues, worked-example reasoning, and exam-style justifications.

**Chinese-first:** section headings, transitions, misconception framing, summary/navigation labels, self-check sections, and teacher-facing commentary.

Other supported profiles are `en-full` and `zh-full`.

## Inputs

```text
sources/syllabi/
sources/official-supplements/
sources/enrichment/
prompt.md  # optional
```

## Initialize

```bash
python scripts/init_workspace.py ./my-course \
  --course "AP Physics 1" \
  --target "Kinematics"
```

## Hard gates

```bash
python scripts/validate_scope.py work/<run>/scope.json
python scripts/validate_requirements.py work/<run>/requirements.json
python scripts/validate_learning_map.py work/<run>/requirements.json work/<run>/learning-map.json
python scripts/validate_coverage.py work/<run>/requirements.json work/<run>/coverage.json
```

Only after all four pass should generation begin.

## Output

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

See `references/pipeline.md`, `references/learning-mode-map.md`, `references/language-policy.md`, and the schema references for the full contract.
