# C. MEX rose
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an array a
#  of length n
#  and a number k
# , where 0≤k≤n
# .
#
# In one operation, you can choose any index i
#  (1≤i≤n
# ) and set ai
#  to any integer value x
#  from the range [0,n]
# .
#
# Find the minimum number of such operations required to satisfy the condition: MEX(a)
# ∗
# =k
#
# ∗
# The minimum excluded (MEX) of a set of numbers a1,a2,…,an
#  is the smallest non-negative integer x
#  that does not appear among the ai
# .
#
# Input
# Each test consists of several sets of input data.
#
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of sets of input data. The description of the sets of input data follows.
#
# The first line of each set of input data contains two integers n
#  and k
#  (1≤n≤2⋅105,0≤k≤n
# ) — the length of the array a
#  and the required MEX(a)
# .
#
# The second line contains n
#  integers a1,a2,…,an
#  (0≤ai≤n
# ) — the elements of the array a
# .
#
# It is guaranteed that the sum of the values of n
#  across all sets of input data does not exceed 2⋅105
# .
#
# Output
# For each set of input data, output one integer — the minimum number of operations required to satisfy the condition MEX(a)=k
# .
#
# Example
# InputCopy
# 5
# 1 0
# 0
# 3 1
# 0 2 3
# 5 5
# 0 1 2 3 4
# 6 2
# 0 3 4 2 6 2
# 7 4
# 0 1 5 4 4 7 3
# OutputCopy
# 1
# 0
# 0
# 2
# 2
# Note
# In the first set of input data, the array a=[0]
# , so MEX=1
# .By removing zero (replacing it with any x∈[1,n]
# ), we get MEX=0
# .Thus, exactly one operation is required.
#
# In the third set of input data, the array contains all the numbers 0,1,2,3,4
# , so MEX(a)=5
#  from the start.
#
# Since this matches the required k
# , no changes are needed and the minimum number of operations is 0
# .