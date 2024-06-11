# 223 - Viết chương trình để đọc dữ liệu từ tệp Excel

import openpyxl

# Đường dẫn đến tệp Excel
file_path = 'example.xlsx'

# Mở tệp Excel
workbook = openpyxl.load_workbook(file_path)

# Chọn sheet cần đọc (ví dụ: sheet đầu tiên)
sheet = workbook.active

# Đọc và hiển thị nội dung của sheet
for row in sheet.iter_rows(values_only=True):
    print(row)
