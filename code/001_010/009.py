# 009 - Viết chương trình để in tất cả các số nguyên tố từ 1 đến 100

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to_100():
    for number in range(1, 101):
        if is_prime(number):
            print(number, end=' ')
    print()  # Dòng mới sau khi in xong tất cả các số nguyên tố

# Gọi hàm để in các số nguyên tố từ 1 đến 100
print_primes_up_to_100()
