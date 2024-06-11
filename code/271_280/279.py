# 279 - Viết chương trình để vẽ các hình chữ nhật lồng vào nhau bằng Turtle

import turtle

def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def nested_rectangles(initial_width, initial_height, num_rectangles, decrement):
    screen = turtle.Screen()
    t = turtle.Turtle()
    
    width = initial_width
    height = initial_height
    
    for _ in range(num_rectangles):
        draw_rectangle(t, width, height)
        width -= decrement
        height -= decrement
        t.penup()
        t.goto(t.xcor() + decrement / 2, t.ycor() - decrement / 2)
        t.pendown()
    
    screen.mainloop()

# Tham số đầu vào: Kích thước ban đầu, số lượng hình chữ nhật, độ giảm kích thước
nested_rectangles(200, 100, 10, 10)
