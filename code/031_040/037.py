# 037 - Viết chương trình để kiểm tra một phần tử có tồn tại trong tuple không

# Khởi tạo một tuple
my_tuple = (10, 20, 30, 40, 50)

# In tuple đã tạo
print("Tuple đã tạo:", my_tuple)

# Nhập phần tử cần kiểm tra từ người dùng
element = input("Nhập phần tử cần kiểm tra: ")

# Chuyển đổi phần tử nhập vào từ người dùng thành kiểu dữ liệu tương ứng
try:
    # Cố gắng chuyển đổi phần tử nhập vào thành số nguyên
    element = int(element)
except ValueError:
    try:
        # Nếu không phải số nguyên, cố gắng chuyển đổi thành số thực
        element = float(element)
    except ValueError:
        # Nếu không phải số thực, giữ nguyên dưới dạng chuỗi
        pass

# Kiểm tra xem phần tử có tồn tại trong tuple không
if element in my_tuple:
    print(f"Phần tử {element} tồn tại trong tuple.")
else:
    print(f"Phần tử {element} không tồn tại trong tuple.")
