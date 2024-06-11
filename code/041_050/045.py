# 045 - Viết chương trình để kiểm tra một key có tồn tại trong dictionary không

# Khởi tạo một dictionary với các cặp key-value ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary ban đầu
print("Dictionary ban đầu:", my_dict)

# Nhập khóa cần kiểm tra từ người dùng
key_to_check = input("Nhập khóa cần kiểm tra: ")

# Kiểm tra xem khóa có tồn tại trong dictionary hay không
if key_to_check in my_dict:
    print(f"Khóa '{key_to_check}' tồn tại trong dictionary.")
else:
    print(f"Khóa '{key_to_check}' không tồn tại trong dictionary.")