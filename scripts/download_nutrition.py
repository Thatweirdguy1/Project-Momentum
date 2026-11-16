"""Download official nutrition exports discovered with Scrapling, preserving source bytes."""
from pathlib import Path
import hashlib
import json
from scrapling.fetchers import Fetcher

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'anuvaad_indb_2024.11.xlsx': 'https://www.anuvaad.org.in/wp-content/uploads/2020/07/Anuvaad_INDB_2024.11.xlsx',
    'usda_foundation_2026-10-29.zip': 'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_json_2026-10-29.zip',
    'usda_sr_legacy_2018-04.zip': 'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_json_2018-04.zip',
    'usda_fndds_2024-10-31.zip': 'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_survey_food_json_2024-10-31.zip',
}

def main():
    folder = ROOT / 'data/nutrition/raw'
    folder.mkdir(parents=True, exist_ok=True)
    records = []
    for name, url in SOURCES.items():
        path = folder / name
        if not path.exists():
            response = Fetcher.get(url, timeout=180, retries=1)
            if response.status != 200:
                raise RuntimeError(f'{name}: HTTP {response.status}')
            body = response.body
            if not body.startswith(b'PK'):
                raise RuntimeError(f'{name}: expected ZIP/XLSX bytes')
            path.write_bytes(body)
        body = path.read_bytes()
        records.append({'file': name, 'source_url': url, 'retrieved_date': '2026-11-16', 'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest(), 'method': 'Scrapling Fetcher.get', 'license': 'CC0-1.0' if name.startswith('usda') else 'Open-access statement; redistribution license not established'})
        print(f'{name}: {len(body):,} bytes', flush=True)
    (folder.parent / 'downloads.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
