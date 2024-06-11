# 013 - Viết hàm để kiểm tra một số có phải là số nguyên tố không.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Nhập số nguyên từ người dùng
try:
    number = int(input("Nhập một số nguyên: "))
    if is_prime(number):
        print(f"{number} là số nguyên tố.")
    else:
        print(f"{number} không phải là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
