# 250 - Viết chương trình để lấy dữ liệu tỷ giá hối đoái từ API

import requests

# URL của API
api_url = "https://api.exchangerate-api.com/v4/latest/USD"

# Cặp tiền tệ cần chuyển đổi
base_currency = "USD"
target_currency = "VND"

try:
    # Gửi yêu cầu HTTP GET đến API
    response = requests.get(api_url)

    # Kiểm tra nếu yêu cầu thành công (mã trạng thái 200)
    if response.status_code == 200:
        # Phân tích dữ liệu JSON nhận được từ API
        data = response.json()
        
        # Lấy tỷ giá hối đoái của cặp tiền tệ yêu cầu
        exchange_rate = data['rates'].get(target_currency)

        if exchange_rate:
            # Hiển thị tỷ giá hối đoái
            print(f"Tỷ giá hối đoái từ {base_currency} sang {target_currency} là: {exchange_rate}")
        else:
            print(f"Không tìm thấy tỷ giá hối đoái cho {target_currency}.")
    else:
        print(f"Không thể lấy dữ liệu từ API. Mã trạng thái HTTP: {response.status_code}")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
