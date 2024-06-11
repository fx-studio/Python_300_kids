# 257 - Viết chương trình để trích xuất tất cả các bảng từ trang web

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_tables(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tất cả các bảng
        tables = []
        for table in soup.find_all('table'):
            # Chuyển đổi bảng HTML thành DataFrame của pandas
            df = pd.read_html(str(table))[0]
            tables.append(df)
        
        # Trả về danh sách các bảng
        return tables
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web: ")
tables = extract_tables(url)
if tables:
    print("Các bảng trên trang web:")
    for i, table in enumerate(tables):
        print(f"Bảng {i+1}:")
        print(table)
else:
    print("Không thể truy cập trang web hoặc không tìm thấy bảng.")
