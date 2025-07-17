# C. Equal Values
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given an array a1,a2,…,an
# , consisting of n
#  integers.
#
# In one operation, you are allowed to perform one of the following actions:
#
# Choose a position i
#  (1<i≤n
# ) and make all elements to the left of i
#  equal to ai
# . That is, assign the value ai
#  to all aj
#  (1≤j<i
# ). The cost of such an operation is (i−1)⋅ai
# .
# Choose a position i
#  (1≤i<n
# ) and make all elements to the right of i
#  equal to ai
# . That is, assign the value ai
#  to all aj
#  (i<j≤n
# ). The cost of such an operation is (n−i)⋅ai
# .
# Note that the elements affected by an operation may already be equal to ai
# , but that doesn't change the cost.
#
# You are allowed to perform any number of operations (including zero). What is the minimum total cost to make all elements of the array equal?
#
# Input
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (2≤n≤5⋅105
# ).
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤n
# ).
#
# The sum of n
#  over all test cases does not exceed 5⋅105
# .
#
# Output
# For each test case, print a single integer — the minimum total cost of operations to make all elements of the array equal.
#
# Example
# InputCopy
# 3
# 4
# 2 4 1 3
# 3
# 1 1 1
# 10
# 7 5 5 5 10 9 9 4 6 10
# OutputCopy
# 3
# 0
# 35
# Note
# In the first test case, you can perform the operation twice:
#
# choose i=3
#  and make all elements to the left of it equal to it, the cost will be 2⋅1=2
# ;
# choose i=3
#  and make all elements to the right of it equal to it, the cost will be 1⋅1=1
# .
# The total cost is 2+1=3
# .
#
# In the second test case, all elements are already equal, so no operations need to be performed.