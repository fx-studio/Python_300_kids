# 255 - Viết chương trình để trích xuất nội dung của một bài viết từ trang web

import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất nội dung bài viết
        # Giả định rằng nội dung bài viết nằm trong thẻ <div> với class "article-content"
        article_content = soup.find('div', class_='article-content')
        
        if article_content:
            # Trả về nội dung bài viết dưới dạng chuỗi
            return article_content.get_text(separator='\n')
        else:
            return None
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web chứa bài viết: ")
content = extract_article_content(url)
if content:
    print("Nội dung của bài viết:")
    print(content)
else:
    print("Không thể truy cập trang web hoặc không tìm thấy nội dung bài viết.")
