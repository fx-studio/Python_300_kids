# 134 - Viết chương trình để kiểm tra một số có phải là số nguyên tố không

def is_prime_recursive(n, divisor=None):
    """
    Hàm đệ quy để kiểm tra số nguyên tố.
    """
    if divisor is None:
        divisor = n - 1

    if n < 2:
        return False
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False

    return is_prime_recursive(n, divisor - 1)

# Kiểm tra hàm với một số đầu vào
number = 29

if is_prime_recursive(number):
    print(f"{number} là số nguyên tố.")
else:
    print(f"{number} không phải là số nguyên tố.")
