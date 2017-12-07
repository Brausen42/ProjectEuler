#!/usr/bin/env python3
from Primes import Primes

p = Primes()
total = 0
cur_prime = p.getNext()
while cur_prime < 2000000:
    total += cur_prime
    cur_prime = p.getNext()

print(total)
