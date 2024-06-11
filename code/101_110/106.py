# 106 - Viết chương trình để tách các từ từ một chuỗi thành danh sách
import re

def doc_file(file_name):
    """
    Hàm để đọc nội dung từ một file văn bản.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        noi_dung = file.read()
    return noi_dung

# Cách 1: Sử dụng hàm split() để tách chuỗi thành danh sách các từ
def tach_tu(file_name):
    """
    Hàm để tách các từ từ một chuỗi thành danh sách.
    """
    noi_dung = doc_file(file_name)
    
    # Tách chuỗi thành danh sách các từ
    danh_sach_tu = noi_dung.split()
    
    return danh_sach_tu

# Cách 2: Sử dụng regular expression
def tach_tu2(file_name):
    """
    Hàm để tách các từ từ một chuỗi thành danh sách.
    """
    noi_dung = doc_file(file_name)
    
    # Sử dụng regular expression để tách từ
    danh_sach_tu = re.findall(r'\b\w+\b', noi_dung)
    
    return danh_sach_tu

# Đường dẫn tới file văn bản
file_name = 'example.txt'

# Gọi hàm và in kết quả
danh_sach_tu = tach_tu(file_name)
print("Cách 1:")    
print(danh_sach_tu)

# Gọi hàm và in kết quả
danh_sach_tu2 = tach_tu2(file_name)
print("Cách 2:") 
print(danh_sach_tu)
