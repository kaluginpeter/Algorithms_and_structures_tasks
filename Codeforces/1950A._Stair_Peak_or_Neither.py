# A. Stair, Peak, or Neither?
# time limit per test1 second
# memory limit per test256 megabytes
# You are given three digits a
# , b
# , and c
# . Determine whether they form a stair, a peak, or neither.
#
# A stair satisfies the condition a<b<c
# .
# A peak satisfies the condition a<b>c
# .
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The only line of each test case contains three digits a
# , b
# , c
#  (0≤a
# , b
# , c≤9
# ).
#
# Output
# For each test case, output "STAIR" if the digits form a stair, "PEAK" if the digits form a peak, and "NONE" otherwise (output the strings without quotes).
#
# Example
# inputCopy
# 7
# 1 2 3
# 3 2 1
# 1 5 3
# 3 4 1
# 0 0 0
# 4 1 7
# 4 5 7
# outputCopy
# STAIR
# NONE
# PEAK
# PEAK
# NONE
# NONE
# STAIR