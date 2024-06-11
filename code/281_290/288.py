# 288 - Viết chương trình để thực hiện phân tích hồi quy đa biến

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def multiple_linear_regression(X, y):
    # Chuyển đổi dữ liệu đầu vào thành mảng numpy
    X = np.array(X)
    y = np.array(y)
    
    # Khởi tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    
    # Huấn luyện mô hình
    model.fit(X, y)
    
    # Lấy hệ số hồi quy và intercept
    coefficients = model.coef_
    intercept = model.intercept_
    
    # Tính toán R-squared
    r_squared = model.score(X, y)
    
    return coefficients, intercept, r_squared

# Ví dụ sử dụng
X = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [6, 7, 8],
    [7, 8, 9],
    [8, 9, 10],
    [9, 10, 11]
]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23]

coefficients, intercept, r_squared = multiple_linear_regression(X, y)
print(f"Coefficients: {coefficients}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_squared}")
