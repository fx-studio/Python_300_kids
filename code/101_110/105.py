# 105 - Viết chương trình để tìm từ xuất hiện nhiều nhất trong một chuỗi.
from collections import Counter

def doc_file(file_name):
    """
    Hàm để đọc nội dung từ một file văn bản.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        noi_dung = file.read()
    return noi_dung

# Cách 1: Sử dụng từ điển để đếm số lần xuất hiện của từng từ
def tim_tu_xuat_hien_nhieu_nhat(file_name):
    """
    Hàm để tìm từ xuất hiện nhiều nhất trong một file văn bản.
    """
    noi_dung = doc_file(file_name)
    
    # Tách chuỗi thành danh sách các từ
    danh_sach_tu = noi_dung.split()
    
    # Sử dụng từ điển để đếm số lần xuất hiện của từng từ
    tu_dem = {}
    for tu in danh_sach_tu:
        tu = tu.lower().strip('.,!?:;()[]')  # Chuyển về chữ thường và loại bỏ dấu câu
        if tu in tu_dem:
            tu_dem[tu] += 1
        else:
            tu_dem[tu] = 1
    
    # Tìm từ xuất hiện nhiều nhất
    tu_nhieu_nhat = max(tu_dem, key=tu_dem.get)
    
    return tu_nhieu_nhat, tu_dem[tu_nhieu_nhat]

# Cách 2: Sử dụng Counter
def tim_tu_xuat_hien_nhieu_nhat2(file_name):
    """
    Hàm để tìm từ xuất hiện nhiều nhất trong một file văn bản.
    """
    noi_dung = doc_file(file_name)
    
    # Tách chuỗi thành danh sách các từ
    danh_sach_tu = noi_dung.split()
    
    # Chuyển các từ về chữ thường và loại bỏ dấu câu
    danh_sach_tu = [tu.lower().strip('.,!?:;()[]') for tu in danh_sach_tu]
    
    # Sử dụng Counter để đếm số lần xuất hiện của từng từ
    tu_dem = Counter(danh_sach_tu)
    
    # Tìm từ xuất hiện nhiều nhất
    tu_nhieu_nhat, so_lan_xuat_hien = tu_dem.most_common(1)[0]
    
    return tu_nhieu_nhat, so_lan_xuat_hien


# Đường dẫn tới file văn bản
file_name = 'example.txt'

# Gọi hàm và in kết quả
tu_nhieu_nhat, so_lan_xuat_hien = tim_tu_xuat_hien_nhieu_nhat(file_name)
print(f"Cách 1: Từ xuất hiện nhiều nhất là: '{tu_nhieu_nhat}' với {so_lan_xuat_hien} lần xuất hiện")


# Gọi hàm và in kết quả
tu_nhieu_nhat, so_lan_xuat_hien = tim_tu_xuat_hien_nhieu_nhat2(file_name)
print(f"Cách 2: Từ xuất hiện nhiều nhất là: '{tu_nhieu_nhat}' với {so_lan_xuat_hien} lần xuất hiện")
