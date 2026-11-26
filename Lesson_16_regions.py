import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_month.csv")
df["region"] = df["place"].str.split(", ").str[-1]
df["region"] = df["region"].replace("CA", "California")
top10 = df["region"].value_counts().head(10)
print(top10)

top10.sort_values().plot(kind="barh")
plt.title("Top 10 Regions by Earthquake Count (Past 30 Days)")
plt.xlabel("Number of Earthquakes")
plt.ylabel("Region")
plt.tight_layout()
plt.show()
