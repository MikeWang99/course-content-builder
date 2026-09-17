# Learning Mode Map · v1.3

`learning-map.json` is a pedagogical interpretation layer built **after** the source-faithful `requirements.json`. It must never rewrite or replace official requirements.

## The three learning modes

### Type A — Must Recall
Knowledge that should be retrievable accurately without reconstructing it from first principles each time.

Typical examples:
- definitions and named laws;
- equations that the course expects students to know or recognize;
- units, symbols, conventions, sequences, standard facts;
- required procedures, rules, safety points, or high-frequency mark-scheme wording.

Default learning action: **compress → closed-book retrieval → spaced retrieval**.

### Type B — Explain / Reconstruct from a Model
Knowledge that should mainly be rebuilt from a mental model, causal chain, representation, or governing principle rather than memorized as prose.

Typical examples:
- why a phenomenon happens;
- mechanism explanations;
- causal chains;
- why a relationship has a given sign, direction, shape, or trend;
- derivations or explanations that can be reconstructed from a smaller model.

Default learning action: **understand model → compress to mechanism/causal chain → reconstruct explanation in exam-ready language**.

### Type C — Apply
Knowledge/skills whose real test is using ideas in a problem, representation, experiment, or unfamiliar context.

Typical examples:
- calculations and equation selection;
- graph/diagram/data interpretation;
- experimental reasoning and practical questions;
- unfamiliar applications;
- model selection, multi-step reasoning, comparison, estimation, and transfer.

Default learning action: **recognize cue/model → practise varied applications → mix with unfamiliar contexts**.

## Classification is not mutually exclusive

Each knowledge item has exactly one `primary_type` and may have zero or more `secondary_types`.

Examples:
- a definition may be `A` primary and `C` secondary because it must be recalled and then used;
- a causal mechanism may be `B` primary and `C` secondary;
- an equation-selection skill is usually `C` primary, while the equation itself may be a separate `A` item.

Do not force an entire broad syllabus objective into one type when it contains separable learning targets. Split it into multiple `KM-*` items if that improves teaching fidelity.

## Canonical JSON

```json
{
  "schema_version": "1.3",
  "status": "ready",
  "items": [
    {
      "id": "KM-001",
      "title": "Average velocity definition",
      "requirement_ids": ["REQ-001"],
      "primary_type": "A",
      "secondary_types": ["C"],
      "rationale": "The definition and notation need precise retrieval, then use in problems.",
      "recommended_learning_action": "Closed-book recall plus short calculation/application prompts."
    }
  ],
  "unresolved": []
}
```

## Required chapter output near the beginning

After the driving question / opening orientation and before the main teaching sequence, include a concise section titled something like:

`## 本章学习模式地图 · Learning Mode Map`

It should show the chapter's knowledge distribution in a compact table:

| Knowledge point | Primary type | What mastery means | Best practice |
|---|---|---|---|
| ... | A · Must Recall | ... | retrieval |
| ... | B · Explain from a Model | ... | reconstruct from mechanism |
| ... | C · Apply | ... | varied application |

Do not dump raw requirement IDs into the student-facing table unless useful.

## Required derived learning assets

Use the map to generate the appropriate learning asset:

- **Type A → Must Recall Bank**: compact, high-value facts/definitions/equations/phrases only; do not turn it into another textbook.
- **Type B → Model Reconstruction Chains**: minimal causal/model skeletons from which the learner can rebuild a full explanation.
- **Type C → Application & Recognition Targets**: problem cues, first thought/model choice, representation choice, and varied application targets.

These can appear near the end as revision assets, while the overview classification belongs near the beginning.

## General learning loop

When useful, reflect this sequence in teaching and revision design:

`Understand → Compress → Retrieve → Apply → Repeat`

Do not interpret this as “memorize everything.” The purpose of the A/B/C split is to choose the right learning action for each kind of knowledge.
