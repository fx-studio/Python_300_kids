# 026 - Viết chương trình để sắp xếp danh sách theo thứ tự giảm dần

import random

# Khởi tạo danh sách ban đầu
my_list = [34, 1, 23, 4, 3, 12, 45, 33, 6, 22]

# In danh sách ban đầu
print("Danh sách ban đầu:", my_list)

# Xáo trộn ngẫu nhiên danh sách
random.shuffle(my_list)
print("Danh sách sau khi xáo trộn:", my_list)

# Sắp xếp danh sách theo thứ tự giảm dần
my_list.sort(reverse=True)

# In danh sách sau khi sắp xếp
print("Danh sách sau khi sắp xếp giảm dần:", my_list)