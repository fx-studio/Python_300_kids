# 217 - Viết chương trình để tạo bảng quan hệ trong cơ sở dữ liệu SQL

import sqlite3

# Kết nối tới cơ sở dữ liệu
def connect_to_db():
    return sqlite3.connect('example.db')

# Tạo các bảng trong cơ sở dữ liệu
def create_tables(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            class_id INTEGER,
            FOREIGN KEY (class_id) REFERENCES Classes(class_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Classes (
            class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subjects (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id)
        )
    ''')

# Thêm dữ liệu mẫu vào các bảng
def insert_initial_data(cursor):
    cursor.execute('SELECT COUNT(*) FROM Students')
    result = cursor.fetchone()
    if result[0] == 0:
        cursor.execute('''
            INSERT INTO Students (name, age, class_id) VALUES
            ('John Doe', 20, 1),
            ('Jane Smith', 22, 2),
            ('Michael Johnson', 21, 1)
        ''')

    cursor.execute('SELECT COUNT(*) FROM Classes')
    result = cursor.fetchone()
    if result[0] == 0:
        cursor.execute('''
            INSERT INTO Classes (class_name) VALUES
            ('Math'),
            ('Science')
        ''')

    cursor.execute('SELECT COUNT(*) FROM Subjects')
    result = cursor.fetchone()
    if result[0] == 0:
        cursor.execute('''
            INSERT INTO Subjects (subject_name, student_id) VALUES
            ('Algebra', 1),
            ('Physics', 2),
            ('Chemistry', 3)
        ''')

# Hàm main
def main():
    conn = connect_to_db()
    cursor = conn.cursor()

    create_tables(cursor)
    insert_initial_data(cursor)

    conn.commit()
    conn.close()
    print("Các bảng đã được tạo thành công trong cơ sở dữ liệu!")

if __name__ == "__main__":
    main()