# 176 - Viết chương trình để tạo một decorator kiểm tra thời gian thực thi của một hàm

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Lấy thời gian bắt đầu
        result = func(*args, **kwargs)  # Gọi hàm gốc
        end_time = time.time()  # Lấy thời gian kết thúc
        execution_time = end_time - start_time  # Tính toán thời gian thực thi
        print(f"Function {func.__name__} took {execution_time:.6f} seconds to execute")
        return result
    return wrapper

@timing_decorator
def example_function():
    #time.sleep(2)  # Giả lập một công việc tốn thời gian
    for _ in range(1000000): # Giả lập một công việc tốn thời gian
        pass
    return "Function execution complete"

# Calling the decorated function
print(example_function())