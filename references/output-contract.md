# Output contract · v1.1

A completed run produces one bounded teaching artifact unless the user explicitly requests more.

```text
out/<course-slug>/<unit-slug>.md
out/<course-slug>/<unit-slug>.sources.json
```

The student-facing Markdown should remain clean. Put audit/provenance detail in `.sources.json`.

The provenance file should record:

- course and bounded request;
- run slug/version;
- authoritative files and matched locators;
- requirement IDs included;
- official constraints;
- enrichment sources by provenance class;
- generation prompt used;
- validation result;
- unresolved items, normally empty.

For revisions, preserve the stable unit slug. Overwrite only when explicitly intended; otherwise use an explicit revision suffix.
