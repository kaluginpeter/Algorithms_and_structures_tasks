# A Nice array is defined to be an array where for every value n in the array, there is also an element n - 1 or n + 1 in the array.
#
# examples:
#
# [2, 10, 9, 3] is a nice array because
#
#  2 =  3 - 1
# 10 =  9 + 1
#  3 =  2 + 1
#  9 = 10 - 1
#
# [4, 2, 3] is a nice array because
#
# 4 = 3 + 1
# 2 = 3 - 1
# 3 = 2 + 1 (or 3 = 4 - 1)
#
# [4, 2, 1] is a not a nice array because
#
# for n = 4, there is neither n - 1 = 3 nor n + 1 = 5
# Write a function named isNice/IsNice that returns true if its array argument is a Nice array, else false. An empty array is not considered nice.
#
# ARRAYSMATHEMATICSFUNDAMENTALS
# Solution
def is_nice(arr):
    return all(i+1 in arr or i-1 in arr for i in arr) if arr else 0