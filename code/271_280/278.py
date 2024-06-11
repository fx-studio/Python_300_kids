# 278 - Viết chương trình để vẽ các đường thẳng song song bằng Turtle

import turtle

# Thiết lập màn hình
screen = turtle.Screen()
screen.title("Vẽ các đường thẳng dọc song song bằng Turtle")

# Tạo đối tượng Turtle
parallel_lines_turtle = turtle.Turtle()

# Thiết lập tốc độ vẽ
parallel_lines_turtle.speed(2)

# Số lượng đường thẳng song song
num_lines = 10

# Khoảng cách giữa các đường thẳng
distance_between_lines = 20

# Độ dài của mỗi đường thẳng
line_length = 300

# Vẽ các đường thẳng dọc song song
for i in range(num_lines):
    parallel_lines_turtle.penup()                # Nhấc bút để di chuyển không vẽ
    parallel_lines_turtle.goto(-100 + i * distance_between_lines, line_length / 2)  # Di chuyển đến vị trí mới
    parallel_lines_turtle.pendown()              # Hạ bút để bắt đầu vẽ
    parallel_lines_turtle.setheading(-90)        # Đặt hướng của Turtle xuống dưới (góc 270 độ)
    parallel_lines_turtle.forward(line_length)   # Vẽ đường thẳng với chiều dài xác định

# Ẩn đối tượng Turtle sau khi vẽ xong
parallel_lines_turtle.hideturtle()

# Giữ màn hình để xem kết quả
screen.mainloop()
