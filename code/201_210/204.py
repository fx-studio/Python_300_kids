# 204 - Viết chương trình để vẽ đồ thị tán xạ bằng Matplotlib

import matplotlib.pyplot as plt

# Khởi tạo dữ liệu
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 100, 200, 500]  # Kích thước của các điểm
colors = ['red', 'blue', 'green', 'orange', 'purple']  # Màu sắc của các điểm

# Vẽ đồ thị tán xạ
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)

# Thêm tiêu đề và nhãn
plt.title('Đồ thị tán xạ đơn giản')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')

# Hiển thị đồ thị
plt.show()