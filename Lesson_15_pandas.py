import pandas as pd

df = pd.read_csv("all_month.csv")

print("Total earthquakes:", len(df))
print("Largest magnitude:", df["mag"].max())
print("Location of largest earthquake:", df.loc[df["mag"].idxmax(), "place"])
print("Average magnitude:", round(df["mag"].mean(), 2))

print("Top 5 largest earthquakes:")
print(df.nlargest(5, "mag")[["mag", "place"]])
