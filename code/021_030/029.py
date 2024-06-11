# 029 - Viết chương trình để tính tổng các phần tử trong danh sách

import random

# Khởi tạo danh sách với các phần tử ngẫu nhiên
# Giả sử danh sách có 10 phần tử với giá trị từ 1 đến 100
my_list = [random.randint(1, 100) for _ in range(10)]

# In danh sách ban đầu
print("Danh sách ban đầu:", my_list)

# Tính tổng các phần tử trong danh sách
total_sum = sum(my_list)

# In ra tổng các phần tử
print("Tổng các phần tử trong danh sách là:", total_sum)