# 130 - Viết chương trình để sử dụng hàm lambda để tìm số lớn nhất trong danh sách

# Danh sách cần tìm số lớn nhất
numbers = [1, 2, 33, 4, 5]

# Tìm số lớn nhất trong danh sách
max_number = max(numbers, key=lambda x: x)

print(f"Số lớn nhất trong danh sách: {max_number}")