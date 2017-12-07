#!/usr/bin/env python3

# pick initial values that should be close
a = 300
b = 300
c = 400

while (a ** 2 + b ** 2 != c ** 2) and b > 0:
    if a ** 2 + b ** 2 > c ** 2:
        b -= 1
        c += 1
    else:
        c -= 1
        a += 1
print(a, b, c, a * b * c)
