# The prime factorization of a positive integer is a list of the integer's prime factors, together with their multiplicities; the process of determining these factors is called integer factorization. The fundamental theorem of arithmetic says that every positive integer has a single unique prime factorization.
#
# The prime factorization of 24, for instance, is (2^3) * (3^1).
#
# Write a class called PrimeFactorizer (inheriting directly from object) whose constructor accepts exactly 1 int and has a property factor containing a dictionary where the keys are prime numbers and the values are the multiplicities.
#
# PrimeFactorizer(24).factor #should return { 2: 3, 3: 1 }
# Algorithms
# Solution
class PrimeFactorizer:
    def __init__(self, x: int) -> None:
        self.x: int = x

    @property
    def factor(self) -> dict[int, int]:
        output: dict[int, int] = dict()
        while not (self.x & 1):
            output[2] = output.get(2, 0) + 1
            self.x //= 2
        bound: int = int(self.x**.5) + 1
        for prime in range(3, bound, 2):
            while self.x % prime == 0:
                output[prime] = output.get(prime, 0) + 1
                self.x //= prime
        if self.x > 2:
            output[self.x] = 1
        return output