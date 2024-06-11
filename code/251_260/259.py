# 259 - Viết chương trình để trích xuất tất cả các đoạn mã nguồn từ trang web

import requests
from bs4 import BeautifulSoup

def extract_code_snippets(url):
    # Gửi yêu cầu HTTP tới URL
    response = requests.get(url)
    
    # Kiểm tra mã trạng thái HTTP
    if response.status_code == 200:
        # Phân tích nội dung HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trích xuất tất cả các đoạn mã nguồn
        code_snippets = []
        for code in soup.find_all(['code', 'pre']):
            code_snippets.append(code.get_text())
        
        # Trả về danh sách các đoạn mã nguồn
        return code_snippets
    else:
        return None

# Nhập URL của trang web từ người dùng
url = input("Nhập URL của trang web: ")
code_snippets = extract_code_snippets(url)
if code_snippets:
    print("Các đoạn mã nguồn trên trang web:")
    for i, snippet in enumerate(code_snippets):
        print(f"Đoạn mã {i+1}:")
        print(snippet)
else:
    print("Không thể truy cập trang web hoặc không tìm thấy đoạn mã nguồn.")

