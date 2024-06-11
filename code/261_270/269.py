# 269 - Viết chương trình để kiểm tra một ma trận có phải là ma trận đối xứng không

def is_symmetric_matrix(matrix):
    # Kiểm tra ma trận có vuông không
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    
    # Kiểm tra tính đối xứng
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    
    return True

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

B = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 6, 6]
]

print("Ma trận A là ma trận đối xứng:", is_symmetric_matrix(A))  # Output: True
print("Ma trận B là ma trận đối xứng:", is_symmetric_matrix(B))  # Output: False
