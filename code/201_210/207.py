# 207 - Viết chương trình để vẽ đồ thị đường cong bằng Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo dữ liệu
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Vẽ đồ thị đường cong
plt.plot(x, y, label='sin(x)')

# Thêm tiêu đề và nhãn
plt.title('Đồ thị đường cong của hàm sin')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')

# Thêm chú thích
plt.legend()

# Hiển thị đồ thị
plt.show()
