import pandas as pd

df = pd.read_csv("scores.csv")
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df = df.dropna(subset=["score"])

averages = df.groupby("category")["score"].mean()

for c in sorted(averages.index):
    print(c, round(averages[c], 2))