# 020 - Viết hàm để tính chu vi và diện tích hình chữ nhật

# Hàm tính chu vi hình chữ nhật
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Hàm tính diện tích hình chữ nhật
def rectangle_area(length, width):
    return length * width

# Nhập chiều dài và chiều rộng từ người dùng
try:
    length = float(input("Nhập chiều dài của hình chữ nhật: "))
    width = float(input("Nhập chiều rộng của hình chữ nhật: "))
    
    if length < 0 or width < 0:
        print("Chiều dài và chiều rộng phải là những số không âm.")
    else:
        perimeter = rectangle_perimeter(length, width)
        area = rectangle_area(length, width)
        print(f"Chu vi của hình chữ nhật là: {perimeter}")
        print(f"Diện tích của hình chữ nhật là: {area}")
except ValueError:
    print("Vui lòng nhập một giá trị hợp lệ cho chiều dài và chiều rộng.")
