# 272 - Viết chương trình để vẽ hình tam giác bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình tam giác bằng Turtle")

# Tạo đối tượng Turtle
triangle_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
triangle_turtle.speed(1)

# Vẽ hình tam giác đều
for _ in range(3):
    triangle_turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
    triangle_turtle.left(120)     # Quay 120 độ sang trái

# Ẩn đối tượng Turtle sau khi vẽ xong
triangle_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
