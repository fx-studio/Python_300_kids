# 295 - Viết chương trình để làm mờ ảnh

import cv2  # Thư viện OpenCV để xử lý ảnh

# Đường dẫn tới file ảnh
image_path = 'img2.jpeg'

# Đọc ảnh từ file
image = cv2.imread(image_path)

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    # Chọn kích thước kernel cho bộ lọc làm mờ (ví dụ: 15x15)
    kernel_size = (15, 15)
    
    # Làm mờ ảnh sử dụng bộ lọc Gaussian
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    
    # Hiển thị ảnh gốc và ảnh đã làm mờ
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', blurred_image)

    # Lưu ảnh đã làm mờ vào file
    blurred_image_path = 'img_blurred.jpeg'
    cv2.imwrite(blurred_image_path, blurred_image)
    
    # Đợi một phím bất kỳ để đóng cửa sổ hiển thị
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Blurred image saved successfully at {blurred_image_path}")
else:
    print("Failed to load image. Check the input path and file format.")
