# 068 - Viết chương trình để thay thế một từ trong chuỗi bằng từ khác

# Nhập vào một chuỗi
input_str = "Hello world, welcome to the world of Python."
print("Chuỗi ban đầu:", input_str)

# Nhập vào từ cần thay thế
word_to_replace = "world"
print("Từ cần thay thế:", word_to_replace)

# Nhập vào từ thay thế
replacement_word = "universe"
print("Từ thay thế:", replacement_word)

# Thay thế từ trong chuỗi
new_str = input_str.replace(word_to_replace, replacement_word)
print("Chuỗi sau khi thay thế:", new_str)