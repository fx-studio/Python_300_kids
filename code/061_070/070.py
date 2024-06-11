# 070 - Viết chương trình để nối các từ thành một chuỗi

# Nhập vào một danh sách các từ
words_list = ["Hello", "world", "welcome", "to", "Python"]
print("Danh sách các từ:", words_list)

# Nối các từ thành một chuỗi bằng khoảng trắng
joined_str = ' '.join(words_list)
print("Chuỗi sau khi nối:", joined_str)


# Nối các từ bằng dấu phẩy
joined_str_comma = ', '.join(words_list)
print("Chuỗi sau khi nối bằng dấu phẩy:", joined_str_comma)


# Nối các từ bằng dấu chấm phẩy
joined_str_semicolon = '; '.join(words_list)
print("Chuỗi sau khi nối bằng dấu chấm phẩy:", joined_str_semicolon)
