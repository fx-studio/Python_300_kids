# 213 - Viết chương trình để chèn dữ liệu vào bảng trong cơ sở dữ liệu SQL

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

def insert_data(cursor, name, age, grade):
    cursor.execute('''
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    ''', (name, age, grade))

def display_data(cursor):
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    create_table_if_not_exists(cursor)
    
    while True:
        print("Menu:")
        print("1. Nhập dữ liệu mới")
        print("2. Xem danh sách dữ liệu")
        print("3. Thoát")
        choice = input("Chọn một tùy chọn (1/2/3): ")
        
        if choice == '1':
            name = input("Nhập tên: ")
            age = input("Nhập tuổi: ")
            grade = input("Nhập xếp hạng: ")
            insert_data(cursor, name, age, grade)
            conn.commit()
            print("Đã thêm dữ liệu thành công!")
        elif choice == '2':
            display_data(cursor)
        elif choice == '3':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    
    conn.close()

if __name__ == "__main__":
    main()
