# 281 - Viết chương trình để tính trung bình, median và mode của một danh sách số

import statistics

def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    try:
        mode = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode = "No unique mode"
    
    return mean, median, mode

# Ví dụ sử dụng
numbers = [1, 2, 2, 3, 4]
mean, median, mode = calculate_statistics(numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
