# 274 - Viết chương trình để vẽ hình ngôi sao bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình ngôi sao bằng Turtle")

# Tạo đối tượng Turtle
star_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
star_turtle.speed(2)

# Vẽ hình ngôi sao
for _ in range(5):
    star_turtle.forward(150)  # Di chuyển về phía trước 150 đơn vị
    star_turtle.right(144)    # Quay 144 độ sang phải

# Ẩn đối tượng Turtle sau khi vẽ xong
star_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
