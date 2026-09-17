---
name: course-builder
description: Build one bounded course unit or chapter from syllabus files through a gated locate-extract-enrich-plan-generate-validate pipeline with auditable source coverage and configurable bilingual teaching output.
---

# Course Builder v1.2.1

Use this skill when the user supplies syllabi, specifications, course frameworks, official supplements, or related source files and asks for the teaching content of one specific unit, chapter, topic, or bounded topic range.

The governing rule is **evidence flows forward**:

`REQUEST → INVENTORY → LOCATE → REQUIREMENTS → ENRICH → COVERAGE → GENERATE → VALIDATE → OUT`

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
│   ├── coverage.json
│   └── coverage.md
└── out/<course-slug>/
    ├── <unit-slug>.md
    └── <unit-slug>.sources.json
```

Chat attachments are valid inputs and must follow the same stage order.

## Stage 0 — Bound the request

Identify exactly one target unless the user explicitly requests a multi-unit or whole-course build. Do not silently broaden the scope.

Create `run.json`. Its `language_profile` defaults to `zh-en-teaching` unless the user explicitly requests another profile.

Supported profiles:

- `zh-en-teaching` — default functional bilingual teaching output;
- `en-full` — essentially all student-facing teaching content in English;
- `zh-full` — Chinese prose with canonical English terminology preserved where useful.

Read `references/language-policy.md` before generation.

## Stage 1 — Inventory and classify sources

Inventory every supplied source before extracting content. Classify sources as:

- `authoritative_syllabus`
- `official_supplement`
- `user_enrichment`
- `generation_prompt`

Authority order:

1. authoritative syllabus;
2. official supplements;
3. user enrichment;
4. external research when requested or materially needed for freshness;
5. model background knowledge for explanation only.

Lower-authority material may enrich teaching but may not silently create, delete, or override syllabus requirements.

## Stage 2 — Locate the requested scope (hard gate 1)

Produce `scope.json` and `scope.md` answering only: **where is the requested target in the authoritative source set?**

Use actual source locators. Preserve source terminology and hierarchy. Record ambiguous or neighboring out-of-scope content rather than silently expanding.

Run:

```bash
python scripts/validate_scope.py work/<run>/scope.json
```

Do not continue until it passes.

## Stage 3 — Build the official requirement packet (hard gate 2)

Extract all in-scope official requirements into `requirements.json` and `requirements.md`.

Each requirement receives a stable `REQ-*` ID and source locator. Authoritative boundaries/exclusions receive `CON-*` IDs.

Recommended requirement categories include topic, learning objective, essential knowledge, skill/practice, equation/relationship, assessment objective, prerequisite, and weighting.

Never synthesize missing official requirements from memory.

Run:

```bash
python scripts/validate_requirements.py work/<run>/requirements.json
```

## Stage 4 — Enrichment pass

Only after the official packet is fixed may enrichment be added.

Write `enrichment.md` with provenance labels such as `official-supplement`, `user-supplied-enrichment`, `external-research`, or `model-explanatory-knowledge`.

Use enrichment to improve explanation, sequencing, examples, misconceptions, or prerequisite refreshers—not to redefine official scope.

## Stage 5 — Build machine-checkable coverage (hard gate 3)

Create `coverage.json` and `coverage.md` before drafting prose.

Every required `REQ-*` ID must map to at least one planned teaching section. Every `CON-*` constraint must have an explicit handling rule.

Run:

```bash
python scripts/validate_coverage.py work/<run>/requirements.json work/<run>/coverage.json
```

## Stage 6 — Prepare the generation packet

Only after the three source/coverage gates pass, assemble inputs in this order:

1. bounded user request;
2. `scope.json`;
3. `requirements.json`;
4. `enrichment.md`;
5. `coverage.json` / `coverage.md`;
6. `run.json` language profile;
7. user `prompt.md`, otherwise `templates/default-teaching-prompt.md`.

The source packet decides **what must be taught**. The teaching prompt decides **how to teach it**. The language profile decides **which language each kind of content should use**.

## Stage 7 — Generate the bounded teaching artifact

Generate only the requested target. Use adaptive pedagogy rather than mechanical templating.

### Default bilingual policy: `zh-en-teaching`

This is **not** line-by-line translation. Each language has a different job.

Use **English-first** for content the teacher/student may need to recognize, say, write, or reason with in an English-language exam or classroom, including:

- official terminology and high-value definitions;
- physics/disciplinary relationships;
- directional, spatial, sign, component, and representation relationships;
- graph interpretation statements;
- model assumptions and conditions;
- derivation steps that carry physical meaning;
- problem-recognition cues and exam wording;
- worked-example physics reasoning and short justifications;
- reusable claim/reasoning sentence patterns.

Use **Chinese-first** for reading-load reduction and navigation, including:

- section headings and structural labels;
- transitions between ideas;
- short teaching commentary;
- misconception framing and diagnosis;
- summary/navigation labels such as `核心误区`, `关系式总表`, `知识地图`, `题型识别`, `自查清单`;
- meta-level explanation of why the next step matters.

Use **selective bilingual presentation** for:

- first occurrence of important terminology, e.g. `displacement（位移）`;
- official objective wording followed by a concise Chinese interpretation;
- exam-ready English sentence patterns followed by a short Chinese usage note;
- table labels when both exam recognition and fast scanning matter.

Do not duplicate every paragraph in both languages.

For Markdown intended for Obsidian-style rendering, use `$...$` for inline math and `$$...$$` for display math.

## Stage 8 — Validate against evidence and language policy

Validate the finished document against requirements, coverage, constraints, and `run.json`.

Check at minimum:

- every required ID is represented;
- no authoritative constraint is violated without an explicit extension label;
- no enrichment-only topic is presented as official required content;
- official terminology remains source-faithful;
- formulas and math markup are valid;
- output remains within the requested target;
- the selected `language_profile` is actually reflected in the output.

Run:

```bash
python scripts/validate_run.py \
  work/<run>/scope.json \
  work/<run>/requirements.json \
  work/<run>/coverage.json \
  out/<course>/<unit>.md \
  --run work/<run>/run.json
```

`zh-en-teaching` must contain meaningful amounts of both English and Chinese. `en-full` and `zh-full` are checked against their requested primary language.

## Stage 9 — Save reusable output

Write:

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

The provenance file should record source set, matched sections, requirement IDs, enrichment sources, generation prompt, validation result, unresolved items, and `language_profile`.

Do not silently overwrite prior versions.

## Non-negotiable rules

- Scope before requirements.
- Requirements before enrichment.
- Requirements before coverage.
- Coverage before prose.
- Official sources outrank teaching prompts.
- Enrichment cannot become syllabus by implication.
- Missing source information stays missing or unresolved.
- One run produces one bounded target unless explicitly requested otherwise.
- Language choice is functional, not duplicated translation.
- For `zh-en-teaching`, exam-facing content should remain directly usable in English while Chinese reduces navigation and reading load.
