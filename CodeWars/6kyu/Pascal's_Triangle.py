# In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula
#
# (
# �
# �
# )
# =
# �
# !
# �
# !
# (
# �
# −
# �
# )
# !
# (
# k
# n
# ​
#  )=
# k!(n−k)!
# n!
# ​
#
# where n denotes a row of the triangle, and k is a position of a term in the row.
#
# Pascal's Triangle
#
# You can read Wikipedia article on Pascal's Triangle for more information.
#
# Task
# Write a function that, given a depth n, returns n top rows
# of Pascal's Triangle flattened into a one-dimensional list/array.
#
# Example:
# n = 1: [1]
# n = 2: [1,  1, 1]
# n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]
# ARRAYSMATHEMATICSALGORITHMS
# Solution
def pascals_triangle(n):
    if n == 1:
        return [1]
    pr = pascals_triangle(n - 1)
    return pr + [1 if i == 0 or i == n - 1 else pr[-i] + pr[-(i + 1)] for i in range(n)]