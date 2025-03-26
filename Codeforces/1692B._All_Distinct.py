# B. All Distinct
# time limit per test1 second
# memory limit per test256 megabytes
# Sho has an array a
#  consisting of n
#  integers. An operation consists of choosing two distinct indices i
#  and j
#  and removing ai
#  and aj
#  from the array.
#
# For example, for the array [2,3,4,2,5]
# , Sho can choose to remove indices 1
#  and 3
# . After this operation, the array becomes [3,2,5]
# . Note that after any operation, the length of the array is reduced by two.
#
# After he made some operations, Sho has an array that has only distinct elements. In addition, he made operations such that the resulting array is the longest possible.
#
# More formally, the array after Sho has made his operations respects these criteria:
#
# No pairs such that (i<j
# ) and ai=aj
#  exist.
# The length of a
#  is maximized.
# Output the length of the final array.
#
# Input
# The first line contains a single integer t
#  (1≤t≤103
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤50
# ) — the length of the array.
#
# The second line of each test case contains n
#  integers ai
#  (1≤ai≤104
# ) — the elements of the array.
#
# Output
# For each test case, output a single integer — the length of the final array. Remember that in the final array, all elements are different, and its length is maximum.
#
# Example
# InputCopy
# 4
# 6
# 2 2 2 3 3 3
# 5
# 9 1 9 9 1
# 4
# 15 16 16 15
# 4
# 10 100 1000 10000
# OutputCopy
# 2
# 1
# 2
# 4
# Note
# For the first test case Sho can perform operations as follows:
#
# Choose indices 1
#  and 5
#  to remove. The array becomes [2,2,2,3,3,3]→[2,2,3,3]
# .
# Choose indices 1
#  and 4
#  to remove. The array becomes [2,2,3,3]→[2,3]
# .
# The final array has a length of 2
# , so the answer is 2
# . It can be proven that Sho cannot obtain an array with a longer length.
# For the second test case Sho can perform operations as follows:
#
# Choose indices 3
#  and 4
#  to remove. The array becomes [9,1,9,9,1]→[9,1,1]
# .
# Choose indices 1
#  and 3
#  to remove. The array becomes [9,1,1]→[1]
# .
# The final array has a length of 1
# , so the answer is 1
# . It can be proven that Sho cannot obtain an array with a longer length.