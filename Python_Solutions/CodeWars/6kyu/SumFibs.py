# Create a function that takes an argument n and sums even Fibonacci numbers up to n's index in the Fibonacci sequence.
#
# Example:
#
# sum_fibs(5) == 2 # (0, 1, 1, 2, 3, 5); 2 is the only even number in the sequence and doesn't have another number in the sequence to get added to in the indexed Fibonacci sequence.
# Example:
#
# sum_fibs(9) == 44 # (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
# # 2 + 8 + 34 = 44
# ALGORITHMS
# Solution
from gmpy2 import fib
def sum_fibs(n):
    return sum(i for i in map(fib, range(n + 1)) if i % 2 == 0)