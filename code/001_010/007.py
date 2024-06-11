# 007 - Chương trình kiểm tra năm nhuận

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Nhập năm từ người dùng
try:
    year = int(input("Nhập một năm: "))
    if is_leap_year(year):
        print(f"Năm {year} là năm nhuận.")
    else:
        print(f"Năm {year} không phải là năm nhuận.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")