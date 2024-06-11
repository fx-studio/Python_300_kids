# 126 - Viết chương trình để sử dụng hàm map với lambda để nhân đôi các phần tử trong danh sách

# Định nghĩa hàm lambda để nhân đôi một số
double = lambda x: x * 2

# Danh sách cần nhân đôi các phần tử
numbers = [1, 2, 3, 4, 5]

# Nhân đôi các phần tử trong danh sách
result = list(map(double, numbers))

print(f"Danh sách sau khi nhân đôi các phần tử: {result}")