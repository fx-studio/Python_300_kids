# 239 - Viết chương trình để tạo một máy chủ UDP đơn giản

import socket

def start_udp_server(host='127.0.0.1', port=65432):
    # Tạo một socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Gán socket đến một địa chỉ IP và một cổng
    server_socket.bind((host, port))
    print(f"Máy chủ UDP đang lắng nghe tại {host}:{port}...")
    
    while True:
        # Nhận dữ liệu từ máy khách
        data, client_address = server_socket.recvfrom(1024)
        print(f"Nhận được từ {client_address}: {data.decode()}")
        
        # Phản hồi lại cho máy khách
        response = f"Đã nhận được: {data.decode()}"
        server_socket.sendto(response.encode(), client_address)

# Bắt đầu máy chủ UDP
start_udp_server()
