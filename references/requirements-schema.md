# Requirement packet schema · v1.1

`requirements.json` is the source-faithful content authority for generation.

## Required top-level fields

- `schema_version`: `1.1`
- `course`: course name when known
- `request`: bounded user target
- `requirements`: array
- `constraints`: array
- `unresolved`: array

## Requirement record

```json
{
  "id": "REQ-001",
  "category": "learning_objective",
  "text": "source-faithful requirement text",
  "source_file": "syllabus.pdf",
  "locator": "Unit 1 / Topic 1.2 / p. 34",
  "scope_class": "required"
}
```

Allowed `scope_class` values:

- `required`
- `optional_official`
- `supporting`

Recommended `category` values:

- `topic`
- `learning_objective`
- `essential_knowledge`
- `skill_or_practice`
- `equation_or_relationship`
- `assessment_objective`
- `prerequisite`
- `weighting`

## Constraint record

Use constraints for official limits/exclusions/boundaries:

```json
{
  "id": "CON-001",
  "category": "boundary_statement",
  "text": "...",
  "source_file": "syllabus.pdf",
  "locator": "..."
}
```

IDs must be unique. Do not invent requirement text merely to populate a category that the source does not provide.
