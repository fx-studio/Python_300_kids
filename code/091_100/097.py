# 097 - Viết chương trình để sử dụng khối lệnh try-except-finally

def try_except_finally():
    try:
        print("Trying to divide by zero...")
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    finally:
        print("This is the finally block.")

try_except_finally()