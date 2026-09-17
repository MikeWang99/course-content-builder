# v1.3.0 — Learning Mode Map

- Added a course-general A/B/C knowledge classification layer:
  - Type A · Must Recall
  - Type B · Explain / Reconstruct from a Model
  - Type C · Apply
- Added `learning-map.json` as a separate pedagogical artifact so source-faithful requirements remain untouched.
- Added `primary_type` + `secondary_types` rather than forcing mutually exclusive classification.
- Added `scripts/validate_learning_map.py` and made the learning map a hard gate before generation.
- Required an opening `Learning Mode Map` / 学习模式地图 in generated chapters.
- Added derived revision assets: Must Recall Bank, Model Reconstruction Chains, and Application & Recognition Targets.
- Added the general learning loop `Understand → Compress → Retrieve → Apply → Repeat` as a strategy, not a universal memorisation rule.
- Updated final validation to require the learning-mode overview in the output.
