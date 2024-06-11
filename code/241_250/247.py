# 247 - Viết chương trình để kiểm tra trạng thái của API

import requests
from requests.exceptions import HTTPError, Timeout, RequestException

# Bước 2: Định nghĩa URL của API
api_url = "https://api.example.com/health"
headers = {
    "Accept": "application/json"
}

# Bước 3: Gửi yêu cầu GET đến API và xử lý lỗi
def check_api_status(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return {
            "status": "success",
            "status_code": response.status_code,
            "message": "API is working normally."
        }
    except HTTPError as http_err:
        return {
            "status": "error",
            "status_code": response.status_code if response else None,
            "message": f"HTTP error occurred: {http_err}"
        }
    except Timeout as timeout_err:
        return {
            "status": "error",
            "message": f"Timeout error occurred: {timeout_err}"
        }
    except RequestException as req_err:
        return {
            "status": "error",
            "message": f"Request error occurred: {req_err}"
        }
    except Exception as err:
        return {
            "status": "error",
            "message": f"An error occurred: {err}"
        }

# Bước 4: Gửi yêu cầu đến API và kiểm tra trạng thái
result = check_api_status(api_url, headers=headers)

# Bước 5: Hiển thị trạng thái của API
print(result)
