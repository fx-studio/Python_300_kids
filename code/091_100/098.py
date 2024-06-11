# 098 - Viết chương trình để bắt nhiều lỗi cùng lúc

def catch_multiple_exceptions(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    except TypeError as e:
        print("Caught an exception:", e)

catch_multiple_exceptions(10, 0)
catch_multiple_exceptions(10, "zero")