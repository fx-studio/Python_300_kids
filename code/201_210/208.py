# 208 - Viết chương trình để vẽ đồ thị 3D bằng Matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Khởi tạo dữ liệu ngẫu nhiên
np.random.seed(0)
x1 = np.random.rand(100)
y1 = np.random.rand(100)
z1 = np.random.rand(100)

x2 = np.random.rand(100)
y2 = np.random.rand(100)
z2 = np.random.rand(100)

x3 = np.random.rand(100)
y3 = np.random.rand(100)
z3 = np.random.rand(100)

# Tạo figure và 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ các dữ liệu lên đồ thị 3D
ax.scatter(x1, y1, z1, c='r', marker='o', label='Dữ liệu 1')
ax.scatter(x2, y2, z2, c='g', marker='^', label='Dữ liệu 2')
ax.scatter(x3, y3, z3, c='b', marker='s', label='Dữ liệu 3')

# Thêm tiêu đề và nhãn trục
ax.set_title('Đồ thị 3D với ba loại dữ liệu khác nhau')
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.set_zlabel('Trục Z')

# Thêm chú thích
ax.legend()

# Hiển thị đồ thị
plt.show()
