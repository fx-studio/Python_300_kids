# 218 - Viết chương trình để thực hiện join giữa hai bảng trong cơ sở dữ liệu SQL

import sqlite3

def connect_to_db():
    return sqlite3.connect('example2.db')

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

def insert_sample_data(cursor):
    # Thêm dữ liệu mẫu vào bảng Classes
    cursor.execute('INSERT INTO Classes (class_name) VALUES ("Class A")')
    cursor.execute('INSERT INTO Classes (class_name) VALUES ("Class B")')
    
    # Thêm dữ liệu mẫu vào bảng Students
    cursor.execute('INSERT INTO Students (name, age, class_id) VALUES ("Alice", 20, 1)')
    cursor.execute('INSERT INTO Students (name, age, class_id) VALUES ("Bob", 22, 2)')
    cursor.execute('INSERT INTO Students (name, age, class_id) VALUES ("Charlie", 23, 1)')

def display_all_data_from_students(cursor):
    cursor.execute('SELECT * FROM Students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_all_data_from_classes(cursor):
    cursor.execute('SELECT * FROM Classes')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_joined_data(cursor):
    cursor.execute('''
        SELECT Students.student_id, Students.name, Students.age, Classes.class_name
        FROM Students
        JOIN Classes ON Students.class_id = Classes.class_id
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    create_tables(cursor)
    insert_sample_data(cursor)
    conn.commit()
    
    while True:
        print("Menu:")
        print("1. Xem dữ liệu từ bảng Học Sinh")
        print("2. Xem dữ liệu từ bảng Lớp Học")
        print("3. Xem dữ liệu từ phép join giữa hai bảng")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn (1/2/3/4): ")
        
        if choice == '1':
            display_all_data_from_students(cursor)
        elif choice == '2':
            display_all_data_from_classes(cursor)
        elif choice == '3':
            display_joined_data(cursor)
        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    
    conn.close()

if __name__ == "__main__":
    main()
