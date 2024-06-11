# 240 - Viết chương trình để tạo một máy khách UDP đơn giản

import socket

def start_udp_client(host='127.0.0.1', port=65432, message="Hello, Server!"):
    # Tạo một socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Gửi thông điệp đến máy chủ
        client_socket.sendto(message.encode(), (host, port))
        print(f"Đã gửi: {message} đến {host}:{port}")
        
        # Nhận phản hồi từ máy chủ
        data, server = client_socket.recvfrom(1024)
        print(f"Phản hồi từ máy chủ: {data.decode()}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
    finally:
        # Đóng kết nối
        client_socket.close()
        print("Đã đóng kết nối")

# Lấy địa chỉ IP, cổng và thông điệp từ người dùng
host = input("Nhập địa chỉ IP của máy chủ: ")
port = int(input("Nhập cổng của máy chủ: "))
message = input("Nhập thông điệp cần gửi: ")

# Gọi hàm để bắt đầu máy khách UDP
start_udp_client(host, port, message)
