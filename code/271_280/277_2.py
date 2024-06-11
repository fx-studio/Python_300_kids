# 277 - Viết chương trình để vẽ đường tròn lồng vào nhau bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ các đường tròn lồng vào nhau với màu sắc bằng Turtle")

# Tạo đối tượng Turtle
colorful_circle_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
colorful_circle_turtle.speed(2)

# Thiết lập bán kính ban đầu
initial_radius = 50

# Số lượng đường tròn
num_circles = 10

# Khoảng cách giữa các tâm của các đường tròn lồng vào nhau
distance_between_circles = 20

# Danh sách các màu sắc
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "brown"]

# Vẽ các đường tròn lồng vào nhau với màu sắc
for i in range(num_circles):
    colorful_circle_turtle.penup()                # Nhấc bút để di chuyển không vẽ
    colorful_circle_turtle.goto(0, -initial_radius - i * distance_between_circles)  # Di chuyển đến vị trí mới
    colorful_circle_turtle.pendown()              # Hạ bút để bắt đầu vẽ
    colorful_circle_turtle.color(colors[i % len(colors)])  # Thay đổi màu sắc
    colorful_circle_turtle.circle(initial_radius + i * distance_between_circles)    # Vẽ đường tròn với bán kính thay đổi

# Ẩn đối tượng Turtle sau khi vẽ xong
colorful_circle_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
