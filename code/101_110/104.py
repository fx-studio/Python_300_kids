# 104 - Viết chương trình để tìm tất cả các từ dài nhất trong một chuỗi

# Cách 1: Sử dụng hàm split() để tách chuỗi thành danh sách các từ
def doc_file(file_name):
    """
    Hàm để đọc nội dung từ một file văn bản.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        noi_dung = file.read()
    return noi_dung

def tim_tu_dai_nhat(file_name):
    """
    Hàm để tìm tất cả các từ dài nhất trong một file văn bản.
    """
    noi_dung = doc_file(file_name)
    
    # Tách chuỗi thành danh sách các từ
    danh_sach_tu = noi_dung.split()
    
    # Tìm độ dài của từ dài nhất
    do_dai_max = 0
    for tu in danh_sach_tu:
        if len(tu) > do_dai_max:
            do_dai_max = len(tu)
    
    # Tìm tất cả các từ có độ dài bằng độ dài của từ dài nhất
    tu_dai_nhat = [tu for tu in danh_sach_tu if len(tu) == do_dai_max]
    
    return tu_dai_nhat

# Cách 2: Sử dụng hàm `max()` & `key`
def tim_tu_dai_nhat2(file_name):
    """
    Hàm để tìm tất cả các từ dài nhất trong một file văn bản.
    """
    noi_dung = doc_file(file_name)
    
    # Tách chuỗi thành danh sách các từ
    danh_sach_tu = noi_dung.split()
    
    # Tìm độ dài của từ dài nhất bằng hàm max với key là độ dài của từ
    do_dai_max = len(max(danh_sach_tu, key=len))
    
    # Tìm tất cả các từ có độ dài bằng độ dài của từ dài nhất
    tu_dai_nhat = [tu for tu in danh_sach_tu if len(tu) == do_dai_max]
    
    return tu_dai_nhat

# Đường dẫn tới file văn bản
file_name = 'example.txt'

# Gọi hàm và in kết quả
tu_dai_nhat = tim_tu_dai_nhat(file_name)
print(f"Cách 1: Từ dài nhất trong file là: {tu_dai_nhat}")

# Gọi hàm và in kết quả
tu_dai_nhat = tim_tu_dai_nhat2(file_name)
print(f"Cách 2: Từ dài nhất trong file là: {tu_dai_nhat}")
