# Pipeline contract · v1.3

Course Builder prevents a long teaching prompt from becoming the source of truth and separates source facts from pedagogical interpretation.

## Order

1. **REQUEST** — choose one bounded target.
2. **INVENTORY** — classify all source files by authority.
3. **LOCATE** — prove where the target lives in authoritative sources (`scope.json`).
4. **REQUIREMENTS** — extract atomic official requirements and constraints (`requirements.json`).
5. **ENRICH** — add supplemental teaching material with separate provenance.
6. **LEARNING MAP** — classify knowledge by how it must be mastered (`learning-map.json`).
7. **COVERAGE** — map every required ID to a planned teaching location (`coverage.json`).
8. **GENERATE** — apply the pedagogical prompt only after the gates pass.
9. **VALIDATE** — verify final prose against requirement IDs, learning map, language profile, and constraints.
10. **OUT** — save the teaching artifact and provenance.

## Four hard gates

- Gate 1: `validate_scope.py`
- Gate 2: `validate_requirements.py`
- Gate 3: `validate_learning_map.py`
- Gate 4: `validate_coverage.py`

Generation is allowed only after all four pass.

## Why a separate learning map?

`requirements.json` must stay source-faithful. Whether a learner should **recall**, **reconstruct/explain**, or **apply** a knowledge point is a teaching interpretation, not an official syllabus fact. Keeping `learning-map.json` separate preserves provenance while making study strategy explicit.

## Learning modes

- **A · Must Recall** — accurate retrieval is central.
- **B · Explain / Reconstruct from a Model** — rebuild from mechanism, representation, or causal chain.
- **C · Apply** — use knowledge in calculations, graphs, data, experiments, model selection, or unfamiliar contexts.

A knowledge point has one primary type and may have secondary types.

## Why machine-readable coverage?

A prose checklist can look complete while silently dropping one learning objective. Stable requirement IDs make omissions detectable before drafting begins.

## Source hierarchy

Authoritative syllabus > official supplement > user enrichment > external research > model explanatory knowledge.

Lower levels can improve explanation but cannot redefine official scope.
