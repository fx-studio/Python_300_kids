# 038 - Viết chương trình để đếm số lần xuất hiện của một phần tử trong tuple

# Khởi tạo một tuple
my_tuple = (10, 20, 30, 20, 40, 50, 20, 60)

# In tuple đã tạo
print("Tuple đã tạo:", my_tuple)

# Nhập phần tử cần đếm số lần xuất hiện từ người dùng
element = input("Nhập phần tử cần đếm số lần xuất hiện: ")

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

# Đếm số lần xuất hiện của phần tử trong tuple
count = my_tuple.count(element)

# In ra số lần xuất hiện của phần tử
print(f"Phần tử {element} xuất hiện {count} lần trong tuple.")
