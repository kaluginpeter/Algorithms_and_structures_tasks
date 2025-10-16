# A. Array Divisibility
# time limit per test1 second
# memory limit per test256 megabytes
# An array of integers a1,a2,⋯,an
#  is beautiful subject to an integer k
#  if it satisfies the following:
#
# The sum of aj
#  over all j
#  such that j
#  is a multiple of k
#  and 1≤j≤n
# , itself, is a multiple of k
# .
# More formally, if ∑k|jaj
#  is divisible by k
#  for all 1≤j≤n
#  then the array a
#  is beautiful subject to k
# . Here, the notation k|j
#  means k
#  divides j
# , that is, j
#  is a multiple of k
# .
# Given n
# , find an array of positive nonzero integers, with each element less than or equal to 105
#  that is beautiful subject to all 1≤k≤n
# .
# It can be shown that an answer always exists.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first and only line of each test case contains a single integer n
#  (1≤n≤100
# ) — the size of the array.
#
# Output
# For each test case, print the required array as described in the problem statement.
#
# Example
# InputCopy
# 3
# 3
# 6
# 7
# OutputCopy
# 4 22 18
# 10 6 15 32 125 54
# 23 18 27 36 5 66 7
# Note
# In the second test case, when n=6
# , for all integers k
#  such that 1≤k≤6
# , let S
#  be the set of all indices of the array that are divisible by k
# .
#
# When k=1
# , S={1,2,3,4,5,6}
#  meaning a1+a2+a3+a4+a5+a6=242
#  must be divisible by 1
# .
# When k=2
# , S={2,4,6}
#  meaning a2+a4+a6=92
#  must be divisible by 2
# .
# When k=3
# , S={3,6}
#  meaning a3+a6=69
#  must divisible by 3
# .
# When k=4
# , S={4}
#  meaning a4=32
#  must divisible by 4
# .
# When k=5
# , S={5}
#  meaning a5=125
#  must divisible by 5
# .
# When k=6
# , S={6}
#  meaning a6=54
#  must divisible by 6
# .
# The array a=[10,6,15,32,125,54]
#  satisfies all of the above conditions. Hence, a
#  is a valid array.