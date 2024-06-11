# 133 - Viết chương trình để tìm bội số chung nhỏ nhất (BSCNN) của hai số

import math

def lcm(a, b):
    """
    Hàm để tìm bội số chung nhỏ nhất (BSCNN) của hai số.
    """
    return abs(a * b) // math.gcd(a, b)

# Hai số đầu vào
a = 15
b = 20

# Gọi hàm và in kết quả
bscnn = lcm(a, b)
print(f"Bội số chung nhỏ nhất của {a} và {b} là: {bscnn}")
