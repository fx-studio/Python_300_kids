# 275 - Viết chương trình để vẽ hình lục giác bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình lục giác bằng Turtle")

# Tạo đối tượng Turtle
hexagon_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
hexagon_turtle.speed(2)

# Vẽ hình lục giác đều
for _ in range(6):
    hexagon_turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
    hexagon_turtle.left(60)      # Quay 60 độ sang trái

# Ẩn đối tượng Turtle sau khi vẽ xong
hexagon_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
