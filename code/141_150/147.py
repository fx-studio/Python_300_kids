# 147 - Viết chương trình để kiểm tra một số có phải là số hoàn hảo không

def sum_of_divisors(n, i=1, sum=0):
    if i == n:
        return sum
    else:
        if n % i == 0:
            sum += i
        return sum_of_divisors(n, i + 1, sum)

def is_perfect(n):
    return sum_of_divisors(n) == n

# Test
print(is_perfect(6))  # True
print(is_perfect(28))  # True
print(is_perfect(12))  # False