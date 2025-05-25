# B. Queries about less or equal elements
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given two arrays of integers a and b. For each element of the second array bj you should find the number of elements in array a that are less than or equal to the value bj.
#
# Input
# The first line contains two integers n, m (1 ≤ n, m ≤ 2·105) — the sizes of arrays a and b.
#
# The second line contains n integers — the elements of array a ( - 109 ≤ ai ≤ 109).
#
# The third line contains m integers — the elements of array b ( - 109 ≤ bj ≤ 109).
#
# Output
# Print m integers, separated by spaces: the j-th of which is equal to the number of such elements in array a that are less than or equal to the value bj.
#
# Examples
# InputCopy
# 5 4
# 1 3 5 7 9
# 6 4 2 8
# OutputCopy
# 3 2 1 4
# InputCopy
# 5 5
# 1 2 1 2 5
# 3 1 4 1 5
# OutputCopy
# 4 2 4 2 5