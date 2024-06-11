# 202 - Viết chương trình để vẽ đồ thị cột bằng Matplotlib

import matplotlib.pyplot as plt

# Khởi tạo dữ liệu
x = ['A', 'B', 'C', 'D', 'E']
y = [5, 7, 3, 8, 4]

# Vẽ đồ thị cột
plt.bar(x, y, color='blue')

# Thêm tiêu đề và nhãn
plt.title('Đồ thị cột đơn giản')
plt.xlabel('Danh mục')
plt.ylabel('Giá trị')

# Hiển thị lưới
plt.grid(True, axis='y')

# Hiển thị đồ thị
plt.show()