# Nutrition data collection

Retrieved 16 November 2026 using Scrapling MCP for discovery and Scrapling `Fetcher.get` for the official binary exports. Download URLs and SHA-256 checksums are recorded in [downloads.json](../data/nutrition/downloads.json).

| Source | Collected data | Published in this repository |
| --- | --- | --- |
| [USDA Foundation Foods](https://fdc.nal.usda.gov/download-datasets/) | October 2026 JSON release, 424 foods | Normalized macro CSV and all nutrient observations |
| [USDA SR Legacy](https://fdc.nal.usda.gov/download-datasets/) | April 2018 JSON release, 7,793 foods | Same |
| [USDA FNDDS](https://fdc.nal.usda.gov/download-datasets/) | 2021–2023 survey foods, October 2024 release, 5,432 foods | Same |
| [Anuvaad INDB](https://www.anuvaad.org.in/indian-nutrient-databank/) | Workbook version 2024.11; 1,014 recipes, 82 columns | Provenance, importer and summary only; full rows stay local pending redistribution permission |
| [WHO nutrition databases](https://www.who.int/teams/nutrition-and-food-safety/databases) | Directory of surveillance, micronutrient, food-safety and policy databases | Source assessment; zero food-level macro rows invented |

The public USDA files contain **13,649 food records** and **1,019,278 nutrient observations**. These are selected complete USDA releases, not every FoodData Central data type: Branded and Experimental are not included. Dataset types and versions remain separate; similar names are not silently merged.

USDA states its data are public domain / CC0 on its [home page](https://fdc.nal.usda.gov/). Attribution: U.S. Department of Agriculture, Agricultural Research Service, Beltsville Human Nutrition Research Center. FoodData Central. Accessed 16 November 2026.

The Anuvaad site describes INDB as open access. Its [methodology](https://www.anuvaad.org.in/methodology/) explains ingredient-based recipe estimates. The [authors' repository](https://github.com/lindsayjaacks/Indian-Nutrient-Databank-INDB-) does not expose an explicit dataset redistribution license in the reviewed root files and says underlying ICMR-NIN source tables must be requested separately. A paper's open-access license is not assumed to license all dataset inputs. Local extraction is complete; INDB rows are excluded from Git and release assets.

## Schema and normalization

- `usda_macros.csv`: source/version/food ID, original description, data type, basis, kcal, protein/carbohydrate/fat/fiber grams, energy nutrient ID/method and source URL.
- `usda_nutrients.csv.gz`: all source nutrient observations, with nutrient ID/name/unit, amount per 100 g, derivation code and sample count when supplied. The gzip file is deterministic.
- `local-only/indb_all_nutrients.csv`: local full 82-column workbook extraction.
- `local-only/indb_macros.csv`: local 2,028 rows, keeping per-100g and per-source-serving bases distinct. The source-serving label does not establish a universal mass.
- `quality-issues.json`: ten negative USDA source observations retained in the long table for audit. Negative macro values are excluded from the normalized macro fields, not clamped to zero.
- `summary.json`: counts and known missingness, including 51 USDA records with no usable kcal value.

Empty cells mean unknown. Zero remains zero. Energy uses source kcal nutrient 1008 where available, then specific/general Atwater nutrients 2048/2047; otherwise source kJ is converted using 4.184 kJ/kcal and explicitly labelled. No 4/4/9 macro-derived calories are substituted for missing source energy. All original energy definitions remain in the long table.

Original food descriptions preserve preparation state. No raw-to-cooked conversion, synonym deduplication, serving-mass inference or claim of laboratory validation is added. INDB values describe reference recipes and cannot establish the composition of an individual home-cooked meal.

## Reproduce locally

```powershell
python -m pip install "scrapling[fetchers]" openpyxl
python scripts/download_nutrition.py
python scripts/normalize_nutrition.py
```

The downloader retrieves official archives rather than scraping one food page at a time; no API key is needed. Original archives remain outside Git. Formula and mapping self-checks run before normalization. See [VALIDATION.md](VALIDATION.md) for checks actually executed.
