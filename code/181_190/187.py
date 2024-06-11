# 187 - Viết chương trình để sử dụng itertools để tạo ra một permutation

import itertools

# Định nghĩa một danh sách
my_list = [1, 2, 3, 4]

# Tạo ra các permutation từ danh sách
permutations = itertools.permutations(my_list)

# Duyệt qua các permutation và in ra từng hoán vị
for perm in permutations:
    print(perm)
