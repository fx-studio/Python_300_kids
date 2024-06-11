# 235 - Viết chương trình để nhận email

import imaplib
import email
from email.header import decode_header

def receive_email(email_user, email_pass):
    # Kết nối đến máy chủ IMAP của Gmail
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    
    # Đăng nhập vào tài khoản email của người dùng
    try:
        mail.login(email_user, email_pass)
    except imaplib.IMAP4.error as e:
        print(f"Lỗi đăng nhập: {e}")
        return

    # Chọn hộp thư đến (INBOX)
    mail.select("inbox")
    
    # Tìm kiếm tất cả các email trong hộp thư đến
    status, messages = mail.search(None, "ALL")
    
    # Chuyển đổi danh sách email ID thành một danh sách các số nguyên
    email_ids = messages[0].split()
    
    # Giới hạn số lượng email cần lấy (ví dụ: 10 email gần nhất)
    num_emails = 10
    latest_email_ids = email_ids[-num_emails:]
    
    for e_id in latest_email_ids:
        # Lấy dữ liệu email
        status, data = mail.fetch(e_id, "(RFC822)")
        
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Lấy thông tin từ email
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                
                from_ = msg.get("From")
                date_ = msg.get("Date")
                
                print(f"Subject: {subject}")
                print(f"From: {from_}")
                print(f"Date: {date_}")
                print("="*50)

                # Nếu email có nhiều phần (multi-part), duyệt qua từng phần
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        
                        try:
                            # Lấy nội dung của phần hiện tại
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        
                        # In nội dung của email
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print("Body:", body)
                        elif "attachment" in content_disposition:
                            print("Email có tệp đính kèm.")
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print("Body:", body)

    # Đóng kết nối với máy chủ
    mail.logout()

# Lấy thông tin từ người dùng
email_user = input("Nhập địa chỉ email của bạn: ")
email_pass = input("Nhập mật khẩu của tài khoản email: ")

# Gọi hàm để nhận email
receive_email(email_user, email_pass)
