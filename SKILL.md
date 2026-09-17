---
name: course-builder
description: Build one bounded course unit or chapter from syllabus files through a gated locate-extract-enrich-plan-generate-validate pipeline with auditable source coverage.
---

# Course Builder v1.1

Use this skill when the user supplies syllabi, specifications, course frameworks, official supplements, or related source files and asks for the teaching content of one specific unit, chapter, topic, or bounded topic range.

The governing rule is **evidence flows forward**:

`REQUEST → INVENTORY → LOCATE → REQUIREMENTS → ENRICH → COVERAGE → GENERATE → VALIDATE → OUT`

Never start with a plausible textbook chapter and justify it against the syllabus afterward.

## Default workspace

```text
course-project/
├── sources/
│   ├── syllabi/                # authoritative syllabus/specification/CED files
│   ├── official-supplements/   # clarifications, corrections, formula sheets, official guides
│   └── enrichment/             # user notes, textbooks, secondary material
├── prompt.md                   # optional user-supplied teaching/writing prompt
├── work/
│   └── <run-slug>/
│       ├── run.json
│       ├── inventory.json
│       ├── scope.json
│       ├── scope.md
│       ├── requirements.json
│       ├── requirements.md
│       ├── enrichment.md
│       ├── coverage.json
│       └── coverage.md
└── out/
    └── <course-slug>/
        ├── <unit-slug>.md
        └── <unit-slug>.sources.json
```

Chat attachments are valid inputs. Treat authoritative attached syllabi as if they were in `sources/syllabi/`; preserve the same stage order.

## Stage 0 — Bound the request

Identify exactly one target unless the user explicitly requests a multi-unit or whole-course build.

Examples: `Kinematics`, `Unit 2`, `Chapter 5`, `Topics 1.3–1.7`.

Create a stable run slug such as `ap-physics-1__kinematics`.

Do not silently broaden `Kinematics` into all mechanics or the full course.

## Stage 1 — Inventory and classify sources

Inventory every supplied source before extracting content.

Classify each source as:

- `authoritative_syllabus`
- `official_supplement`
- `user_enrichment`
- `generation_prompt`

Record filename/title, authority class, edition/year when known, and any obvious limitations.

Authority order:

1. authoritative syllabus;
2. official supplements;
3. user enrichment;
4. external research when explicitly requested or materially needed for freshness;
5. model background knowledge for explanation only.

Lower-authority material may enrich teaching but may not silently create, delete, or override syllabus requirements.

## Stage 2 — Locate the requested scope (hard gate 1)

Search authoritative sources for the exact requested target. Produce `scope.json` and `scope.md`.

`scope.json` answers only: **where is the requested target in the authoritative source set?**

Canonical shape:

```json
{
  "schema_version": "1.1",
  "course": "AP Physics 1",
  "request": "Kinematics",
  "status": "ready",
  "matched_sections": [
    {
      "source_file": "AP-Physics-1-CED.pdf",
      "locator": "Unit ... / Topics ... / pages ...",
      "title": "...",
      "evidence": "short source-faithful description"
    }
  ],
  "excluded_neighbors": [],
  "unresolved": []
}
```

Rules:

- `matched_sections` must point to actual supplied source content.
- Preserve source terminology and hierarchy.
- Record neighboring material that looks similar but is outside the requested scope in `excluded_neighbors` when this helps prevent accidental expansion.
- If the request maps ambiguously to multiple sections, set `status: review` and explain the ambiguity.
- If no relevant authoritative section exists, do not invent one.

Run `scripts/validate_scope.py`. Generation remains blocked until this gate passes.

## Stage 3 — Build the official requirement packet (hard gate 2)

From the located sections, extract all in-scope official requirements into `requirements.json` and a readable `requirements.md`.

Do **not** use a hard-coded teaching outline as the source of truth.

Every requirement receives a stable ID and source locator:

```json
{
  "schema_version": "1.1",
  "course": "AP Physics 1",
  "request": "Kinematics",
  "requirements": [
    {
      "id": "REQ-001",
      "category": "learning_objective",
      "text": "...",
      "source_file": "AP-Physics-1-CED.pdf",
      "locator": "...",
      "scope_class": "required"
    }
  ],
  "constraints": [
    {
      "id": "CON-001",
      "category": "boundary_statement",
      "text": "...",
      "source_file": "AP-Physics-1-CED.pdf",
      "locator": "..."
    }
  ],
  "unresolved": []
}
```

