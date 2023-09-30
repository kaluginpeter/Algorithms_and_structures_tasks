# Steps
#
# Square the numbers that are greater than zero.
# Multiply by 3 every third number.
# Multiply by -1 every fifth number.
# Return the sum of the sequence.
# Example
# { -2, -1, 0, 1, 2 } returns -6
#
# 1. { -2, -1, 0, 1 * 1, 2 * 2 }
# 2. { -2, -1, 0 * 3, 1, 4 }
# 3. { -2, -1, 0, 1, -1 * 4 }
# 4. -6
# P.S.: The sequence consists only of integers. And try not to use "for", "while" or "loop" statements.
#
# FUNDAMENTALSARRAYS
# Solution
def calc(a):
    return sum(v**(1 + (v>=0)) * (1 + 2*(not k%3)) * (-1)**(not k%5) for k, v in enumerate(a, 1))