# 103 - Viết chương trình để đếm số câu trong một đoạn văn

import re

# Cách 1: Sử dụng regex
def dem_so_cau_1(doan_van):
    """
    Hàm này sử dụng regex để tách đoạn văn thành các câu và đếm số câu.
    """
    # Sử dụng regex để tách đoạn văn thành các câu
    cau = re.split(r'[.?!]', doan_van)
    # Loại bỏ các phần tử rỗng
    cau = [c for c in cau if c.strip()]
    return len(cau)

# Cách 2: Sử dụng vòng lặp
def dem_so_cau_2(doan_van):
    """
    Hàm này duyệt qua từng ký tự trong đoạn văn và đếm số dấu câu để xác định số câu.
    """
    so_cau = 0
    dau_cau = {'.', '?', '!'}
    
    for ky_tu in doan_van:
        if ky_tu in dau_cau:
            so_cau += 1
    
    return so_cau

# Nhập đoạn văn từ người dùng
doan_van = input("Nhập một đoạn văn: ")

# Gọi hàm và in kết quả
so_cau = dem_so_cau_1(doan_van)
print(f"Số câu trong đoạn văn (cách 1) là: {so_cau}")

# Gọi hàm và in kết quả
so_cau = dem_so_cau_2(doan_van)
print(f"Số câu trong đoạn văn (cách 2) là: {so_cau}")
