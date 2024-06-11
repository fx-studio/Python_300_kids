# 286 - Viết chương trình để tính ma trận tương quan của hai danh sách số

import numpy as np
import pandas as pd

def calculate_correlation_matrix(x, y):
    data = {'X': x, 'Y': y}
    df = pd.DataFrame(data)
    correlation_matrix = df.corr()
    return correlation_matrix

# Ví dụ sử dụng
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23]
correlation_matrix = calculate_correlation_matrix(x, y)
print(correlation_matrix)
