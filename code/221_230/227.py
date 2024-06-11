# 227 - Viết chương trình để phân tích dữ liệu từ tệp CSV

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, city={self.city})"

import csv

# Đường dẫn đến tệp CSV
file_path = 'students.csv'

# Danh sách để lưu trữ các đối tượng Student
students = []

# Đọc dữ liệu từ tệp CSV và tạo các đối tượng Student
with open(file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Đọc dòng tiêu đề
    for row in csvreader:
        # Tạo đối tượng Student và thêm vào danh sách
        student = Student(name=row[0], age=int(row[1]), city=row[2])
        students.append(student)

# Hiển thị danh sách các đối tượng Student
for student in students:
    print(student)
