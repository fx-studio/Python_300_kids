# 119 - Viết chương trình để in lịch của một tháng nhất định

import calendar

def in_lich_thang(nam, thang):
    """
    Hàm để in lịch của một tháng nhất định.
    """
    # Tạo đối tượng TextCalendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # In lịch của tháng
    # Lấy chuỗi lịch của tháng
    # - nam: năm
    # - thang: tháng
    # - return: 
    #   - chuỗi lịch của tháng
    #   - mỗi hàng của lịch là một tuần, bắt đầu từ thứ hai
    #   - mỗi tuần bắt đầu từ chủ nhật
    #   - mỗi ngày được in ra với độ rộng 3 ký tự
    #   - mỗi hàng có độ rộng 20 ký tự
    #   - mỗi hàng được kết thúc bởi ký tự xuống dòng
    #   - mỗi tháng bắt đầu bởi một hàng trống
    #   - mỗi tháng kết thúc bởi hai hàng trống
    # Lưu ý: Đối số thứ hai của hàm formatmonth() là thứ bắt đầu của tuần
    lich_thang = cal.formatmonth(nam, thang)
    
    # In lịch
    print(lich_thang)

# Năm và tháng đầu vào
nam = 2024
thang = 5

# Gọi hàm và in kết quả
in_lich_thang(nam, thang)
