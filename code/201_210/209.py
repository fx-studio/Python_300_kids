# 209 - Viết chương trình để vẽ đồ thị heatmap bằng Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo dữ liệu ngẫu nhiên
np.random.seed(0) # Đặt seed cho tính ngẫu nhiên. Để mỗi lần chạy chương trình, dữ liệu ngẫu nhiên không thay đổi. 
data = np.random.rand(10, 12)

# Vẽ đồ thị heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, cmap='viridis')

# Thêm tiêu đề và nhãn
plt.title('Đồ thị Heatmap với dữ liệu ngẫu nhiên')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')

# Hiển thị đồ thị
plt.show()