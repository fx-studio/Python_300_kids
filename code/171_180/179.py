# 179 - Viết chương trình để tạo một decorator nhận một đối số từ bên ngoài

def multiply(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return n * func(*args, **kwargs)
        return wrapper
    return decorator

@multiply(3)
def add(a, b):
    return a + b

# input from user
a = int(input("Enter a : "))
b = int(input("Enter b: "))
print(add(a, b))  # Output: (a + b) * 3