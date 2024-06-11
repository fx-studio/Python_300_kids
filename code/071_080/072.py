# 072 - Viết chương trình để ghi nội dung vào một file văn bản

# Đường dẫn đến file văn bản
file_path = 'example_output.txt'

# Nội dung cần ghi vào file
content_to_write = "Hello, world!\nWelcome to the world of Python programming."

try:
    # Mở file văn bản với chế độ ghi
    with open(file_path, 'w') as file:
        # Ghi nội dung vào file
        file.write(content_to_write)
        # In thông báo ghi thành công
        print(f"Nội dung đã được ghi vào file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")