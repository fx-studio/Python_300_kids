# 300 - Viết chương trình để xoay ảnh

from PIL import Image
from matplotlib import pyplot as plt

# Đường dẫn tới file ảnh
image_path = 'img2.jpeg'

# Đọc ảnh từ file
image = Image.open(image_path)

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    def rotate_image(image, angle):
        return image.rotate(angle, expand=True)

    # Xoay ảnh với các góc khác nhau
    angles = [30, 60, 90, 180]
    rotated_images = [rotate_image(image, angle) for angle in angles]

    # Hiển thị ảnh gốc và ảnh đã xoay
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.title('Original Image')
    plt.imshow(image)

    for i, angle in enumerate(angles):
        plt.subplot(2, 3, i+2)
        plt.title(f'Rotated {angle} degrees')
        plt.imshow(rotated_images[i])

    plt.show()
else:
    print("Failed to load image. Check the input path and file format.")