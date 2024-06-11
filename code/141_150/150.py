# 150 - Viết chương trình để tìm khoảng cách của 2 điểm A & B trong hệ tọa độ Oxy

import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

pointA = (float(input("Enter x coordinate for point A: ")), float(input("Enter y coordinate for point A: ")))
pointB = (float(input("Enter x coordinate for point B: ")), float(input("Enter y coordinate for point B: ")))

distance = calculate_distance(pointA, pointB)
print(f"The distance between point A and point B is: {distance}")