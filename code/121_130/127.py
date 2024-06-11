# 127 - Viết chương trình để sử dụng hàm filter với lambda để lọc các số lớn hơn 10 trong danh sách

# Định nghĩa hàm lambda để kiểm tra một số có lớn hơn 10 hay không
greater_than_10 = lambda x: x > 10

# Danh sách cần lọc các số lớn hơn 10
numbers = [5, 10, 15, 20, 25]

# Lọc các số lớn hơn 10 trong danh sách
result = list(filter(greater_than_10, numbers))

print(f"Danh sách sau khi lọc các số lớn hơn 10: {result}")