# 178 - Viết chương trình để tạo một decorator chuyển đổi giá trị trả về thành một kiểu dữ liệu khác

def convert_return_type(target_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Gọi hàm gốc
            try:
                converted_result = target_type(result)  # Chuyển đổi giá trị trả về
                return converted_result
            except (ValueError, TypeError) as e:
                print(f"Conversion error: {e}")
                return result  # Trả về giá trị gốc nếu chuyển đổi thất bại
        return wrapper
    return decorator

@convert_return_type(str)
def example_function():
    return 123

@convert_return_type(list)
def example_function_list():
    return 'abc'

# Calling the decorated functions
result1 = example_function()
print(f"Result: {result1} & {type(result1)}")  # Kết quả sẽ là chuỗi "123"

result2 = example_function_list()
print(f"Result: {result2} & {type(result2)}")  # Kết quả sẽ là list ['a', 'b', 'c']
