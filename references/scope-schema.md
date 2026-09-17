# Scope packet schema · v1.1

`scope.json` answers one question: **where is the requested bounded target in the authoritative source set?**

Required fields:

- `schema_version`: `1.1`
- `course`: course name when known
- `request`: user target
- `status`: `ready` or `review`
- `matched_sections`: non-empty when ready
- `excluded_neighbors`: array
- `unresolved`: array

A matched section must include `source_file`, `locator`, and preferably `title` plus a short source-faithful `evidence` description.

Do not place the whole teaching outline in `scope.json`. Official requirements belong in `requirements.json`.
