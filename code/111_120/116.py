# 116 - Viết chương trình để tính thời gian chênh lệch giữa hai thời gian

from datetime import datetime

def tinh_thoi_gian_chenh_lech(thoi_gian1, thoi_gian2, dinh_dang):
    """
    Hàm để tính thời gian chênh lệch giữa hai thời gian.
    """
    # Chuyển đổi chuỗi thời gian thành đối tượng datetime
    thoi_gian1_obj = datetime.strptime(thoi_gian1, dinh_dang)
    thoi_gian2_obj = datetime.strptime(thoi_gian2, dinh_dang)
    
    # Tính toán chênh lệch thời gian
    chenh_lech = thoi_gian2_obj - thoi_gian1_obj
    
    return chenh_lech

# Thời gian đầu vào
thoi_gian1 = "14:30:00"
thoi_gian2 = "18:45:01"
dinh_dang = "%H:%M:%S"

# Gọi hàm và in kết quả
chenh_lech = tinh_thoi_gian_chenh_lech(thoi_gian1, thoi_gian2, dinh_dang)
print("Chênh lệch thời gian giữa hai thời gian là:", chenh_lech)
