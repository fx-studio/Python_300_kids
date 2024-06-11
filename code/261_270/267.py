# 267 - Viết chương trình để tính hạng của một ma trận

import numpy as np

def rank_of_matrix(matrix):
    # Chuyển ma trận thành dạng numpy array
    np_matrix = np.array(matrix)
    
    # Sử dụng numpy để tính hạng của ma trận
    rank = np.linalg.matrix_rank(np_matrix)
    return rank

# Ví dụ sử dụng
A = [
    [10, 20, 10],
    [-20, -30, 10],
    [30, 50, 0]
]

result = rank_of_matrix(A)
print(f"Hạng của ma trận là: {result}")

# --------------------------- #

def gauss_jordan_rank(matrix):
    # Copy ma trận để tránh thay đổi ma trận gốc
    M = [row[:] for row in matrix]
    m = len(M)
    n = len(M[0])
    rank = 0

    for r in range(min(m, n)):
        if M[r][r] != 0:
            rank += 1
            for row in range(r+1, m):
                factor = M[row][r] / M[r][r]
                for col in range(r, n):
                    M[row][col] -= factor * M[r][col]
        else:
            for row in range(r+1, m):
                if M[row][r] != 0:
                    M[r], M[row] = M[row], M[r]
                    rank += 1
                    break
    
    # Đếm số hàng khác không
    for row in M:
        if any([abs(x) > 1e-10 for x in row]):
            rank += 1

    return rank

# Ví dụ sử dụng
A = [
    [10, 20, 10],
    [-20, -30, 10],
    [30, 50, 0]
]

result_gj = gauss_jordan_rank(A)
print(f"Hạng của ma trận (phương pháp Gauss-Jordan) là: {result_gj}")

# --------------------------- #