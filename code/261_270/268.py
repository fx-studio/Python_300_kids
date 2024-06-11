# 268 - Viết chương trình để kiểm tra một ma trận có phải là ma trận đơn vị không

def is_identity_matrix(matrix):
    # Kiểm tra ma trận có vuông không
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    
    # Kiểm tra các phần tử của ma trận
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    
    return True

# Ví dụ sử dụng
A = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

B = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

print("Ma trận A là ma trận đơn vị:", is_identity_matrix(A))  # Output: True
print("Ma trận B là ma trận đơn vị:", is_identity_matrix(B))  # Output: False
