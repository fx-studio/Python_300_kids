# 228 - Viết chương trình để phân tích dữ liệu từ tệp Excel

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, city={self.city})"

import openpyxl

# Đường dẫn đến tệp Excel
file_path = 'example.xlsx'

# Danh sách để lưu trữ các đối tượng Student
students = []

# Mở tệp Excel và đọc nội dung
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

# Đọc dữ liệu từ sheet và tạo các đối tượng Student
for row in sheet.iter_rows(min_row=2, values_only=True):  # Bỏ qua dòng tiêu đề
    name, age, city = row
    student = Student(name=name, age=age, city=city)
    students.append(student)

# Hiển thị danh sách các đối tượng Student
for student in students:
    print(student)
