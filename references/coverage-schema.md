# Coverage plan schema · v1.1

`coverage.json` is the hard interface between source extraction and prose generation.

```json
{
  "schema_version": "1.1",
  "status": "ready",
  "coverage": [
    {
      "requirement_id": "REQ-001",
      "planned_section": "Velocity",
      "teaching_mode": ["intuition", "representation"],
      "status": "planned"
    }
  ],
  "constraint_handling": [
    {
      "constraint_id": "CON-001",
      "handling": "exclude-or-label-extension"
    }
  ],
  "unresolved": []
}
```

Every `scope_class=required` requirement must be planned. Optional/supporting requirements may be deliberately omitted, but omission should be explicit when material.

Every authoritative constraint must have a handling entry. This does not mean the constraint must become a student-facing section; it means the generation stage has an explicit instruction for respecting it.
