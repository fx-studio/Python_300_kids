# 004 - Chương trình tính tiền taxi dựa trên số km đã đi

# Hàm tính toán
def calculate_taxi_fare(km):
    if km <= 1:
        fare = 10000
    elif km <= 10:
        fare = 10000 + (km - 1) * 8500
    else:
        fare = 10000 + 9 * 8500 + (km - 10) * 7500
    return fare

# Nhập số km từ người dùng
try:
    distance = float(input("Nhập số km đã đi: "))
    if distance < 0:
        print("Số km không hợp lệ. Vui lòng nhập số dương.")
    else:
        total_fare = calculate_taxi_fare(distance)
        print(f"Tổng tiền taxi là: {total_fare} VNĐ")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")

