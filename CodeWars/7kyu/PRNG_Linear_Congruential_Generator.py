# The Linear Congruential Generator (LCG) is one of the oldest pseudo random number generator functions.
#
# The algorithm is as follows:
#
# Xn+1=(aXn + c) mod m
# where:
#
# a/A is the multiplier (we'll be using 2)
# c/C is the increment (we'll be using 3)
# m/M is the modulus (we'll be using 10)
# X0 is the seed.
#
# Your task
# Define a method random/Random in the class LCG that provides the next random number based on a seed. You never return the initial seed value.
#
# Similar to random return the result as a floating point number in the range [0.0, 1.0)
#
# Example
# # initialize the generator with seed = 5
# LCG(5)
#
# # first random number (seed = 5)
# LCG.random() = 0.3      # (2 * 5 + 3) mod 10 = 3 --> return 0.3
#
# # next random number (seed = 3)
# LCG.random() = 0.9      # (2 * 3 + 3) mod 10 = 9 --> return 0.9
#
# # next random number (seed = 9)
# LCG.random() = 0.1
#
# # next random number (seed = 1)
# LCG.random() = 0.5
# ALGORITHMS
# Solution
class LCG(object):
    a = 2
    c = 3
    m = 10

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        x: int = (self.a * self.seed + self.c) % self.m
        self.seed = x
        return x / 10