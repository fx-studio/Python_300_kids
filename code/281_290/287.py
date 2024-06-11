# 287 - Viết chương trình để thực hiện phân tích hồi quy đơn giản

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def simple_linear_regression(x, y):
    # Chuyển đổi dữ liệu đầu vào thành mảng numpy và reshape để phù hợp với mô hình scikit-learn
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)
    
    # Khởi tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    
    # Huấn luyện mô hình
    model.fit(x, y)
    
    # Lấy hệ số hồi quy
    slope = model.coef_[0]
    intercept = model.intercept_
    
    # Tính toán R-squared
    r_squared = model.score(x, y)
    
    return slope, intercept, r_squared

# Ví dụ sử dụng
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23]
slope, intercept, r_squared = simple_linear_regression(x, y)
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_squared}")

# Vẽ biểu đồ
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, np.array(x) * slope + intercept, color='red', label='Regression line')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
