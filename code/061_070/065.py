# 065 - Viết chương trình để chuyển đổi chuỗi thành chữ thường

# Tạo một chuỗi
str1 = "Hello, World!"

# Chuyển đổi chuỗi thành chữ thường
lowercase_str = str1.lower()
print(lowercase_str)

# Hoặc sử dụng vòng lặp
# Tạo một chuỗi
str1 = "Hello, World!"

# Chuyển đổi chuỗi thành chữ thường
lowercase_str = ""
for char in str1:
    if 'A' <= char <= 'Z':
        lowercase_str += chr(ord(char) + 32)
    else:
        lowercase_str += char
print(lowercase_str)