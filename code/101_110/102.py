# 102 - Viết chương trình để đếm số ký tự trong một chuỗi

def dem_so_ky_tu_1(chuoi):
    """
    Hàm này sử dụng hàm len() để đếm số ký tự trong chuỗi.
    """
    return len(chuoi)

def dem_so_ky_tu_2(chuoi):
    """
    Hàm này sử dụng vòng lặp để đếm số ký tự trong chuỗi.
    """
    dem = 0
    for ky_tu in chuoi:
        dem += 1
    return dem

# Nhập chuỗi từ người dùng
chuoi = input("Nhập một chuỗi: ")

# Gọi hàm và in kết quả
so_ky_tu = dem_so_ky_tu_1(chuoi)
print(f"Số ký tự trong chuỗi (cách 1) là: {so_ky_tu}")

# Gọi hàm và in kết quả
so_ky_tu = dem_so_ky_tu_2(chuoi)
print(f"Số ký tự trong chuỗi (cách 2) là: {so_ky_tu}")


