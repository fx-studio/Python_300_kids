from fractions import Fraction

class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        return Fraction(self.numerator, self.denominator) + Fraction(other.numerator, other.denominator)

    def subtract(self, other):
        return Fraction(self.numerator, self.denominator) - Fraction(other.numerator, other.denominator)

    def multiply(self, other):
        return Fraction(self.numerator, self.denominator) * Fraction(other.numerator, other.denominator)

    def divide(self, other):
        return Fraction(self.numerator, self.denominator) / Fraction(other.numerator, other.denominator)


# Test
frac1 = MyFraction(1, 2)
frac2 = MyFraction(2, 3)

print(f"Tổng: {frac1.add(frac2)}")
print(f"Hiệu: {frac1.subtract(frac2)}")
print(f"Tích: {frac1.multiply(frac2)}")
print(f"Thương: {frac1.divide(frac2)}")