Recommended requirement categories include:

- `topic`
- `learning_objective`
- `essential_knowledge`
- `skill_or_practice`
- `equation_or_relationship`
- `assessment_objective`
- `prerequisite`
- `weighting`

Use `constraints` for boundary/exclusion statements that control what must **not** be presented as required content.

Possible `scope_class` values:

- `required`
- `optional_official`
- `supporting`

Never synthesize missing official requirements from model knowledge.

Run `scripts/validate_requirements.py` before continuing.

## Stage 4 — Enrichment pass

Only after the official requirement packet is fixed may enrichment be added.

Write `enrichment.md` with clearly separated provenance labels:

- `official-supplement`
- `user-supplied-enrichment`
- `external-research`
- `model-explanatory-knowledge`

Use enrichment for better explanations, examples, prerequisite refreshers, misconceptions, or teaching sequence—not to redefine official scope.

If enrichment conflicts with an authoritative constraint, the authoritative source wins and the conflict must be recorded.

External research is not mandatory when the supplied authoritative source set is sufficient. If current verification is required, keep externally verified facts distinguishable from locally sourced requirements.

## Stage 5 — Build machine-checkable coverage (hard gate 3)

Create both `coverage.json` and `coverage.md` **before** drafting the teaching chapter.

`coverage.json` maps each requirement ID to a planned destination:

```json
{
  "schema_version": "1.1",
  "status": "ready",
  "coverage": [
    {
      "requirement_id": "REQ-001",
      "planned_section": "Velocity",
      "teaching_mode": ["intuition", "representation", "worked_example"],
      "status": "planned"
    }
  ],
  "constraint_handling": [
    {
      "constraint_id": "CON-001",
      "handling": "exclude-or-label-extension"
    }
  ],
  "unresolved": []
}
```

Rules:

- Every `required` requirement must appear exactly once or more in the coverage plan.
- No unknown requirement ID may appear.
- Every authoritative constraint must have an explicit handling rule.
- A user prompt's hard-coded topic list is advisory only. If it conflicts with the official packet, the official packet wins.

Run `scripts/validate_coverage.py`.

## Stage 6 — Prepare the generation packet

Only after the three gates pass, assemble the generation inputs in this order:

1. bounded user request;
2. `scope.json`;
3. `requirements.json`;
4. `enrichment.md`;
5. `coverage.json` / `coverage.md`;
6. user `prompt.md`, otherwise `templates/default-teaching-prompt.md`.

The first five items decide **what must be taught and what is bounded**. The generation prompt decides **how to teach and how to write**.

A generation prompt may not override an official requirement or constraint.

## Stage 7 — Generate the bounded teaching artifact

Generate only the requested target.

For large units, drafting may happen internally in sections, but the delivered artifact should be coherent and complete.

Use adaptive pedagogy rather than mechanical templating. A hook, misconception block, worked example, graph translation task, or derivation should appear because it serves learning—not because every subsection must contain every device.

When optional extension material materially improves understanding, label it clearly as non-required/extension content according to the course context.

For Markdown intended for Obsidian-style rendering, use `$...$` for inline math and `$$...$$` for display math.

## Stage 8 — Validate against evidence, not memory

Validate the finished document against `requirements.json`, `coverage.json`, and authoritative constraints.

Check at minimum:

- all required IDs planned in coverage are actually represented in the final artifact;
- no authoritative constraint is violated without an explicit extension label;
- no enrichment-only topic is presented as official required content;
- official terminology remains source-faithful;
- formulas and math markup are valid and not duplicated by paste/render artifacts;
- teaching devices introduced in the prompt are closed properly (for example, a driving question is revisited if one was used);
- output remains within the requested target.

Run `scripts/validate_run.py` in folder workflows.

## Stage 9 — Save reusable output

Write:

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

The companion provenance file records the source set, matched sections, requirement IDs, enrichment sources, generation prompt, validation result, and unresolved items.

Do not silently overwrite prior versions. Update intentionally when requested or create an explicit revision.

## Non-negotiable rules

- Scope before requirements.
- Requirements before enrichment.
- Requirements before coverage.
- Coverage before prose.
- Official sources outrank teaching prompts.
- Enrichment cannot become syllabus by implication.
- Missing source information stays missing or unresolved; do not fill it from memory.
- One run produces one bounded target unless the user explicitly asks otherwise.
