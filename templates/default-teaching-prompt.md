# Default Teaching Content Prompt · v1.1

Use this prompt only after `scope.json`, `requirements.json`, and `coverage.json` pass validation.

## Mission

Create a complete teaching document for the **requested bounded unit/chapter/topic only**. Assume a learner who is studying the topic systematically for the first time and may not yet see why the ideas are needed.

The official requirement packet controls **what must be covered**. This prompt controls **how to teach it**.

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

After the hook, explicitly identify what tools the learner does not yet have and show how the chapter will acquire them.

## 2. Make the chapter roadmap causal

Show why one idea leads to the next rather than listing headings only.

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

## 4. Explain equations rather than displaying them

For each important relationship, explain as applicable:

- symbols and units;
- scalar/vector or other structural meaning;
- sign conventions;
- assumptions/conditions;
- what changes and what stays fixed;
- why the relationship makes sense;
- how a learner recognizes when to use it.

Prefer derivation, graph reasoning, proportional reasoning, or model reasoning over formula memorization when those are appropriate to the subject.

Use `$...$` for inline math and `$$...$$` for display math.

## 5. Connect representations

Where the subject uses multiple representations, explicitly translate between them rather than teaching them independently.

Examples may include verbal descriptions, diagrams, graphs, equations, tables, vectors, symbolic models, experimental data, or other course-specific representations.

Ask learners to move in both directions: representation → meaning and meaning → representation.

## 6. Teach problem recognition

For each major problem family, explain:

- what cues identify the model;
- the first useful thought;
- what information matters;
- what common cue is misleading;
- what conditions must be checked before using a method.

The target habit is **recognize the model → choose a representation/relationship**, not **see numbers → search for a formula**.

## 7. Use worked examples to expose thinking

Use examples only where they add learning value. Across the chapter, include a useful mix of conceptual, basic quantitative, multi-step, and assessment-style reasoning when relevant to the course.

A strong worked example includes:

**Problem → What should we notice first? → Model/representation → Reasoning → Solution → Check → Common wrong path**

## 8. Use prediction and cognitive conflict selectively

Before revealing an unintuitive result, invite a prediction when that contrast will genuinely help learning.

Do not turn every subsection into a quiz.

## 9. Diagnose misconceptions

For major misconceptions, explain:

**Wrong intuition → Why it feels plausible → Where it fails → Correct mental model**

Do not merely say “remember this is wrong.”

## 10. Respect official boundaries

Never present enrichment as official required content.

If an extension is useful, label it clearly as an extension/non-required item in language appropriate to the course.

Do not use a familiar textbook topic to override the source packet.

## 11. Integrate official practices and assessment skills

Use the official skills/practices/assessment objectives from `requirements.json` and `coverage.json`.

Where appropriate, include prompts such as:

- predict without calculating;
- sketch or interpret a representation;
- explain reasoning;
- justify a claim using a principle;
- compare two models or cases;
- reason proportionally;
- interpret data or experimental evidence.

Only include modes that are actually relevant to the supplied course requirements.

## 12. Close the learning loop

If a driving question was used, return to it near the end. Let the learner try again before giving the complete explanation.

Finish with the most useful subset of:

- conceptual knowledge map;
- formula/relationship table with meaning and conditions;
- representation summary;
- problem-type recognition map;
- major misconceptions;
- `I can...` checklist mapped to official requirements.

The ending should make conceptual dependencies visible, not merely repeat section titles.

## Style

Use the user's requested language. Preserve official terminology precisely, introducing translations when useful. Write like an expert teacher guiding a learner through reasoning—not like an encyclopedia, formula sheet, or syllabus dump.

Prefer clear, compact explanations over repeated pedagogical boilerplate. Quality > quantity for hooks, stories, and real-world examples.
