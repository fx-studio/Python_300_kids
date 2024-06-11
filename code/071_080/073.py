# 073 - Viết chương trình để đếm số dòng trong một file văn bản

# Đường dẫn đến file văn bản
file_path = 'example.txt'

try:
    # Mở file văn bản với chế độ đọc
    with open(file_path, 'r') as file:
        # Đếm số lượng dòng trong file
        line_count = sum(1 for line in file)
        # In số lượng dòng
        print(f"Số lượng dòng trong file: {line_count}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
