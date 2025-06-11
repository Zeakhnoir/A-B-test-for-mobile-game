import pandas as pd

# 1️⃣  Load the data -------------------------------------------
df = pd.read_csv("cookie_cats.csv")      # adjust the path if the file lives elsewhere

# 2️⃣  Compute per-version stats -------------------------------
stats = (
    df[df["version"].isin(["gate_30", "gate_40"])]      # keep just the two cohorts
      .groupby("version")["sum_gamerounds"]
      .agg( mean="mean",               # arithmetic average
            sample_var=lambda x: x.var(ddof=1),  # unbiased sample variance
            n="size")                  # sample size (handy to print)
)

print(stats)

# --- Retention counts for gate_30 vs. gate_40 -------------------------------
ret_cols = ["retention_1", "retention_7"]

# Booleans sum to the number of True values
retention_counts = (
    df[df["version"].isin(["gate_30", "gate_40"])]
      .groupby("version")[ret_cols]
      .sum()              # counts the Trues
      .astype(int)        # make it clear they’re integers
      .rename(columns={"retention_1": "retained_day1",
                       "retention_7": "retained_day7"})
)

print("Number of retained players:")
print(retention_counts)
# --- Retention rates for gate_30 vs. gate_40 -------------------------------
