# 234 - Viết chương trình để gửi email

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Tạo đối tượng MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Gắn phần nội dung email vào đối tượng MIMEText
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Kết nối đến máy chủ SMTP của Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Đăng nhập vào tài khoản email của người gửi
        server.login(sender_email, sender_password)
        
        # Gửi email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        
        # Đóng kết nối đến máy chủ SMTP
        server.quit()
        
        print("Email đã được gửi thành công.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi gửi email: {e}")

# Lấy thông tin từ người dùng
sender_email = input("Nhập địa chỉ email người gửi: ")
sender_password = input("Nhập mật khẩu của tài khoản email người gửi: ")
recipient_email = input("Nhập địa chỉ email người nhận: ")
subject = input("Nhập tiêu đề email: ")
body = input("Nhập nội dung email: ")

# Gọi hàm để gửi email
send_email(sender_email, sender_password, recipient_email, subject, body)
