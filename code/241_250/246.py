# 246 - Viết chương trình để xử lý lỗi khi gọi API

import requests
from requests.exceptions import HTTPError, Timeout, RequestException

# Bước 2: Định nghĩa hàm để gửi yêu cầu HTTP và xử lý lỗi
def send_request(method, url, **kwargs):
    try:
        if method.upper() == 'GET':
            response = requests.get(url, **kwargs)
        elif method.upper() == 'POST':
            response = requests.post(url, **kwargs)
        elif method.upper() == 'PUT':
            response = requests.put(url, **kwargs)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, **kwargs)
        else:
            raise ValueError("Phương thức HTTP không hợp lệ")

        # Kiểm tra mã trạng thái HTTP
        response.raise_for_status()
        
        # Trả về nội dung phản hồi JSON nếu có
        if response.content:
            return response.json()
        return {"message": "Thành công nhưng không có nội dung trả về."}
    
    except HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Timeout as timeout_err:
        return {"error": f"Timeout error occurred: {timeout_err}"}
    except RequestException as req_err:
        return {"error": f"Request error occurred: {req_err}"}
    except ValueError as val_err:
        return {"error": f"Value error occurred: {val_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}

# Bước 3: Định nghĩa URL của API và các cấu hình khác
api_url = "https://api.example.com/data/1"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload = {
    "key1": "value1",
    "key2": "value2"
}

# Bước 4: Gửi yêu cầu đến API và xử lý phản hồi
method = 'PUT'  # Hoặc 'GET', 'POST', 'DELETE'
response = send_request(method, api_url, headers=headers, json=payload)

# Bước 5: Hiển thị kết quả hoặc thông báo lỗi
print(response)
