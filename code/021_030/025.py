# 025 - Viết chương trình để sắp xếp danh sách theo thứ tự tăng dần

import random

# Khởi tạo danh sách ban đầu
my_list = [34, 1, 23, 4, 3, 12, 45, 33, 6, 22]

# Trộn ngẫu nhiên danh sách
random.shuffle(my_list)

# In danh sách ban đầu
print("Danh sách ban đầu:", my_list)

# Sắp xếp danh sách theo thứ tự tăng dần
my_list.sort()

# In danh sách sau khi sắp xếp
print("Danh sách sau khi sắp xếp tăng dần:", my_list)