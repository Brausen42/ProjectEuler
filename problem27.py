# taken from http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

max_n = -1
max_a = -1
max_b = -1

for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        primed = True
        while primed:
            next_potential_prime  = (n**2) + (n * a) + b
            primed = isprime(abs(next_potential_prime))
            n += 1
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b

print("largest a: " + str(max_a))
print("largest b: " + str(max_b))
print("largest n: " + str(max_n))
print("largest a*b: " + str(max_a * max_b))
