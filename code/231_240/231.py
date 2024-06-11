# 231 - Viết chương trình để tải xuống một tệp từ internet

import requests

def download_file(url, local_filename):
    # Gửi yêu cầu HTTP GET đến URL
    with requests.get(url, stream=True) as r:
        # Kiểm tra mã trạng thái của phản hồi
        r.raise_for_status()
        # Mở tệp cục bộ để ghi
        with open(local_filename, 'wb') as f:
            # Ghi dữ liệu vào tệp theo từng khối (chunk)
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# # Nhận URL từ người dùng
# url = input("Nhập URL của tệp cần tải xuống: ")
# local_filename = url.split('/')[-1]  # Tạo tên tệp cục bộ từ URL

# URL của tệp bạn muốn tải xuống
url = 'https://filesamples.com/samples/document/txt/sample3.txt'
# Tên tệp lưu trữ trên máy local
local_filename = 'downloaded_sample3.txt'

# Gọi hàm để tải tệp xuống
try:
    download_file(url, local_filename)
    print(f"Tệp đã được tải xuống thành công và lưu tại: {local_filename}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
