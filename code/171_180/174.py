# 174 - Viết chương trình để tạo một decorator gọi một hàm nhiều lần

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(10)
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()