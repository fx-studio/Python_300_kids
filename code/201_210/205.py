# 205 - Viết chương trình để vẽ đồ thị hộp bằng Matplotlib

import matplotlib.pyplot as plt

# Khởi tạo dữ liệu
data = [ [7, 8, 9, 4, 3, 6, 7, 9, 6, 5],
         [3, 5, 6, 2, 3, 6, 4, 6, 5, 4],
         [8, 9, 7, 8, 9, 5, 8, 9, 7, 6] ]

# Vẽ đồ thị hộp
plt.boxplot(data)

# Thêm tiêu đề và nhãn
plt.title('Đồ thị hộp đơn giản')
plt.xlabel('Nhóm')
plt.ylabel('Giá trị')

# Hiển thị đồ thị
plt.show()