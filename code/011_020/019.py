# 019 - Viết hàm để tính chu vi và diện tích hình tròn

import math

# Hàm tính chu vi hình tròn
def circumference(radius):
    return 2 * math.pi * radius

# Hàm tính diện tích hình tròn
def area(radius):
    return math.pi * radius * radius

# Nhập bán kính từ người dùng
try:
    radius = float(input("Nhập bán kính của hình tròn: "))
    if radius < 0:
        print("Bán kính phải là một số không âm.")
    else:
        circ = circumference(radius)
        ar = area(radius)
        print(f"Chu vi của hình tròn là: {circ}")
        print(f"Diện tích của hình tròn là: {ar}")
except ValueError:
    print("Vui lòng nhập một giá trị hợp lệ cho bán kính.")
