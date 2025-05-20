# A. Jagged Swaps
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a permutation†
#  a
#  of size n
# . You can do the following operation
#
# Select an index i
#  from 2
#  to n−1
#  such that ai−1<ai
#  and ai>ai+1
# . Swap ai
#  and ai+1
# .
# Determine whether it is possible to sort the permutation after a finite number of operations.
#
# †
#  A permutation is an array consisting of n
#  distinct integers from 1
#  to n
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array) and [1,3,4]
#  is also not a permutation (n=3
#  but there is 4
#  in the array).
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤5000
# ). Description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (3≤n≤10
# ) — the size of the permutation.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤n
# ) — the elements of permutation a
# .
#
# Output
# For each test case, print "YES" if it is possible to sort the permutation, and "NO" otherwise.
#
# You may print each letter in any case (for example, "YES", "Yes", "yes", "yEs" will all be recognized as positive answer).
#
# Example
# InputCopy
# 6
# 3
# 1 2 3
# 5
# 1 3 2 5 4
# 5
# 5 4 3 2 1
# 3
# 3 1 2
# 4
# 2 3 1 4
# 5
# 5 1 2 3 4
# OutputCopy
# YES
# YES
# NO
# NO
# NO
# NO
# Note
# In the first test case, the permutation is already sorted.
#
# In the second test case, we can choose index i=2
#  as 1<3
#  and 3>2
#  to form [1,2,3,5,4]
# . Then, we can choose index i=4
#  as 3<5
#  and 5>4
#  to form [1,2,3,4,5]
# .
#
# In the third test case, it can be proven that it is impossible to sort the permutation.