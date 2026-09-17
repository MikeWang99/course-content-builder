# Default Teaching Content Prompt · v1.2

Use this prompt only after `scope.json`, `requirements.json`, and `coverage.json` pass validation.

## Mission

Create a complete teaching document for the **requested bounded unit/chapter/topic only**. Assume a learner who is studying the topic systematically for the first time and may not yet see why the ideas are needed.

The official requirement packet controls **what must be covered**. This prompt controls **how to teach it**.

## Output language profile

Unless the user explicitly requests another profile, use `zh-en-teaching` from `references/language-policy.md`.

This is a functional bilingual format, not a translation exercise:

- **English-first:** official terminology, important definitions, physics relationships, directional/spatial statements, graph/representation language, sign conventions, derivation steps with physical meaning, model conditions, problem-recognition cues, exam-style reasoning, and worked-example physics reasoning.
- **Chinese-first:** section headings, transitions, teacher-facing navigation, misconception explanations, summary labels, relationship-table labels, self-check sections, and short pedagogical commentary.
- **Bilingual selectively:** first occurrence of high-value terms, official objective wording plus a concise Chinese interpretation, reusable exam sentence patterns, and table labels when dual recognition is useful.

Do not write every paragraph twice. The English content should be directly usable in class or exam preparation; the Chinese content should reduce reading load and make the teaching structure faster to scan.

## Learning arc

When appropriate, organize the chapter around:

**Curiosity → Question → Need for a model → Concept → Representation → Relationship/equation → Reasoning → Application → Return to the question**

Do not force this arc mechanically onto every minor subsection.

## 1. Begin with a useful driving question

Use one concrete, answerable, syllabus-relevant driving question when the topic supports it.

A good driving question should do at least one of these:

- expose a counterintuitive prediction;
- turn a familiar observation into a precise question;
- reveal why the learner needs a new concept/model;
- support a return-and-explain payoff later.

Do not use generic hooks such as “cars use velocity.”

After the hook, explain in Chinese if useful what tools are still missing, but state the core physical quantities/models in English.

## 2. Make the chapter roadmap causal

Show why one idea leads to the next rather than listing headings only. Chinese transition sentences are encouraged here because they reduce cognitive load.

For example, a new quantity or model should appear because the previous description is insufficient, not merely because it is next in a textbook.

## 3. Teach major concepts with an adaptive concept cycle

For major concepts, use as many of these elements as genuinely help:

- short hook or prediction;
- intuition before notation;
- precise definition;
- why the concept is needed;
- disciplinary/physical meaning;
- representations;
- equation or relationship when relevant;
- why the relationship works;
- conditions and limitations;
- problem-recognition cues;
- application or worked example;
- misconception diagnosis.

Do **not** repeat all of these as twelve fixed headings for every concept.

For high-value terminology, introduce the canonical English term first, e.g. `displacement（位移）`, `instantaneous velocity（瞬时速度）`, `reference frame（参考系）`.

## 4. Explain equations rather than displaying them

For each important relationship, explain as applicable:

- symbols and units;
- scalar/vector or other structural meaning;
- sign conventions;
- assumptions/conditions;
- what changes and what stays fixed;
- why the relationship makes sense;
- how a learner recognizes when to use it.

Use English for the central physics statements and derivation logic when those are likely to be spoken or assessed. Chinese may be used between steps to explain why the next move is natural.

Prefer derivation, graph reasoning, proportional reasoning, or model reasoning over formula memorization when those are appropriate to the subject.

Use `$...$` for inline math and `$$...$$` for display math.

## 5. Connect representations

Where the subject uses multiple representations, explicitly translate between them rather than teaching them independently.

Examples may include verbal descriptions, diagrams, graphs, equations, tables, vectors, symbolic models, experimental data, or other course-specific representations.

Representation relationships should be stated in English where possible, for example:

- `The slope of a position-time graph represents velocity.`
- `The signed area under a velocity-time graph gives displacement.`
- `A negative velocity indicates motion in the chosen negative direction; it does not by itself mean the object is slowing down.`

A concise Chinese explanation may follow when it helps interpretation.

## 6. Teach problem recognition

For each major problem family, explain:

- what cues identify the model;
- the first useful thought;
- what information matters;
- what common cue is misleading;
- what conditions must be checked before using a method.

Keep key cue phrases in English because students may see them directly on exams, e.g. `starts from rest`, `constant acceleration`, `relative to`, `highest point`, `neglect air resistance`.

The target habit is **recognize the model → choose a representation/relationship**, not **see numbers → search for a formula**.

## 7. Use worked examples to expose thinking

Use examples only where they add learning value. Across the chapter, include a useful mix of conceptual, basic quantitative, multi-step, and assessment-style reasoning when relevant to the course.

A strong worked example includes:

**Problem → What should we notice first? → Model/representation → Reasoning → Solution → Check → Common wrong path**

The actual physics reasoning, equations, conditions, and final justification should be English-first. Short Chinese comments may explain why a step is strategically useful.

## 8. Use prediction and cognitive conflict selectively

Before revealing an unintuitive result, invite a prediction when that contrast will genuinely help learning.

Do not turn every subsection into a quiz.

## 9. Diagnose misconceptions

Use Chinese-first diagnostic framing for fast reading, while preserving the central English physics statement.

Recommended form:

**核心误区**

- Wrong intuition: `negative acceleration means slowing down`
- 为什么看起来合理：中文解释
- Where it fails: English physics statement + concise Chinese explanation
- Correct mental model: English-first, with Chinese clarification if needed

Do not merely say “remember this is wrong.”

## 10. Respect official boundaries

Never present enrichment as official required content.

If an extension is useful, label it clearly as an extension/non-required item in language appropriate to the course.

Do not use a familiar textbook topic to override the source packet.

## 11. Integrate official practices and assessment skills

Use the official skills/practices/assessment objectives from `requirements.json` and `coverage.json`.

Where appropriate, preserve exam-style English prompts such as:

- `Predict without calculating.`
- `Sketch the graph.`
- `Explain your reasoning.`
- `Justify your answer using a physics principle.`
- `Compare the two cases.`
- `How would increasing X affect Y?`

Chinese can explain what the prompt is testing or what structure a good response should use.

Only include modes that are actually relevant to the supplied course requirements.

## 12. Close the learning loop

If a driving question was used, return to it near the end. Let the learner try again before giving the complete explanation.

Finish with the most useful subset of:

- 知识地图 / conceptual knowledge map;
- 关系式总表 / relationship table with English relationship statements, meaning, and conditions;
- representation summary;
- 题型识别 / problem-type recognition map;
- 核心误区 / major misconceptions;
- 自查清单 / `I can...` checklist mapped to official requirements.

The ending should make conceptual dependencies visible, not merely repeat section titles.

## Style

Default to the `zh-en-teaching` profile unless the user explicitly overrides it.

Write like an expert teacher who can switch languages strategically: English carries exam-facing physics content; Chinese carries navigation, explanation glue, and teacher-facing structure.

Do not translate the same full paragraph twice. Do not replace standard English physics terminology with improvised Chinese-only phrasing. Preserve official English wording when it has exam value.

Prefer clear, compact explanations over repeated pedagogical boilerplate. Quality > quantity for hooks, stories, and real-world examples.
