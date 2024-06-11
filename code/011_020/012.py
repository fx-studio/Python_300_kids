# 012 - Chương trình tính tổng các số từ 1 đến n

def sum_of_numbers(n):
    if n < 1:
        return "Vui lòng nhập một số nguyên dương lớn hơn hoặc bằng 1."
    return n * (n + 1) // 2

# Nhập số nguyên dương từ người dùng
try:
    number = int(input("Nhập một số nguyên dương: "))
    if number < 1:
        print("Vui lòng nhập một số nguyên dương lớn hơn hoặc bằng 1.")
    else:
        print(f"Tổng các số từ 1 đến {number} là: {sum_of_numbers(number)}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")