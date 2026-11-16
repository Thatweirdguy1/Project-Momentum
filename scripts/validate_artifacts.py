"""Check published dataset integrity and linked design artifacts; no network required."""
from pathlib import Path
import csv
import gzip
import json
import struct

ROOT=Path(__file__).resolve().parents[1]
screens=json.loads((ROOT/'design/screens.json').read_text(encoding='utf-8'))
assert len(screens)==10
for screen in screens:
    html=ROOT/'design'/screen['html']
    assert html.exists() and '<html' in html.read_text(encoding='utf-8').lower()
    data=(ROOT/'design'/screen['screenshot']).read_bytes()
    assert data[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',data[16:24])[0]>100
summary=json.loads((ROOT/'data/nutrition/summary.json').read_text())
with (ROOT/'data/nutrition/usda_macros.csv').open(encoding='utf-8',newline='') as handle:
    rows=list(csv.DictReader(handle))
assert len(rows)==summary['usda_macro_rows']==13649
assert len({(r['source_version'],r['source_food_id']) for r in rows})==len(rows)
assert sum(r['energy_kcal']=='' for r in rows)==summary['usda_missing_energy_rows']
for row in rows:
    assert row['basis']=='per_100g'
    for key in ('energy_kcal','protein_g','carbohydrate_g','fat_g','fiber_g'):
        assert row[key]=='' or float(row[key])>=0
with gzip.open(ROOT/'data/nutrition/usda_nutrients.csv.gz','rt',encoding='utf-8',newline='') as handle:
    assert sum(1 for _ in csv.DictReader(handle))==summary['usda_nutrient_rows']==1019278
exercises=json.loads((ROOT/'data/exercises/exercises.json').read_text(encoding='utf-8'))
assert len(exercises)==1324 and len({e['id'] for e in exercises})==1324
assert all(e['text_license']=='MIT' and e['media_included'] is False and 'image' not in e and 'gif_url' not in e for e in exercises)
print('Validated: ten HTML/PNG concepts, 13,649 macro records, 1,019,278 nutrient observations, 1,324 exercise text records.')
