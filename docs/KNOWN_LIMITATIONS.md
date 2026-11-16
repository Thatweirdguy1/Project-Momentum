# Known limitations

The v0.2.0 local food diary is functional; see [FOOD_DIARY.md](FOOD_DIARY.md) for its tested scope and exact remaining differences from MyFitnessPal. Earlier design-only limitations below apply to the original Stitch concepts, not the new diary controls. The diary is browser-local, requires a first successful cache fill for offline launch, and needs regular exports. Live barcode-service availability is unverified; no photo/voice AI or native/cloud integration is connected.

- This repository is a research/design and local-tools milestone. The 28 selected calculator methods and reference-data explorers work locally. Stitch HTML controls are primarily static. There is no functioning account, backend, native app, live AI, HealthKit or sync connection.
- Public-source collection is bounded, not an exhaustive competitor data export. No private food database, commercial programs or in-app video files are included.
- No competitor binary was inspected. An iPhone installation is not an Android APK or an automatically readable iOS artifact.
- Stitch's list-screens endpoint returned empty data during this session despite generation returning completed screen artifacts. Exports use the actual resource IDs returned by generation.
- The browser profile opened the Stitch project without authentication and displayed a 404/access page. The MCP account created the private project and returned its resources. Open the project with the Google account connected to Stitch MCP.
- Generated copy required editorial correction: unsupported fitness/nutrition guarantees, invented encryption, incorrect storage/HealthKit assumptions and automatic rescheduling claims were removed from reviewed exports.
- Sample numbers, dates, plans, recipe yields, load choices and nutrition ranges are illustrative, not individual recommendations or verified food data.
- CDN Tailwind, Google Fonts and Material Symbols are referenced by the generated exports. Network access is needed for full visual fidelity. These are not production bundles or offline PWA assets.
- Native Dynamic Type/VoiceOver, Watch controls, touch ergonomics, comprehensive contrast and full responsive behavior have not been validated on physical devices.
- All memorandum acceptance tests remain unexecuted; file/render checks do not substitute for them.
- Local calculator implementations cover the 28 directory categories with documented selected methods, not every source option or chart. Clinical validation, pediatric methods, individualized nutrition advice and medication dosing are outside this release.
- Collected INDB recipe rows remain local pending clear redistribution permission. Public USDA tables cover Foundation, SR Legacy and FNDDS; Branded and Experimental are not included.
- The public exercise crawl is bounded: 195 listing pages, 904 references and 24 representative detail pages. It is not complete coverage of every commercial catalog. The separately licensed text dataset contains all 1,324 records at its pinned commit.
