# 014 - Viết hàm để tìm số lớn nhất trong một danh sách

def find_max(numbers):
    if not numbers:
        return "Danh sách rỗng, không có số lớn nhất."
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# Nhập danh sách các số từ người dùng
try:
    input_numbers = input("Nhập các số, cách nhau bởi dấu cách: ")
    numbers = [float(num) for num in input_numbers.split()]
    
    if not numbers:
        print("Danh sách rỗng, không có số lớn nhất.")
    else:
        max_number = find_max(numbers)
        print(f"Số lớn nhất trong danh sách là: {max_number}")
except ValueError:
    print("Vui lòng nhập các số hợp lệ.")
