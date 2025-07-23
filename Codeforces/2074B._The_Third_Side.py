# B. The Third Side
# time limit per test2 seconds
# memory limit per test256 megabytes
# The pink soldiers have given you a sequence a
#  consisting of n
#  positive integers.
#
# You must repeatedly perform the following operation until there is only 1
#  element left.
#
# Choose two distinct indices i
#  and j
# .
# Then, choose a positive integer value x
#  such that there exists a non-degenerate triangle∗
#  with side lengths ai
# , aj
# , and x
# .
# Finally, remove two elements ai
#  and aj
# , and append x
#  to the end of a
# .
# Please find the maximum possible value of the only last element in the sequence a
# .
#
# ∗
# A triangle with side lengths a
# , b
# , c
#  is non-degenerate when a+b>c
# , a+c>b
# , b+c>a
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤2⋅105
# ).
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤1000
# ) — the elements of the sequence a
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output the maximum possible value of the only last element on a separate line.
#
# Example
# InputCopy
# 4
# 1
# 10
# 3
# 998 244 353
# 5
# 1 2 3 4 5
# 9
# 9 9 8 2 4 4 3 5 3
# OutputCopy
# 10
# 1593
# 11
# 39
# Note
# On the first test case, there is already only one element. The value of the only last element is 10
# .
#
# On the second test case, a
#  is initially [998,244,353]
# . The following series of operations is valid:
#
# Erase a2=244
#  and a3=353
# , and append 596
#  to the end of a
# . a
#  is now [998,596]
# .
# Erase a1=998
#  and a2=596
# , and append 1593
#  to the end of a
# . a
#  is now [1593]
# .
# It can be shown that the only last element cannot be greater than 1593
# . Therefore, the answer is 1593
# .