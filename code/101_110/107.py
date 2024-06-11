# 107 - Viết chương trình để nối các từ trong danh sách thành một chuỗi

# Cách 1: Sử dụng hàm join()
def noi_tu_thanh_chuoi(danh_sach_tu):
    """
    Hàm để nối các từ trong danh sách thành một chuỗi.
    """
    chuoi_ket_qua = ' '.join(danh_sach_tu)
    return chuoi_ket_qua

# Cách 2: Sử dụng vòng lặp
def noi_tu_thanh_chuoi2(danh_sach_tu):
    """
    Hàm để nối các từ trong danh sách thành một chuỗi.
    """
    chuoi_ket_qua = ""
    for tu in danh_sach_tu:
        chuoi_ket_qua += tu + " "
    chuoi_ket_qua = chuoi_ket_qua.strip()  # Loại bỏ khoảng trắng dư thừa ở cuối chuỗi
    return chuoi_ket_qua

# Khởi tạo danh sách các từ
danh_sach_tu = ["Đây", "là", "một", "chuỗi", "các", "từ"]

# Gọi hàm và in kết quả
chuoi_ket_qua = noi_tu_thanh_chuoi(danh_sach_tu)
print(chuoi_ket_qua)

# Gọi hàm và in kết quả
chuoi_ket_qua2 = noi_tu_thanh_chuoi2(danh_sach_tu)
print(chuoi_ket_qua2)

