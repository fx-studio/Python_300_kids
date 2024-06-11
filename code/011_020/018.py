# 018 - Viết hàm để chuyển đổi độ C sang độ F

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Nhập nhiệt độ tính bằng độ Celsius từ người dùng
try:
    celsius = float(input("Nhập nhiệt độ tính bằng độ Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C bằng {fahrenheit}°F")
except ValueError:
    print("Vui lòng nhập một giá trị hợp lệ cho độ Celsius.")
