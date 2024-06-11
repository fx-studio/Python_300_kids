# 206 - Viết chương trình để vẽ đồ thị thanh ngang bằng Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo dữ liệu ngẫu nhiên
np.random.seed(0)  # Đặt seed cho tính ngẫu nhiên
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 100, size=len(categories))

# Vẽ đồ thị thanh ngang
plt.barh(categories, values, color='skyblue')

# Thêm tiêu đề và nhãn
plt.title('Đồ thị thanh ngang với dữ liệu ngẫu nhiên')
plt.xlabel('Giá trị')
plt.ylabel('Danh mục')

# Hiển thị đồ thị
plt.show()