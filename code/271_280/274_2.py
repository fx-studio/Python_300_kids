# 274 - Viết chương trình để vẽ hình ngôi sao bằng Turtle (2)

import turtle

# Tạo hàm vẽ ngôi sao với tham số cho kích thước và vị trí
def draw_star(size, x, y):
    star_turtle.penup()       # Nhấc bút để di chuyển không vẽ
    star_turtle.goto(x, y)    # Di chuyển đến vị trí (x, y)
    star_turtle.pendown()     # Hạ bút để bắt đầu vẽ

    for _ in range(5):
        star_turtle.forward(size)  # Di chuyển về phía trước với độ dài kích thước 'size'
        star_turtle.right(144)     # Quay 144 độ sang phải

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình ngôi sao tùy chọn bằng Turtle")

# Tạo đối tượng Turtle
star_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
star_turtle.speed(2)

# Vẽ các ngôi sao với kích thước và vị trí khác nhau
draw_star(100, 0, 0)        # Vẽ ngôi sao tại vị trí trung tâm (0, 0) với kích thước 100
draw_star(50, -200, 100)    # Vẽ ngôi sao nhỏ hơn tại vị trí (-200, 100) với kích thước 50
draw_star(75, 200, -150)    # Vẽ ngôi sao tại vị trí (200, -150) với kích thước 75

# Ẩn đối tượng Turtle sau khi vẽ xong
star_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
