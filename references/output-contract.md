# Output contract

A completed run produces one bounded teaching artifact, not an entire course unless explicitly requested.

Recommended output:

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

The student-facing Markdown should be readable without source-audit clutter. Put detailed provenance in the companion `.sources.json` file.

The provenance file should contain:

- course and requested scope;
- timestamp/run slug if available;
- source files used;
- matched syllabus section locators;
- enrichment sources;
- prompt used (`user-supplied` or bundled default);
- validation result;
- unresolved items.

For revisions, preserve a stable unit slug and distinguish revisions explicitly when overwrite was not requested.
