# 095 - Viết chương trình để bắt lỗi khi đọc file không tồn tại

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "Error: File not found!"

    return content

print(read_file('non_existent_file.txt'))