# usgs-earthquake-analysis
Python script that analyzes real USGS earthquake data

![Magnitude histogram](magnitude_histogram.png)

## What It Does

Reads a month of real worldwide earthquake data from the USGS and reports:
- Total number of earthquakes
- Largest magnitude and where it happened
- Average magnitude

## How to Run
1. Download the "Past 30 Days - All Earthquakes" CSV from the USGS website (earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php). It is saved as `all_month.csv`.
2. Put `all_month.csv` in the same folder as `Lesson_13_largest_quake.py`.
3. Run `python Lesson_13_largest_quake.py`

## Sample Output
- Total earthquakes: 9528
- Largest magnitude: 6.8
- Location of largest earthquake: 105 km NE of Lospalos, Timor Leste
- Average magnitude: 1.81

## What I Practiced
Reading CSV files with `csv.DictReader`, `try/except`, lists, tracking a maximum value

## Author
ChaoyingW, learning Python
