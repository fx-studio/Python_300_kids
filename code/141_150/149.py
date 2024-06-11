# 149 - Viết chương trình để nhập vào một số nguyên dương n, phân tích n thành các thừa số nguyên tố

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = int(input("Enter a positive integer: "))
factors = prime_factors(n)
print(f"Prime factors of {n}: {factors}")