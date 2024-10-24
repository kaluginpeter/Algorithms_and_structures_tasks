# C. Longest Good Array
# time limit per test2 seconds
# memory limit per test256 megabytes
# Today, Sakurako was studying arrays. An array a
#  of length n
#  is considered good if and only if:
#
# the array a
#  is increasing, meaning ai−1<ai
#  for all 2≤i≤n
# ;
# the differences between adjacent elements are increasing, meaning ai−ai−1<ai+1−ai
#  for all 2≤i<n
# .
# Sakurako has come up with boundaries l
#  and r
#  and wants to construct a good array of maximum length, where l≤ai≤r
#  for all ai
# .
#
# Help Sakurako find the maximum length of a good array for the given l
#  and r
# .
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# )  — the number of test cases.
#
# The only line of each test case contains two integers l
#  and r
#  (1≤l≤r≤109
# ).
#
# Output
# For each test case, output a single integer  — the length of the longest good array Sakurako can form given l
#  and r
# .
#
# Example
# inputCopy
# 5
# 1 2
# 1 5
# 2 2
# 10 20
# 1 1000000000
# outputCopy
# 2
# 3
# 1
# 5
# 44721
# Note
# For l=1
#  and r=5
# , one possible array could be (1,2,5)
# . It can be proven that an array of length 4
#  does not exist for the given l
#  and r
# .
#
# For l=2
#  and r=2
# , the only possible array is (2)
# .
#
# For l=10
#  and r=20
# , the only possible array is (10,11,13,16,20)
# .