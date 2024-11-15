# A. Odd Set
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a multiset (i. e. a set that can contain multiple equal integers) containing 2n
#  integers. Determine if you can split it into exactly n
#  pairs (i. e. each element should be in exactly one pair) so that the sum of the two elements in each pair is odd (i. e. when divided by 2
# , the remainder is 1
# ).
#
# Input
# The input consists of multiple test cases. The first line contains an integer t
#  (1≤t≤100
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains an integer n
#  (1≤n≤100
# ).
#
# The second line of each test case contains 2n
#  integers a1,a2,…,a2n
#  (0≤ai≤100
# ) — the numbers in the set.
#
# Output
# For each test case, print "Yes" if it can be split into exactly n
#  pairs so that the sum of the two elements in each pair is odd, and "No" otherwise. You can print each letter in any case.
#
# Example
# InputCopy
# 5
# 2
# 2 3 4 5
# 3
# 2 3 4 5 5 5
# 1
# 2 4
# 1
# 2 3
# 4
# 1 5 3 2 6 7 3 4
# OutputCopy
# Yes
# No
# No
# Yes
# No
# Note
# In the first test case, a possible way of splitting the set is (2,3)
# , (4,5)
# .
#
# In the second, third and fifth test case, we can prove that there isn't any possible way.
#
# In the fourth test case, a possible way of splitting the set is (2,3)
# .