# A. Be Positive
# time limit per test1 second
# memory limit per test256 megabytes
# Given an array a
#  of n
#  elements, where each element is equal to −1
# , 0
# , or 1
# . In one operation, you can choose an index i
#  and increase ai
#  by 1
#  (that is, assign ai:=ai+1
# ). Operations can be performed any number of times, choosing any indices.
#
# The goal is to make the product of all elements in the array strictly positive with the minimum number of operations, that is, a1⋅a2⋅a3⋅…⋅an>0
# . Find the minimum number of operations.
#
# It is guaranteed that this is always possible.
#
# Input
# Each test consists of several test cases.
#
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (1≤n≤8
# ) — the length of the array a
# .
#
# The second line contains n
#  integers a1,a2,…,an
# , where −1≤ai≤1
#  — the elements of the array a
# .
#
# Output
# For each test case, output one integer — the minimum number of operations required to make the product of the elements in the array strictly positive.
#
# Example
# InputCopy
# 3
# 3
# -1 0 1
# 4
# -1 -1 0 1
# 5
# -1 -1 -1 0 0
# OutputCopy
# 3
# 1
# 4
# Note
# In the first test case: from [−1,0,1]
# , you can obtain [1,1,1]
#  in 3
#  operations.
#
# In the second test case: it is enough to perform 0→1
#  (1 operation). In the resulting array a=[−1,−1,1,1]
# , the product of all elements is 1
# .
#
# In the third test case: turning two zeros into ones (2 operations), and one −1
#  into 1
#  (another 2 operations), for a total of 4
# .