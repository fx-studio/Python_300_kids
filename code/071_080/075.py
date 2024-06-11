# 075 - Viết chương trình để đếm số ký tự trong một file văn bản

# Đường dẫn đến file văn bản
file_path = 'example.txt'

try:
    # Mở file văn bản với chế độ đọc
    with open(file_path, 'r') as file:
        # Đọc toàn bộ nội dung của file
        content = file.read()
        # Lọc bỏ các ký tự khoảng trắng và xuống dòng
        filtered_content = ''.join(c for c in content if c not in (' ', '\n', '\t'))
        # Đếm số lượng ký tự trong nội dung đã lọc
        char_count = len(filtered_content)
        # In số lượng ký tự
        print(f"Số lượng ký tự trong file (bỏ qua khoảng trắng và xuống dòng): {char_count}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
