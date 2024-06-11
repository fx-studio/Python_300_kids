# 278 - Viết chương trình để vẽ các đường thẳng song song bằng Turtle (2)

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ các đường thẳng song song với màu sắc bằng Turtle")

# Tạo đối tượng Turtle
colorful_lines_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
colorful_lines_turtle.speed(2)

# Số lượng đường thẳng song song
num_lines = 10

# Khoảng cách giữa các đường thẳng
distance_between_lines = 20

# Độ dài của mỗi đường thẳng
line_length = 300

# Danh sách các màu sắc
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Vẽ các đường thẳng song song với màu sắc
for i in range(num_lines):
    colorful_lines_turtle.penup()                # Nhấc bút để di chuyển không vẽ
    colorful_lines_turtle.goto(-line_length / 2, -100 + i * distance_between_lines)  # Di chuyển đến vị trí mới
    colorful_lines_turtle.pendown()              # Hạ bút để bắt đầu vẽ
    colorful_lines_turtle.color(colors[i % len(colors)])  # Thay đổi màu sắc
    colorful_lines_turtle.forward(line_length)   # Vẽ đường thẳng với chiều dài xác định

# Ẩn đối tượng Turtle sau khi vẽ xong
colorful_lines_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
