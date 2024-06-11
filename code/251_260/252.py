# 252 - Viết chương trình để trích xuất tiêu đề của trang web

import requests
from bs4 import BeautifulSoup

def extract_title(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tiêu đề trang web
        title = soup.title.string
        
        # Trả về tiêu đề
        return title
    else:
        return None

# URL của trang web cần trích xuất tiêu đề
url = "http://example.com"
title = extract_title(url)
if title:
    print(f"Tiêu đề của trang web là: {title}")
else:
    print("Không thể truy cập trang web hoặc trang web không có tiêu đề.")
