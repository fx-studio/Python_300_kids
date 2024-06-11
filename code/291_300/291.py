# 291 - Viết chương trình để đọc một ảnh từ file

import cv2  # Thư viện OpenCV để xử lý ảnh

# Đường dẫn tới file ảnh
image_path = 'img2.jpeg'

# Đọc ảnh từ file
image = cv2.imread(image_path)

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    # Hiển thị ảnh sử dụng OpenCV
    cv2.imshow('Displayed Image', image)

    # Đợi một phím bất kỳ để đóng cửa sổ hiển thị
    cv2.waitKey(0)

    # Đóng tất cả các cửa sổ hiển thị
    cv2.destroyAllWindows()
else:
    print("Failed to load image. Check the path and file format.")

