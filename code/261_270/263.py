# 263 - Viết chương trình để tính tích của hai ma trận

def multiply_matrices(A, B):
    # Kiểm tra kích thước ma trận
    if len(A[0]) != len(B):
        raise ValueError("Số cột của ma trận A phải bằng số hàng của ma trận B")
    
    # Khởi tạo ma trận kết quả với kích thước (số hàng của A) x (số cột của B)
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = [[0 for _ in range(p)] for _ in range(m)]
    
    # Tính tích của từng phần tử
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply_matrices(A, B)
for row in result:
    print(row)
