# 017 - Viết hàm để tính lũy thừa của một số

def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        result = 1 / result
    return result

# Nhập cơ số và số mũ từ người dùng
try:
    base = float(input("Nhập cơ số: "))
    exponent = int(input("Nhập số mũ: "))
    print(f"{base} ^ {exponent} = {power(base, exponent)}")
except ValueError:
    print("Vui lòng nhập cơ số là một số và số mũ là một số nguyên hợp lệ.")
