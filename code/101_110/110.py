# 110 - Viết chương trình để kiểm tra một chuỗi có phải là palindrome không

# Cách 1: Sử dụng cách đảo ngược chuỗi
def kiem_tra_palindrome(chuoi):
    """
    Hàm để kiểm tra một chuỗi có phải là palindrome không.
    """
    chuoi = chuoi.replace(" ", "").lower()
    return chuoi == chuoi[::-1]

# Cách 2: Sử dụng vòng lặp
def kiem_tra_palindrome2(chuoi):
    """
    Hàm để kiểm tra một chuỗi có phải là palindrome không.
    """
    chuoi = chuoi.replace(" ", "").lower()
    n = len(chuoi)
    for i in range(n // 2):
        if chuoi[i] != chuoi[n - i - 1]:
            return False
    return True

# Chuỗi cần kiểm tra
chuoi1 = "A man a plan a canal Panama"
chuoi2 = "Hello World"

# Gọi hàm và in kết quả
print(kiem_tra_palindrome(chuoi1))  # True
print(kiem_tra_palindrome(chuoi2))  # False

# Gọi hàm và in kết quả
print(kiem_tra_palindrome2(chuoi1))  # True
print(kiem_tra_palindrome2(chuoi2))  # False
