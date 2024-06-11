# 113 - Viết chương trình để lấy thời gian hiện tại

from datetime import datetime

def lay_thoi_gian_hien_tai():
    """
    Hàm để lấy thời gian hiện tại theo định dạng 24 giờ và 12 giờ (AM/PM).
    """
    # Lấy thời gian hiện tại
    hien_tai = datetime.now()
    
    # Định dạng thời gian theo kiểu 24 giờ
    thoi_gian_24h = hien_tai.strftime("%H:%M:%S")
    
    # Định dạng thời gian theo kiểu 12 giờ (AM/PM)
    thoi_gian_12h = hien_tai.strftime("%I:%M:%S %p")
    
    return thoi_gian_24h, thoi_gian_12h

# Gọi hàm và in kết quả
thoi_gian_24h, thoi_gian_12h = lay_thoi_gian_hien_tai()
print("Thời gian hiện tại theo kiểu 24 giờ:", thoi_gian_24h)
print("Thời gian hiện tại theo kiểu 12 giờ (AM/PM):", thoi_gian_12h)
