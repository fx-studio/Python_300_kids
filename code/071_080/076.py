# 076 - Viết chương trình để kiểm tra một file có tồn tại không

import os

# Đường dẫn đến file cần kiểm tra
file_path = 'example.txt'

# Kiểm tra sự tồn tại của file
if os.path.isfile(file_path):
    print(f"File '{file_path}' tồn tại.")
else:
    print(f"File '{file_path}' không tồn tại.")