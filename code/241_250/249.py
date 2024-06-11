# 249 - Viết chương trình để lấy dữ liệu thời tiết từ API

import requests

# Bước 2: Định nghĩa hàm để gửi yêu cầu HTTP đến API và lấy dữ liệu thời tiết
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'vi'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Request error occurred: {req_err}"}

# Bước 3: Định nghĩa URL của API và các cấu hình khác
api_key = "your_api_key_here"  # Thay thế bằng API key của bạn
cities = ["Hanoi", "Ho Chi Minh City", "Da Nang", "Hue", "Can Tho"]

# Bước 4: Gửi yêu cầu đến API cho mỗi thành phố và xử lý phản hồi
for city in cities:
    weather_data = get_weather(city, api_key)
    if 'error' in weather_data:
        print(f"Lỗi khi lấy dữ liệu thời tiết cho {city}: {weather_data['error']}")
    else:
        print(f"Thời tiết tại {city}:")
        print(f"Nhiệt độ: {weather_data['main']['temp']}°C")
        print(f"Mô tả: {weather_data['weather'][0]['description']}")
        print("-----------")
