# 132 - Viết chương trình để in ra 10 số hạnh phúc đầu tiên

def is_happy_number(n):
    """
    Hàm kiểm tra một số có phải là số hạnh phúc hay không.
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(char) ** 2 for char in str(n))
    return n == 1

def first_n_happy_numbers(n):
    """
    Hàm trả về danh sách n số hạnh phúc đầu tiên.
    """
    happy_numbers = []
    num = 1
    while len(happy_numbers) < n:
        if is_happy_number(num):
            happy_numbers.append(num)
        num += 1
    return happy_numbers

# Số lượng số hạnh phúc cần tìm
n = 10

# Gọi hàm và in kết quả
happy_numbers = first_n_happy_numbers(n)
print("10 số hạnh phúc đầu tiên:", happy_numbers)
