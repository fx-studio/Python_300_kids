# 193 - Viết chương trình để tạo một generator sinh ra các số nguyên tố

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Sử dụng generator
n = 10  # Ví dụ với n = 10
for number in prime_numbers(n):
    print(number)
