# 226 - Viết chương trình để ghi dữ liệu vào tệp JSON

import json

# Dữ liệu giả về danh sách học sinh
students = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Đường dẫn đến tệp JSON
file_path = 'students.json'

# Ghi dữ liệu vào tệp JSON
with open(file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(students, jsonfile, ensure_ascii=False, indent=4)
