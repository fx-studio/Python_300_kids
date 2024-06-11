# 280 - Viết chương trình để vẽ hoa bằng Turtle
import turtle

def draw_petal(t, radius):
    t.circle(radius, 60)  # Vẽ cung tròn 60 độ
    t.left(120)           # Quay trái 120 độ để vẽ cánh đối xứng
    t.circle(radius, 60)
    t.left(120)           # Quay trái 120 độ để trở lại vị trí ban đầu

def draw_flower(num_petals, radius):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(10)  # Tăng tốc độ vẽ

    for _ in range(num_petals):
        draw_petal(t, radius)
        t.left(360 / num_petals)  # Quay trái để chuẩn bị vẽ cánh hoa tiếp theo
    
    t.hideturtle()  # Ẩn con trỏ sau khi vẽ xong
    screen.mainloop()

# Tham số đầu vào: Số lượng cánh hoa và bán kính của cánh
draw_flower(12, 100)
