# 211 - Viết chương trình để kết nối với cơ sở dữ liệu SQL
import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect('example.db')

# Tạo đối tượng cursor để tương tác với cơ sở dữ liệu
cursor = conn.cursor()

# Tạo bảng mới có tên là "students"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')

# Chèn dữ liệu vào bảng "students"
cursor.execute('''
    INSERT INTO students (name, age, grade)
    VALUES ('Alice', 21, 'A')
''')
cursor.execute('''
    INSERT INTO students (name, age, grade)
    VALUES ('Bob', 22, 'B')
''')
cursor.execute('''
    INSERT INTO students (name, age, grade)
    VALUES ('Charlie', 23, 'C')
''')

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
