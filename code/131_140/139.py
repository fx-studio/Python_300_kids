# 139 - Viết chương trình để in ra n số hoàn hảo đầu tiên

def is_perfect_number(num):
    # Tính tổng các ước số dương của num (không bao gồm chính nó)
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num

def find_perfect_numbers(n):
    perfect_numbers = []
    number = 1
    while len(perfect_numbers) < n:
        if is_perfect_number(number):
            perfect_numbers.append(number)
        number += 1
    return perfect_numbers

# Nhập giá trị n từ người dùng
n = int(input("Nhập số lượng số hoàn hảo cần tìm: "))

# Tìm và in ra n số hoàn hảo đầu tiên
perfect_numbers = find_perfect_numbers(n)
print(f"{n} số hoàn hảo đầu tiên là: {perfect_numbers}")
