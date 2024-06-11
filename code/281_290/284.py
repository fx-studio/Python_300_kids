# 284 - Viết chương trình để vẽ biểu đồ boxplot của một danh sách số

import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplot(numbers):
    sns.boxplot(data=numbers)
    plt.title('Boxplot')
    plt.xlabel('Value')
    plt.show()

# Ví dụ sử dụng
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8]
plot_boxplot(numbers)
