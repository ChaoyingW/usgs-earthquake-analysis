import csv

# 将文件名指定为电脑中的 USGS 数据文件
filename = "all_month.csv"

total_count = 0
magnitudes = []
max_magnitude = 0.0
max_place = ""  # 专门用来记录最大震级发生的地点

with open(filename, encoding="utf-8") as f:
  reader = csv.DictReader(f)

  for row in reader:
    try:
      mag = float(row["mag"])
    except ValueError:
      # 跳过无法转成数字的坏数据
      continue

    total_count += 1
    magnitudes.append(mag)

    # 如果发现了更大的震级，同时更新数值和对应的地点
    if mag > max_magnitude:
      max_magnitude = mag
      max_place = row["place"]  # 读出这一行的 place 列

# 安全计算平均震级（防止列表为空时除以 0 报错）
if len(magnitudes) > 0:
  average_magnitude = sum(magnitudes) / len(magnitudes)
else:
  average_magnitude = 0.0

# 打印最终的地震数据分析报告
print("Total earthquakes:", total_count)
print("Largest magnitude:", max_magnitude)
print("Location of largest earthquake:", max_place)  # 打印最大震级发生地点
print("Average magnitude:", round(average_magnitude, 2))
