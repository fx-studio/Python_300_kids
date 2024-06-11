# 298 - Viết chương trình để thay đổi kích thước ảnh

import cv2
from matplotlib import pyplot as plt

# Đường dẫn tới file ảnh
image_path = 'img2.jpeg'

# Đọc ảnh từ file
image = cv2.imread(image_path)

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    # Kích thước mới (chiều rộng và chiều cao)
    new_width = 800
    new_height = 600

    # Thay đổi kích thước ảnh
    resized_image = cv2.resize(image, (new_width, new_height))

    # Hiển thị ảnh gốc và ảnh đã thay đổi kích thước
    plt.figure(figsize=(10, 10))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 2, 2)
    plt.title('Resized Image')
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

    plt.show()
else:
    print("Failed to load image. Check the input path and file format.")