# 172 - Viết chương trình để tạo một decorator chấp nhận đối số

# Ví dụ 1
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

# Calling the decorated function
print("Ví dụ 1")
say_hello()

# ================================================================================================== #
# Ví dụ 2
def multiply_by(factor):
    def multiply_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * factor
        return wrapper
    return multiply_decorator

@multiply_by(2)
def add_numbers(a, b):
    return a + b

print("Ví dụ 2")
print(add_numbers(3, 4))  # Output: 14