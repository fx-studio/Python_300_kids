# 265 - Viết chương trình để tính ma trận nghịch đảo của một ma trận

import numpy as np

def invert_matrix(matrix):
    # Kiểm tra ma trận có vuông không
    if len(matrix) != len(matrix[0]):
        raise ValueError("Ma trận phải là ma trận vuông")
    
    # Tính định thức của ma trận
    det = np.linalg.det(matrix)
    if det == 0:
        raise ValueError("Ma trận không khả nghịch (định thức bằng 0)")
    
    # Tính ma trận nghịch đảo
    inv_matrix = np.linalg.inv(matrix)
    return inv_matrix

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

result = invert_matrix(A)
print("Ma trận nghịch đảo là:")
print(result)

# --------------------------- #

def gauss_jordan_inverse(matrix):
    n = len(matrix)
    
    # Tạo ma trận đơn vị
    I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    
    # Nối ma trận đơn vị vào bên phải ma trận gốc
    M = [row + I_row for row, I_row in zip(matrix, I)]
    
    # Áp dụng phương pháp Gauss-Jordan
    for i in range(n):
        # Tìm phần tử lớn nhất trong cột hiện tại
        max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
        # Đổi chỗ hàng hiện tại với hàng chứa phần tử lớn nhất
        M[i], M[max_row] = M[max_row], M[i]
        
        # Chia hàng hiện tại cho phần tử chéo chính
        pivot = M[i][i]
        M[i] = [x / pivot for x in M[i]]
        
        # Biến các hàng khác thành 0 ở cột hiện tại
        for j in range(n):
            if i != j:
                factor = M[j][i]
                M[j] = [M[j][k] - factor * M[i][k] for k in range(2 * n)]
    
    # Tách phần bên phải của ma trận đã nối để lấy ma trận nghịch đảo
    inv_matrix = [row[n:] for row in M]
    return inv_matrix

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

result_gj = gauss_jordan_inverse(A)
print("Ma trận nghịch đảo (phương pháp Gauss-Jordan) là:")
for row in result_gj:
    print(row)

# --------------------------- #