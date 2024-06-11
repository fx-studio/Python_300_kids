# 048 - Viết chương trình để lấy tất cả các cặp key-value trong dictionary

# Khởi tạo một dictionary với các cặp key-value ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary ban đầu
print("Dictionary ban đầu:", my_dict)

# Lấy tất cả các cặp key-value trong dictionary
items = my_dict.items()

# Chuyển đổi các cặp key-value thành danh sách (list)
items_list = list(items)

# In ra danh sách các cặp key-value
print("Danh sách các cặp key-value trong dictionary:", items_list)
