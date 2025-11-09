# C. Maximum Even Sum
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given two integers a
#  and b
# . You are to perform the following procedure:
#
# First, you choose an integer k
#  such that b
#  is divisible by k
# . Then, you simultaneously multiply a
#  by k
#  and divide b
#  by k
# .
#
# Find the greatest possible even value of a+b
# . If it is impossible to make a+b
#  even, output −1
#  instead.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers a
#  and b
#  (1≤a,b≤a⋅b≤1018)
# .
#
# Output
# For each test case, output the maximum even value of a+b
#  on a new line.
#
# Example
# InputCopy
# 7
# 8 1
# 1 8
# 7 7
# 2 6
# 9 16
# 1 6
# 4 6
# OutputCopy
# -1
# 6
# 50
# 8
# 74
# -1
# 14
# Note
# In the first test case, it can be shown it is impossible for a+b
#  to be even.
#
# In the second test case, the optimal k
#  is 2
# . The sum is 2+4=6
# .