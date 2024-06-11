# 264 - Viết chương trình để tính định thức của một ma trận

import numpy as np

def calculate_determinant(matrix):
    # Kiểm tra ma trận có vuông không
    if len(matrix) != len(matrix[0]):
        raise ValueError("Ma trận phải là ma trận vuông")
    
    # Sử dụng numpy để tính định thức
    det = np.linalg.det(matrix)
    return det

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = calculate_determinant(A)
print(f"Định thức của ma trận là: {result}")


# --------------------------- #
def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def calculate_determinant_recursive(matrix):
    # Kiểm tra ma trận có vuông không
    if len(matrix) != len(matrix[0]):
        raise ValueError("Ma trận phải là ma trận vuông")
    
    # Trường hợp cơ bản cho ma trận 2x2
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1)**c) * matrix[0][c] * calculate_determinant_recursive(get_matrix_minor(matrix, 0, c))
    
    return determinant

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_recursive = calculate_determinant_recursive(A)
print(f"Định thức của ma trận (phương pháp đệ quy) là: {result_recursive}")
# --------------------------- #