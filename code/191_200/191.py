# 191 - Viết chương trình để tạo một generator sinh ra các số nguyên từ 1 đến n

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Sử dụng generator
n = 10  # Ví dụ với n = 10
for number in generate_numbers(n):
    print(number)
