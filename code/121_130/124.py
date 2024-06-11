# 124 - Viết chương trình để sử dụng hàm lambda để tính lũy thừa của một số

# Định nghĩa hàm lambda để tính lũy thừa của một số
power = lambda x, y: x ** y

# Số và số mũ
number = 2
exponent = 3

# Tính lũy thừa của số
result = power(number, exponent)

print(f"{number} lũy thừa {exponent} là: {result}")