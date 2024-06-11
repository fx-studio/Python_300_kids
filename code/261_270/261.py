# 261 - Viết chương trình để tính tổng của hai ma trận

def add_matrices(matrix1, matrix2):
    # Kiểm tra kích thước của hai ma trận
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Hai ma trận phải có cùng kích thước")

    # Tạo ma trận kết quả với kích thước tương tự
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)
    
    return result_matrix

# Ví dụ về cách sử dụng hàm
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = add_matrices(matrix1, matrix2)
for row in result:
    print(row)
