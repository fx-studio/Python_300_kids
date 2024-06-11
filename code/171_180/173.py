# 173 - Viết chương trình để tạo một decorator với nhiều hàm trả về

def route(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if path == "/home":
                return home(*args, **kwargs)
            elif path == "/about":
                return about(*args, **kwargs)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

def home(name):
    return f"Welcome to the home page, {name}!"

def about(name):
    return f"This is the about page. Nice to meet you, {name}!"

@route("/home")
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  # Output: Welcome to the home page, John!