# 078 - Viết chương trình để đọc file theo từng dòng

# Đường dẫn đến file văn bản
file_path = 'example.txt'

try:
    # Mở file văn bản với chế độ đọc
    with open(file_path, 'r') as file:
        # Lặp qua từng dòng trong file
        for line in file:
            # In từng dòng ra màn hình
            print(line, end='')
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
