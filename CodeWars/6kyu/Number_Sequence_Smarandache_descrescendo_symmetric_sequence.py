# Build the sequence which is defined as follows
#
# 1,
# 1, 2, 1,
# 1, 2, 3, 2, 1,
# 1, 2, 3, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1,
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
# ...
# Task
# write a function solve(n, bound) which builds this sequence until an element in the sequnce equals bound (not including bound). Return the sum of every nth element of the sequence (not including the 0th element).
#
# Example
# solve(2, 4) produces the following sequence
#
# 1,
# 1, 2, 1,
# 1, 2, 3, 2, 1,
# 1, 2, 3,
#
# solve(2, 4) = 2 + 1 + 3 + 1 + 2 = 9
# Other examples
# solve(3, 3) = 1
# solve(2, 3) = 2 + 1 = 3
# Note
# bound will always be greater than 1 (bound>1)
#
# ALGORITHMS