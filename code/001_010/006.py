# 006 - Chương trình in bảng cửu chương từ 1 đến 10

def print_multiplication_table():
    for i in range(1, 11):
        print(f"Bảng cửu chương {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # In dòng trống để ngăn cách giữa các bảng cửu chương

# Gọi hàm để in bảng cửu chương
print_multiplication_table()
