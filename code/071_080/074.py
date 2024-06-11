# 074 - Viết chương trình để đếm số từ trong một file văn bản

# Đường dẫn đến file văn bản
file_path = 'example.txt'

try:
    # Mở file văn bản với chế độ đọc
    with open(file_path, 'r') as file:
        # Khởi tạo biến đếm số từ
        word_count = 0
        # Đọc từng dòng của file
        for line in file:
            # Tách dòng thành các từ và đếm số từ
            words = line.split()
            word_count += len(words)
        # In số lượng từ
        print(f"Số lượng từ trong file: {word_count}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
