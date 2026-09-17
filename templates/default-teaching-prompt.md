# Default Teaching Content Prompt · v1.3

Use this prompt only after `scope.json`, `requirements.json`, `learning-map.json`, and `coverage.json` pass validation.

## Mission

Create a complete teaching document for the **requested bounded unit/chapter/topic only**. Assume a learner who is studying the topic systematically for the first time and may not yet see why the ideas are needed.

The official requirement packet controls **what must be covered**. The learning map controls **how each item is best mastered**. This prompt controls **how to teach it**.

## Output language profile

Unless the user explicitly requests another profile, use `zh-en-teaching` from `references/language-policy.md`.

This is a functional bilingual format, not a translation exercise:

- **English-first:** official terminology, important definitions, physical/disciplinary relationships, directional/spatial statements, graph/representation language, sign conventions, derivation steps with physical meaning, model conditions, problem-recognition cues, exam-style reasoning, and worked-example reasoning.
- **Chinese-first:** section headings, transitions, teacher-facing navigation, misconception explanations, summary labels, self-check sections, and short pedagogical commentary.
- **Bilingual selectively:** first occurrence of high-value terms, official objective wording plus a concise Chinese interpretation, reusable exam sentence patterns, and table labels when dual recognition is useful.

Do not write every paragraph twice.

## Learning strategy layer

Use the A/B/C knowledge classification from `learning-map.json`.

- **Type A · Must Recall** — precise retrieval matters.
- **Type B · Explain / Reconstruct from a Model** — rebuild from a mental model, causal chain, representation, or governing principle.
- **Type C · Apply** — use knowledge in calculations, graphs, data, experiments, model selection, or unfamiliar contexts.

A knowledge point may have secondary types. Do not force a false either/or classification.

Use the general learning loop when helpful: **Understand → Compress → Retrieve → Apply → Repeat**. This loop does not mean all knowledge should be memorized.

## 1. Begin with a useful driving question

Use one concrete, answerable, syllabus-relevant driving question when the topic supports it. Prefer a counterintuitive prediction, familiar observation turned precise, or a question that reveals why a new model is needed.

After the hook, explain what tools are still missing. State core disciplinary quantities/models in English where useful.

## 2. Give a causal roadmap

Show why one idea leads to the next rather than listing headings only. Chinese transition sentences are encouraged here because they reduce cognitive load.

## 3. Show the chapter Learning Mode Map near the beginning

After the opening orientation/driving question and roadmap, insert `## 本章学习模式地图 · Learning Mode Map`.

Create a compact table based on `learning-map.json`:

| Knowledge point | Type | What mastery means | Best learning action |
|---|---|---|---|
| ... | A · Must Recall | accurate retrieval | closed-book + spaced retrieval |
| ... | B · Explain from a Model | rebuild explanation from mechanism/model | causal/model reconstruction |
| ... | C · Apply | transfer to problems/representations | varied application |

Keep the table useful for planning and scanning. Do not dump raw JSON or requirement IDs unless they help the teacher. If one item has secondary types, show them concisely, e.g. `A → C` or `B + C`.

## 4. Teach major concepts with an adaptive concept cycle

For major concepts, use as many of these elements as genuinely help: short hook/prediction; intuition; precise definition; why the concept is needed; physical meaning; representations; equation/relationship; why it works; conditions; problem-recognition cues; application/worked example; misconception diagnosis.

Do **not** repeat all of these as fixed headings for every concept. For high-value terminology, introduce the canonical English term first, e.g. `displacement（位移）`.

## 5. Match teaching method to learning type

### For Type A
Make the target compact and recallable. Prefer exact definitions, equations, units, conventions, standard facts, procedure points, or reusable exam wording. Avoid burying recall targets inside long prose.

### For Type B
Teach the smallest model or mechanism that lets the learner regenerate the explanation. Prefer causal chains, diagrams, representations, conservation arguments, governing principles, or qualitative relationships over memorized paragraphs.

### For Type C
Teach recognition and transfer: what cue suggests the model, what should be represented first, what changes across contexts, and how to test the idea in unfamiliar questions.

## 6. Explain equations rather than displaying them

For each important relationship, explain symbols/units, structure, sign conventions, assumptions, what changes and stays fixed, why it makes sense, and how to recognize when to use it.

Use English for central disciplinary statements and derivation logic when those are likely to be spoken or assessed. Chinese may connect steps.

Use `$...$` for inline math and `$$...$$` for display math.

## 7. Connect representations

Translate explicitly among verbal descriptions, diagrams, graphs, equations, tables, vectors, symbolic models, experimental data, or other course-relevant representations. Representation relationships should be English-first when exam recognition matters.

## 8. Teach problem recognition

For each major problem family, explain cues, first useful thought, relevant information, misleading cues, and conditions that must be checked. Keep common exam cues in English when useful.

Target habit: **recognize the model → choose a representation/relationship**, not **see numbers → search for a formula**.

## 9. Use worked examples to expose thinking

Use examples where they add learning value. A strong example includes **Problem → What should we notice first? → Model/representation → Reasoning → Solution → Check → Common wrong path**.

The actual disciplinary reasoning, equations, conditions, and final justification should be English-first under `zh-en-teaching`. Short Chinese comments may explain strategy.

## 10. Diagnose misconceptions

Use Chinese-first diagnostic framing for fast reading while preserving the central English disciplinary statement. Recommended structure: Wrong intuition → 为什么看起来合理 → Where it fails → Correct mental model.

## 11. Respect official boundaries

Never present enrichment as official required content. If an extension is useful, label it clearly as non-required/extension content.

## 12. Integrate official practices and assessment skills

Use the official skills/practices/assessment objectives from `requirements.json` and `coverage.json`. Where relevant, preserve exam-style English prompts such as `Predict without calculating`, `Sketch the graph`, `Explain your reasoning`, `Justify your answer`, `Compare`, or `How would X affect Y?`.

## 13. Close the learning loop with type-specific revision assets

If a driving question was used, return to it first.

Then include the most useful subset of the following, with the first three driven directly by `learning-map.json`:

### A. Must Recall Bank
A compact bank for Type A items. Include only high-value definitions, equations, units, conventions, required facts, procedures, or wording. Keep it short enough to retrieve repeatedly; do not make another textbook.

### B. Model Reconstruction Chains
For Type B items, provide minimal model/causal skeletons from which a student can regenerate the full explanation, e.g. `cause → intermediate physical change → consequence → observable result`. The skeleton should reduce memorization, not become a memorized paragraph.

### C. Application & Recognition Targets
For Type C items, summarize problem cues, first thought/model choice, representation choice, common transfer variations, and what unfamiliar applications should be practised.

Also add where useful: 知识地图 / conceptual knowledge map; 关系式总表 / relationship table; representation summary; 题型识别 / problem-type map; 核心误区 / major misconceptions; 自查清单 / `I can...` checklist mapped to official requirements.

## Style

Write like an expert teacher who can switch languages strategically and choose different learning methods for different knowledge types.

Do not translate the same full paragraph twice. Do not replace standard English terminology with improvised Chinese-only wording. Do not make every item look equally memorization-heavy.

Prefer clear, compact explanations over repeated pedagogical boilerplate. Quality > quantity for hooks, stories, and examples.
