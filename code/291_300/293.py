# 293 - Viết chương trình để lưu một ảnh vào file

import cv2  # Thư viện OpenCV để xử lý ảnh

# Đường dẫn tới file ảnh cần đọc
input_image_path = 'img2.jpeg'

# Đọc ảnh từ file
image = cv2.imread(input_image_path)

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    # Đường dẫn và tên file để lưu ảnh
    output_image_path = 'img_output.jpeg'
    
    # Lưu ảnh vào file sử dụng OpenCV
    cv2.imwrite(output_image_path, image)
    
    print(f"Image saved successfully at {output_image_path}")
else:
    print("Failed to load image. Check the input path and file format.")
