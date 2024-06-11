# 222 - Viết chương trình để ghi dữ liệu vào tệp CSV

import csv

# Dữ liệu cần ghi vào tệp CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Đường dẫn đến tệp CSV
file_path = 'output.csv'

# Ghi dữ liệu vào tệp CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow(row)
