# 224 - Viết chương trình để ghi dữ liệu vào tệp Excel

import openpyxl

# Dữ liệu cần ghi vào tệp Excel
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Tạo workbook mới
workbook = openpyxl.Workbook()
sheet = workbook.active

# Ghi dữ liệu vào sheet
for row in data:
    sheet.append(row)

# Đường dẫn đến tệp Excel
file_path = 'example.xlsx'

# Lưu workbook vào tệp Excel
workbook.save(file_path)