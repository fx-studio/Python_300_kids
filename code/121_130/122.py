# 122 - Viết chương trình để sử dụng hàm filter để lọc các số chẵn trong danh sách

def is_even(n):
    """
    Hàm để kiểm tra một số có phải là số chẵn hay không.
    """
    return n % 2 == 0

# Danh sách đầu vào
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sử dụng hàm filter để lọc các số chẵn trong danh sách
even_numbers = list(filter(is_even, numbers))

print("Danh sách các số chẵn:", even_numbers)