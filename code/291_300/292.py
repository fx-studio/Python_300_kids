# 292 - Viết chương trình để hiển thị một ảnh

from PIL import Image  # Thư viện Pillow để xử lý ảnh

# Đường dẫn tới file ảnh
image_path = 'img2.jpeg'

# Đọc ảnh từ file
try:
    image = Image.open(image_path)
    image.show()  # Hiển thị ảnh sử dụng PIL
except Exception as e:
    print(f"Failed to load image: {e}")
