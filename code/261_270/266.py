# 266 - Viết chương trình để tính ma trận chuyển vị của một ma trận

def transpose_matrix(matrix):
    # Lấy kích thước của ma trận gốc
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Tạo ma trận mới với số hàng và số cột đảo ngược
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Gán giá trị vào ma trận chuyển vị
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [4, 5, 6]
]

result = transpose_matrix(A)
print("Ma trận chuyển vị là:")
for row in result:
    print(row)

# --------------------------- #

import numpy as np

def transpose_matrix_numpy(matrix):
    return np.transpose(matrix)

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [4, 5, 6]
]

result_numpy = transpose_matrix_numpy(A)
print("Ma trận chuyển vị (sử dụng numpy) là:")
print(result_numpy)

# --------------------------- #