# A. United We Stand
# time limit per test1 second
# memory limit per test256 megabytes
# Given an array a
#  of length n
# , containing integers. And there are two initially empty arrays b
#  and c
# . You need to add each element of array a
#  to exactly one of the arrays b
#  or c
# , in order to satisfy the following conditions:
#
# Both arrays b
#  and c
#  are non-empty. More formally, let lb
#  be the length of array b
# , and lc
#  be the length of array c
# . Then lb,lc≥1
# .
# For any two indices i
#  and j
#  (1≤i≤lb,1≤j≤lc
# ), cj
#  is not a divisor of bi
# .
# Output the arrays b
#  and c
#  that can be obtained, or output −1
#  if they do not exist.
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤500
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the length of array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of array a
# .
#
# Output
# For each test case, output a single integer −1
#  if a solution does not exist.
#
# Otherwise, in the first line, output two integers lb
#  and lc
#  — the lengths of arrays b
#  and c
#  respectively.
#
# In the second line, output lb
#  integers b1,b2,…,blb
#  — the elements of array b
# .
#
# In the third line, output lc
#  integers c1,c2,…,clc
#  — the elements of array c
# .
#
# If there are multiple solutions, output any of them. You can output the elements of the arrays in any order.
#
# Example
# InputCopy
# 5
# 3
# 2 2 2
# 5
# 1 2 3 4 5
# 3
# 1 3 5
# 7
# 1 7 7 2 9 1 4
# 5
# 4 8 12 12 4
# OutputCopy
# -1
# 3 2
# 1 3 5
# 2 4
# 1 2
# 1
# 3 5
# 2 5
# 1 1
# 2 4 7 7 9
# 3 2
# 4 8 4
# 12 12
# Note
# In the first test case, a solution does not exist.
#
# In the second test case, we can obtain b=[1,3,5]
#  and c=[2,4]
# . Then elements 2
#  and 4
#  do not divide elements 1,3
#  and 5
# .
#
# In the fifth test case, we can obtain b=[4,8,4]
#  and c=[12,12]
# .