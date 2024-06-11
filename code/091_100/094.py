# 094 - Viết chương trình để bắt lỗi khi chuyển đổi kiểu dữ liệu không hợp lệ

try:
    value = int('abc')
except ValueError:
    value = "Error: Invalid type conversion!"

print(value)