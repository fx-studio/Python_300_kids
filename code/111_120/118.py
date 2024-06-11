# 118 - Viết chương trình để tính số giây từ thời gian hiện tại đến một thời gian nhất định

from datetime import datetime

def tinh_so_giay_den_thoi_gian_dich(thoi_gian_dich, dinh_dang):
    """
    Hàm để tính số giây từ thời gian hiện tại đến một thời gian nhất định.
    """
    # Lấy thời gian hiện tại
    thoi_gian_hien_tai = datetime.now()
    
    # Chuyển đổi chuỗi thời gian của thời gian đích thành đối tượng datetime
    thoi_gian_dich_obj = datetime.strptime(thoi_gian_dich, dinh_dang)
    
    # Tính toán chênh lệch thời gian
    chenh_lech = thoi_gian_dich_obj - thoi_gian_hien_tai
    
    return chenh_lech.total_seconds()

# Thời gian đích đầu vào
thoi_gian_dich = "31-12-2024 23:59:59"
dinh_dang = "%d-%m-%Y %H:%M:%S"

# Gọi hàm và in kết quả
so_giay = tinh_so_giay_den_thoi_gian_dich(thoi_gian_dich, dinh_dang)
print("Số giây từ thời gian hiện tại đến thời gian đích là:", so_giay)
