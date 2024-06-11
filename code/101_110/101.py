# 101 - Viết chương trình để đếm số từ trong một chuỗi

def dem_so_tu(chuoi):
    """
    Hàm này nhận vào một chuỗi và trả về số từ trong chuỗi đó.
    """
    # Tách chuỗi thành danh sách các từ
    danh_sach_tu = chuoi.split()
    
    # Đếm số từ trong danh sách
    so_tu = len(danh_sach_tu)
    
    return so_tu

# Nhập chuỗi từ người dùng
chuoi = input("Nhập một chuỗi: ")

# Gọi hàm và in kết quả
so_tu = dem_so_tu(chuoi)
print(f"Số từ trong chuỗi là: {so_tu}")
