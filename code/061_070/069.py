# 069 - Viết chương trình để tách chuỗi thành danh sách các từ

# Nhập vào một chuỗi
input_str = "Hello world, welcome to the world of Python."
print("Chuỗi ban đầu:", input_str)

# Tách chuỗi thành danh sách các từ bằng khoảng trắng
words_list = input_str.split()
print("Danh sách các từ (tách bằng khoảng trắng):", words_list)

# Tách chuỗi bằng dấu phẩy
input_str_comma = "apple,banana,orange,grape"
print("Chuỗi ban đầu:", input_str_comma)

words_list_comma = input_str_comma.split(',')
print("Danh sách các từ (tách bằng dấu phẩy):", words_list_comma)

# Tách chuỗi bằng dấu chấm
input_str_dot = "This.is.a.sample.sentence."
print("Chuỗi ban đầu:", input_str_dot)

words_list_dot = input_str_dot.split('.')
print("Danh sách các từ (tách bằng dấu chấm):", words_list_dot)
