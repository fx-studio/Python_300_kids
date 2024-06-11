# 273 - Viết chương trình để vẽ hình tròn bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình tròn bằng các đoạn thẳng nhỏ")

# Tạo đối tượng Turtle
small_segment_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
small_segment_turtle.speed(1)

# Vẽ hình tròn bằng các đoạn thẳng nhỏ
for _ in range(360):
    small_segment_turtle.forward(1)  # Di chuyển về phía trước 1 đơn vị
    small_segment_turtle.left(1)     # Quay 1 độ sang trái

# Ẩn đối tượng Turtle sau khi vẽ xong
small_segment_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()