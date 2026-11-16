"""Normalize official food exports without replacing missing values with zero."""
from pathlib import Path
import csv
import gzip
import hashlib
import io
import json
import math
import zipfile
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/nutrition'
FIELDS = ['source', 'source_version', 'source_food_id', 'food_name', 'data_type', 'basis', 'serving_label', 'energy_kcal', 'protein_g', 'carbohydrate_g', 'fat_g', 'fiber_g', 'energy_nutrient_id', 'energy_method', 'source_url']

def number(value):
    if value is None or value == '':
        return None
    try:
        result = float(value)
    except (ValueError, TypeError):
        return None
    if not math.isfinite(result):
        raise ValueError(f'Invalid nutrient amount: {value!r}')
    return result

def energy(nutrients):
    # Keep the source's kcal definitions distinct; prefer general Energy when present.
    for nutrient_id in (1008, 2048, 2047):
        n = nutrients.get(nutrient_id)
        if n and n.get('amount') is not None and n['nutrient']['unitName'].lower() == 'kcal':
            amount = number(n['amount'])
            if amount >= 0:
                return amount, str(nutrient_id), 'source kcal'
    n = nutrients.get(1062)
    if n and n.get('amount') is not None and n['nutrient']['unitName'].lower() == 'kj':
        return number(n['amount']) / 4.184, '1062', 'kJ / 4.184'
    return None, '', 'missing'

def grams(nutrients, key):
    n = nutrients.get(key)
    if n is None or n.get('amount') is None:
        return None
    if n['nutrient']['unitName'].lower() != 'g':
        raise ValueError(f'Unexpected macro unit: {n}')
    amount = number(n['amount'])
    return amount if amount is not None and amount >= 0 else None

def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def main():
    downloads = json.loads((DATA / 'downloads.json').read_text(encoding='utf-8'))
    macros, counts, long_count, issues = [], {}, 0, []
    target = DATA / 'usda_nutrients.csv.gz'
    nutrient_fields = ['source_version', 'fdc_id', 'nutrient_id', 'nutrient_name', 'unit', 'amount_per_100g', 'derivation_code', 'data_points']
    with target.open('wb') as raw, gzip.GzipFile(fileobj=raw, mode='wb', mtime=0) as compressed, io.TextIOWrapper(compressed, encoding='utf-8', newline='') as text:
        writer = csv.DictWriter(text, fieldnames=nutrient_fields)
        writer.writeheader()
        for source in downloads:
            if not source['file'].startswith('usda_'):
                continue
            path = DATA / 'raw' / source['file']
            assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256']
            with zipfile.ZipFile(path) as archive:
                name = next(n for n in archive.namelist() if n.endswith('.json'))
                foods = next(iter(json.loads(archive.read(name)).values()))
            counts[source['file']] = len(foods)
            for food in foods:
                nutrients = {n['nutrient']['id']: n for n in food.get('foodNutrients', [])}
                kcal, energy_id, method = energy(nutrients)
                macros.append(dict(zip(FIELDS, ['USDA FoodData Central', source['file'], str(food['fdcId']), food['description'], food.get('dataType', ''), 'per_100g', '', kcal, grams(nutrients, 1003), grams(nutrients, 1005), grams(nutrients, 1004), grams(nutrients, 1079), energy_id, method, f'https://fdc.nal.usda.gov/food-details/{food["fdcId"]}/nutrients'])))
                for n in food.get('foodNutrients', []):
                    nutrient = n['nutrient']
                    if number(n.get('amount')) is not None and number(n['amount']) < 0:
                        issues.append({'source_version': source['file'], 'fdc_id': food['fdcId'], 'nutrient_id': nutrient['id'], 'source_amount': n['amount'], 'issue': 'Negative source value retained in long table; excluded from normalized macro fields'})
                    writer.writerow(dict(zip(nutrient_fields, [source['file'], food['fdcId'], nutrient['id'], nutrient['name'], nutrient['unitName'], number(n.get('amount')), n.get('foodNutrientDerivation', {}).get('code', ''), n.get('dataPoints', '')])))
                    long_count += 1
    write_csv(DATA / 'usda_macros.csv', macros, FIELDS)
    workbook = openpyxl.load_workbook(DATA / 'raw/anuvaad_indb_2024.11.xlsx', read_only=True, data_only=True)
    values = workbook.active.values
    headers = next(values)
    original = [dict(zip(headers, row)) for row in values if row[0]]
    local = DATA / 'local-only'
    write_csv(local / 'indb_all_nutrients.csv', original, headers)
    indian = []
    for food in original:
        for prefix, basis in [('', 'per_100g'), ('unit_serving_', 'per_source_serving')]:
            indian.append(dict(zip(FIELDS, ['Anuvaad INDB', '2024.11', food['food_code'], food['food_name'], 'recipe estimate; ' + str(food['primarysource']), basis, food['servings_unit'] if prefix else '', number(food[prefix + 'energy_kcal']), number(food[prefix + 'protein_g']), number(food[prefix + 'carb_g']), number(food[prefix + 'fat_g']), number(food[prefix + 'fibre_g']), 'energy_kcal', 'source kcal', 'https://www.anuvaad.org.in/indian-nutrient-databank/'])))
    write_csv(local / 'indb_macros.csv', indian, FIELDS)
    assert len({(r['source_version'], r['source_food_id']) for r in macros}) == len(macros)
    assert len({(r['source_food_id'], r['basis']) for r in indian}) == len(indian)
    summary = {'usda_foods_by_archive': counts, 'usda_macro_rows': len(macros), 'usda_nutrient_rows': long_count, 'usda_missing_energy_rows': sum(r['energy_kcal'] is None for r in macros), 'indb_foods_local_only': len(original), 'indb_macro_rows_local_only': len(indian), 'indb_original_columns': len(headers), 'who_food_macro_rows': 0, 'indb_redistribution': 'Not published: no explicit dataset redistribution license established', 'missing_value_policy': 'Empty CSV cell means unknown, never zero', 'basis': 'USDA per 100 g; INDB per 100 g and separately per source serving; household mass not inferred'}
    (DATA / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    (DATA / 'quality-issues.json').write_text(json.dumps(issues, indent=2) + '\n', encoding='utf-8')
    summary['negative_source_values_flagged'] = len(issues)
    (DATA / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))

def self_check():
    assert number(None) is None and number('NA') is None and number(0) == 0
    assert energy({}) == (None, '', 'missing')
    assert math.isclose(energy({1062: {'amount': 418.4, 'nutrient': {'unitName': 'kJ'}}})[0], 100)
    assert energy({1008: {'amount': 0, 'nutrient': {'unitName': 'kcal'}}})[0] == 0
    assert number(-1) == -1  # Preserve source anomalies for audit, never clamp to zero.
    assert grams({1005: {'amount': -0.475, 'nutrient': {'unitName': 'g'}}}, 1005) is None

if __name__ == '__main__':
    self_check()
    main()
