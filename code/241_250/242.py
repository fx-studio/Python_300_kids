# 242 - Viết chương trình để gửi yêu cầu POST đến API và lấy dữ liệu

import requests

# Bước 2: Định nghĩa URL của API và dữ liệu gửi kèm
api_url = "https://api.example.com/data"
payload = {
    "key1": "value1",
    "key2": "value2"
}
headers = {
    "Content-Type": "application/json"
}

# Bước 3: Gửi yêu cầu POST đến API
response = requests.post(api_url, json=payload, headers=headers)

# Bước 4: Nhận và xử lý dữ liệu trả về từ API
if response.status_code == 200:
    data = response.json()
else:
    data = None
    print(f"Lỗi khi gửi yêu cầu POST: {response.status_code}")

# Bước 5: Hiển thị dữ liệu
if data:
    print("Dữ liệu nhận được từ API:")
    print(data)
else:
    print("Không nhận được dữ liệu từ API.")
