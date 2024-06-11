# 241 - Viết chương trình để gửi yêu cầu GET đến API và lấy dữ liệu

import requests

# Bước 2: Định nghĩa URL của API
api_url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

# Bước 3: Gửi yêu cầu GET đến API
response = requests.get(api_url)

# Bước 4: Nhận và xử lý dữ liệu trả về từ API
if response.status_code == 200:
    data = response.json()
else:
    data = None
    print(f"Lỗi khi gửi yêu cầu GET: {response.status_code}")

# Bước 5: Hiển thị dữ liệu
if data:
    print("Dữ liệu nhận được từ API:")
    print(data)
else:
    print("Không nhận được dữ liệu từ API.")
