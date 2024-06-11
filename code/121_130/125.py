# 125 - Viết chương trình để sử dụng hàm lambda để kiểm tra số chẵn lẻ

# Định nghĩa hàm lambda để kiểm tra một số là chẵn hay lẻ
is_even = lambda x: "Chẵn" if x % 2 == 0 else "Lẻ"

# Số cần kiểm tra
number = 3

# Kiểm tra số là chẵn hay lẻ
result = is_even(number)

print(f"Số {number} là: {result}")