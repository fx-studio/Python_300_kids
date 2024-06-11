# 294 - Viết chương trình để chuyển đổi ảnh màu thành ảnh xám

from PIL import Image  # Thư viện Pillow để xử lý ảnh

# Đường dẫn tới file ảnh màu
image_path = 'img2.jpeg'

try:
    # Đọc ảnh màu từ file
    image = Image.open(image_path)

    # Chuyển đổi ảnh màu thành ảnh xám
    gray_image = image.convert('L')
    
    # Hiển thị ảnh xám
    gray_image.show()

    # Lưu ảnh xám vào file
    gray_image_path = 'img_gray.jpeg'
    gray_image.save(gray_image_path)

    print(f"Grayscale image saved successfully at {gray_image_path}")
except Exception as e:
    print(f"Failed to load or convert image: {e}")
