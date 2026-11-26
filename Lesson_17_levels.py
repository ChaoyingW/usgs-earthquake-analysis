import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_month.csv")
df = df.dropna(subset=["mag"])
df["level"] = pd.cut(df["mag"], bins=[-20, 4, 6, 20], labels=["Safe", "Warning", "Alert"], right=False)
counts = df["level"].value_counts().sort_index()
print(counts)

counts.plot(kind="bar")
plt.title("Earthquakes by Alert Level (Past 30 Days)")
plt.xlabel("Level")
plt.ylabel("Number of Earthquakes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
