# 043 - Viết chương trình để thêm một cặp key-value vào dictionary

# Khởi tạo một dictionary với các cặp khóa-giá trị ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary đã tạo
print("Dictionary ban đầu:", my_dict)

# Nhập khóa cần thêm từ người dùng
new_key = input("Nhập khóa cần thêm: ")

# Nhập giá trị cần thêm từ người dùng
new_value = input("Nhập giá trị cần thêm: ")

# Thêm cặp key-value vào dictionary
my_dict[new_key] = new_value

# In ra dictionary sau khi thêm cặp key-value
print("Dictionary sau khi thêm cặp key-value:", my_dict)