# 015 - Viết hàm để tính tổng các chữ số của một số

def sum_of_digits(n):
    # Đảm bảo n là số dương
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Nhập số nguyên từ người dùng
try:
    number = int(input("Nhập một số nguyên: "))
    print(f"Tổng các chữ số của {number} là: {sum_of_digits(number)}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
