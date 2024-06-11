# 192 - Viết chương trình để tạo một generator sinh ra các số Fibonacci

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Sử dụng generator
n = 10  # Ví dụ với n = 10
for number in fibonacci(n):
    print(number)
