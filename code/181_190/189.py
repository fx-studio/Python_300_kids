# 189 - Viết chương trình để sử dụng itertools để tạo ra một product

import itertools

# Định nghĩa các collection
list1 = [1, 2]
list2 = ['a', 'b']
list3 = ['x', 'y']

# Tạo ra các product từ các collection
product_result = itertools.product(list1, list2, list3)

# Duyệt qua các product và in ra từng kết hợp
for combo in product_result:
    print(combo)
