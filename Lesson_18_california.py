import pandas as pd

df = pd.read_csv("all_month.csv")
df["region"] = df["place"].str.split(", ").str[-1]
df["region"] = df["region"].replace("CA", "California")
ca = df[df["region"] == "California"]
ca_places = ca["place"].str.split(" of ").str[-1]
print(ca_places.value_counts().head(10))
