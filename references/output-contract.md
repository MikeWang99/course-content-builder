# Output contract · v1.3

A completed run produces one bounded teaching artifact, not an entire course unless explicitly requested.

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

The student/teacher-facing Markdown should remain readable without source-audit clutter.

Near the beginning, it must contain a compact `Learning Mode Map` / `学习模式地图` derived from `learning-map.json`.

Near the end, it should derive useful type-specific revision assets where applicable:

- Type A → Must Recall Bank
- Type B → Model Reconstruction Chains
- Type C → Application & Recognition Targets

The companion provenance file should contain:

- course and requested scope;
- run slug/version when available;
- source files used;
- matched syllabus section locators;
- requirement IDs;
- learning-map IDs plus A/B/C primary/secondary types;
- enrichment sources;
- generation prompt used;
- language profile;
- validation result;
- unresolved items.

For revisions, preserve a stable unit slug and distinguish revisions explicitly when overwrite was not requested.
