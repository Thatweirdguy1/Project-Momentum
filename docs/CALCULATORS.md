# Local calculator implementation

The [Calculator.net fitness/health directory](https://www.calculator.net/fitness-and-health-calculator.html) listed 28 categories when collected on 16 November 2026. Each is represented by an original local implementation in [engine.mjs](../web/calculators/engine.mjs). No Calculator.net page, advertisement, tracking script or server-side calculator is embedded or called by the local app. Inputs are processed in browser memory and are not saved or uploaded.

These implementations cover the listed categories with explicit selected methods. They do **not** reproduce every Calculator.net option, chart, proprietary adjustment, age group or result. This distinction is visible in the UI.

| Category | Local method / supported scope |
| --- | --- |
| BMI | Adult kg/m² and broad population bands |
| Calorie | Selected BMR × user-supplied activity multiplier; optional user-entered kcal adjustment |
| Body fat | US Navy circumference equations; cm converted to inches |
| BMR | Mifflin–St Jeor, revised Harris–Benedict, Katch–McArdle |
| Ideal weight | Devine, Robinson, Miller, Hamwi historical equations |
| Pace | min/km, km/h and constant-pace distance projection |
| Army body fat | Historical 2023 Taylor–McClung one-site equation, rounded lb/half-inch inputs; no current eligibility decision |
| Lean body mass | Adult Boer, James, Hume; no pediatric or drug-dose output |
| Healthy weight | Adult BMI 18.5–24.9 reference interval |
| Calories burned | User-supplied MET; gross and above-rest estimates |
| One rep max | Epley, Brzycki; completed whole-number sets of 1–10 reps |
| Target heart rate | Tanaka or Fox maximum estimate with Karvonen reserve zones |
| Pregnancy / Due date | LMP with cycle correction, conception, known EDD, IVF transfer/embryo age, or ultrasound age; UTC calendar arithmetic |
| Pregnancy weight gain | Total singleton/twin gain reference ranges by prepregnancy BMI; no weekly individualized prescription |
| Pregnancy conception | Reverse EDD by 266 days and an approximate intercourse window |
| Ovulation / Conception | LMP, selected cycle length, 14-day luteal assumption and approximate fertile window |
| Period | Next six starts under a constant-cycle assumption |
| Macro | User-selected kcal split; 4/4/9 energy conversion |
| Carbohydrate / Fat intake | Adult AMDR reference ranges (45–65% carbohydrate, 20–35% fat) for selected kcal |
| Protein | Weight × user-selected g/kg; no disease-specific recommendation |
| TDEE | Selected BMR × selected activity factor |
| GFR | Adult race-free 2021 CKD-EPI creatinine; mg/dL or µmol/L |
| Body type | Seven-category clothing heuristic plus waist/hip ratio; no health judgement |
| Body surface area | Mosteller, Du Bois, Haycock; no dosing |
| BAC | Simplified Widmark estimate from total beverage volume/ABV and elapsed time; no driving/sobriety clearance |

## Source inspection

Scrapling collected the directory and public page explanations. Some MCP bulk requests failed; the local Scrapling acquisition then successfully fetched all 28 pages and recorded hashes and inline/external-script counts in [calculator-script-inventory.json](../research/calculator-script-inventory.json).

REA statically parsed three public inline scripts (BMI, BMR and Calorie), 6,935 bytes total, without execution. Evidence `ev_f2dd9b69c2cce4b20860324f4a3284203196f3a41c06026c93a3e0fa6edb0b88`; three files parsed, no parse failures. Their UI helpers include settings/unit interactions. The scope leaves 90 of 93 inventoried inline files unanalysed and does not recover server-side calculations or prove behavioral equivalence. Original source scripts remain local and are not shipped with the app. No Ghidra/Rizin analysis of a native calculator binary is claimed.

## Primary references and limits

- [NIH/NHLBI adult BMI](https://www.nhlbi.nih.gov/calculate-your-bmi).
- [National Kidney Foundation 2021 CKD-EPI equation](https://www.kidney.org/professionals/ckd-epi-creatinine-equation-2021). eGFR is for stable adult creatinine, not acute kidney injury, children or pregnancy; no diagnosis or dose is derived.
- [CDC pregnancy weight-gain reference](https://www.cdc.gov/maternal-infant-health/pregnancy-weight/index.html).
- [ACOG due-date methods](https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2017/05/methods-for-estimating-the-due-date). Clinical dating can supersede calendar estimates.
- [Original Taylor–McClung policy study](https://www.nature.com/articles/s41366-024-01701-5), identifying the 2023 Army equation. Current military policy/eligibility is not implemented.
- Published equations and bibliographic references on each corresponding Calculator.net page, accessible from every tool. The local code uses equations and original UI/copy, not scraped calculator implementations.

All inputs use explicit metric units except creatinine's selectable units. Date tools use date-only UTC arithmetic to avoid timezone/DST shifts. Missing, invalid, nonfinite and out-of-domain inputs produce errors; measurements outside useful circumference ranges are rejected. Estimates are never applied to a fitness plan or diary. Reproductive dates are unsuitable as contraception or paternity evidence; BAC cannot determine whether someone may safely or legally drive. Medical review and full published-reference conformance remain required before clinical use.

## Validation

Run `node web/calculators/engine.test.mjs`. Tests exercise all 28 categories and include numeric fixtures, creatinine-unit equivalence, leap-day calendars, single-rep behavior, macro accounting and invalid inputs. Browser checks submitted all 28 forms and confirmed a result without a form error. These checks establish the implemented scope, not complete Calculator.net parity or medical certification.
