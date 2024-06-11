# 212 - Viết chương trình để tạo bảng trong cơ sở dữ liệu SQL

import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect('example.db')

# Tạo đối tượng cursor để tương tác với cơ sở dữ liệu
cursor = conn.cursor()

# Tạo bảng mới có tên là "students" nếu bảng chưa tồn tại
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')

# Kiểm tra xem bảng đã tồn tại hay chưa
cursor.execute('SELECT count(name) FROM sqlite_master WHERE type="table" AND name="students"')
if cursor.fetchone()[0] == 1:
    print("Bảng 'students' đã tồn tại. Bỏ qua bước tạo bảng.")

# Chèn dữ liệu vào bảng "students"
students_data = [
    ('Alice', 21, 'A'),
    ('Bob', 22, 'B'),
    ('Charlie', 23, 'C')
]

for student in students_data:
    cursor.execute('''
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    ''', student)

# Lưu các thay đổi
conn.commit()

# Truy vấn dữ liệu từ bảng "students"
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

# Hiển thị kết quả truy vấn
for row in rows:
    print(row)

# Đóng kết nối cơ sở dữ liệu
conn.close()
