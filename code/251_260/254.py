# 254 - Viết chương trình để trích xuất tất cả các hình ảnh từ trang web

import requests
from bs4 import BeautifulSoup

def extract_images(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tất cả các hình ảnh
        images = []
        for img in soup.find_all('img', src=True):
            images.append(img['src'])
        
        # Trả về danh sách các hình ảnh
        return images
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web: ")
images = extract_images(url)
if images:
    print("Các hình ảnh trên trang web:")
    for img in images:
        print(img)
else:
    print("Không thể truy cập trang web hoặc trang web không có hình ảnh.")
