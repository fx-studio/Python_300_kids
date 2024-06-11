# 140 - Viết chương trình để in ra các số Armstrong từ 1 đến 1000

def is_armstrong_number(num):
    # Chuyển số thành chuỗi để dễ dàng truy cập từng chữ số
    num_str = str(num)
    # Tính số lượng chữ số
    num_digits = len(num_str)
    # Tính tổng các lũy thừa bậc num_digits của các chữ số
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    # Kiểm tra nếu tổng này bằng chính số đó
    return sum_of_powers == num

# Danh sách để lưu trữ các số Armstrong
armstrong_numbers = []

# Kiểm tra các số từ 1 đến 1000
for num in range(1, 1001):
    if is_armstrong_number(num):
        armstrong_numbers.append(num)

# In danh sách các số Armstrong từ 1 đến 1000
print(f"Các số Armstrong từ 1 đến 1000 là: {armstrong_numbers}")
