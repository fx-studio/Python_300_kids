# 046 - Viết chương trình để lấy tất cả các key trong dictionary

# Khởi tạo một dictionary với các cặp key-value ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary ban đầu
print("Dictionary ban đầu:", my_dict)

# Lấy tất cả các key trong dictionary
keys = my_dict.keys()

# In ra danh sách các key
print("Các key trong dictionary:", list(keys))
