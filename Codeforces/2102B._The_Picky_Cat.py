# B. The Picky Cat
# time limit per test1 second
# memory limit per test256 megabytes
#
# You are given an array of integers a1,a2,…,an
# . You are allowed to do the following operation any number of times (possibly zero):
#
# Choose an index i
#  (1≤i≤n
# ). Multiply ai
#  by −1
#  (i.e., update ai:=−ai
# ).
# Your task is to determine whether it is possible to make the element at index 1
#  become the median of the array after doing the above operation any number of times. Note that operations can be applied to index 1
#  as well, meaning the median can be either the original value of a1
#  or its negation.
#
# The median of an array b1,b2,…,bm
#  is defined as the ⌈m2⌉
# -th∗
#  smallest element of array b
# . For example, the median of the array [3,1,2]
#  is 2
# , while the median of the array [10,1,8,3]
#  is 3
# .
#
# It is guaranteed that the absolute value of the elements of a
#  are distinct. Formally, there are no pairs of indices 1≤i<j≤n
#  where |ai|=|aj|
# .
#
# ∗
# ⌈x⌉
#  is the ceiling function which returns the least integer greater than or equal to x
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤105
# ) — the length of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (|ai|≤106
# , |ai|≠|aj|
# ) — the elements of the array a
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# .
#
# Output
# For each testcase, output "YES" if it is possible to make the element at index 1
#  become the median of the array, and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 7
# 3
# 2 3 1
# 5
# 1 2 3 4 5
# 4
# 4 2 0 -5
# 4
# -5 0 4 3
# 4
# -10 8 3 2
# 1
# 1
# 10
# 9 1000 -999 -13 456 -223 23 24 10 0
# OutputCopy
# YES
# YES
# YES
# NO
# NO
# YES
# YES
# Note
# In the first test case, a1=2
#  is already the median of the array a=[2,3,1]
# , so no operation is required.
#
# In the second test case, we can do two operations: one on index 2
# , and one on index 5
# . The array becomes [1,−2,3,4,−5]
# , which has a median of 1
# .
#
# In the third test case, if you do an operation on index 1
# , the array will become [−4,2,0,−5]
# , which has a median of −4
# .
#
# In the fourth test case, it can be proven that no sequence of operations can make the median of the array become 5
#  or −5
# .