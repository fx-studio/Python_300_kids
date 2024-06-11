# 225 - Viết chương trình để đọc dữ liệu từ tệp JSON

import json

# Đường dẫn đến tệp JSON
file_path = 'students.json'

# Đọc dữ liệu từ tệp JSON
with open(file_path, 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Hiển thị dữ liệu
print(data)