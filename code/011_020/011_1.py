# 011 - Chương trình tính giai thừa của một số nguyên sử dụng vòng lặp

def factorial_iterative(n):
    if n < 0:
        return "Giai thừa không xác định cho số âm"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Nhập số nguyên dương từ người dùng
try:
    number = int(input("Nhập một số nguyên dương: "))
    if number < 0:
        print("Giai thừa không xác định cho số âm")
    else:
        print(f"Giai thừa của {number} là: {factorial_iterative(number)}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
