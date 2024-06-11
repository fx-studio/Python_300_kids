# 182 - Viết chương trình để tạo một iterator từ một tuple

# Định nghĩa một tuple
my_tuple = (10, 20, 30, 40, 50)

# Tạo một iterator từ tuple
my_iterator = iter(my_tuple)

# Sử dụng vòng lặp for để duyệt qua các phần tử của iterator
for element in my_iterator:
    print(element)