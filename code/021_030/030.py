# 030 - Viết chương trình để đếm số lần xuất hiện của một phần tử trong danh sách

# Khởi tạo danh sách ban đầu
my_list = [1, 3, 7, 8, 7, 5, 6, 7, 2, 7, 10]

# In danh sách ban đầu
print("Danh sách ban đầu:", my_list)

# Nhập phần tử muốn đếm số lần xuất hiện từ người dùng
element_to_count = input("Nhập phần tử muốn đếm số lần xuất hiện: ")

# Chuyển đổi phần tử nhập vào từ người dùng thành kiểu dữ liệu tương ứng
try:
    # Cố gắng chuyển đổi phần tử nhập vào thành số nguyên
    element_to_count = int(element_to_count)
except ValueError:
    try:
        # Nếu không phải số nguyên, cố gắng chuyển đổi thành số thực
        element_to_count = float(element_to_count)
    except ValueError:
        # Nếu không phải số thực, giữ nguyên dưới dạng chuỗi
        pass

# Đếm số lần xuất hiện của phần tử trong danh sách
count = my_list.count(element_to_count)

# In ra số lần xuất hiện của phần tử
print(f"Phần tử {element_to_count} xuất hiện {count} lần trong danh sách.")