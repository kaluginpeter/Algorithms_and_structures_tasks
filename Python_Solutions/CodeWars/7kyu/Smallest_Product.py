# Given a non-empty array of non-empty integer arrays, multiply the contents of each nested array and return the smallest total.
#
# Example
# input = [
#   [1, 5],
#   [2],
#   [-1, -3]
# ]
#
# result = 2
# FUNDAMENTALS
# Solution
import math
# Однострочное решение
def smallest_product(a):
    return min([math.prod(i) for i in a])

# Более подробное решение
# def smallest_product(список_списков):
#     список_сумм = []
#     for список in список_списков:
#         список_сумм.append(math.prod(список))
#     минимальное_значение = min(список_сумм)
#     return минимальное_значение