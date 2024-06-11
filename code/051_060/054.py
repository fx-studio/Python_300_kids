# 054 - Viết chương trình để kiểm tra một phần tử có tồn tại trong set không

# Khởi tạo một set ban đầu
my_set = {'apple', 'banana', 'cherry'}
print("Set ban đầu:", my_set)

# Kiểm tra sự tồn tại của phần tử trong set
element = 'banana'
if element in my_set:
    print(f"Phần tử '{element}' tồn tại trong set.")
else:
    print(f"Phần tử '{element}' không tồn tại trong set.")

element = 'orange'
if element in my_set:
    print(f"Phần tử '{element}' tồn tại trong set.")
else:
    print(f"Phần tử '{element}' không tồn tại trong set.")