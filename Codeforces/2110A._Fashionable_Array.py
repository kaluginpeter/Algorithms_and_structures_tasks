# A. Fashionable Array
# time limit per test1 second
# memory limit per test256 megabytes
# In 2077, everything became fashionable among robots, even arrays...
#
# We will call an array of integers a
#  fashionable if min(a)+max(a)
#  is divisible by 2
#  without a remainder, where min(a)
#  — the value of the minimum element of the array a
# , and max(a)
#  — the value of the maximum element of the array a
# .
#
# You are given an array of integers a1,a2,…,an
# . In one operation, you can remove any element from this array. Your task is to determine the minimum number of operations required to make the array a
#  fashionable.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤103
# ). The description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (1≤n≤50
# ) — the size of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤50
# ) — the elements of the array a
# .
#
# Output
# For each test case, output one integer — the minimum number of operations required to make the array a
#  fashionable.
#
# Example
# InputCopy
# 6
# 2
# 5 2
# 7
# 3 1 4 1 5 9 2
# 7
# 2 7 4 6 9 11 5
# 3
# 1 2 1
# 2
# 2 1
# 8
# 8 6 3 6 4 1 1 6
# OutputCopy
# 1
# 0
# 2
# 1
# 1
# 3
# Note
# In the first test case, at least one element needs to be removed since min(a)+max(a)=2+5=7
# , and 7
#  is not divisible by 2
# . If any of the elements are removed, only one element will remain. Then max(a)+min(a)
#  will be divisible by 2
# .
#
# In the second test case, nothing needs to be removed since min(a)+max(a)=1+9=10
# , and 10
#  is divisible by 2
# .
#
# In the third test case, you can remove the elements with values 2
#  and 4
# , then min(a)+max(a)=5+11=16
# , and 16
#  is divisible by 2
# .