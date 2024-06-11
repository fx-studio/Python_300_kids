# 008 - Viết chương trình để đếm số lượng số chẵn và lẻ trong một danh sách

def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    for number in numbers:
        if number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

# Nhập danh sách các số nguyên từ người dùng
try:
    input_list = input("Nhập các số nguyên, cách nhau bằng dấu cách: ")
    numbers = [int(num) for num in input_list.split()]
    
    even_count, odd_count = count_even_odd(numbers)
    print(f"Số lượng số chẵn: {even_count}")
    print(f"Số lượng số lẻ: {odd_count}")
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ.")
