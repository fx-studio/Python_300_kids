# 175 - Viết chương trình để tạo một decorator sửa đổi giá trị trả về của một hàm

def modify_return_value_decorator(func):
    def wrapper(*args, **kwargs):
        # Gọi hàm gốc và lấy giá trị trả về
        result = func(*args, **kwargs)
        # Sửa đổi giá trị trả về
        modified_result = result * 2  # Ví dụ: nhân đôi giá trị trả về
        return modified_result
    return wrapper

@modify_return_value_decorator
def get_number(num):
    return num

# Input from user
num = int(input("Enter a number: "))

# Calling the decorated function
print(get_number(num))