# 111 - Viết chương trình để lấy ngày và giờ hiện tại

from datetime import datetime

def lay_ngay_gio_hien_tai():
    """
    Hàm để lấy ngày và giờ hiện tại.
    """
    # Lấy thời gian hiện tại
    hien_tai = datetime.now()
    
    # Định dạng ngày và giờ hiện tại
    ngay_gio_hien_tai = hien_tai.strftime("%Y-%m-%d %H:%M:%S")
    return ngay_gio_hien_tai

# Gọi hàm và in kết quả
print("Ngày và giờ hiện tại là:", lay_ngay_gio_hien_tai())
