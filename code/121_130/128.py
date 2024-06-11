# 128 - Viết chương trình để sử dụng hàm reduce với lambda để tính tích các phần tử trong danh sách

from functools import reduce

# Định nghĩa hàm lambda để nhân hai số lại với nhau
multiply = lambda x, y: x * y

# Danh sách cần tính tích các phần tử
numbers = [1, 2, 3, 4, 5]

# Tính tích các phần tử trong danh sách
result = reduce(multiply, numbers)

print(f"Tích của các phần tử trong danh sách: {result}")