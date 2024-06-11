# 297 - Viết chương trình để lọc ảnh

# Các thư viện cần thiết
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đọc ảnh từ file
image = cv2.imread('img2.jpeg')

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    # Áp dụng bộ lọc Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Áp dụng bộ lọc Sharpening
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Chuyển đổi ảnh sang màu xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Hiển thị ảnh gốc và ảnh đã lọc
    plt.figure(figsize=(10, 10))

    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 2)
    plt.title('Gaussian Blur')
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 3)
    plt.title('Sharpened Image')
    plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 4)
    plt.title('Grayscale Image')
    plt.imshow(gray_image, cmap='gray')

    plt.show()
else:
    print("Failed to load image. Check the input path and file format.")
