# 260 - Viết chương trình để trích xuất tất cả các thẻ meta từ trang web

import requests
from bs4 import BeautifulSoup

def extract_meta_tags(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tất cả các thẻ meta
        meta_tags = []
        for meta in soup.find_all('meta'):
            meta_tags.append(meta.attrs)
        
        # Trả về danh sách các thẻ meta
        return meta_tags
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web: ")
meta_tags = extract_meta_tags(url)
if meta_tags:
    print("Các thẻ meta trên trang web:")
    for i, meta in enumerate(meta_tags):
        print(f"Thẻ meta {i+1}: {meta}")
else:
    print("Không thể truy cập trang web hoặc không tìm thấy thẻ meta.")
