# 203 - Viết chương trình để vẽ đồ thị tròn bằng Matplotlib

import matplotlib.pyplot as plt

# Khởi tạo dữ liệu
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # Đẩy phần đầu tiên ra

# Vẽ đồ thị tròn
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Thêm tiêu đề
plt.title('Đồ thị tròn đơn giản')

# Hiển thị đồ thị
plt.axis('equal')  # Đảm bảo đồ thị tròn
plt.show()
