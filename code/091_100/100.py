# 100 - Viết chương trình để bắt lỗi và ném lỗi cho hàm khác để ghi log lỗi vào file

# Hàm bắt và nem lỗi
def throw_error():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise e
    except TypeError as e:
        raise e

# Hàm ghi log lỗi vào file
def log_error():
    try:
        throw_error()
    except Exception as e:
        with open('error.txt', 'a') as f:
            f.write(str(e) + '\n')

# Gọi hàm log_error
log_error()