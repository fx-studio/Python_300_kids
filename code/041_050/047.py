# 047 - Viết chương trình để lấy tất cả các giá trị trong dictionary

# Khởi tạo một dictionary với các cặp key-value ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary ban đầu
print("Dictionary ban đầu:", my_dict)

# Lấy tất cả các giá trị trong dictionary
values = my_dict.values()

# Chuyển đổi các giá trị thành một array (danh sách trong Python)
values_array = list(values)

# In ra array các giá trị
print("Array các giá trị trong dictionary:", values_array)
