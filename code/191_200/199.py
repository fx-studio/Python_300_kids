# 199 - Viết chương trình để tạo một generator sinh ra các số hoàn hảo

def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def perfect_numbers(n):
    count = 0
    num = 2
    while count < n:
        if is_perfect(num):
            yield num
            count += 1
        num += 1

# Sử dụng generator
n = 3  # Ví dụ với n = 3
perfect_gen = perfect_numbers(n)

# Duyệt qua các phần tử bằng next
for _ in range(n):
    print(next(perfect_gen))