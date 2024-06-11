# 270 - Viết chương trình để kiểm tra một ma trận có phải là ma trận tam giác trên không

def is_upper_triangular(matrix):
    # Kiểm tra ma trận có vuông không
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    
    # Kiểm tra các phần tử dưới đường chéo chính
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    
    return True

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

B = [
    [1, 2, 3],
    [0, 4, 5],
    [7, 0, 6]
]

print("Ma trận A là ma trận tam giác trên:", is_upper_triangular(A))  # Output: True
print("Ma trận B là ma trận tam giác trên:", is_upper_triangular(B))  # Output: False
