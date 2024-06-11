# 146 - Viết chương trình để tính Tính căn bậc hai của một số nguyên dương x bằng thuật toán Babylonian

import math

def babylonian_sqrt(x):
    guess = x
    while abs(guess * guess - x) > 1e-10:
        guess = (guess + x / guess) / 2
    return guess

# Test
x = 16
print("Babylonian method:", babylonian_sqrt(x))
print("math.sqrt:", math.sqrt(x))