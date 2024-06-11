# 285 - Viết chương trình để vẽ biểu đồ scatterplot của hai danh sách số

import matplotlib.pyplot as plt
import seaborn as sns

def plot_scatterplot(x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y)
    plt.title('Scatterplot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True)
    plt.show()

# Ví dụ sử dụng
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23]
plot_scatterplot(x, y)
