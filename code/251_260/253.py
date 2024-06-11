# 253 - Viết chương trình để trích xuất tất cả các liên kết từ trang web

import requests
from bs4 import BeautifulSoup

def extract_links(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tất cả các liên kết
        links = []
        for link in soup.find_all('a', href=True):
            links.append(link['href'])
        
        # Trả về danh sách các liên kết
        return links
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web: ")
links = extract_links(url)
if links:
    print("Các liên kết trên trang web:")
    for link in links:
        print(link)
else:
    print("Không thể truy cập trang web hoặc trang web không có liên kết.")
