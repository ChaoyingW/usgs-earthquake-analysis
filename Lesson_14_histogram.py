import csv
import matplotlib.pyplot as plt

magnitudes = []

with open("all_month.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["mag"] != "":
            magnitudes.append(float(row["mag"]))

plt.hist(magnitudes, bins=30)
plt.title("Earthquake Magnitudes (Past 30 Days)")
plt.xlabel("Magnitude")
plt.ylabel("Number of Earthquakes")
plt.show()
          
         

