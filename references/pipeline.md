# Pipeline contract

Course Builder uses a gated pipeline so that syllabus grounding and teaching prose cannot blur together.

## The order

1. **REQUEST** — determine the bounded target.
2. **INVENTORY** — know what files exist and which are authoritative.
3. **LOCATE** — find exact syllabus sections for the target.
4. **EXTRACT** — build the official requirement packet.
5. **ENRICH** — add supplemental information without changing official scope.
6. **COVERAGE PLAN** — map every official requirement to the future document.
7. **GENERATE** — apply the pedagogical/writing prompt.
8. **VALIDATE** — compare generated content back to official coverage and boundaries.
9. **OUT** — save a reusable unit artifact and provenance.

## Why this order matters

A long teaching prompt can strongly bias a model toward familiar textbook structure. If generation starts before source scoping, the model may write a plausible chapter and only later try to justify it against the syllabus. That reverses the evidence flow.

The scope packet therefore acts as a hard interface between source reading and content writing.

## Source hierarchy

Authoritative syllabus > official supplement > user enrichment > external research > model background knowledge.

Model background knowledge may help explain or teach a requirement, but it cannot create a requirement that the source packet does not support.
