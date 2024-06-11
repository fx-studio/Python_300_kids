# 283 - Viết chương trình để vẽ biểu đồ phân phối của một danh sách số

import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(numbers):
    sns.histplot(numbers, kde=True)
    plt.title('Distribution Plot')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Ví dụ sử dụng
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8]
plot_distribution(numbers)
