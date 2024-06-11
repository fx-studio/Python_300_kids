# 188 - Viết chương trình để sử dụng itertools để tạo ra một combination

import itertools

# Định nghĩa một danh sách
my_list = [1, 2, 3, 4]

# Định nghĩa độ dài của tổ hợp
r = 2

# Tạo ra các combination từ danh sách
combinations = itertools.combinations(my_list, r)

# Duyệt qua các combination và in ra từng tổ hợp
for combo in combinations:
    print(combo)
