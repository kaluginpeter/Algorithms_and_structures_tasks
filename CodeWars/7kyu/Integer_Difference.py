# Write a function that accepts two arguments: an array/list of integers and another integer (n).
#
# Determine the number of times where two integers in the array have a difference of n.
#
# For example:
#
# [1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
# [1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)
# FUNDAMENTALS
# Solution
def int_diff(lst, n):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if abs(lst[i] - lst[j]) == n:
                count += 1
    return count