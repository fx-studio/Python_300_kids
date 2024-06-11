# 112 - Viết chương trình để lấy ngày hiện tại

from datetime import datetime

def lay_ngay_thang_nam_gio_phut_giay_hien_tai():
    """
    Hàm để lấy ngày, tháng, năm, giờ, phút, giây hiện tại và xuất ra từng dòng.
    """
    # Lấy thời gian hiện tại
    hien_tai = datetime.now()
    
    # Truy xuất từng thành phần ngày, tháng, năm, giờ, phút, giây
    nam = hien_tai.year
    thang = hien_tai.month
    ngay = hien_tai.day
    gio = hien_tai.hour
    phut = hien_tai.minute
    giay = hien_tai.second
    
    # In từng thành phần ra từng dòng
    print("Năm:", nam)
    print("Tháng:", thang)
    print("Ngày:", ngay)
    print("Giờ:", gio)
    print("Phút:", phut)
    print("Giây:", giay)

# Gọi hàm và in kết quả
lay_ngay_thang_nam_gio_phut_giay_hien_tai()
