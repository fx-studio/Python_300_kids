# 299 - Viết chương trình để cắt ảnh

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đường dẫn tới file ảnh
image_path = 'img2.jpeg'

# Đọc ảnh từ file
image = cv2.imread(image_path)

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    height, width, _ = image.shape
    
    # Kích thước hình vuông
    square_size = min(height, width) // 3
    
    # Cắt hình vuông
    square = image[:square_size, :square_size]

    # Tạo mặt nạ cho hình tròn
    mask_circle = np.zeros((height, width), dtype=np.uint8)
    center = (width // 2, height // 2)
    radius = min(center[0], center[1], height - center[1], width - center[0]) // 2
    cv2.circle(mask_circle, center, radius, 255, -1)
    
    # Ứng dụng mặt nạ hình tròn
    circle = cv2.bitwise_and(image, image, mask=mask_circle)
    circle = circle[center[1] - radius:center[1] + radius, center[0] - radius:center[0] + radius]

    # Tạo mặt nạ cho hình tam giác
    mask_triangle = np.zeros((height, width), dtype=np.uint8)
    points = np.array([[width // 2, height // 4], [width // 4, 3 * height // 4], [3 * width // 4, 3 * height // 4]])
    cv2.drawContours(mask_triangle, [points], 0, 255, -1)
    
    # Ứng dụng mặt nạ hình tam giác
    triangle = cv2.bitwise_and(image, image, mask=mask_triangle)
    triangle = triangle[height // 4:3 * height // 4, width // 4:3 * width // 4]

    # Hiển thị ảnh gốc và ảnh đã cắt
    plt.figure(figsize=(10, 10))

    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 2)
    plt.title('Square')
    plt.imshow(cv2.cvtColor(square, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 3)
    plt.title('Circle')
    plt.imshow(cv2.cvtColor(circle, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 2, 4)
    plt.title('Triangle')
    plt.imshow(cv2.cvtColor(triangle, cv2.COLOR_BGR2RGB))

    plt.show()
else:
    print("Failed to load image. Check the input path and file format.")