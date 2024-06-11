# 276 - Viết chương trình để vẽ hình ngũ giác bằng Turtle (2)

import turtle

# Tạo hàm vẽ ngũ giác với tham số cho kích thước và vị trí
def draw_pentagon(size, x, y):
    pentagon_turtle.penup()       # Nhấc bút để di chuyển không vẽ
    pentagon_turtle.goto(x, y)    # Di chuyển đến vị trí (x, y)
    pentagon_turtle.pendown()     # Hạ bút để bắt đầu vẽ

    for _ in range(5):
        pentagon_turtle.forward(size)  # Di chuyển về phía trước với độ dài kích thước 'size'
        pentagon_turtle.left(72)       # Quay 72 độ sang trái

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ hình ngũ giác tùy chọn bằng Turtle")

# Tạo đối tượng Turtle
pentagon_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
pentagon_turtle.speed(2)

# Vẽ các hình ngũ giác với kích thước và vị trí khác nhau
draw_pentagon(100, 0, 0)         # Vẽ ngũ giác tại vị trí trung tâm (0, 0) với kích thước 100
draw_pentagon(50, -200, 100)     # Vẽ ngũ giác nhỏ hơn tại vị trí (-200, 100) với kích thước 50
draw_pentagon(75, 200, -150)     # Vẽ ngũ giác tại vị trí (200, -150) với kích thước 75

# Ẩn đối tượng Turtle sau khi vẽ xong
pentagon_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
