# 215 - Viết chương trình để cập nhật dữ liệu trong bảng trong cơ sở dữ liệu SQL

import sqlite3

def connect_to_db():
    return sqlite3.connect('example.db')

def create_table_if_not_exists(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')

def display_all_data(cursor):
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_data_by_id(cursor, student_id, name, age, grade):
    cursor.execute('''
        UPDATE students
        SET name = ?, age = ?, grade = ?
        WHERE id = ?
    ''', (name, age, grade, student_id))

def main():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    create_table_if_not_exists(cursor)
    
    while True:
        print("Menu:")
        print("1. Xem toàn bộ dữ liệu")
        print("2. Cập nhật dữ liệu theo ID")
        print("3. Thoát")
        choice = input("Chọn một tùy chọn (1/2/3): ")
        
        if choice == '1':
            display_all_data(cursor)
        elif choice == '2':
            student_id = input("Nhập ID của sinh viên cần cập nhật: ")
            name = input("Nhập tên mới: ")
            age = input("Nhập tuổi mới: ")
            grade = input("Nhập xếp hạng mới: ")
            update_data_by_id(cursor, student_id, name, age, grade)
            conn.commit()
            print("Dữ liệu đã được cập nhật thành công!")
        elif choice == '3':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    
    conn.close()

if __name__ == "__main__":
    main()
