# 143 - Viết chương trình để tìm nghiệm của hệ phương trình bậc nhất 2 ẩn số x & y

def solve_linear_system(a1, b1, c1, a2, b2, c2):
    D = a1*b2 - a2*b1
    if D == 0:
        return "Hệ phương trình có vô số nghiệm hoặc vô nghiệm"
    else:
        x = (c1*b2 - c2*b1) / D
        y = (a1*c2 - a2*c1) / D
        return f"Hệ phương trình có nghiệm duy nhất: (x, y) = ({x}, {y})"

# Nhap a1, b1, c1, a2, b2, c2
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))

print(solve_linear_system(a1, b1, c1, a2, b2, c2))