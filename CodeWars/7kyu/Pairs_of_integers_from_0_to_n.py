# Write a function generatePairs (Javascript) / generate_pairs (Python / Ruby) that accepts an integer argument n and generates an array containing the pairs of integers [a, b] that satisfy the following conditions:
#
# 0 <= a <= b <= n
# The pairs should be sorted by increasing values of a then increasing values of b.
#
# For example,
#
# generate_pairs(2) should return
# [ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
# FUNDAMENTALS
# Solution
def generate_pairs(n):
    return [[i,j] for i in range(n+1) for j in range(i, n+1)]