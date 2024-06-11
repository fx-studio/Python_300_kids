# 238 - Viết chương trình để tạo một máy khách TCP đơn giản

import socket

def start_tcp_client(host='127.0.0.1', port=65432, message="Hello, Server!"):
    # Tạo một socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Kết nối đến máy chủ với địa chỉ IP và cổng cụ thể
    client_socket.connect((host, port))
    print(f"Kết nối đến máy chủ {host}:{port}")
    
    try:
        # Gửi thông điệp đến máy chủ
        client_socket.sendall(message.encode())
        print(f"Đã gửi: {message}")
        
        # Nhận phản hồi từ máy chủ
        data = client_socket.recv(1024)
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

# Gọi hàm để bắt đầu máy khách TCP
start_tcp_client(host, port, message)
