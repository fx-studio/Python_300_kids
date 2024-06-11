# 195 - Viết chương trình để tạo một generator sinh ra các số lẻ

def odd_numbers(n):
    count = 0
    num = 1
    while count < n:
        yield num
        count += 1
        num += 2

# Sử dụng generator và duyệt các phần tử bằng next
n = 10  # Ví dụ với n = 10
odd_gen = odd_numbers(n)

# Duyệt qua các phần tử bằng next
for _ in range(n):
    print(next(odd_gen))