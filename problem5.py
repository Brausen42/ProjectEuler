#!/usr/bin/env python3
from functools import reduce


def smallestMultiple(n):
    cur = n
    while not(reduce(lambda x,y : x and (cur % y == 0), range(n, 0, -1), True)):
        cur += n  # add n because that's the next potential multiple
    return cur


print(smallestMultiple(20))
