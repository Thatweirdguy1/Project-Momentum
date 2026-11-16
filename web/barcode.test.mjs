import assert from 'node:assert/strict';
import {barcode,productFood} from './barcode.mjs';
assert.equal(barcode('4006381333931'),'4006381333931');
assert.equal(barcode('3017-620422003'),'3017620422003');
assert.throws(()=>barcode('4006381333932'));assert.throws(()=>barcode('../password'));
const f=productFood('4006381333931',{product_name:'Synthetic label',nutrition_data_per:'100g',nutriments:{'energy-kcal_100g':100,proteins_100g:0,sodium_100g:.1,fat_100g:null}});
assert.equal(f.nutrients.sodium_mg,100);assert.equal(f.nutrients.protein_g,0);assert.equal(f.nutrients.fat_g,null);assert.equal(f.nutrients.fiber_g,null);
assert.ok(f.source.includes('ODbL'));assert.throws(()=>productFood('4006381333931',{product_name:'Liquid',nutrition_data_per:'100ml'}));
console.log('Barcode checks passed: check digits, source attribution, g→mg, unknown vs zero, volume ambiguity.');
