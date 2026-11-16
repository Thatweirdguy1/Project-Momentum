"""Build a small diary lookup from the already collected USDA observations."""
from pathlib import Path
import csv,gzip
root=Path(__file__).resolve().parents[1]
mapping={'1093':'sodium_mg','2000':'sugar_g','1063':'sugar_g','1258':'saturated_fat_g','1253':'cholesterol_mg','1092':'potassium_mg','1087':'calcium_mg','1089':'iron_mg','1162':'vitamin_c_mg'}
rows={}
with gzip.open(root/'data/nutrition/usda_nutrients.csv.gz','rt',encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f):
  if r['nutrient_id'] not in mapping:continue
  key=(r['source_version'],r['fdc_id']);field=mapping[r['nutrient_id']]
  out=rows.setdefault(key,{'source_version':key[0],'source_food_id':key[1]})
  value=r['amount_per_100g']
  if value and float(value)>=0 and (field not in out or r['nutrient_id']=='2000'):out[field]=value
fields=['source_version','source_food_id',*dict.fromkeys(mapping.values())]
with (root/'data/nutrition/usda_diary_micronutrients.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows.values())
print('Built micronutrient lookup for',len(rows),'USDA food records; no missing values inferred.')
