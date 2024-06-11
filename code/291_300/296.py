# 296 - Viết chương trình để phát hiện cạnh trong ảnh

import cv2  # Thư viện OpenCV để xử lý ảnh

# Đường dẫn tới file ảnh
image_path = 'img2.jpeg'

# Đọc ảnh từ file
image = cv2.imread(image_path)

# Kiểm tra xem ảnh đã được đọc thành công chưa
if image is not None:
    # Chuyển đổi ảnh màu sang ảnh xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Áp dụng bộ lọc Canny để phát hiện cạnh
    edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)
    
    # Hiển thị ảnh gốc và ảnh đã phát hiện cạnh
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge Detected Image', edges)

    # Lưu ảnh đã phát hiện cạnh vào file
    edges_image_path = 'img_edges.jpeg'
    cv2.imwrite(edges_image_path, edges)
    
    # Đợi một phím bất kỳ để đóng cửa sổ hiển thị
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Edge detected image saved successfully at {edges_image_path}")
else:
    print("Failed to load image. Check the input path and file format.")
