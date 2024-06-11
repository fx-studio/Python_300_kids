# 137 - Viết chương trình để tính sin(x) & cos(x) bằng các triển khai chuỗi Taylor

import math

def taylor_sin(x, terms):
    sin_x = 0
    for n in range(terms):
        sign = (-1)**n
        sin_x += sign * (x**(2*n + 1)) / math.factorial(2*n + 1)
    return sin_x

def taylor_cos(x, terms):
    cos_x = 0
    for n in range(terms):
        sign = (-1)**n
        cos_x += sign * (x**(2*n)) / math.factorial(2*n)
    return cos_x


# Nhập giá trị x từ người dùng (góc tính theo degree)
x_degree = float(input("Nhập giá trị của x (degree): "))

# chuyển đổi degree sang radian
x = math.radians(x_degree)

# Nhập số lượng phần tử của chuỗi Taylor
terms = int(input("Nhập số lượng phần tử của chuỗi Taylor: "))

# Tính giá trị sin(x) và cos(x) bằng chuỗi Taylor
sin_x = taylor_sin(x, terms)
cos_x = taylor_cos(x, terms)

# In kết quả
print(f"Giá trị sin({x_degree}) bằng chuỗi Taylor với {terms} phần tử là: {sin_x}")
print(f"Giá trị cos({x_degree}) bằng chuỗi Taylor với {terms} phần tử là: {cos_x}")
