# 233 - Viết chương trình để kiểm tra tốc độ internet

import speedtest

def check_internet_speed():
    # Khởi tạo đối tượng Speedtest
    st = speedtest.Speedtest()
    
    # Chọn máy chủ tốt nhất dựa trên ping
    st.get_best_server()
    
    # Đo tốc độ tải xuống
    download_speed = st.download()
    
    # Đo tốc độ tải lên
    upload_speed = st.upload()
    
    # Đo độ trễ (ping)
    ping = st.results.ping
    
    # Chuyển đổi tốc độ từ bps sang Mbps
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000
    
    # In kết quả
    print(f"Tốc độ tải xuống: {download_speed_mbps:.2f} Mbps")
    print(f"Tốc độ tải lên: {upload_speed_mbps:.2f} Mbps")
    print(f"Độ trễ (ping): {ping:.2f} ms")

# Gọi hàm kiểm tra tốc độ internet
check_internet_speed()
