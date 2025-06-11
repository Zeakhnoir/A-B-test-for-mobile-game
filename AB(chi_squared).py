import pandas as pd
from scipy.stats import chi2_contingency

# --------------------------------------------------
# 1.  Load your data  (edit path / filename)
# --------------------------------------------------
df = pd.read_csv("cookie_cats.csv")

# --------------------------------------------------
# 2.  Build a joint-state column
#     '00' = opened neither day-1 nor day-7
#     '10' = opened day-1 only
#     '01' = (rare) skipped day-1 but came day-7
#     '11' = opened on both days
# --------------------------------------------------
df["state"] = df["retention_1"].astype(str) + df["retention_7"].astype(str)

# --------------------------------------------------
# 3.  2 × 4 contingency table:  version × state
# --------------------------------------------------
ct = pd.crosstab(df["version"], df["state"])
print("Observed counts:\n", ct, "\n")

# --------------------------------------------------
# 4.  Pearson chi-square test
# --------------------------------------------------
chi2, p, dof, expected = chi2_contingency(ct)

print(f"Chi² statistic = {chi2:.3f}")
print(f"Degrees of freedom = {dof}")
print(f"p-value = {p:.4f}\n")

print("Expected counts under H₀ (independence):\n",
      pd.DataFrame(expected, index=ct.index, columns=ct.columns))
