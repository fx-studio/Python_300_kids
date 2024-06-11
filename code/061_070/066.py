# 066 - Viết chương trình để đếm số lần xuất hiện của một ký tự trong chuỗi

# Nhập vào một chuỗi
input_str = "hello world"
print("Chuỗi ban đầu:", input_str)

# Nhập vào ký tự cần đếm
char_to_count = 'l'
print("Ký tự cần đếm:", char_to_count)

# Đếm số lần xuất hiện của ký tự trong chuỗi
count = input_str.count(char_to_count)
print(f"Số lần xuất hiện của ký tự '{char_to_count}' trong chuỗi: {count}")