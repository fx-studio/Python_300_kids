# 091 - Viết chương trình để bắt lỗi chia cho 0

# try / except with ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Error: Division by zero is not allowed!"

print(result)

# Function
def safe_division(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"

print(safe_division(10, 0))