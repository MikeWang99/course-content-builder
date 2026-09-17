# Pipeline contract · v1.1

Course Builder prevents a long teaching prompt from becoming the source of truth.

## Order

1. **REQUEST** — choose one bounded target.
2. **INVENTORY** — classify all source files by authority.
3. **LOCATE** — prove where the target lives in authoritative sources (`scope.json`).
4. **REQUIREMENTS** — extract atomic official requirements and constraints (`requirements.json`).
5. **ENRICH** — add supplemental teaching material with separate provenance.
6. **COVERAGE** — map every required ID to a planned teaching location (`coverage.json`).
7. **GENERATE** — apply the pedagogical prompt only after the gates pass.
8. **VALIDATE** — verify final prose against requirement IDs and constraints.
9. **OUT** — save the teaching artifact and provenance.

## Three hard gates

- Gate 1: `validate_scope.py`
- Gate 2: `validate_requirements.py`
- Gate 3: `validate_coverage.py`

Generation is allowed only after all three pass.

## Why separate scope from requirements?

`scope.json` proves **where** the requested topic is located. `requirements.json` records **what** the source requires. Keeping these separate prevents an overgrown scope file from mixing location evidence, official content, and teaching interpretation.

## Why machine-readable coverage?

A prose checklist can look complete while silently dropping one learning objective. Stable requirement IDs make omissions detectable before drafting begins.

## Source hierarchy

Authoritative syllabus > official supplement > user enrichment > external research > model explanatory knowledge.

Lower levels can improve explanation but cannot redefine official scope.
