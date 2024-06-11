# 136 - Viết chương trình để tính tổng các số từ 1 đến n

def calculate_sum(n):
    # Tính tổng các số từ 1 đến n
    return sum(range(1, n + 1))

# Nhập giá trị n từ người dùng
n = int(input("Nhập một số nguyên dương n: "))

# Kiểm tra nếu n là số nguyên dương
if n > 0:
    # Tính tổng và in kết quả
    total_sum = calculate_sum(n)
    print(f"Tổng các số từ 1 đến {n} là: {total_sum}")
else:
    print("Vui lòng nhập một số nguyên dương.")
