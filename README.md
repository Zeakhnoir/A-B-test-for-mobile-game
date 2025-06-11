# Cookie Cats A/B-Test Analysis 🐱🍪

This repo walks through a **real A/B test** run by the mobile puzzle game **Cookie Cats**.  
The test asked: **Does moving the energy gate from level 30 to level 40 change player behaviour?**

| Cohort | Gate appears at |
| ------ | --------------- |
| **gate_30** | level 30 (control) |
| **gate_40** | level 40 (treatment) |

The code answers two product questions:

1. **Retention impact** – Do different gate positions change the odds that a player comes back on day 1 and/or day 7?  
2. **Engagement impact** – Do players who face the later gate play more (or fewer) levels before churning?

---

## What’s inside

| File | Purpose |
|------|---------|
| `analysis_abtest.py` | End-to-end script: loads data, builds joint “state” column (`00`, `10`, `01`, `11`), runs a 2×4 **Pearson χ²** test, and prints expected vs. observed counts. |
| `engagement_stats.py` | Computes mean, unbiased variance, and sample size for `sum_gamerounds` per cohort, plus day-1/7 retention counts & rates. |
| `cookie_cats.csv` | Raw anonymised player-level dataset released by TEEKI / Wooga on Kaggle. |

---

## Quick start

```bash
# 1. Clone repo & install deps
pip install -r requirements.txt   # pandas, scipy, etc.

# 2. Place cookie_cats.csv in the project root
# 3. Run the analyses
python analysis_abtest.py
python engagement_stats.py
