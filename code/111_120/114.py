# 114 - Viết chương trình để chuyển đổi định dạng ngày tháng

from datetime import datetime

def chuyen_doi_dinh_dang_ngay_thang(ngay_thang, dinh_dang_cu, dinh_dang_moi):
    """
    Hàm để chuyển đổi định dạng ngày tháng.
    """
    # Chuyển đổi chuỗi ngày tháng thành đối tượng datetime
    ngay_thang_obj = datetime.strptime(ngay_thang, dinh_dang_cu)
    
    # Chuyển đổi đối tượng datetime thành chuỗi theo định dạng mới
    ngay_thang_moi = ngay_thang_obj.strftime(dinh_dang_moi)
    
    return ngay_thang_moi

# Định dạng cũ và mới
ngay_thang_cu = "24-05-2024"
dinh_dang_cu = "%d-%m-%Y"
dinh_dang_moi = "%Y/%m/%d"

# Gọi hàm và in kết quả
ngay_thang_moi = chuyen_doi_dinh_dang_ngay_thang(ngay_thang_cu, dinh_dang_cu, dinh_dang_moi)
print("Ngày tháng mới theo định dạng:", ngay_thang_moi)
