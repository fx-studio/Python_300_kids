## 256 - Viết chương trình để trích xuất tất cả các đoạn văn từ trang web

import requests
from bs4 import BeautifulSoup

def extract_paragraphs(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tất cả các đoạn văn
        paragraphs = []
        for p in soup.find_all('p'):
            paragraphs.append(p.get_text())
        
        # Trả về danh sách các đoạn văn
        return paragraphs
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web: ")
paragraphs = extract_paragraphs(url)
if paragraphs:
    print("Các đoạn văn trên trang web:")
    for p in paragraphs:
        print(p)
else:
    print("Không thể truy cập trang web hoặc không tìm thấy đoạn văn.")
