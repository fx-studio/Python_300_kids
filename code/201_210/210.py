# 210 - Viết chương trình để vẽ đồ thị histogram bằng Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo dữ liệu ngẫu nhiên
np.random.seed(0)
data = np.random.randn(1000)  # 1000 giá trị ngẫu nhiên theo phân phối chuẩn

# Vẽ đồ thị histogram
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=True, color='blue')

# Thêm tiêu đề và nhãn
plt.title('Đồ thị Histogram với dữ liệu ngẫu nhiên')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')

# Hiển thị đồ thị
plt.show()