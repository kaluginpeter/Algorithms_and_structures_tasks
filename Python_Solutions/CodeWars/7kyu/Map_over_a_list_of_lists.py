# Write a function which maps a function over the lists in a list:
#
# def grid_map(inp, op)
#     # which performs op(element) for all elements of inp
# Example 1:
#
# x = [[1,2,3],
#      [4,5,6]]
#
# grid_map(x, lambda x: x + 1)
# -- returns [[2,3,4],[5,6,7]]
#
# grid_map(x, lambda x: x ** 2)
# -- returns [[1,4,9],[16,25,36]]
# Example 2
#
# x = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
# grid_map(x, lambda x: x.upper())
# -- returns [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]
# FUNDAMENTALSLISTS
# Solution
def grid_map(inp, op):
    return [list(map(op, i)) for i in inp]