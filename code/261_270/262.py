# 262 - Viết chương trình để tính hiệu của hai ma trận

def subtract_matrices(A, B):
    # Kiểm tra kích thước ma trận
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Hai ma trận phải có cùng kích thước")
    
    # Khởi tạo ma trận kết quả với cùng kích thước
    rows = len(A)
    cols = len(A[0])
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Tính hiệu của từng phần tử
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] - B[i][j]
    
    return C

# Ví dụ sử dụng
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = subtract_matrices(A, B)
for row in result:
    print(row)
