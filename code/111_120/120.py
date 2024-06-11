# 120 - Viết chương trình để in lịch của một năm nhất định

import calendar

def in_lich_nam(nam):
    """
    Hàm để in lịch của một năm nhất định.
    """
    # Tạo đối tượng TextCalendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # In lịch của năm
    lich_nam = cal.formatyear(nam)
    print(lich_nam)

# Năm đầu vào
nam = 2024

# Gọi hàm và in kết quả
in_lich_nam(nam)
