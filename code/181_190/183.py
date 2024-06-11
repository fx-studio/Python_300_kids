# 183 - Viết chương trình để tạo một iterator từ một chuỗi

# Định nghĩa một chuỗi
my_string = "Hello, World!"

# Tạo một iterator từ chuỗi
my_iterator = iter(my_string)

# Sử dụng vòng lặp for để duyệt qua các phần tử của iterator
for character in my_iterator:
    print(character)