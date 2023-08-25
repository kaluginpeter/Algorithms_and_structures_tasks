# Build a function sumNestedNumbers/sum_nested_numbers that finds the sum of all numbers in a series of nested arrays raised to the power of their respective nesting levels. Numbers in the outer most array should be raised to the power of 1.
#
# For example,
#
# sumNestedNumbers([1, [2], 3, [4, [5]]])
# should return 1 + 2*2 + 3 + 4*4 + 5*5*5 === 149
#
# FUNDAMENTALS
# Solution
def sum_nested_numbers(a, c=0):
    return a ** c if not isinstance(a, list) else sum(sum_nested_numbers(i, c+1) for i in a)