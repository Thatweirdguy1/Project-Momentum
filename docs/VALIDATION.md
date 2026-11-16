# Validation performed

For v0.2.0 diary persistence, serving arithmetic, recipe snapshots, offline/cross-tab checks, backup/restore and controlled barcode testing, see [FOOD_DIARY.md](FOOD_DIARY.md). Those tests ran in isolated browser contexts with synthetic records. Earlier calculator/reference results below remain valid for `web/tools.html` after the diary became the default entry point.

Executed 16 November 2026 on Windows with Node 24.18.0 and Python 3.13.

| Check | Result | Scope |
| --- | --- | --- |
| `node web/calculators/engine.test.mjs` | Passed | All 28 categories exercised; BMI/BMR/TDEE/pace/macros/BSA/eGFR fixtures; creatinine unit equivalence; single rep; leap-day date arithmetic; invalid inputs |
| Browser form submissions | Passed | All 28 category forms produced results without form errors using synthetic inputs |
| Exercise explorer | Passed | Dataset loads, squat search, equipment/language controls present, Hindi instruction details rendered |
| USDA food explorer | Passed | Dataset loads; rice search returned 456 records, with display capped at 100 |
| Local INDB file import | Passed | 2,028 per-100g/source-serving rows imported in browser memory; page reload clears imported state |
| Mobile workspace | Passed | 390 × 844 viewport, BMI form/result, no document-level horizontal overflow |
| `python scripts/validate_artifacts.py` | Passed | Ten HTML/PNG pairs, 13,649 macro rows, 1,019,278 nutrient observations, 1,324 unique exercise text records, media exclusion |
| Nutrition import self-checks | Passed | Null vs zero, kJ conversion tolerance, negative-source macro exclusion, duplicate source-key protection |
| Public nutrition archive identity | Passed | SHA-256 retained for all four official downloads |
| REA calculator inspection | Bounded static result | Three public inline scripts parsed; no execution or server-side formula recovery |
| Native competitor inspection | Unavailable | No app artifacts; ADB device inventory empty |

The first numeric eGFR test fixture was corrected after independent evaluation of the published 2021 equation; the implemented example for a 30-year-old male at 1 mg/dL is 103.84 mL/min/1.73m². A floating-point equality assertion on kJ conversion was changed to a tolerance. Source-data validation caught ten negative nutrient observations, which are explicitly flagged rather than silently replaced.

Screenshots of the reviewed local pages are in `design/screenshots/`; these are actual browser renders. Stitch screen HTML and screenshots were updated through the MCP API after editorial review. Generation alone is not treated as proof of correct behavior.

Not executed: physical iPhone/Watch tests, native accessibility, HealthKit authorization/deduplication, offline workout durability, multi-account RLS, backup restore, push caps/timezones, complete medical-equation conformance or complete Calculator.net parity. The memorandum's A01–A10 system tests remain pending. CI results are separate from the locally executed checks and must be inspected after push.
