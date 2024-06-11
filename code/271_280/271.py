# 271 - Viết chương trình để vẽ hình vuông bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình vuông bằng Turtle")

# Tạo đối tượng Turtle
square_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
square_turtle.speed(1)

# Vẽ hình vuông
for _ in range(4):
    square_turtle.forward(100)  # Di chuyển về phía trước 100 đơn vị
    square_turtle.right(90)     # Quay 90 độ sang phải

# Ẩn đối tượng Turtle sau khi vẽ xong
square_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
