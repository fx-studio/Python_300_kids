# 135 - chương trình để tìm tất cả các số nguyên tố từ 1 đến 100

def is_prime(n):
    # Kiểm tra nếu n nhỏ hơn 2, thì không phải là số nguyên tố
    if n < 2:
        return False
    # Kiểm tra các ước từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Danh sách để lưu trữ các số nguyên tố
prime_numbers = []

# Kiểm tra các số từ 1 đến 100
for num in range(1, 101):
    if is_prime(num):
        prime_numbers.append(num)

# In danh sách các số nguyên tố từ 1 đến 100
print(prime_numbers)