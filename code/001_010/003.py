# 003 - Viết chương trình để tìm số lớn nhất trong ba số.

# Hàm kiểm tra
def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Nhập ba số nguyên từ người dùng
try:
    num1 = int(input("Nhập số nguyên thứ nhất: "))
    num2 = int(input("Nhập số nguyên thứ hai: "))
    num3 = int(input("Nhập số nguyên thứ ba: "))
    
    max_number = find_max_of_three(num1, num2, num3)
    print(f"Số lớn nhất trong ba số là: {max_number}")
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")
