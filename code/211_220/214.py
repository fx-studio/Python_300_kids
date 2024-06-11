# 214 - Viết chương trình để truy vấn dữ liệu từ bảng trong cơ sở dữ liệu SQL
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

def display_data_by_name(cursor, name):
    cursor.execute('SELECT * FROM students WHERE name = ?', (name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_data_by_age(cursor, age):
    cursor.execute('SELECT * FROM students WHERE age = ?', (age,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_data_by_grade(cursor, grade):
    cursor.execute('SELECT * FROM students WHERE grade = ?', (grade,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = connect_to_db()
    cursor = conn.cursor()

    create_table_if_not_exists(cursor)

    while True:
        print("Menu:")
        print("1. Xem tất cả dữ liệu")
        print("2. Xem dữ liệu theo tên")
        print("3. Xem dữ liệu theo tuổi")
        print("4. Xem dữ liệu theo xếp hạng")
        print("5. Thoát")
        choice = input("Chọn một tùy chọn (1/2/3/4/5): ")

        if choice == '1':
            display_all_data(cursor)
        elif choice == '2':
            name = input("Nhập tên: ")
            display_data_by_name(cursor, name)
        elif choice == '3':
            age = input("Nhập tuổi: ")
            display_data_by_age(cursor, age)
        elif choice == '4':
            grade = input("Nhập xếp hạng: ")
            display_data_by_grade(cursor, grade)
        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

    conn.close()

if __name__ == "__main__":
    main()