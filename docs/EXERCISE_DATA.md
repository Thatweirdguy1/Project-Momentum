# Exercise data collection

Scrapling collected the public directories supplied by the user: [JEFIT](https://www.jefit.com/exercises), [Muscle & Strength](https://www.muscleandstrength.com/exercises), and the [GitHub exercise dataset](https://github.com/hasaneyldrm/exercises-dataset). The Google share link resolved to the [ACE Exercise Library](https://www.acefitness.org/resources/everyone/exercise-library/).

## Reusable text dataset

The pinned upstream commit is `7455efae41b330c265e7cd4b78dfa848e7ce5ebd`. Its actual JSON contains **1,324 exercise records** and instruction text in ten languages: English, Spanish, French, Hindi, Italian, Korean, Polish, Russian, Turkish and Chinese. Metadata/text are published in [exercises.json](../data/exercises/exercises.json), retaining upstream IDs and attribution. The local browser can search names/muscles, filter equipment, and display translated instructions.

The upstream MIT license and its explicit media exception are preserved in [upstream-LICENSE](../data/exercises/upstream-LICENSE) and [upstream-NOTICE.md](../data/exercises/upstream-NOTICE.md). Images and animated GIFs are © Gym visual and require a separate license. They are not copied into this repository or embedded/hotlinked by the local explorer. The local clone contains upstream media but is excluded from publication.

Instruction text has not been clinically or professionally validated. Category/target labels are source metadata, not a guarantee of suitability or exact muscle recruitment.

## Public directory research

The bounded crawl fetched **195 listing/category pages**, discovered **904 unique exercise-page references**, and inspected **24 representative detail pages** across JEFIT, Muscle & Strength and ACE. No failed requests were reported in this run. Exact coverage and crawl limits are in [summary.json](../data/exercises/summary.json).

[public-directory.json](../data/exercises/public-directory.json) contains exercise names/URLs, discovery provenance, detail-collection status and exposed media references where available. Full page text remains local under `data/exercises/local-only/`. Non-MIT instructions, photographs, GIFs and video files are not republished. Public availability does not establish a reusable media license.

The 904 references are a bounded cross-source discovery set, not 904 deduplicated movements or complete coverage of each site's catalog. The crawl follows observed links, with three listing waves, at most 100 listing pages per wave and up to eight detail pages per source. Private endpoints and login-gated data were not accessed.

To repeat, clone the upstream repository into `local-exercises-dataset`, check the desired commit, then run `python scripts/collect_exercises.py`. Re-review upstream licenses before refreshing; changes are not silently accepted as licensed media.
