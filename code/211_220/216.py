# 216 - Viết chương trình để xóa dữ liệu trong bảng trong cơ sở dữ liệu SQL

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

def delete_data_by_id(cursor, student_id):
    cursor.execute('''
        DELETE FROM students WHERE id = ?
    ''', (student_id,))

def delete_all_data(cursor):
    cursor.execute('DELETE FROM students')

def main():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    create_table_if_not_exists(cursor)
    
    while True:
        print("Menu:")
        print("1. Xem toàn bộ dữ liệu")
        print("2. Xóa dữ liệu theo ID")
        print("3. Xóa toàn bộ dữ liệu")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn (1/2/3/4): ")
        
        if choice == '1':
            display_all_data(cursor)
        elif choice == '2':
            student_id = input("Nhập ID của sinh viên cần xóa: ")
            delete_data_by_id(cursor, student_id)
            conn.commit()
            print(f"Dữ liệu có ID {student_id} đã được xóa thành công!")
        elif choice == '3':
            delete_all_data(cursor)
            conn.commit()
            print("Toàn bộ dữ liệu đã được xóa thành công!")
        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    
    conn.close()

if __name__ == "__main__":
    main()
