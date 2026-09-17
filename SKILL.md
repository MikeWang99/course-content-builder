---
name: course-builder
description: Build one bounded course unit or chapter from syllabus files through a gated locate-extract-enrich-classify-plan-generate-validate pipeline with auditable source coverage, learning-mode classification, and configurable bilingual teaching output.
---

# Course Builder v1.3.0

Use this skill when the user supplies syllabi, specifications, course frameworks, official supplements, or related source files and asks for the teaching content of one specific unit, chapter, topic, or bounded topic range.

The governing rule is **evidence flows forward**:

`REQUEST → INVENTORY → LOCATE → REQUIREMENTS → ENRICH → LEARNING MAP → COVERAGE → GENERATE → VALIDATE → OUT`

Never start with a plausible textbook chapter and justify it against the syllabus afterward.

## Default workspace

```text
course-project/
├── sources/
│   ├── syllabi/
│   ├── official-supplements/
│   └── enrichment/
├── prompt.md
├── work/<run-slug>/
│   ├── run.json
│   ├── inventory.json
│   ├── scope.json
│   ├── scope.md
│   ├── requirements.json
│   ├── requirements.md
│   ├── enrichment.md
│   ├── learning-map.json
│   ├── learning-map.md
│   ├── coverage.json
│   └── coverage.md
└── out/<course-slug>/
    ├── <unit-slug>.md
    └── <unit-slug>.sources.json
```

Chat attachments are valid inputs and must follow the same stage order.

## Stage 0 — Bound the request

Identify exactly one target unless the user explicitly requests a multi-unit or whole-course build. Do not silently broaden the scope.

Create `run.json`. Its `language_profile` defaults to `zh-en-teaching`. Its `learning_mode_profile` defaults to `ABC`.

Supported language profiles:

- `zh-en-teaching` — default functional bilingual teaching output;
- `en-full` — essentially all student-facing teaching content in English;
- `zh-full` — Chinese prose with canonical English terminology preserved where useful.

Read `references/language-policy.md` before generation.

## Stage 1 — Inventory and classify sources

Inventory every supplied source before extracting content. Classify sources as `authoritative_syllabus`, `official_supplement`, `user_enrichment`, or `generation_prompt`.

Authority order: authoritative syllabus > official supplement > user enrichment > external research when needed > model background knowledge for explanation only.

Lower-authority material may enrich teaching but may not silently create, delete, or override syllabus requirements.

## Stage 2 — Locate the requested scope (hard gate 1)

Produce `scope.json` and `scope.md` answering only: **where is the requested target in the authoritative source set?**

Use actual source locators. Preserve source terminology and hierarchy. Record ambiguous or neighboring out-of-scope content rather than silently expanding.

Run `python scripts/validate_scope.py work/<run>/scope.json` and do not continue until it passes.

## Stage 3 — Build the official requirement packet (hard gate 2)

Extract all in-scope official requirements into `requirements.json` and `requirements.md`.

Each requirement receives a stable `REQ-*` ID and source locator. Authoritative boundaries/exclusions receive `CON-*` IDs. Never synthesize missing official requirements from memory.

Run `python scripts/validate_requirements.py work/<run>/requirements.json`.

## Stage 4 — Enrichment pass

Only after the official packet is fixed may enrichment be added.

Write `enrichment.md` with provenance labels such as `official-supplement`, `user-supplied-enrichment`, `external-research`, or `model-explanatory-knowledge`.

Use enrichment to improve explanation, sequencing, examples, misconceptions, prerequisite refreshers, and learning strategy—not to redefine official scope.

## Stage 5 — Build the Learning Mode Map (hard gate 3)

After requirements and enrichment are known, classify the chapter's knowledge into a separate pedagogical artifact: `learning-map.json` and `learning-map.md`.

Do **not** put these classifications into `requirements.json`; official requirements must remain source-faithful.

Use three general learning modes:

### Type A — Must Recall
The learner should retrieve this accurately without reconstructing it from first principles every time.

Common examples: definitions, required equations, units, conventions, standard facts, required procedures, named rules, precise high-frequency exam wording.

Default learning action: **compress → closed-book retrieval → spaced retrieval**.

### Type B — Explain / Reconstruct from a Model
The learner should rebuild the explanation from a mental model, causal chain, representation, or governing principle rather than memorize long prose.

Common examples: why a phenomenon happens, causal mechanisms, why a graph/relationship has a certain shape or sign, derivations that can be rebuilt from a smaller model.

Default learning action: **understand model → compress mechanism → reconstruct explanation**.

### Type C — Apply
Mastery is demonstrated by using knowledge in a problem, representation, experiment, or unfamiliar context.

