# 221 - Viết chương trình để đọc dữ liệu từ tệp CSV

import csv

# Đường dẫn đến tệp CSV
file_path = 'abc.csv'

# Đọc và hiển thị nội dung tệp CSV
with open(file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)