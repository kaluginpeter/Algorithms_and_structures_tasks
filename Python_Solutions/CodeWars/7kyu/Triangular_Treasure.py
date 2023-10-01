# Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.
#
# 1st (1)   2nd (3)    3rd (6)
# *          **        ***
#            *         **
#                      *
# You need to return the nth triangular number. You should return 0 for out of range values:
#
# For example: (Input --> Output)
#
# 0 --> 0
# 2 --> 3
# 3 --> 6
# -10 --> 0
# ALGORITHMSMATHEMATICS
# Solution
def triangular(n):
    return n * (n + 1) // 2 if n > 0 else 0