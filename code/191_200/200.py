# 200 - Viết chương trình để tạo một generator sinh ra các số chính phương

def square_numbers(n):
    for i in range(1, n+1):
        yield i * i

# Use the generator
for number in square_numbers(5):
    print(number)  # Output: 1, 4, 9, 16, 25