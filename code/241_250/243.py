# 243 - Viết chương trình để phân tích dữ liệu JSON từ API

import requests
import json

# Bước 2: Định nghĩa URL của API và các cấu hình khác
api_url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
headers = {
    "Accept": "application/json"
}

# Bước 3: Gửi yêu cầu GET đến API
response = requests.get(api_url, headers=headers)

# Bước 4: Nhận và xử lý dữ liệu JSON từ API
if response.status_code == 200:
    data = response.json()
else:
    data = None
    print(f"Lỗi khi gửi yêu cầu GET: {response.status_code}")

# Bước 5: Phân tích và xử lý dữ liệu JSON
def analyze_data(data):
    if data:
        # Ví dụ: tính tổng dân số qua các năm
        total_population = 0
        for item in data['data']:
            total_population += item['Population']
        return total_population
    return None

# Bước 6: Hiển thị kết quả phân tích
if data:
    result = analyze_data(data)
    if result is not None:
        print(f"Tổng dân số là: {result}")
    else:
        print("Dữ liệu không hợp lệ hoặc không có trường 'Population'")
else:
    print("Không nhận được dữ liệu từ API.")

