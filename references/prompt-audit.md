# Audit of the supplied AP Physics 1 teaching prompt

The supplied prompt contains strong pedagogical design, but as a reusable pipeline it has several structural risks.

## 1. Source grounding and prose generation are mixed

The prompt says to check the latest official CED and also immediately defines extensive chapter content and writing rules. Without a separate scope artifact, the model can begin from the hard-coded chapter list and use the syllabus only as a later check.

**Fix:** require `scope.json` before prose generation.

## 2. A hard-coded topic list can conflict with the authoritative syllabus

The prompt contains a large `Kinematics must include` list. This is useful as a teaching checklist, but it must not outrank official syllabus boundaries.

**Fix:** treat hard-coded lists as teaching suggestions; the extracted official packet is authoritative.

## 3. External/current research is not separated from local sources

The prompt asks for the latest CED, clarifications, framework, etc. If local official files are already supplied, this can cause unnecessary source drift or repeated web lookup.

**Fix:** local authoritative sources first; external verification only when requested/needed.

## 4. No explicit bounded-generation rule

A very long prompt encourages one-shot generation and can accidentally expand toward a whole course.

**Fix:** each run has exactly one bounded target such as one unit/chapter/topic range.

## 5. No intermediate coverage matrix

The final QA asks whether all learning objectives are covered, but there is no pre-generation map showing where each official requirement will appear.

**Fix:** create `coverage.md` before generation.

## 6. Repeated instructions increase prompt competition

Hook/intuition/why/representation/misconception/problem recognition/return-to-hook appear in several overlapping sections. Repetition is pedagogically understandable but increases token cost and can cause the model to apply every pattern mechanically.

**Fix:** move repeated rules into one reusable pedagogical template, and let the pipeline decide when it is invoked.

## 7. Several math examples show paste/render duplication

Examples such as average velocity, constant-acceleration equations, sign combinations, and vector components contain duplicated plain-text + LaTeX fragments in the supplied Markdown.

**Fix:** validate math markup before final output; use one canonical LaTeX representation.

## 8. No persistent output/provenance contract

The prompt does not define a reusable folder/file destination or source map.

**Fix:** write the requested unit to `out/` with a companion source/provenance file.
