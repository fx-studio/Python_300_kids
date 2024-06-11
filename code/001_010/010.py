# 010 - Viết chương trình để tìm ước số chung lớn nhất (USCLN) của hai số

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Nhập hai số nguyên từ người dùng
try:
    num1 = int(input("Nhập số thứ nhất: "))
    num2 = int(input("Nhập số thứ hai: "))
    
    uscln = gcd(num1, num2)
    print(f"Ước số chung lớn nhất của {num1} và {num2} là: {uscln}")
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ.")
