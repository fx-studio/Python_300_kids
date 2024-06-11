# 148 - Viết chương trình liệt kê, đếm và tính tổng các ước số của số nguyên dương n

def find_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return divisors, len(divisors), sum(divisors)

n = int(input("Enter a positive integer: "))
divisors, count, total = find_divisors(n)
print(f"Divisors of {n}: {divisors}")
print(f"Number of divisors: {count}")
print(f"Sum of divisors: {total}")