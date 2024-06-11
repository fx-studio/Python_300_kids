# 044 - Viết chương trình để xóa một cặp key-value khỏi dictionary

# Khởi tạo một dictionary với các cặp key-value ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary ban đầu
print("Dictionary ban đầu:", my_dict)

# Nhập khóa cần xóa từ người dùng
key_to_delete = input("Nhập khóa cần xóa: ")

# Kiểm tra xem khóa có tồn tại trong dictionary hay không
if key_to_delete in my_dict:
    # Xóa cặp key-value bằng phương thức pop()
    my_dict.pop(key_to_delete)
    print(f"Đã xóa cặp key-value có khóa '{key_to_delete}'.")
else:
    # Thông báo khóa không tồn tại trong dictionary
    print(f"Khóa '{key_to_delete}' không tồn tại trong dictionary.")

# In ra dictionary sau khi xóa cặp key-value
print("Dictionary sau khi xóa cặp key-value:", my_dict)