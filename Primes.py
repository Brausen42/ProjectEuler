import math


def sieve(nums):
    i = 0
    while i < len(nums):
        nums = nums[:i + 1] + list(filter(
            lambda x: x % nums[i] != 0,
            nums[i + 1:]))
        i += 1
    return nums


class Primes(object):
    primes = sieve([2] + list(range(3, 1000, 2)))

    def __findNextPrime():
        potential = Primes.primes[-1] + 2

        def isPrime(pot):
            limit = math.sqrt(pot)
            i = 0
            while Primes.primes[i] <= limit:
                if pot % Primes.primes[i] == 0:
                    return False
                i += 1
            return True

        while not(isPrime(potential)):
            potential += 2
        Primes.primes.append(potential)

    def __generateToNth(n):
        while len(Primes.primes) < n:
            Primes.__findNextPrime()

    def isPrime(n):
        while n > Primes.primes[-1]:
            Primes.__findNextPrime()
        return n in Primes.primes

    def __init__(self):
        self.index = 0

    def getNext(self):
        while not(self.index < len(Primes.primes)):
            Primes.__findNextPrime()
        self.index += 1
        return Primes.primes[self.index - 1]

    def getNth(self, n):
        self.index = n
        if len(Primes.primes) <= self.index:
            Primes.__generateToNth(self.index)
        return Primes.primes[self.index - 1]
