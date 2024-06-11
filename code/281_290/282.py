# 282 - Viết chương trình để tính phương sai và độ lệch chuẩn của một danh sách số

import statistics

def calculate_variance_and_std_dev(numbers):
    variance = statistics.variance(numbers)
    std_dev = statistics.stdev(numbers)
    
    return variance, std_dev

# Ví dụ sử dụng
numbers = [1, 2, 2, 3, 4]
variance, std_dev = calculate_variance_and_std_dev(numbers)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
