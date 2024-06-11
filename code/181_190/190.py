# 190 - Viết chương trình để sử dụng itertools để tạo ra một combinations_with_replacement

import itertools

# Định nghĩa một danh sách
my_list = [1, 2, 3, 4, 5, 6]

# Định nghĩa độ dài của tổ hợp
r = 3

# Tạo ra các combinations with replacement từ danh sách
combinations_with_replacement = itertools.combinations_with_replacement(my_list, r)

# Duyệt qua các combinations with replacement và in ra từng tổ hợp
for combo in combinations_with_replacement:
    print(combo)