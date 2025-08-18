# C. Make it Equal
# time limit per test2 seconds
# memory limit per test256 megabytes
# Given two multisets S
#  and T
#  of size n
#  and a positive integer k
# , you may perform the following operations any number (including zero) of times on S
# :
#
# Select an element x
#  in S
# , and remove one occurrence of x
#  in S
# . Then, either insert x+k
#  into S
# , or insert |x−k|
#  into S
# .
# Determine if it is possible to make S
#  equal to T
# . Two multisets S
#  and T
#  are equal if every element appears the same number of times in S
#  and T
# .
#
# Input
# Each test contains multiple test cases. The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line contains two integers n
#  and k
#  (1≤n≤2⋅105
# , 1≤k≤109
# ) — the size of S
#  and the constant, respectively.
#
# The second line contains n
#  integers S1,S2,…,Sn
#  (0≤Si≤109
# ) — the elements in S
# .
#
# The third line contains n
#  integers T1,T2,…,Tn
#  (0≤Ti≤109
# ) — the elements in T
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output "YES" if it is possible to make S
#  equal to T
# , and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 5
# 1 3
# 1
# 2
# 1 8
# 4
# 12
# 3 5
# 6 2 9
# 8 4 11
# 2 7
# 2 8
# 2 9
# 3 2
# 0 1 0
# 1 0 1
# OutputCopy
# YES
# YES
# YES
# NO
# NO
# Note
# In the first test case, we can remove one occurrence of 1
#  from S
#  and insert |1−k|=|1−3|=2
#  into S
# , making S
#  equal to T
# .
#
# In the second test case, we can remove one occurrence of 4
#  from S
#  and insert 4+k=4+8=12
#  into S
# , making S
#  equal to T
# .
#
# In the last test case, we can show that it is impossible to make S
#  equal to T
# .