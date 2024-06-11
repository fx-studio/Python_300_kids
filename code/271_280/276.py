# 276 - Viết chương trình để vẽ hình ngũ giác bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình ngũ giác bằng Turtle")

# Tạo đối tượng Turtle
pentagon_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
pentagon_turtle.speed(2)

# Vẽ hình ngũ giác đều
for _ in range(5):
    pentagon_turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
    pentagon_turtle.left(72)      # Quay 72 độ sang trái

# Ẩn đối tượng Turtle sau khi vẽ xong
pentagon_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
