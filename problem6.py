#!/usr/bin/env python3
from functools import reduce


def sumOfSquares(n):
    return reduce(lambda x, y: x + y, map(lambda x: x**2,
                                          range(1, n + 1)))


def squareOfSums(n):
    return reduce(lambda x, y: x + y, range(1, n + 1)) ** 2


print(str(squareOfSums(100) - sumOfSquares(100)))
