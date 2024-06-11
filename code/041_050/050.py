# 050 - Viết chương trình để nối hai dictionary

# Khởi tạo hai dictionary với các cặp key-value ban đầu
dict1 = {
    'name': 'Alice',
    'age': 25
}

dict2 = {
    'city': 'New York',
    'country': 'USA'
}

# In hai dictionary ban đầu
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

# Phương pháp 1: Sử dụng phương thức update() để nối hai dictionary
dict3 = dict1.copy()  # Tạo một bản sao của dict1 để không thay đổi dict1 gốc
dict3.update(dict2)
print("Kết quả nối dictionary bằng phương thức update():", dict3)

# Phương pháp 2: Sử dụng toán tử ** để nối hai dictionary
dict4 = {**dict1, **dict2}
print("Kết quả nối dictionary bằng toán tử **:", dict4)
