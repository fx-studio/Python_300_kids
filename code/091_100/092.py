# 092 - Viết chương trình để bắt lỗi khi truy cập chỉ mục không tồn tại trong danh sách

try:
    my_list = [1, 2, 3]
    value = my_list[5]
except IndexError:
    value = "Error: Index out of range!"

print(value)