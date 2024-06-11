# 141 - Viết chương trình để tính tổng, hiệu, tích và thương của hai phân số

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return f"{numerator // gcd(numerator, denominator)}/{denominator // gcd(numerator, denominator)}"

    def subtract(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return f"{numerator // gcd(numerator, denominator)}/{denominator // gcd(numerator, denominator)}"

    def multiply(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return f"{numerator // gcd(numerator, denominator)}/{denominator // gcd(numerator, denominator)}"

    def divide(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return f"{numerator // gcd(numerator, denominator)}/{denominator // gcd(numerator, denominator)}"


# Test
frac1 = MyFraction(1, 2)
frac2 = MyFraction(2, 3)

print(f"Tổng: {frac1.add(frac2)}")
print(f"Hiệu: {frac1.subtract(frac2)}")
print(f"Tích: {frac1.multiply(frac2)}")
print(f"Thương: {frac1.divide(frac2)}")