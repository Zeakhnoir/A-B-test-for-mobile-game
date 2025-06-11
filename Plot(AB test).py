import pandas as pd
import matplotlib.pyplot as plt

# ---------- 1. Load and quick-clean ---------- #
# Replace with your actual path if the file is elsewhere
df = pd.read_csv("cookie_cats.csv")          # ← your CSV name

# Keep only the columns we need
df = df[["version", "sum_gamerounds"]]

# (Optional) trim the top 1 % outliers so the plot isn’t squashed
upper_cap = df["sum_gamerounds"].quantile(0.99)
df = df[df["sum_gamerounds"] <= upper_cap]

# ---------- 2. Split the two A/B groups ---------- #
gate_30 = df[df["version"] == "gate_30"]["sum_gamerounds"]
gate_40 = df[df["version"] == "gate_40"]["sum_gamerounds"]

# ---------- 3. Plot overlaid histograms ---------- #
plt.figure(figsize=(8, 5))
bins = range(0, int(df["sum_gamerounds"].max()) + 20, 20)

plt.hist(gate_30, bins=bins, alpha=0.6, label="Gate 30")
plt.hist(gate_40, bins=bins, alpha=0.6, label="Gate 40")

plt.title("Player engagement by first-gate placement")
plt.xlabel("Sum of game rounds per player (first 14 days)")
plt.ylabel("Number of players")
plt.legend()
plt.tight_layout()
plt.show()

# ---------- 4. (Optional) quick box-and-whisker ---------- #
plt.figure(figsize=(5, 6))
plt.boxplot([gate_30, gate_40],
            labels=["Gate 30", "Gate 40"],
            showfliers=False)          # hide extreme dots for clarity
plt.ylabel("Sum of game rounds per player")
plt.title("Engagement distribution")
plt.tight_layout()
plt.show()
