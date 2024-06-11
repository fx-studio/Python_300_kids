# 115 - Viết chương trình để tính thời gian chênh lệch giữa hai ngày

from datetime import datetime

def tinh_thoi_gian_chenh_lech(ngay1, ngay2, dinh_dang):
    """
    Hàm để tính thời gian chênh lệch giữa hai ngày.
    """
    # Chuyển đổi chuỗi ngày tháng thành đối tượng datetime
    ngay1_obj = datetime.strptime(ngay1, dinh_dang)
    ngay2_obj = datetime.strptime(ngay2, dinh_dang)
    
    # Tính toán chênh lệch thời gian
    chenh_lech = ngay2_obj - ngay1_obj
    
    return chenh_lech

# Ngày tháng đầu vào
ngay1 = "01-01-2023"
ngay2 = "24-05-2024"
dinh_dang = "%d-%m-%Y"

# Gọi hàm và in kết quả
chenh_lech = tinh_thoi_gian_chenh_lech(ngay1, ngay2, dinh_dang)
print("Chênh lệch thời gian giữa hai ngày là:", chenh_lech)
