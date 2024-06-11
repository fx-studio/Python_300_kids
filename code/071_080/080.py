# 080 - Viết chương trình để sao chép nội dung của một file sang file khác

# Đường dẫn đến file nguồn và file đích
source_file_path = 'source.txt'
destination_file_path = 'destination.txt'

try:
    # Mở file nguồn với chế độ đọc
    with open(source_file_path, 'r') as source_file:
        # Đọc toàn bộ nội dung của file nguồn
        content = source_file.read()
    
    # Mở file đích với chế độ ghi
    with open(destination_file_path, 'w') as destination_file:
        # Ghi toàn bộ nội dung vào file đích
        destination_file.write(content)
    
    print(f"Nội dung đã được sao chép từ '{source_file_path}' sang '{destination_file_path}'.")
except FileNotFoundError:
    print(f"Không tìm thấy file: {source_file_path} hoặc {destination_file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
