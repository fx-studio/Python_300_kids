# 117 - Viết chương trình để tính số ngày từ ngày hiện tại đến một ngày nhất định

from datetime import datetime

def tinh_so_ngay_den_ngay_dich(ngay_dich, dinh_dang):
    """
    Hàm để tính số ngày từ ngày hiện tại đến một ngày nhất định.
    """
    # Lấy ngày hiện tại
    ngay_hien_tai = datetime.now()
    
    # Chuyển đổi chuỗi ngày tháng của ngày đích thành đối tượng datetime
    ngay_dich_obj = datetime.strptime(ngay_dich, dinh_dang)
    
    # Tính toán chênh lệch ngày
    chenh_lech = ngay_dich_obj - ngay_hien_tai
    
    return chenh_lech.days

# Ngày đích đầu vào
ngay_dich = "31-12-2024"
dinh_dang = "%d-%m-%Y"

# Gọi hàm và in kết quả
so_ngay = tinh_so_ngay_den_ngay_dich(ngay_dich, dinh_dang)
print("Số ngày từ ngày hiện tại đến ngày đích là:", so_ngay)
