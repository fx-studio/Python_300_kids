# 273 - Viết chương trình để vẽ hình tròn bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình tròn bằng Turtle")

# Tạo đối tượng Turtle
circle_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
circle_turtle.speed(1)

# Vẽ hình tròn với bán kính 100 đơn vị
circle_turtle.circle(100)

# Ẩn đối tượng Turtle sau khi vẽ xong
circle_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
