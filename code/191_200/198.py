# 198 - Viết chương trình để tạo một generator sinh ra các số Armstrong

def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == num

def armstrong_numbers(n):
    count = 0
    num = 1
    while count < n:
        if is_armstrong(num):
            yield num
            count += 1
        num += 1

# Sử dụng generator
n = 10  # Ví dụ với n = 10
armstrong_gen = armstrong_numbers(n)

# Duyệt qua các phần tử bằng next
for _ in range(n):
    print(next(armstrong_gen))