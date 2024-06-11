# 109 - Viết chương trình để loại bỏ các ký tự đặc biệt khỏi chuỗi

import re

def loai_bo_ky_tu_dac_biet(chuoi):
    """
    Hàm để loại bỏ các ký tự đặc biệt khỏi chuỗi, chỉ giữ lại chữ cái và số.
    """
    chuoi_ket_qua = re.sub(r'[^A-Za-z0-9]', '', chuoi)
    return chuoi_ket_qua

# Chuỗi ban đầu chứa các ký tự đặc biệt
chuoi_ban_dau = "Hello, World! Đây là một chuỗi #123 với ký tự đặc biệt @2024."

# Gọi hàm và in kết quả
chuoi_ket_qua = loai_bo_ky_tu_dac_biet(chuoi_ban_dau)
print(chuoi_ket_qua)
