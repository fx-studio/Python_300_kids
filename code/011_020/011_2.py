# 011 - Chương trình tính giai thừa của một số nguyên sử dụng đệ quy

def factorial_recursive(n):
    if n < 0:
        return "Giai thừa không xác định cho số âm"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Nhập số nguyên dương từ người dùng
try:
    number = int(input("Nhập một số nguyên dương: "))
    if number < 0:
        print("Giai thừa không xác định cho số âm")
    else:
        print(f"Giai thừa của {number} là: {factorial_recursive(number)}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
