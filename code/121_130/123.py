# 123 - Viết chương trình để sử dụng hàm reduce để tính tổng các phần tử trong danh sách

from functools import reduce

def add(x, y):
    """
    Hàm để tính tổng hai số.
    """
    return x + y

# Danh sách đầu vào
numbers = [1, 2, 3, 4, 5]

# Sử dụng hàm reduce để tính tổng các phần tử trong danh sách
total = reduce(add, numbers)

print("Tổng các phần tử trong danh sách:", total)