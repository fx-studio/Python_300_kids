# 071 - Viết chương trình để đọc nội dung của một file văn bản

# Đường dẫn đến file văn bản
file_path = 'example.txt'

try:
    # Mở file văn bản với chế độ đọc
    with open(file_path, 'r') as file:
        # Đọc toàn bộ nội dung của file
        content = file.read()
        # In nội dung của file
        print("Nội dung của file:")
        print(content)
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")