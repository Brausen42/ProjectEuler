#!/usr/bin/env python3

largest = 0

for num1 in range(100, 1000):
    for num2 in range(num1, 1000):
        product = str(num1 * num2)
        if product == ''.join(reversed(product)) and int(product) > int(largest):
            largest = product

print(largest)
