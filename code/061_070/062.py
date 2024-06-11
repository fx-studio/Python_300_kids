# 062 - Viết chương trình để nối hai chuỗi

# Tạo hai chuỗi
str1 = "Hello, "
str2 = "World!"

# Nối hai chuỗi
str3 = str1 + str2
print(str3)

# Hoặc sử dụng phương thức join()
# Tạo hai chuỗi
str1 = "Hello, "
str2 = "World!"

# Nối hai chuỗi
str3 = ''.join([str1, str2])
print(str3)

# Hoặc sử dụng f-string
# Tạo hai chuỗi
str1 = "Hello, "
str2 = "World!"

# Nối hai chuỗi
str3 = f"{str1}{str2}"
print(str3)

# Hoặc sử dụng phương thức format()
# Tạo hai chuỗi
str1 = "Hello, "
str2 = "World!"

# Nối hai chuỗi
str3 = "{}{}".format(str1, str2)
print(str3)
