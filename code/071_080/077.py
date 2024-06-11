# 077 - Viết chương trình để xóa một file văn bản

import os

# Đường dẫn đến file cần xóa
file_path = 'example_output.txt'

try:
    # Kiểm tra sự tồn tại của file
    if os.path.isfile(file_path):
        # Xóa file
        os.remove(file_path)
        print(f"File '{file_path}' đã được xóa.")
    else:
        print(f"File '{file_path}' không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
