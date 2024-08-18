# Problem
# Complete the function that takes an odd integer (0 < n < 1000000) which is the difference between two consecutive perfect squares, and return these squares as a string in the format "bigger-smaller"
#
# Examples
# 9  -->  "25-16"
# 5  -->  "9-4"
# 7  -->  "16-9"
# MATHEMATICSALGORITHMS
# Solution
def find_squares(n):
    i = (n - 1) // 2
    return f'{(i + 1)**2}-{i**2}'