---
name: course-builder
description: Build one requested course unit or chapter from local syllabus sources through a gated locate-extract-enrich-generate-validate pipeline, with source traceability and reusable outputs.
---

# Course Builder v1

Use this skill when the user provides one or more syllabi/specifications/course-framework files and asks for the teaching content of a specific unit, chapter, topic, or bounded section.

The governing rule is **scope before prose**. Never begin writing the course notes until the requested scope has been located and recorded from the supplied syllabus sources.

## Default workspace

When operating on a folder, use this structure when possible:

```text
course-project/
├── sources/
│   ├── syllabi/          # authoritative course specifications
│   └── enrichment/       # optional clarifications, teacher notes, supplements
├── prompt.md             # optional user-supplied generation prompt
├── work/
│   └── <run-slug>/
│       ├── inventory.json
│       ├── scope.json
│       ├── scope.md
│       ├── enrichment.md
│       └── coverage.md
└── out/
    └── <course-slug>/
        ├── <unit-slug>.md
        └── <unit-slug>.sources.json
```

If files are attached directly in chat rather than stored in a folder, treat them exactly like `sources/syllabi/` or `sources/enrichment/` inputs and still follow the same stage order.

## Stage 0 — Interpret the request

Identify only the requested bounded target, e.g. `Kinematics`, `Unit 2`, `Chapter 5`, or `Topic 1.3–1.7`.

Do **not** expand the request into the entire course unless the user explicitly asks for the entire course.

Create a stable run slug, e.g. `ap-physics-1__kinematics`.

## Stage 1 — Inventory sources

Inventory all supplied files before searching them.

Classify each source as one of:

- `authoritative_syllabus`: official specification/CED/syllabus/course framework;
- `official_supplement`: official clarification/correction/formula sheet/teacher guide;
- `enrichment`: textbook, teacher notes, user notes, secondary explanation;
- `generation_prompt`: user-supplied writing/pedagogy prompt.

Authority order:

1. authoritative syllabus;
2. official supplements;
3. user-provided enrichment;
4. external research, only when requested or needed for current verification.

Never allow enrichment to silently override a syllabus boundary.

## Stage 2 — Locate the requested scope (mandatory hard gate)

Search the authoritative syllabus sources for the requested unit/chapter/topic and locate the exact relevant section(s).

Produce `work/<run>/scope.json` and `scope.md` before generating teaching prose.

`scope.json` must contain:

```json
{
  "schema_version": "1.0",
  "course": "AP Physics 1",
  "request": "Kinematics",
  "status": "ready",
  "matched_sections": [
    {
      "source_file": "AP-Physics-1-CED.pdf",
      "locator": "Unit 1 / Topics 1.1-1.x / pages ...",
      "title": "...",
      "evidence": "short source-faithful description"
    }
  ],
  "official_requirements": {
    "topics": [],
    "learning_objectives": [],
    "essential_knowledge": [],
    "skills_or_practices": [],
    "equations": [],
    "boundary_statements": [],
    "weighting": []
  },
  "unresolved": []
}
```

Rules:

- `matched_sections` must point to actual supplied source content.
- Preserve the source's terminology and organization.
- Do not fill missing syllabus fields from general knowledge.
- If the requested name is ambiguous, record the competing matches in `unresolved`; do not silently choose a broader scope.
- If the source has no relevant section, say so and do not invent one.

Run `scripts/validate_scope.py` if using a folder workflow. Generation is blocked until it passes.

## Stage 3 — Extract the official content packet

From the located scope, build a compact, source-faithful packet containing only material relevant to the requested target:

- official topic hierarchy;
- learning objectives/outcomes;
- required knowledge/content statements;
- science practices/assessment objectives;
- equations or required relationships;
- boundary/exclusion statements;
- assessment weighting when present;
- prerequisite/dependency statements when present.

This packet is the **content authority** for the generation stage.

Do not copy unrelated neighboring units merely because they appear on the same page.

## Stage 4 — Enrichment pass

Only after the official packet exists, inspect `sources/enrichment/` and any user-supplied supplemental files.

Add useful enrichment to `enrichment.md`, clearly separated from official syllabus requirements.

For every enrichment item, label its provenance as one of:

- `official-supplement`;
- `user-supplied-enrichment`;
- `external-research`.

External web research is optional, not the default. Use it when the user explicitly asks for latest/current verification or when the task requires current official material that is not present locally.

If enrichment conflicts with an authoritative boundary, the syllabus wins and the conflict must be noted.

## Stage 5 — Build the coverage plan before prose

Create `coverage.md` mapping every official requirement to the section where it will be taught.

Minimum structure:

```markdown
| Official requirement | Planned teaching section | Source | Status |
|---|---|---|---|
| ... | ... | ... | planned |
```

No official requirement may disappear between extraction and generation.

If the user's writing prompt contains a hard-coded topic list that differs from the official packet, treat that list as a **teaching suggestion**, not as syllabus authority. Required source content must be included; out-of-scope material must be marked as extension or omitted according to the prompt.

## Stage 6 — Generate only the requested unit/chapter

Choose the generation prompt in this order:

1. user-supplied `prompt.md` or explicitly attached prompt;
2. `templates/default-teaching-prompt.md`.

The generation model receives, in this order:

1. the bounded user request;
2. `scope.json` / official content packet;
3. enrichment packet;
4. coverage plan;
5. the generation prompt.

This order is mandatory. The generation prompt controls pedagogy and style, but it may not expand or contradict the official scope packet.

For very large units, generate internally in sections if necessary, then assemble one coherent final unit document. Do not respond with a partial unit merely because the prompt is long.

## Stage 7 — Validate

Before delivery, check:

- every official requirement in `coverage.md` is represented;
- no boundary statement is violated without an explicit extension label;
- no unsupported topic is presented as required syllabus content;
- terminology is consistent with the source;
- formulas/math markup are valid and not duplicated by rendering artifacts;
- hooks/examples return to the concepts they introduce when required by the generation prompt;
- output is only the requested unit/chapter, not the full course.

When using a folder workflow, run `scripts/validate_run.py`.

## Stage 8 — Save outputs

If the user asks to save/manage the result, write the finished unit to:

```text
out/<course-slug>/<unit-slug>.md
```

Also save a compact provenance file:

```text
out/<course-slug>/<unit-slug>.sources.json
```

The provenance file should list source files, matched syllabus sections, enrichment sources, unresolved items (normally empty), and generation prompt used.

Do not overwrite a previous output silently. If the same unit already exists, use an explicit revision suffix or intentionally update it when the user asks.

## Non-negotiable order

`REQUEST → INVENTORY → LOCATE → EXTRACT → ENRICH → COVERAGE PLAN → GENERATE → VALIDATE → OUT`

Never reorder this as `REQUEST → GENERATE → check syllabus afterward`.
