# Complete the square sum function so that it squares each number passed into it and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because
# 1
# 2
# +
# 2
# 2
# +
# 2
# 2
# =
# 9
# 1
# 2
#  +2
# 2
#  +2
# 2
#  =9.
#
# ARRAYSLISTSFUNDAMENTALS
# Solution
def square_sum(numbers):
    return sum([integer*integer for integer in numbers])