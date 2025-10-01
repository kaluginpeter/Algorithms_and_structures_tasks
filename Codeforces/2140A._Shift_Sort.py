# A. Shift Sort
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a binary string∗
#  s
#  of length n
#  and you are allowed to perform the following operation any number of times (including zero):
#
# Choose 3
#  indices 1≤i<j<k≤n
#  and right shift or left shift the values on si
# , sj
# , sk
#  cyclically.
# For the binary string 110110, if we choose i=1
# , j=2
# , k=3
#  and perform a right shift cyclically, the string becomes 011110; if we choose i=4
# , j=5
# , k=6
#  and perform a left shift cyclically, the string becomes 110101.
#
# Determine the minimum number of operations required to sort the given binary string.
#
# ∗
# A binary string is a string that consists only of the characters 0 and 1.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (3≤n≤100
# ) — the length of the string.
#
# The second line contains a binary string s
#  of length n
# .
#
# Output
# For each test case, output a single integer — the minimum number of operations required to sort the given binary string.
#
# Example
# InputCopy
# 4
# 3
# 001
# 4
# 0110
# 6
# 110100
# 6
# 101011
# OutputCopy
# 0
# 1
# 2
# 1
# Note
# For the first test case, the given string is already sorted. So, no operations are needed.
#
# For the second test case, we can choose i=1
# , j=2
# , k=4
#  and perform a right shift cyclically. The string becomes equal to 0011, which is sorted.