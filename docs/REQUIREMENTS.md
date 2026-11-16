# Sanitized requirements and design coverage

Derived from the supplied memorandum v1.0, dated 12 November 2026. Personal history, device ownership details, private conversation IDs and the source PDF are excluded from this public repository. Requirements are product contracts, not completed engineering work.

| Memorandum area | Required behavior | Design coverage | Engineering acceptance still required |
| --- | --- | --- | --- |
| 01–02 Scope | One next action; reliable return after interruptions; unified account | Web/iPhone Today and recovery | Five-second comprehension and real usage validation |
| 03 UX | Calm dark theme, large controls, keyboard/VoiceOver/Dynamic Type, reduced motion | Shared design system and ten screens | Native accessibility, contrast, large text and keyboard audit |
| 04 Training | Gym/home templates; normal/short/minimum/recovery; sets/reps/load/RIR/rest; swaps; pause/finish | Web Training/Plan and iPhone workout | Session snapshots, correction/undo, safe lifecycle and progression tests |
| 05 Nutrition | Manual/repeat/text/photo; portions; cooked yield; provenance; uncertainty; user confirmation | Web Food and iPhone meal review | Validated units, nutrient arithmetic, snapshots and licensed lookup |
| 06 Automation | Proposed limits: 3 proactive/day, 2/event, 60-minute unrelated spacing; quiet 22:00–08:00; reset after disengagement | Settings and recovery concepts | Transactional account ledger, timezone/DST tests, late-sync cancellation |
| 07 Watch/Health | Offline Watch events; durable phone acknowledgement; workout UUID dedupe; separate cloud consent | Workout status and settings concepts | Native Watch app, HealthKit, WatchConnectivity and physical-device tests |
| 08 Architecture | SwiftUI iPhone/watchOS, React/TS Windows PWA, Supabase | Platform design direction only | Xcode targets, account/backend, native persistence and web shell |
| 09 Schema | Ownership, units, revision and snapshot contracts | Documented contract only | SQL migrations, ownership keys, RLS and validation |
| 10 Sync | Outbox, stable IDs, retry dedupe, conflict preservation, tombstones and upgrades | Simulated offline/pending/conflict states | Exactly-once effective records, restart and concurrency tests |
| 11–12 Build/install | Supported Mac/Xcode, signing, real phone/Watch installation and renewal | No installation claimed | Signed feasibility spike and distribution runbook |
| 13 Privacy | Scoped consent, minimal cloud data, secure identity, export/delete, backup restore | Settings concept | Two-user isolation, processor review, cache wipe and restore tests |
| 14 Roadmap | Feasibility before feature expansion | Design milestone only | Execute phase gates with build/device evidence |
| 15 Acceptance | A01–A10 full system checks | Not executed by static designs | Identity, offline, interruptions, Health, automation, recovery, food, lifecycle, migrations, usability/install |
| 16 Implementation | Minimal reliable vertical slice, shared deterministic fixtures | No application backend scaffolded | Durable workout path and parity fixtures |
| 17 Budget | Revalidate providers, licenses and running costs before purchase | No purchase or enrollment | Concrete quotes and owner decisions |
| 18 Provenance | Primary sources and clear uncertainty | Research links and media inventory | Update source/license review at implementation |

## Critical invariants

1. Saved locally, acknowledged by phone and synced to cloud are distinct states.
2. Retry cannot duplicate sessions or effective sets; conflicts retain unsent work.
3. Missing logs prove neither rest nor low food intake. No automatic target adjustment from incomplete example data.
4. Minimum completion counts as modified completion, not equivalent training volume.
5. Rescheduling preserves history and checks spacing/availability; no silent plan change or live recorder takeover.
6. Watch owns writing its workout; phone links the Health UUID without writing it again.
7. HealthKit permissions, cloud summaries, external AI and diagnostics are separate consents.
8. Provider encryption is not end-to-end encryption. No unimplemented privacy guarantees.
9. AI/network failure must leave manual food and workout logging available.
10. A static mockup or screenshot does not establish native integration, durable offline behavior or clinical effectiveness.

## States to implement beyond the current samples

Loading, empty, saved locally, waiting for phone, pending cloud upload, synced, offline, conflict and recoverable error need distinct text and actions. Onboarding drafts, one-question steps, permission denial, pain/stop, abandoned sessions, export/deletion scope and reset-after-absence need dedicated interaction tests. The ten key screens are a visual foundation, not the complete state graph.
