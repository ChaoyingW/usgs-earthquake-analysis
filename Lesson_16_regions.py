import pandas as pd

df = pd.read_csv("all_month.csv")
df["region"] = df["place"].str.split(", ").str[-1]
print(df["region"].value_counts().head(10))
