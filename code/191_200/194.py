# 194 - Viết chương trình để tạo một generator sinh ra các số chẵn

def even_numbers(n):
    count = 0
    num = 2
    while count < n:
        yield num
        count += 1
        num += 2

# Sử dụng generator
n = 10  # Ví dụ với n = 10
for number in even_numbers(n):
    print(number)