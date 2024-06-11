# 108 - Viết chương trình để thay thế một từ trong chuỗi bằng từ khác

# Cách 1: Sử dụng hàm replace()
def thay_the_tu(chuoi, tu_cu, tu_moi):
    """
    Hàm để thay thế một từ trong chuỗi bằng từ khác.
    """
    chuoi_ket_qua = chuoi.replace(tu_cu, tu_moi)
    return chuoi_ket_qua

# Cách 2: Sử dụng biểu thức chính quy
import re

def thay_the_tu2(chuoi, tu_cu, tu_moi):
    """
    Hàm để thay thế một từ trong chuỗi bằng từ khác sử dụng biểu thức chính quy.
    """
    chuoi_ket_qua = re.sub(r'\b{}\b'.format(re.escape(tu_cu)), tu_moi, chuoi)
    return chuoi_ket_qua


# Chuỗi ban đầu
chuoi_ban_dau = "Đây là một ví dụ về chuỗi. Đây là một ví dụ khác."

# Từ cần thay thế và từ thay thế
tu_cu = "ví dụ"
tu_moi = "demo"

# Gọi hàm và in kết quả
chuoi_ket_qua = thay_the_tu(chuoi_ban_dau, tu_cu, tu_moi)
print(chuoi_ket_qua)

# Gọi hàm và in kết quả
chuoi_ket_qua2 = thay_the_tu2(chuoi_ban_dau, tu_cu, tu_moi)
print(chuoi_ket_qua2)

