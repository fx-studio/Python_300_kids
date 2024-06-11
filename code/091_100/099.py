# 099 - Viết chương trình để bắt lỗi và tiếp tục thực hiện các lệnh khác

def catch_error_and_continue():
    try:
        print("Trying to divide by zero...")
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught an exception:", e)

    print("This is a statement after the try/except block.")

catch_error_and_continue()