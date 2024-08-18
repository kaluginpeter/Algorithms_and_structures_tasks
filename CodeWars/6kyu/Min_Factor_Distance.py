# Write a function that returns the smallest distance between two factors of a number. The input will always be a number greater than one.
#
# Example:
#
# 13013 has factors: [ 1, 7, 11, 13, 77, 91, 143, 169, 1001, 1183, 1859, 13013]
#
# Hence the asnwer will be 2 (=13-11)
#
# FUNDAMENTALS
# Solution
from functools import reduce
def min_distance(n):
    factor = sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**.5)+1) if n % i == 0))))
    return min(factor[i+1] - factor[i] for i in range(len(factor)) if i + 1 < len(factor))