# 027 - Viết chương trình để tìm phần tử lớn nhất trong danh sách

import random

# Khởi tạo mảng số nguyên với các giá trị ngẫu nhiên từ 1 đến 100
my_list = [random.randint(1, 100) for _ in range(10)]

# In ra mảng
print("Mảng số nguyên với các giá trị ngẫu nhiên:", my_list)

# Tìm phần tử lớn nhất trong danh sách
max_element = max(my_list)

# In ra phần tử lớn nhất
print("Phần tử lớn nhất trong danh sách là:", max_element)