# A. MEX Partition
# time limit per test1 second
# memory limit per test256 megabytes
#
# Let a partition of a multiset B
#  be a collection of multisets s1,s2,…,sk
#  such that each element appears the same number of times in B
#  and across all of s1,s2,…,sk
# .
#
# For example, some partitions of {1,2,3,3}
#  include {1,3}+{2,3},{1,2,3,3}
# , and {2}+{1,3}+{3}
# , but not {1,2}+{3}
# .
#
# A partition is called valid if the mex
# ∗
#  of all multisets in the partition is the same. The score of a valid partition is the mex
#  of any multiset in the partition.
#
# You are given a multiset A
#  of size n
# . Find the minimum score over all valid partitions of A
# .
#
# ∗
# The minimum excluded (MEX) of a collection of integers c1,c2,…,ck
#  is defined as the smallest non-negative integer x
#  which does not occur in the collection c
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first line of each test case contains an integer n
#  (1≤n≤100
# ).
#
# The second line contains n
#  integers A1,A2,…,An
#  denoting the elements of A
#  (0≤Ai≤100
# ).
#
# It is not guaranteed that the elements are given in non-decreasing order.
#
# Output
# For each test case, output the minimum score over all valid partitions.
#
# Example
# InputCopy
# 2
# 3
# 0 0 0
# 2
# 1 2
# OutputCopy
# 1
# 0
# Note
# In the first test case, the minimum score of 1
#  can be obtained by the partition {0}+{0}+{0}
# . The partition is valid because each multiset has a mex
#  of 1
# , which is consequently the score of the partition.
#
# In the second test case, we can use {1,2}
#  as the only multiset in the partition, which has mex0
# .