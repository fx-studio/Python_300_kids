# 251 - Viết chương trình để tải xuống trang web

import requests
from bs4 import BeautifulSoup

# Nhập URL của trang web cần tải xuống
url = input("Nhập URL của trang web cần tải xuống: ")

# Tên tệp để lưu nội dung HTML
output_file = "downloaded_page.html"

try:
    # Gửi yêu cầu HTTP GET đến URL
    response = requests.get(url)

    # Kiểm tra nếu yêu cầu thành công (mã trạng thái 200)
    if response.status_code == 200:
        # Lưu nội dung HTML vào tệp
        with open(output_file, "w", encoding='utf-8') as file:
            file.write(response.text)
        print(f"Nội dung HTML của trang web đã được lưu vào tệp '{output_file}'.")

        # Phân tích cú pháp HTML bằng BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Trích xuất và in tiêu đề trang
        page_title = soup.title.string
        print(f"Tiêu đề trang web: {page_title}")

        # Trích xuất tất cả các liên kết (links) từ trang
        links = soup.find_all('a')
        print("\nCác liên kết (links) trên trang web:")
        for link in links:
            href = link.get('href')
            text = link.get_text(strip=True)
            print(f"Text: {text}, URL: {href}")

        # Trích xuất các đoạn văn bản (paragraphs)
        paragraphs = soup.find_all('p')
        print("\nCác đoạn văn bản (paragraphs) trên trang web:")
        for p in paragraphs:
            print(p.get_text(strip=True))

    else:
        print(f"Không thể tải xuống trang web. Mã trạng thái HTTP: {response.status_code}")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
