# 042 - Viết chương trình để truy cập giá trị của một key trong dictionary

# Khởi tạo một dictionary với các cặp khóa-giá trị
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary đã tạo
print("Dictionary đã tạo:", my_dict)

# Nhập khóa cần truy cập từ người dùng
key = input("Nhập khóa cần truy cập: ")

# Kiểm tra xem khóa có tồn tại trong dictionary hay không
if key in my_dict:
    # Truy cập và in giá trị tương ứng với khóa
    value = my_dict[key]
    print(f"Giá trị của khóa '{key}' là: {value}")
else:
    # Thông báo khóa không tồn tại trong dictionary
    print(f"Khóa '{key}' không tồn tại trong dictionary.")
