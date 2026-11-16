# Food diary build — v0.2.0-diary

Momentum now opens to a functioning food diary at `web/diary.html`. The existing calculator/reference workspace remains at `web/tools.html`. The diary follows MyFitnessPal's familiar meal-based workflow using original Momentum styling and independently sourced nutrition data. It is not an exact copy or a claim of complete MyFitnessPal parity.

The sanitized static build is also published through GitHub Pages at [the HTTPS preview](https://thatweirdguy1.github.io/Project-Momentum/web/diary.html). Windows and iPhone browsers each retain independent local records. Hosting source files does not create cross-device diary synchronization. A restrictive page content policy allows local assets and the explicit Open Food Facts connection only.

## Implemented

| Workflow | Behavior |
| --- | --- |
| Daily diary | Date navigation; Breakfast, Lunch, Dinner and Snacks; food rows, portions, calories and macro columns |
| Food search | Collected USDA foods plus custom foods, recipes and local INDB imports; all-word search; recent, frequent and favorite filters |
| Serving review | Grams, known source servings or a user-entered serving mass; no universal bowl/roti mass |
| Quick add | Named calorie estimates and optional macros/micronutrients; blanks stay unknown |
| Editing | Change portions and destination meal; delete an entry; undo the last committed change during the current page session |
| Repeat/copy | Copy a meal to another date/meal or copy yesterday; originals and nutrient snapshots remain intact |
| Saved meals | Save a group of diary foods; log it later as individual entries into the selected meal |
| Custom foods | Per-100g or per-serving labels, optional serving mass; editing a food does not rewrite prior diary entries |
| Recipes | Ingredient snapshots, measured final cooked yield, batch serving count, per-gram and per-serving nutrition; editable recipes preserve previously logged snapshots |
| Nutrition report | Calories, macros, fiber, sodium, sugars, saturated fat, cholesterol, potassium, calcium, iron and vitamin C when source values exist; seven-day logged-energy/status table |
| Goals | Optional owner-entered calorie/macro goals; remaining calories = entered goal − known logged intake; exercise is not automatically added back |
| Water/notes | Water increments/manual total, explicit note/status save, logging completeness and recent-day navigation |
| Barcode | Manual barcode/check-digit validation; requested Open Food Facts lookup; source/ODbL attribution; review before adding; previously logged barcode foods available offline |
| Backup | Versioned JSON export/validated replacement restore, CSV export with spreadsheet-formula escaping, undo after restore |
| Local persistence | IndexedDB transaction commits; stale revision protection across tabs; storage failures leave prior committed state intact |
| Offline shell | Service worker caches app files, calculator modules and food lookups after successful first load; offline diary reload/search tested |

Source workflow references reviewed 16 November 2026: [logging food and portions](https://support.myfitnesspal.com/hc/en-us/articles/360032274592-How-to-log-food-to-your-diary), [saved meals versus recipes](https://support.myfitnesspal.com/hc/en-us/articles/360032625331-Create-find-and-log-your-saved-meals), [quick add](https://support.myfitnesspal.com/hc/en-us/articles/360032621971-Getting-started-with-Quick-Add), and [recipe creation](https://support.myfitnesspal.com/hc/en-us/articles/360032271452-How-to-create-and-find-your-recipes). These references describe product workflows; their implementation and assets were not copied.

## Data and privacy

No synthetic records are seeded in the user's diary. Browser tests use isolated contexts and explicitly named synthetic foods. Published screenshots show those test records, not personal health information.

The diary stays in IndexedDB under this browser profile and origin. Other devices/profiles/ports do not share it. Browser clearing/uninstall or storage eviction can remove local data. Export JSON regularly. Saving locally does not mean synced or end-to-end encrypted. Notes and manual targets are never uploaded by this implementation. Unsaved note drafts survive ordinary UI rerenders/date navigation within the page; reload can discard drafts that have not been explicitly saved.

The only external food-service request is an explicit barcode lookup: the entered code is sent to [Open Food Facts API v2](https://openfoodfacts.github.io/openfoodfacts-server/api/). Personal diary contents are not submitted. Community label data must be checked against the package. ODbL source attribution is retained in food snapshots and exports; no Open Food Facts bulk dataset is republished here. A live request in this environment returned an unreadable/non-JSON response; successful response mapping is tested with a controlled mock, and production availability is not claimed verified. Network/service errors preserve the diary and allow manual entry.

USDA additional nutrients are derived from the already collected long-form table into `usda_diary_micronutrients.csv`, covering 13,618 food records with at least a referenced nutrient. Raw-to-cooked state is not inferred. This is a convenience lookup, not a new nutrient database. Missing values remain unknown and are counted in reports. Recipe totals propagate unknown ingredient nutrients rather than presenting false precision.

## Validation actually executed

- `node web/diary-model.test.mjs`: gram/serving scaling, zero versus missing, snapshots, copy/edit, saved meals, cooked-yield recipes, restore, invalid dates/duplicates/units/version.
- `node web/barcode.test.mjs`: GTIN check digits, g→mg conversion, attribution, null versus zero and rejection of ambiguous 100ml labels.
- Browser checks: quick add → edit → reload; copy/undo; custom food; cooked recipe; water/notes; 390px viewport; offline reload/USDA search; concurrent same-revision writes (one accepted, one rejected).
- Additional isolated browser checks: controlled barcode response → log → nutrient report; JSON download → delete → restore; save/log a saved meal to another meal.
- Existing 28-calculator and dataset validation checks remain in CI.

`scripts/diary-browser-check.js` is a function accepted by the Playwright MCP `browser_run_code_unsafe` filename option, with the local server running on port 8765. It uses isolated browser storage and does not modify the ordinary user diary. Its screenshot paths are Windows workspace paths and need adjustment when running elsewhere.

## Remaining differences from MyFitnessPal

No MyFitnessPal account/database/API integration; no complete proprietary restaurant/branded-food catalog; no photo/voice AI, live camera barcode scanner, automatic recipe-URL importer, social feed, subscription system or device-calorie compensation. No cloud account/sync, native iPhone/Watch recorder, HealthKit or clinical personalization is implemented. Meal categories are currently fixed. Browser installation is manifest-based; native iOS installation is a separate workstream. These are explicit gaps, not simulated working features.
