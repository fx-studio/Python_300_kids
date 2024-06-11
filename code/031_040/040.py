# 040 - Viết chương trình để tìm phần tử nhỏ nhất trong tuple

# Khởi tạo một tuple
my_tuple = (10, 20, 30, 40, 5, 50, 3, 25)
print("Tuple đã tạo:", my_tuple)

# Giả sử phần tử đầu tiên là phần tử nhỏ nhất
min_element = my_tuple[0]

# Duyệt qua từng phần tử trong tuple để tìm phần tử nhỏ nhất
for element in my_tuple:
    if element < min_element:
        min_element = element

# In ra phần tử nhỏ nhất
print("Phần tử nhỏ nhất trong tuple là:", min_element)
