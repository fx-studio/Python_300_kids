# 244 - Viết chương trình để gửi yêu cầu PUT đến API và cập nhật dữ liệu

import requests

# Bước 2: Định nghĩa URL của API và dữ liệu gửi kèm
api_url = "https://api.example.com/data/1"
payload = {
    "key1": "new_value1",
    "key2": "new_value2"
}
headers = {
    "Content-Type": "application/json"
}

# Bước 3: Gửi yêu cầu PUT đến API
response = requests.put(api_url, json=payload, headers=headers)

# Bước 4: Nhận và xử lý phản hồi từ API
if response.status_code == 200:
    updated_data = response.json()
    print("Cập nhật dữ liệu thành công.")
    print("Dữ liệu đã cập nhật:")
    print(updated_data)
else:
    print(f"Lỗi khi gửi yêu cầu PUT: {response.status_code}")
    print("Phản hồi từ API:")
    print(response.text)
