# A. Print a Pedestal (Codeforces logo?)
# time limit per test1 second
# memory limit per test256 megabytes
# Given the integer n
#  — the number of available blocks. You must use all blocks to build a pedestal.
#
# The pedestal consists of 3
#  platforms for 2
# -nd, 1
# -st and 3
# -rd places respectively. The platform for the 1
# -st place must be strictly higher than for the 2
# -nd place, and the platform for the 2
# -nd place must be strictly higher than for the 3
# -rd place. Also, the height of each platform must be greater than zero (that is, each platform must contain at least one block).
#
# Example pedestal of n=11
#  blocks: second place height equals 4
#  blocks, first place height equals 5
#  blocks, third place height equals 2
#  blocks.
# Among all possible pedestals of n
#  blocks, deduce one such that the platform height for the 1
# -st place minimum as possible. If there are several of them, output any of them.
#
# Input
# The first line of input data contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Each test case contains a single integer n
#  (6≤n≤105
# ) — the total number of blocks for the pedestal. All n
#  blocks must be used.
#
# It is guaranteed that the sum of n
#  values over all test cases does not exceed 106
# .
#
# Output
# For each test case, output 3
#  numbers h2,h1,h3
#  — the platform heights for 2
# -nd, 1
# -st and 3
# -rd places on a pedestal consisting of n
#  blocks (h1+h2+h3=n
# , 0<h3<h2<h1
# ).
#
# Among all possible pedestals, output the one for which the value of h1
#  minimal. If there are several of them, output any of them.
#
# Example
# InputCopy
# 6
# 11
# 6
# 10
# 100000
# 7
# 8
# OutputCopy
# 4 5 2
# 2 3 1
# 4 5 1
# 33334 33335 33331
# 2 4 1
# 3 4 1
# Note
# In the first test case we can not get the height of the platform for the first place less than 5
# , because if the height of the platform for the first place is not more than 4
# , then we can use at most 4+3+2=9
#  blocks. And we should use 11=4+5+2
#  blocks. Therefore, the answer 4 5 2 fits.
#
# In the second set, the only suitable answer is: 2 3 1.