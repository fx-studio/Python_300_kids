# 229 - Viết chương trình để phân tích dữ liệu từ tệp JSON

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, city={self.city})"

import json

# Đường dẫn đến tệp JSON
file_path = 'students.json'

# Đọc dữ liệu từ tệp JSON
with open(file_path, 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Danh sách để lưu trữ các đối tượng Student
students = []

# Tạo các đối tượng Student từ dữ liệu đọc được
for item in data:
    student = Student(name=item['name'], age=item['age'], city=item['city'])
    students.append(student)

# Hiển thị danh sách các đối tượng Student
for student in students:
    print(student)
