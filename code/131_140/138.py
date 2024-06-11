# 138 - Viết chương trình để tính Lôgarit tự nhiên ln(x)

def taylor_ln(x, terms):
    if x <= 0:
        raise ValueError("Giá trị của x phải lớn hơn 0")
    if x == 1:
        return 0

    # Sử dụng ln(x) = 2 * sum((y^n / n) for n in range(1, terms + 1))
    # với y = (x - 1) / (x + 1)
    y = (x - 1) / (x + 1)
    ln_x = 0
    for n in range(1, terms + 1):
        ln_x += (y**(2*n - 1)) / (2*n - 1)
    return 2 * ln_x

# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị của x (x > 0 và x ≠ 1): "))

# Nhập số lượng phần tử của chuỗi Taylor
terms = int(input("Nhập số lượng phần tử của chuỗi Taylor: "))

# Tính giá trị ln(x) bằng chuỗi Taylor
try:
    ln_x = taylor_ln(x, terms)
    print(f"Giá trị ln({x}) bằng chuỗi Taylor với {terms} phần tử là: {ln_x}")
except ValueError as e:
    print(e)
