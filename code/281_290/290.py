# 290 - Viết chương trình để phân tích dữ liệu sử dụng Numpy

import numpy as np

def analyze_data(data):
    # Chuyển đổi dữ liệu đầu vào thành mảng numpy
    data = np.array(data)
    
    # Tính toán các giá trị thống kê cơ bản
    mean = np.mean(data)
    variance = np.var(data)
    std_deviation = np.std(data)
    median = np.median(data)
    min_value = np.min(data)
    max_value = np.max(data)
    sum_value = np.sum(data)

    return {
        "mean": mean,
        "variance": variance,
        "std_deviation": std_deviation,
        "median": median,
        "min_value": min_value,
        "max_value": max_value,
        "sum_value": sum_value
    }

# Ví dụ sử dụng
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
statistics = analyze_data(data)

print("Data Analysis Results:")
for key, value in statistics.items():
    print(f"{key}: {value}")
