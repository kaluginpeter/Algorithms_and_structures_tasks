# A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".
#
# In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".
#
# [ 0,  1,    3,      6,   ...]
#   0  0+1  0+1+2  0+1+2+3
# Your Task
# Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms.
#
# Examples
#  5  -->  [0,  1,  3,  6,  10,  15]
# -5  -->  [0, -1, -3, -6, -10, -15]
#  7  -->  [0,  1,  3,  6,  10,  15,  21,  28]
# FUNDAMENTALS
# Solution
def sum_of_n(n):
    if n < 0:
        return sorted([sum(x for x in range(i,1)) for i in range(n, 1)])[::-1]
    return [sum([x for x in range(i+1)]) for i in range(n+1)]