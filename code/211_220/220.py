# 220 - Viết chương trình để thực hiện subquery trong cơ sở dữ liệu SQL

import sqlite3

def create_database():
    # Tạo cơ sở dữ liệu SQLite và bảng mẫu
    conn = sqlite3.connect('example4.db')
    cursor = conn.cursor()

    # Tạo bảng Employees
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      department TEXT NOT NULL,
                      salary REAL NOT NULL)''')

    # Tạo bảng Departments
    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
                      department_id INTEGER PRIMARY KEY,
                      department_name TEXT NOT NULL)''')

    # Thêm dữ liệu mẫu
    cursor.execute("INSERT INTO Employees (name, department, salary) VALUES ('Alice', 'HR', 50000)")
    cursor.execute("INSERT INTO Employees (name, department, salary) VALUES ('Bob', 'IT', 60000)")
    cursor.execute("INSERT INTO Employees (name, department, salary) VALUES ('Charlie', 'IT', 70000)")
    cursor.execute("INSERT INTO Employees (name, department, salary) VALUES ('David', 'HR', 55000)")
    
    cursor.execute("INSERT INTO Departments (department_name) VALUES ('HR')")
    cursor.execute("INSERT INTO Departments (department_name) VALUES ('IT')")
    cursor.execute("INSERT INTO Departments (department_name) VALUES ('Finance')")

    conn.commit()
    conn.close()

def execute_query(query):
    conn = sqlite3.connect('example4.db')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def menu():
    while True:
        print("\nMenu:")
        print("1. Xem tất cả nhân viên")
        print("2. Xem tất cả phòng ban")
        print("3. Xem nhân viên với mức lương cao nhất trong từng phòng ban (subquery)")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            query = "SELECT * FROM Employees"
            rows = execute_query(query)
            print("\nTất cả nhân viên:")
            for row in rows:
                print(row)

        elif choice == '2':
            query = "SELECT * FROM Departments"
            rows = execute_query(query)
            print("\nTất cả phòng ban:")
            for row in rows:
                print(row)

        elif choice == '3':
            query = """
            SELECT name, department, salary 
            FROM Employees
            WHERE salary = (
                SELECT MAX(salary)
                FROM Employees AS e2
                WHERE e2.department = Employees.department
            )
            """
            rows = execute_query(query)
            print("\nNhân viên với mức lương cao nhất trong từng phòng ban:")
            for row in rows:
                print(row)

        elif choice == '4':
            print("Thoát chương trình.")
            break

        else:
            print("Tùy chọn không hợp lệ, vui lòng chọn lại.")

# Tạo cơ sở dữ liệu và bảng mẫu
create_database()

# Chạy menu chương trình
menu()
