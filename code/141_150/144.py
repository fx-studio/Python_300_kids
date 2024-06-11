# 144 - Viết chương trình để tìm các bộ ba Pythagorean nhỏ hơn 100 là 3 số nguyên liên tiếp hoặc 3 số chẵn liên tiếp

def find_pythagorean_triplets():
    triplets = []
    for a in range(1, 98):
        b, c = a + 1, a + 2  # 3 số liên tiếp
        if a*a + b*b == c*c:
            triplets.append((a, b, c))
        b, c = a + 2, a + 4  # 3 số chẵn liên tiếp
        if a*a + b*b == c*c:
            triplets.append((a, b, c))
    return triplets

print(find_pythagorean_triplets())