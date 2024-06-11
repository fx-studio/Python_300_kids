# 024 - Viết chương trình để xóa một phần tử khỏi danh sách

# Khởi tạo danh sách ban đầu
my_list = [1, 2, 3, 4, 5]

# Nhập phần tử muốn xóa từ người dùng
element_to_remove = input("Nhập phần tử muốn xóa khỏi danh sách: ")

# Chuyển đổi phần tử nhập vào từ người dùng thành kiểu dữ liệu tương ứng
try:
    # Cố gắng chuyển đổi phần tử nhập vào thành số nguyên
    element_to_remove = int(element_to_remove)
except ValueError:
    try:
        # Nếu không phải số nguyên, cố gắng chuyển đổi thành số thực
        element_to_remove = float(element_to_remove)
    except ValueError:
        # Nếu không phải số thực, giữ nguyên dưới dạng chuỗi
        pass

# Xóa phần tử khỏi danh sách nếu tồn tại
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print("Danh sách sau khi xóa phần tử:", my_list)
else:
    print("Phần tử không tồn tại trong danh sách.")