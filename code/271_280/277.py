# 277 - Viết chương trình để vẽ đường tròn lồng vào nhau bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ các đường tròn lồng vào nhau bằng Turtle")

# Tạo đối tượng Turtle
nested_circle_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
nested_circle_turtle.speed(2)

# Thiết lập bán kính ban đầu
initial_radius = 50

# Số lượng đường tròn
num_circles = 5

# Khoảng cách giữa các tâm của các đường tròn lồng vào nhau
distance_between_circles = 30

# Vẽ các đường tròn lồng vào nhau
for i in range(num_circles):
    nested_circle_turtle.penup()                # Nhấc bút để di chuyển không vẽ
    nested_circle_turtle.goto(0, -initial_radius - i * distance_between_circles)  # Di chuyển đến vị trí mới
    nested_circle_turtle.pendown()              # Hạ bút để bắt đầu vẽ
    nested_circle_turtle.circle(initial_radius + i * distance_between_circles)    # Vẽ đường tròn với bán kính thay đổi

# Ẩn đối tượng Turtle sau khi vẽ xong
nested_circle_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
