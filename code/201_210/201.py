# 201 - Viết chương trình để vẽ đồ thị đường bằng Matplotlib

import matplotlib.pyplot as plt

# Khởi tạo dữ liệu
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Vẽ đồ thị đường
plt.plot(x, y, marker='o')

# Thêm tiêu đề và nhãn
plt.title('Đồ thị đường đơn giản')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')

# Hiển thị lưới
plt.grid(True)

# Hiển thị đồ thị
plt.show()