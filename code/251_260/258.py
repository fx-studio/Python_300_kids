# 258 - Viết chương trình để trích xuất tất cả các tiêu đề từ trang web

import requests
from bs4 import BeautifulSoup

def extract_headings(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tất cả các tiêu đề
        headings = []
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            headings.append(heading.get_text().strip())
        
        # Trả về danh sách các tiêu đề
        return headings
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web: ")
headings = extract_headings(url)
if headings:
    print("Các tiêu đề trên trang web:")
    for heading in headings:
        print(heading)
else:
    print("Không thể truy cập trang web hoặc không tìm thấy tiêu đề.")
