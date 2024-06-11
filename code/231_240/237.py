# 237 - Viết chương trình để tạo một máy chủ TCP đơn giản

import socket

def start_tcp_server(host='127.0.0.1', port=65432):
    # Tạo một socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Gán socket đến một địa chỉ IP và một cổng
    server_socket.bind((host, port))
    
    # Đặt socket ở trạng thái lắng nghe các kết nối đến
    server_socket.listen()
    print(f"Máy chủ TCP đang lắng nghe tại {host}:{port}...")
    
    while True:
        # Chấp nhận kết nối từ máy khách
        client_socket, client_address = server_socket.accept()
        print(f"Đã kết nối với {client_address}")
        
        with client_socket:
            while True:
                # Nhận dữ liệu từ máy khách
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Nhận được từ {client_address}: {data.decode()}")
                
                # Phản hồi lại cho máy khách
                client_socket.sendall(data)

# Bắt đầu máy chủ TCP
start_tcp_server()
