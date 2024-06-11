# 121 - Viết chương trình để sử dụng hàm map để nhân đôi các phần tử trong danh sách

def double(n):
    """
    Hàm để nhân đôi một số.
    """
    return n * 2

# Danh sách đầu vào
numbers = [1, 2, 3, 4, 5]

# Sử dụng hàm map để nhân đôi các phần tử trong danh sách
doubled_numbers = list(map(double, numbers))

print("Danh sách sau khi nhân đôi các phần tử:", doubled_numbers)