Common examples: calculations, equation/model selection, graph/data interpretation, practical reasoning, unfamiliar applications, multi-step transfer.

Default learning action: **recognize cue/model → practise varied applications → mix unfamiliar contexts**.

Classification is **not mutually exclusive**. Each `KM-*` item has exactly one `primary_type` and may have `secondary_types`. Split a broad requirement into multiple knowledge-map items when that produces a more faithful learning diagnosis.

Read `references/learning-mode-map.md` and run:

```bash
python scripts/validate_learning_map.py \
  work/<run>/requirements.json \
  work/<run>/learning-map.json
```

Every required `REQ-*` must be represented by at least one `KM-*` item before continuing.

## Stage 6 — Build machine-checkable coverage (hard gate 4)

Create `coverage.json` and `coverage.md` before drafting prose.

Every required `REQ-*` ID must map to at least one planned teaching section. Every `CON-*` constraint must have an explicit handling rule.

The coverage plan should use the learning map when choosing teaching modes: retrieval-oriented handling for A, model/causal reconstruction for B, and varied application/recognition work for C.

Run `python scripts/validate_coverage.py work/<run>/requirements.json work/<run>/coverage.json`.

## Stage 7 — Prepare the generation packet

Only after all four gates pass, assemble inputs in this order: bounded request; `scope.json`; `requirements.json`; `enrichment.md`; `learning-map.json` / `learning-map.md`; `coverage.json` / `coverage.md`; `run.json`; then user `prompt.md` or `templates/default-teaching-prompt.md`.

The source packet decides **what must be taught**. The learning map decides **how each knowledge point is best mastered**. The teaching prompt decides **how to teach it**. The language profile decides **which language each kind of content should use**.

## Stage 8 — Generate the bounded teaching artifact

Generate only the requested target. Use adaptive pedagogy rather than mechanical templating.

### Mandatory opening learning classification

Near the beginning—after the opening orientation/driving question and roadmap, but before the main teaching sequence—include a compact section such as `## 本章学习模式地图 · Learning Mode Map`.

Show major knowledge points and their Type A/B/C classification, what mastery means, and the recommended learning action. Use primary and secondary modes when needed.

### Derived learning assets

- **Type A → Must Recall Bank**: compact facts, definitions, equations, conventions, required phrases/procedures; do not create another textbook.
- **Type B → Model Reconstruction Chains**: minimal causal/mechanism chains or representation logic from which the learner can rebuild a full explanation.
- **Type C → Application & Recognition Targets**: cues, first thought/model choice, representation choice, problem families, and unfamiliar-application targets.

Use `Understand → Compress → Retrieve → Apply → Repeat` when helpful, but do not interpret it as “memorize everything.”

### Default bilingual policy: `zh-en-teaching`

Use **English-first** for official terminology, definitions, relationships, derivation physics, graph/vector/spatial language, model conditions, problem cues, worked-example reasoning, and reusable exam-style justifications.

Use **Chinese-first** for section headings, transitions, teaching commentary, misconception framing, summary labels, navigation, and meta-level explanation.

Use selective bilingual presentation for first-use high-value terms, official objective wording plus concise Chinese interpretation, and exam-ready English patterns plus short Chinese notes.

For Obsidian-style Markdown, use `$...$` for inline math and `$$...$$` for display math.

## Stage 9 — Validate against evidence, learning map, and language policy

Check that every required ID is represented and classified; the opening contains the Learning Mode Map; authoritative constraints are respected; enrichment is not presented as official content; terminology and math are valid; scope stays bounded; and the requested language profile is reflected.

Run:

```bash
python scripts/validate_run.py \
  work/<run>/scope.json \
  work/<run>/requirements.json \
  work/<run>/learning-map.json \
  work/<run>/coverage.json \
  out/<course>/<unit>.md \
  --run work/<run>/run.json
```

## Stage 10 — Save reusable output

Write `out/<course-slug>/<unit-slug>.md` and `out/<course-slug>/<unit-slug>.sources.json`.

The provenance file should record source set, matched sections, requirement IDs, learning-map IDs/types, enrichment sources, generation prompt, validation result, unresolved items, and `language_profile`.

Do not silently overwrite prior versions.

## Non-negotiable rules

- Scope before requirements.
- Requirements before enrichment.
- Source-faithful requirements before pedagogical classification.
- Learning map before coverage and prose.
- Coverage before prose.
- Official sources outrank teaching prompts.
- Enrichment cannot become syllabus by implication.
- Missing source information stays missing or unresolved.
- One run produces one bounded target unless explicitly requested otherwise.
- A/B/C classification guides learning action; it does not replace syllabus structure.
- Language choice is functional, not duplicated translation.
