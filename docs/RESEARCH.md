# Competitor research

Collected 16 November 2026 with Scrapling. Public product descriptions are vendor claims, not independently tested behavior. No signed-in diary, private API, proprietary food database, paid program, or in-app video library was accessed. This is a bounded public-source collection, not an exhaustive copy of the four products.

## Capability comparison

| Product | Publicly described capabilities | Momentum design implication | Still unknown |
| --- | --- | --- | --- |
| [MyFitnessPal](https://www.myfitnesspal.com/) | Food diary, macros and micronutrients, barcode/photo/voice entry, recipes, restaurant foods, connected devices and nutrition coaching | Recent/repeat meals first; manual entry alongside assisted input; preserve provenance and user review | Food licensing, individual entry accuracy, tier/region availability and actual offline behavior |
| [MOTRA](https://www.motraapp.com/) | Wearable heart-rate zones, effort points, workout activity history and token rewards | Optional effort context and recognition of completed activity; no token economy or incentives to overexert | Scoring implementation, device coverage and anti-cheat claims |
| [MacroFactor Nutrition](https://macrofactor.com/macrofactor/) | Adaptive nutrition coaching, weight trends, food search, barcode/label/photo/text logging, recipes, quick-add, micronutrients, export | Fast logging, explicit completeness, trends with missing data, optional reviewable target proposals | Exact algorithm, database access/license, India coverage and behavior with incomplete records |
| [MacroFactor Workouts](https://macrofactor.com/workouts/) | Equipment profiles, program builder, progression, reps/sets/RIR/rest, swaps, warm-ups, volume/PR charts, exercise cues and technique videos | Structured original templates, equipment substitutions and prior performance; owner-approved progression | Exact progression engine, licensed content, full exercise inventory and native recording behavior |

The Workouts page was also inspected in the user-selected browser. It publicly lists more than 900 exercises and technique videos; this is a catalog-size claim, not a collected exercise/video dataset. A later Scrapling response for the same requested URL appeared to contain Nutrition content. The original public-page capture and browser observation contained the Workouts feature list; URL alone is therefore not used to identify page content.

Additional public pages collected: [MOTRA How it works](https://www.motraapp.com/how-it-works), [MOTRA Coach](https://www.motraapp.com/coach), and the [MacroFactor homepage](https://macrofactor.com/). Raw page captures remain local; this repository publishes summaries and public media references rather than whole competitor pages.

## Food and nutrition data

No commercial food records were exported. The UI contains synthetic Indian-meal examples, not a verified food database. A production record needs food ID, source/license/version, raw-or-cooked state, serving mass/unit, nutrients and confidence. Household measures need user-specific mass; one roti or katori is not a universal serving.

Recipes must retain ingredient amounts including oil/ghee, measured final cooked yield and serving weight. Calculate nutrients per gram from the full batch and snapshot them in confirmed entries. Restaurant estimates need ranges and editable assumptions. Unknown meals remain unknown; drafts do not count as confirmed intake. Photo estimates require confirmation and cannot establish hidden oil or exact mass.

## Workouts, training and video data

The collection records advertised tracking fields and public media links. It does not contain commercial program templates, an extracted exercise database, video files, transcripts or a reconstructed progression algorithm. Public video URLs remain references; public reachability does not grant redistribution rights. Build original guidance or obtain a license before shipping instructional media.

Use movement pattern, equipment, instructions, source, license, review date and optional licensed video URL for a future exercise record. Keep an active session's template snapshot stable. Proposed load increments need a reason and approval; a missed workout never triggers increased load or stacked catch-up work.

## Inspection evidence and limits

REA `list_adb_devices` returned an empty device list using ADB 37.0.1. Evidence: `ev_3ecbfdabce0ad32a4be61a508051679c2157311d7c7ceb2de80df48d148e440c` (local inspection, not product behavior). No competitor APK/IPA was supplied. The owner has iPhone installations; Android ADB/JADX/Apktool cannot inspect those iOS installations.

Craft Anything's session reported clean-room mode and no active target. Its brief and plan were initialized. Ghidra and Rizin directories were present locally, but no competitor binary was opened, decompiled, executed or tested. REA, Ghidra, Rizin, JADX, Apktool and Craft Anything must not be cited as proof of competitor internals here.

For a later authorized artifact review: obtain a legitimate unencrypted analyzable artifact, record version/hash/provenance, select a narrow feature question, inspect statically, and distinguish static inference from runtime evidence. For iPhone UX verification, use an authorized recording/capture path with personal records redacted. No device unlocking, DRM removal, credential extraction or paywall workaround is part of this milestone.

## Collection coverage

- Public marketing and feature descriptions: collected for all four products.
- Public media references: inventoried from collected HTML where exposed.
- Food record database / complete exercise library / in-app videos: not collected.
- Signed-in workflows, subscription features, native offline/sync and algorithms: unverified.
- Memorandum requirements: mapped in [REQUIREMENTS.md](REQUIREMENTS.md); not claimed implemented.
