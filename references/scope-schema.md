# Scope packet schema

`scope.json` is the hard gate before course-content generation.

Required top-level fields:

- `schema_version`: currently `1.0`.
- `course`: source course name when known.
- `request`: user's bounded target.
- `status`: `ready` or `review`.
- `matched_sections`: non-empty when ready.
- `official_requirements`: object.
- `unresolved`: list.

Recommended `official_requirements` arrays:

- `topics`
- `learning_objectives`
- `essential_knowledge`
- `skills_or_practices`
- `equations`
- `boundary_statements`
- `weighting`
- `prerequisites`

Each extracted item should preserve source wording closely enough to remain auditable. When practical, include a source locator per item.

`status=ready` requires no unresolved scope ambiguity. A missing optional syllabus category can be represented as an empty array; do not invent content to fill it.
