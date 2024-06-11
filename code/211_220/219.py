# 219 - Viết chương trình để thực hiện aggregate functions trong cơ sở dữ liệu SQL

import sqlite3

def connect_to_db():
    return sqlite3.connect('example3.db')

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

def insert_sample_data(cursor):
    cursor.execute('INSERT INTO Students (name, age) VALUES ("Alice", 20)')
    cursor.execute('INSERT INTO Students (name, age) VALUES ("Bob", 22)')
    cursor.execute('INSERT INTO Students (name, age) VALUES ("Charlie", 23)')
    cursor.execute('INSERT INTO Students (name, age) VALUES ("David", 21)')
    cursor.execute('INSERT INTO Students (name, age) VALUES ("Eve", 22)')

def get_total_students(cursor):
    cursor.execute('SELECT COUNT(*) FROM Students')
    return cursor.fetchone()[0]

def get_average_age(cursor):
    cursor.execute('SELECT AVG(age) FROM Students')
    return cursor.fetchone()[0]

def get_max_age(cursor):
    cursor.execute('SELECT MAX(age) FROM Students')
    return cursor.fetchone()[0]

def get_min_age(cursor):
    cursor.execute('SELECT MIN(age) FROM Students')
    return cursor.fetchone()[0]

def main():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    create_table(cursor)
    insert_sample_data(cursor)
    conn.commit()
    
    while True:
        print("Menu:")
        print("1. Xem tổng số học sinh")
        print("2. Xem tuổi trung bình của học sinh")
        print("3. Xem tuổi lớn nhất của học sinh")
        print("4. Xem tuổi nhỏ nhất của học sinh")
        print("5. Thoát")
        choice = input("Chọn một tùy chọn (1/2/3/4/5): ")
        
        if choice == '1':
            total_students = get_total_students(cursor)
            print(f"Tổng số học sinh: {total_students}")
        elif choice == '2':
            average_age = get_average_age(cursor)
            print(f"Tuổi trung bình của học sinh: {average_age:.2f}")
        elif choice == '3':
            max_age = get_max_age(cursor)
            print(f"Tuổi lớn nhất của học sinh: {max_age}")
        elif choice == '4':
            min_age = get_min_age(cursor)
            print(f"Tuổi nhỏ nhất của học sinh: {min_age}")
        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
    
    conn.close()

if __name__ == "__main__":
    main()
