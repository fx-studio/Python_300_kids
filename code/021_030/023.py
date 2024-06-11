# 023 - Viết chương trình để thêm một phần tử vào đầu danh sách

# Khởi tạo danh sách ban đầu
my_list = [1, 2, 3, 4, 5]

# Nhập phần tử muốn thêm từ người dùng
new_element = input("Nhập phần tử muốn thêm vào đầu danh sách: ")

# Thêm phần tử vào đầu danh sách
my_list.insert(0, new_element)

# In danh sách sau khi thêm phần tử
print("Danh sách sau khi thêm phần tử:", my_list)