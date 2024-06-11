# 197 - Viết chương trình để tạo một generator sinh ra các chuỗi hoàn hảo

def is_palindrome(s):
    return s == s[::-1]

def perfect_strings(strings):
    for s in strings:
        if is_palindrome(s):
            yield s

# Sử dụng generator
string_list = ["level", "world", "radar", "python", "madam", "example"]
perfect_gen = perfect_strings(string_list)

# Duyệt qua các phần tử bằng next
try:
    while True:
        print(next(perfect_gen))
except StopIteration:
    pass