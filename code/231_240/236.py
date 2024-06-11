# 236 - Viết chương trình để phân giải tên miền

import socket

def resolve_domain(domain):
    try:
        # Phân giải tên miền thành địa chỉ IP
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return f"Không thể phân giải tên miền: {e}"

# Lấy tên miền từ người dùng
domain = input("Nhập tên miền cần phân giải: ")

# Gọi hàm để phân giải tên miền
ip_address = resolve_domain(domain)
print(f"Địa chỉ IP của tên miền {domain} là: {ip_address}")
