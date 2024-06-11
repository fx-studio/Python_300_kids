# 079 - Viết chương trình để ghi thêm nội dung vào cuối file

# Đường dẫn đến file văn bản
file_path = 'example.txt'
# Nội dung cần ghi thêm
content_to_add = "\nThis is the new content added to the file."

try:
    # Mở file văn bản với chế độ ghi thêm
    with open(file_path, 'a') as file:
        # Ghi nội dung mới vào cuối file
        file.write(content_to_add)
    print(f"Nội dung đã được ghi thêm vào file '{file_path}'.")
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
