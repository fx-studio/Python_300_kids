# 232 - Viết chương trình để kiểm tra kết nối internet

import requests

def check_internet_connection():
    url = "http://www.google.com"
    timeout = 5
    try:
        # Gửi yêu cầu GET đến URL và thiết lập thời gian chờ
        response = requests.get(url, timeout=timeout)
        # Kiểm tra mã trạng thái của phản hồi
        if response.status_code == 200:
            print("Kết nối internet hoạt động bình thường.")
        else:
            print("Không thể kết nối internet.")
    except requests.ConnectionError:
        print("Không thể kết nối internet.")
    except requests.Timeout:
        print("Yêu cầu kết nối internet đã bị quá thời gian chờ.")

# Gọi hàm kiểm tra kết nối internet
check_internet_connection()
