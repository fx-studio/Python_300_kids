# 245 - Viết chương trình để gửi yêu cầu DELETE đến API và xóa dữ liệu

import requests

# Bước 2: Định nghĩa URL của API
api_url = "https://api.example.com/data/1"
headers = {
    "Accept": "application/json"
}

# Bước 3: Gửi yêu cầu DELETE đến API
response = requests.delete(api_url, headers=headers)

# Bước 4: Nhận và xử lý phản hồi từ API
if response.status_code == 200:
    print("Xóa dữ liệu thành công.")
    print("Phản hồi từ API:")
    print(response.json())
elif response.status_code == 204:
    print("Xóa dữ liệu thành công nhưng không có nội dung trả về.")
else:
    print(f"Lỗi khi gửi yêu cầu DELETE: {response.status_code}")
    print("Phản hồi từ API:")
    print(response.text)
