# 002 - Viết chương trình để kiểm tra số chẵn hay lẻ.

# Hàm kiểm tra số được nhập
def check_even_odd(n):
    if n % 2 == 0:
        return "Số bạn nhập là số chẵn."
    else:
        return "Số bạn nhập là số lẻ."

# Nhập số nguyên từ người dùng
try:
    number = int(input("Nhập một số nguyên: "))
    result = check_even_odd(number)
    print(result)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
