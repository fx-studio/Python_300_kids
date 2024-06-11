# 016 - Viết hàm để kiểm tra một chuỗi có phải là palindrome không

def is_palindrome(s):
    # Chuyển tất cả ký tự về chữ thường và loại bỏ các ký tự không phải chữ cái và số
    s = ''.join(char.lower() for char in s if char.isalnum())
    # So sánh chuỗi với chuỗi đảo ngược của nó
    return s == s[::-1]

# Nhập chuỗi từ người dùng
input_string = input("Nhập một chuỗi: ")

if is_palindrome(input_string):
    print(f'"{input_string}" là palindrome.')
else:
    print(f'"{input_string}" không phải là palindrome.')
